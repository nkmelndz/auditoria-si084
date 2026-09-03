### Header Based Generic OOB Interaction (oob-header-based-interaction:dns) found on 172.20.0.7

----
**Details**: **oob-header-based-interaction:dns** matched at 172.20.0.7

**Protocol**: HTTP

**Full URL**: http://172.20.0.7

**Timestamp**: Thu Sep 3 05:43:06 +0000 UTC 2026

**Template Information**

| Key | Value |
| --- | --- |
| Name | Header Based Generic OOB Interaction |
| Authors | pdteam |
| Tags | oast, ssrf, generic, vuln |
| Severity | info |
| Description | The remote server fetched a spoofed URL from the request headers. |
| CWE-ID | [CWE-918](https://cwe.mitre.org/data/definitions/918.html) |
| CVSS-Score | 0.00 |

**Request**
```http
GET / HTTP/1.1
Host: 172.20.0.7
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 root@dacgflmtle895jd60mfge174wfc9h4krq.oast.online
Accept: */*
Accept-Language: en
Cache-Control: no-transform
Cf-Connecting_ip: spoofed.dacgflmtle895jd60mfg3pdsanysc4d3p.oast.online
Client-Ip: spoofed.dacgflmtle895jd60mfg498dno6eb8hxf.oast.online
Contact: root@dacgflmtle895jd60mfgudjfgmn8g8jw6.oast.online
Forwarded: for=spoofed.dacgflmtle895jd60mfg7984za5cb6tyo.oast.online;by=spoofed.dacgflmtle895jd60mfg5udnn6iboj19c.oast.online;host=spoofed.dacgflmtle895jd60mfgpzbiib3omidjp.oast.online
From: root@dacgflmtle895jd60mfgdcknoj8358npm.oast.online
Profile: http://dacgflmtle895jd60mfgkruajz6ap5dwb.oast.online/profile.xml
Referer: http://dacgflmtle895jd60mfg63rjagsnezps7.oast.online/ref
True-Client-Ip: spoofed.dacgflmtle895jd60mfg69n48xp6dqrhf.oast.online
X-Client-Ip: spoofed.dacgflmtle895jd60mfg5eii4niogrunt.oast.online
X-Forwarded-For: spoofed.dacgflmtle895jd60mfg5o68te6qxq788.oast.online
X-Forwarded-Host: spoofed.dacgflmtle895jd60mfgpsk5n3atb35fo.oast.online
X-Forwarded-Server: spoofed.dacgflmtle895jd60mfgtdez1nwezbztd.oast.online
X-HTTP-Host-Override: spoofed.dacgflmtle895jd60mfgzgdezmgt7byzu.oast.online
X-Host: spoofed.dacgflmtle895jd60mfg9n4r6jnhk3c38.oast.online
X-Originating-Ip: spoofed.dacgflmtle895jd60mfgbmkaeppk6b97m.oast.online
X-Real-Ip: spoofed.dacgflmtle895jd60mfgqe74a88r7dkjx.oast.online
X-Wap-Profile: http://dacgflmtle895jd60mfgdmp5fknj1fxo5.oast.online/wap.xml
Accept-Encoding: gzip


```

**Response**
```http
HTTP/1.1 302 Found
Cache-Control: no-cache, must-revalidate, max-age=0, no-store, private
Content-Type: text/html; charset=UTF-8
Date: Thu, 03 Sep 2026 05:43:02 GMT
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Location: http://172.20.0.7/wp-admin/install.php
Server: Apache/2.4.68 (Debian)
X-Powered-By: PHP/8.3.33
X-Redirect-By: WordPress
Content-Length: 0


```
**Interaction Data**
----
dns (A) Interaction from 187.86.167.59 at dacgflmtle895jd60mfg5o68te6qxq788
**Interaction Request**
```
;; opcode: QUERY, status: NOERROR, id: 18976
;; flags:; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version 0; flags: do; udp: 512
; COOKIE: 55ec5bca741602b0

;; QUESTION SECTION:
;_.dacgflmtle895jd60mfg5o68te6qxq788.oast.online.	IN	 A

```

**Interaction Response**
```
;; opcode: QUERY, status: NOERROR, id: 18976
;; flags: qr aa; QUERY: 1, ANSWER: 1, AUTHORITY: 2, ADDITIONAL: 2

;; QUESTION SECTION:
;_.dacgflmtle895jd60mfg5o68te6qxq788.oast.online.	IN	 A

;; ANSWER SECTION:
_.dacgflmtle895jd60mfg5o68te6qxq788.oast.online.	3600	IN	A	178.128.87.9

;; AUTHORITY SECTION:
_.dacgflmtle895jd60mfg5o68te6qxq788.oast.online.	3600	IN	NS	ns1.oast.online.
_.dacgflmtle895jd60mfg5o68te6qxq788.oast.online.	3600	IN	NS	ns2.oast.online.

;; ADDITIONAL SECTION:
ns1.oast.online.	3600	IN	A	178.128.87.9
ns2.oast.online.	3600	IN	A	178.128.87.9

```

References: 
- https://github.com/PortSwigger/collaborator-everywhere

**CURL command**
```sh
curl -X 'GET' -d '' -H 'Accept: */*' -H 'Accept-Language: en' -H 'Cache-Control: no-transform' -H 'Cf-Connecting_ip: spoofed.dacgflmtle895jd60mfg3pdsanysc4d3p.oast.online' -H 'Client-Ip: spoofed.dacgflmtle895jd60mfg498dno6eb8hxf.oast.online' -H 'Contact: root@dacgflmtle895jd60mfgudjfgmn8g8jw6.oast.online' -H 'Forwarded: for=spoofed.dacgflmtle895jd60mfg7984za5cb6tyo.oast.online;by=spoofed.dacgflmtle895jd60mfg5udnn6iboj19c.oast.online;host=spoofed.dacgflmtle895jd60mfgpzbiib3omidjp.oast.online' -H 'From: root@dacgflmtle895jd60mfgdcknoj8358npm.oast.online' -H 'Profile: http://dacgflmtle895jd60mfgkruajz6ap5dwb.oast.online/profile.xml' -H 'Referer: http://dacgflmtle895jd60mfg63rjagsnezps7.oast.online/ref' -H 'True-Client-Ip: spoofed.dacgflmtle895jd60mfg69n48xp6dqrhf.oast.online' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 root@dacgflmtle895jd60mfge174wfc9h4krq.oast.online' -H 'X-Client-Ip: spoofed.dacgflmtle895jd60mfg5eii4niogrunt.oast.online' -H 'X-Forwarded-For: spoofed.dacgflmtle895jd60mfg5o68te6qxq788.oast.online' -H 'X-Forwarded-Host: spoofed.dacgflmtle895jd60mfgpsk5n3atb35fo.oast.online' -H 'X-Forwarded-Server: spoofed.dacgflmtle895jd60mfgtdez1nwezbztd.oast.online' -H 'X-HTTP-Host-Override: spoofed.dacgflmtle895jd60mfgzgdezmgt7byzu.oast.online' -H 'X-Host: spoofed.dacgflmtle895jd60mfg9n4r6jnhk3c38.oast.online' -H 'X-Originating-Ip: spoofed.dacgflmtle895jd60mfgbmkaeppk6b97m.oast.online' -H 'X-Real-Ip: spoofed.dacgflmtle895jd60mfgqe74a88r7dkjx.oast.online' -H 'X-Wap-Profile: http://dacgflmtle895jd60mfgdmp5fknj1fxo5.oast.online/wap.xml' 'http://172.20.0.7'
```

----

Generated by [Nuclei v3.11.1](https://github.com/projectdiscovery/nuclei)