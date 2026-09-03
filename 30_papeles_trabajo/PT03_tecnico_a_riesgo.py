import pandas as pd
import os

# --- EVIDENCIA TÉCNICA ---
ruta_reporte = "../20_evidencia/E03_scan/reporte_nuclei/index.md"
hallazgos = []

# Mapeamos las severidades textuales a un equivalente CVSS
mapa_severidad = {"info": 0.0, "low": 3.0, "medium": 5.0, "high": 7.5, "critical": 9.8}

with open(ruta_reporte, "r", encoding="utf-8") as f:
    for linea in f:
        if linea.startswith("| [172"):
            partes = [p.strip() for p in linea.split("|")]
            if len(partes) >= 4:
                # Extraer IP (ej. "[172.20.0.6](archivo.md)" -> "172.20.0.6")
                ip = partes[1].split("[")[1].split("]")[0]
                vulnerabilidad = partes[2]
                severidad_txt = partes[3]
                cvss = mapa_severidad.get(severidad_txt.lower(), 0.0)
                
                # Descartar los informativos (simulando Severity >= 4.0)
                if cvss >= 4.0:
                    hallazgos.append({"Host": ip, "NVT Name": vulnerabilidad, "Severity": cvss})

v = pd.DataFrame(hallazgos)

# --- CONTEXTO DE NEGOCIO ---
# Relacionamos las IPs reales de tus contenedores con los activos del negocio
ACTIVOS = {
    "172.20.0.5": dict(nombre="Base de datos ERP",  dueno="Gerencia de Finanzas",
                       clasificacion="Restringida", expuesto=False, criticidad=5),
    "172.20.0.2": dict(nombre="Portal de clientes", dueno="Gerencia Comercial",
                       clasificacion="Confidencial", expuesto=True,  criticidad=4),
    "172.20.0.7": dict(nombre="Portal corporativo", dueno="Gerencia Comercial",
                       clasificacion="Pública",     expuesto=True,  criticidad=2),
    "172.20.0.6": dict(nombre="App legada interna", dueno="Gerencia de Operaciones",
                       clasificacion="Interna",     expuesto=False, criticidad=3),
}

def probabilidad(cvss, expuesto):
    """La exposición a Internet eleva la probabilidad de explotación."""
    base = 1 if cvss < 4 else 2 if cvss < 7 else 3 if cvss < 9 else 4
    return min(5, base + (1 if expuesto else 0))

def impacto(criticidad, clasificacion):
    """El impacto lo determina el valor del activo, no la severidad técnica."""
    extra = {"Restringida": 1, "Confidencial": 0, "Interna": 0, "Pública": -1}
    return max(1, min(5, criticidad + extra.get(clasificacion, 0)))

filas = []
for _, r in v.iterrows():
    a = ACTIVOS.get(r["Host"].strip(), None)
    if not a:
        continue
    p = probabilidad(r["Severity"], a["expuesto"])
    i = impacto(a["criticidad"], a["clasificacion"])
    filas.append({
        "id_riesgo": f"R-{len(filas)+1:03d}",
        "activo": a["nombre"], "dueno_del_riesgo": a["dueno"],
        "clasificacion": a["clasificacion"],
        "amenaza": "Explotación remota de vulnerabilidad conocida",
        "vulnerabilidad": r["NVT Name"], "cve": "N/D",
        "cvss": r["Severity"], "probabilidad": p, "impacto": i,
        "riesgo_inherente": p * i,
        "nivel": "Crítico" if p*i >= 20 else "Alto" if p*i >= 12
                 else "Medio" if p*i >= 6 else "Bajo",
    })

if len(filas) > 0:
    reg = pd.DataFrame(filas).sort_values("riesgo_inherente", ascending=False)
    reg.to_csv("../40_hallazgos/PT03_registro_riesgos.csv", index=False)
    print(reg[["id_riesgo", "activo", "vulnerabilidad", "nivel", "riesgo_inherente"]].head(15).to_string(index=False))
    print("\nDistribución por nivel:\n", reg["nivel"].value_counts().to_string())
else:
    print("No se encontraron vulnerabilidades mayores a severidad 4.0.")
