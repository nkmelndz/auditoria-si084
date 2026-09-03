### README.md file disclosure (readme-md) found on 172.20.0.6

----
**Details**: **readme-md** matched at 172.20.0.6

**Protocol**: HTTP

**Full URL**: http://172.20.0.6/README.md

**Timestamp**: Thu Sep 3 05:43:23 +0000 UTC 2026

**Template Information**

| Key | Value |
| --- | --- |
| Name | README.md file disclosure |
| Authors | ambassify |
| Tags | exposure, markdown, files, vuln |
| Severity | info |
| Description | Internal documentation file often used in projects which can contain sensitive information. |
| shodan-query | html:"README.MD" |

**Request**
```http
GET /README.md HTTP/1.1
Host: 172.20.0.6
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: */*
Accept-Language: en
Accept-Encoding: gzip


```

**Response**
```http
HTTP/1.1 200 OK
Content-Length: 9180
Accept-Ranges: bytes
Content-Type: text/markdown
Date: Thu, 03 Sep 2026 05:43:23 GMT
Etag: "23dc-5780ba3955700"
Last-Modified: Fri, 12 Oct 2018 17:44:28 GMT
Server: Apache/2.4.25 (Debian)

# DAMN VULNERABLE WEB APPLICATION

Damn Vulnerable Web Application (DVWA) is a PHP/MySQL web application that is damn vulnerable. Its main goal is to be an aid for security professionals to test their skills and tools in a legal environment, help web developers better understand the processes of securing web applications and to aid both students & teachers to learn about web application security in a controlled class room environment.

The aim of DVWA is to **practice some of the most common web vulnerabilities**, with **various levels of difficulty**, with a simple straightforward interface.
Please note, there are **both documented and undocumented vulnerabilities** with this software. This is intentional. You are encouraged to try and discover as many issues as possible.
- - -

## WARNING!

Damn Vulnerable Web Application is damn vulnerable! **Do not upload it to your hosting provider's public html folder or any Internet facing servers**, as they will be compromised. It is recommended using a virtual machine (such as [VirtualBox](https://www.virtualbox.org/) or [VMware](https://www.vmware.com/)), which is set to NAT networking mode. Inside a guest machine, you can download and install [XAMPP](https://www.apachefriends.org/en/xampp.html) for the web server and database.

### Disclaimer

We do not take responsibility for the way in which any one uses this application (DVWA). We have made the purposes of the application clear and it should not be used maliciously. We have given warnings and taken measures to prevent users from installing DVWA on to live web servers. If your web server is compromised via an installation of DVWA it is not our responsibility it is the responsibility of the person/s who uploaded and installed it.

- - -

## License

This file is part of Damn Vulnerable Web Application (DVWA).

Damn Vulnerable Web Application (DVWA) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Damn Vulnerable Web Application (DVWA) is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Damn Vulnerable Web Application (DVWA).  If not, see http://www.gnu.org/licenses/.

- - -
## Download and install as a docker container
- [dockerhub page](https://hub.docker.com/r/vulnerables/web-dvwa/)
\`docker run --rm -it -p 80:80 vulnerables/web-dvwa\`

Please ensure you are using aufs due to previous MySQL issues. Run \`docker info\` to check your storage driver. If it isn't aufs, please change it as such. There are guides for each operating system on how to do that, but they're quite different so we won't cover that here.

## Download

DVWA is available either as a package that will run on your own web server or as a Live CD:

  + DVWA v1.9 Source (Stable) - \\[1.3 MB\\] [Download ZIP](https://github.com/ethicalhack3r/DVWA/archive/v1.9.zip) - Released 2015-10-05
  + DVWA v1.0.7 LiveCD - \\[480 MB\\] [Download ISO](http://www.dvwa.co.uk/DVWA-1.0.7.iso) - Released 2010-09-08
  + DVWA Development Source (Latest) [Download ZIP](https://github.com/ethicalhack3r/DVWA/archive/master.zip) // \`git clone https://github.com/ethicalhack3r/DVWA\`

- - -

## Installation

**Please make sure your config/config.inc.php file exists. Only having a config.inc.php.dist will not be sufficient and you'll have to edit it to suit your environment and rename it to config.inc.php. [Windows may hide the trailing extension.](https://support.microsoft.com/en-in/help/865219/how-to-show-or-hide-file-name-extensions-in-windows-explorer)**

### Installation Videos

- [How to setup DVWA (Damn Vulnerable Web Application) on Ubuntu](https://www.youtube.com/watch?v=5BG6iq_AUvM) [21:01 minutes]
- [Installing Damn Vulnerable Web Application (DVWA) on Windows 10](https://www.youtube.com/watch?v=cak2lQvBRAo) [12:39 minutes]

### Windows + XAMPP

The easiest way to install DVWA is to download and install [XAMPP](https://www.apachefriends.org/en/xampp.html) if you do not already have a web server setup.

XAMPP is a very easy to install Apache Distribution for Linux, Solaris, Windows and Mac OS X. The package includes the Apache web server, MySQL, PHP, Perl, a FTP server and phpMyAdmin.

XAMPP can be downloaded from:
https://www.apachefriends.org/en/xampp.html

Simply unzip dvwa.zip, place the unzipped files in your public html folder, then point your browser to: http://127.0.0.1/dvwa/setup.php

### Linux Packages

If you are using a Debian based Linux distribution, you will .... Truncated ....
```


**CURL command**
```sh
curl -X 'GET' -d '' -H 'Accept: */*' -H 'Accept-Language: en' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0' 'http://172.20.0.6/README.md'
```

----

Generated by [Nuclei v3.11.1](https://github.com/projectdiscovery/nuclei)