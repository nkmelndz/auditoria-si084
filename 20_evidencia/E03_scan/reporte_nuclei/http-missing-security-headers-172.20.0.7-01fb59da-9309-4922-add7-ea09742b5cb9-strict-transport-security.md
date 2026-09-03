### HTTP Missing Security Headers (http-missing-security-headers:strict-transport-security) found on 172.20.0.7

----
**Details**: **http-missing-security-headers:strict-transport-security** matched at 172.20.0.7

**Protocol**: HTTP

**Full URL**: http://172.20.0.7/wp-admin/install.php

**Timestamp**: Thu Sep 3 05:41:51 +0000 UTC 2026

**Template Information**

| Key | Value |
| --- | --- |
| Name | HTTP Missing Security Headers |
| Authors | socketz, geeknik, g4l1t0, convisoappsec, kurohost, dawid-czarnecki, forgedhallpass, jub0bs, userdehghani, celbahraoui, safejulian |
| Tags | misconfig, headers, generic, vuln |
| Severity | info |
| Description | This template searches for missing HTTP security headers. The impact of these missing headers can vary.<br> |
| CWE-ID | [CWE-693](https://cwe.mitre.org/data/definitions/693.html) |
| CVSS-Score | 0.00 |

**Request**
```http
GET / HTTP/1.1
Host: 172.20.0.7
User-Agent: Mozilla/5.0 (Macintosh: Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15
Accept: */*
Accept-Language: en
Accept-Encoding: gzip


```

**Response**
```http
HTTP/1.1 200 OK
Cache-Control: no-cache, must-revalidate, max-age=0, no-store, private
Content-Type: text/html; charset=utf-8
Date: Thu, 03 Sep 2026 05:41:49 GMT
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Server: Apache/2.4.68 (Debian)
Vary: Accept-Encoding
X-Powered-By: PHP/8.3.33

<!DOCTYPE html>
<html lang="en-US">
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="robots" content="noindex,nofollow" />
	<title>WordPress &rsaquo; Installation</title>
	<link rel='stylesheet' id='dashicons-css' href='http://172.20.0.7/wp-includes/css/dashicons.min.css?ver=7.1' media='all' />
<link rel='stylesheet' id='buttons-css' href='http://172.20.0.7/wp-includes/css/buttons.min.css?ver=7.1' media='all' />
<link rel='stylesheet' id='forms-css' href='http://172.20.0.7/wp-admin/css/forms.min.css?ver=7.1' media='all' />
<link rel='stylesheet' id='l10n-css' href='http://172.20.0.7/wp-admin/css/l10n.min.css?ver=7.1' media='all' />
<link rel='stylesheet' id='wp-base-styles-css' href='http://172.20.0.7/wp-includes/css/dist/base-styles/admin-schemes.min.css?ver=7.1' media='all' />
<link rel='stylesheet' id='install-css' href='http://172.20.0.7/wp-admin/css/install.min.css?ver=7.1' media='all' />
</head>
<body class="wp-core-ui admin-color-modern language-chooser">
<p id="logo">WordPress</p>

	<form id="setup" method="post" action="?step=1"><label for='language'>Select a default language</label>
<select size='14' name='language' id='language'>
<option value="" lang="en" selected="selected" data-continue="Continue" data-installed="1">English (United States)</option>
<option value="af" lang="af" data-continue="Gaan voort">Afrikaans</option>
<option value="am" lang="am" data-continue="ቀጥል">አማርኛ</option>
<option value="arg" lang="an" data-continue="Continar">Aragonés</option>
<option value="ar" lang="ar" data-continue="متابعة">العربية</option>
<option value="ary" lang="ar" data-continue="المتابعة">العربية المغربية</option>
<option value="as" lang="as" data-continue="Continue">অসমীয়া</option>
<option value="azb" lang="az" data-continue="Continue">گؤنئی آذربایجان</option>
<option value="az" lang="az" data-continue="Davam">Azərbaycan dili</option>
<option value="bel" lang="be" data-continue="Працягнуць">Беларуская мова</option>
<option value="bg_BG" lang="bg" data-continue="Напред">Български</option>
<option value="bn_BD" lang="bn" data-continue="চালিয়ে যান">বাংলা</option>
<option value="bo" lang="bo" data-continue="མུ་མཐུད་དུ།">བོད་ཡིག</option>
<option value="bs_BA" lang="bs" data-continue="Nastavi">Bosanski</option>
<option value="ca" lang="ca" data-continue="Continua">Català</option>
<option value="ceb" lang="ceb" data-continue="Padayun">Cebuano</option>
<option value="cs_CZ" lang="cs" data-continue="Pokračovat">Čeština</option>
<option value="cy" lang="cy" data-continue="Parhau">Cymraeg</option>
<option value="da_DK" lang="da" data-continue="Fortsæt">Dansk</option>
<option value="de_AT" lang="de" data-continue="Weiter">Deutsch (Österreich)</option>
<option value="de_DE" lang="de" data-continue="Weiter">Deutsch</option>
<option value="de_DE_formal" lang="de" data-continue="Weiter">Deutsch (Sie)</option>
<option value="de_CH" lang="de" data-continue="Weiter">Deutsch (Schweiz)</option>
<option value="de_CH_informal" lang="de" data-continue="Weiter">Deutsch (Schweiz, Du)</option>
<option value="dsb" lang="dsb" data-continue="Dalej">Dolnoserbšćina</option>
<option value="dzo" lang="dz" data-continue="Continue">རྫོང་ཁ</option>
<option value="el" lang="el" data-continue="Συνέχεια">Ελληνικά</option>
<option value="en_GB" lang="en" data-continue="Continue">English (UK)</option>
<option value="en_NZ" lang="en" data-continue="Continue">English (New Zealand)</option>
<option value="en_AU" lang="en" data-continue="Continue">English (Australia)</option>
<option value="en_CA" lang="en" data-continue="Continue">English (Canada)</option>
<option value="en_ZA" lang="en" data-continue="Continue">English (South Africa)</option>
<option value="eo" lang="eo" data-continue="Daŭrigi">Esperanto</option>
<option value="es_AR" lang="es" data-continue="Continuar">Español de Argentina</option>
<option value="es_CO" lang="es" data-continue="Continuar">Español de Colombia</option>
<option value="es_CR" lang="es" data-continue="Continuar">Español de Costa Rica</option>
<option value="es_CL" lang="es" data-continue="Continuar">Español de Chile</option>
<option value="es_PE" lang="es" data-continue="Continuar">Español de Perú</option>
<option value="es_VE" lang="es" data-continue="Continuar">Español de Venezuela</option>
<option value="es_EC" lang="es" data-continue="Continuar">Español de Ecuador</option>
<option value="es_DO" lang="es" data-continue="Continuar">Español de República Dominicana</option>
<option value="es_UY" lang="es" data-c.... Truncated ....
```


**CURL command**
```sh
curl -X 'GET' -d '' -H 'Accept: */*' -H 'Accept-Language: en' -H 'Referer: http://172.20.0.7' -H 'User-Agent: Mozilla/5.0 (Macintosh: Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15' 'http://172.20.0.7/wp-admin/install.php'
```

----

Generated by [Nuclei v3.11.1](https://github.com/projectdiscovery/nuclei)