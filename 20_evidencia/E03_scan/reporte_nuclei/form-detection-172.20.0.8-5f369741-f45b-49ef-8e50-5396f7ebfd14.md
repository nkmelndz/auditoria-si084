### Form Detection (form-detection) found on 172.20.0.8

----
**Details**: **form-detection** matched at 172.20.0.8

**Protocol**: HTTP

**Full URL**: https://172.20.0.8/

**Timestamp**: Thu Sep 3 05:41:34 +0000 UTC 2026

**Template Information**

| Key | Value |
| --- | --- |
| Name | Form Detection |
| Authors | pdteam |
| Tags | form, misc, miscellaneous, vuln |
| Severity | info |
| Description | A template to detect HTML Forms in page response.<br> |

**Request**
```http
GET / HTTP/1.1
Host: 172.20.0.8
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15
Accept: */*
Accept-Language: en
Accept-Encoding: gzip


```

**Response**
```http
HTTP/1.1 200 OK
Cache-Control: no-store, no-cache, must-revalidate
Content-Security-Policy: default-src * 'unsafe-inline' 'unsafe-eval' data:
Content-Type: text/html; charset=utf-8
Date: Thu, 03 Sep 2026 05:41:34 GMT
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Referrer-Policy: no-referrer-when-downgrade
Referrer-Policy: origin
Server: Apache
Set-Cookie: ***
Strict-Transport-Security: max-age=63072000; includeSubdomains; preload
Vary: Accept-Encoding
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Xss-Protection: 1; mode=block
X-Xss-Protection: 1; mode=block

<!DOCTYPE html>
<html dir="ltr" lang="en" xml:lang="en">
<head>
    <title>SimpleRisk: Enterprise Risk Management Simplified</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
    
    <!-- Favicon icon -->
    <link rel='shortcut icon' href='favicon.ico' />
    
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/style.min.css?20260828-001" />

    <!-- jQuery CSS -->
    <link rel="stylesheet" href="vendor/node_modules/jquery-ui/dist/themes/base/jquery-ui.min.css?20260828-001">

    <!-- extra css -->
    <link rel="stylesheet" href="vendor/components/font-awesome/css/fontawesome.min.css?20260828-001">

    <!-- jQuery Javascript -->
    <script src="vendor/node_modules/jquery/dist/jquery.min.js?20260828-001" id="script_jquery"></script>
    <script src="vendor/node_modules/jquery-ui/dist/jquery-ui.min.js?20260828-001" id="script_jqueryui"></script>

    <!-- Bootstrap tether Core JavaScript -->
    <script src="vendor/node_modules/bootstrap/dist/js/bootstrap.bundle.min.js" defer></script>

</head>
<body class="sr-auth-page">
    <div class="preloader">
        <div class="lds-ripple">
            <div class="lds-pos"></div>
            <div class="lds-pos"></div>
        </div>
    </div>
    <div class="sr-auth">

        <aside class='sr-auth-brand'>
            <div class='sr-auth-brand-media' aria-hidden='true'></div>
            <div class='sr-auth-brand-scrim' aria-hidden='true'></div>
    
            <span class='sr-auth-brandmark'>
                <img class='sr-auth-brandlogo' src='images/simplerisk-logo-icon.png' alt='SimpleRisk' />
                <span class='sr-auth-brandtext'><span class='s'>Simple</span><span class='r'>Risk</span></span>
            </span>
        
            <p class='sr-auth-tagline sr-auth-tagline--lg'>From ZERO to GRC in minutes.</p>
    
            <p class='sr-auth-legal'>© 2026 SimpleRisk. All rights reserved.</p>
        </aside>
            <main class="sr-auth-main">
            <div class="sr-auth-col">
                <div class="sr-auth-card">
                    <div class="sr-auth-card-head">
                        <h2>Login to SimpleRisk</h2>
                        <p>Enter the credentials for your account.</p>
                    </div>
                    <form class="loginForm" action="" method="post" name="authenticate">
                        <input type="hidden" name="csrf_token" value="4d5df50d1332a50aefbd28e106d2b9ae68b4e44417ea7fc7dfae72f5bd3fe369">
                        <div class="sr-auth-card-body">
                            <div class="sr-auth-field">
                                <label for="user">Username</label>
                                <input type="text" class="form-control user" id="user" name="user" autocomplete="username" value="" required />
                            </div>
                            <div class="sr-auth-field">
                                <label for="pass">Password</label>
                                <div class="sr-auth-pass">
                                    <input type="password" class="form-control pass" id="pass" name="pass" autocomplete="current-password" value="" required />
                                    <span id="eye-icon"><i class="fa fa-eye"></i></span>
                                </div>
                            </div>
                            <div class="sr-auth-linkrow">
                                <a class="sr-auth-link" href="reset.php">Forgot your password</a>
                            </div>
                            <div class="sr-auth-actions">
                                <button type="reset" class="btn btn-dark">Reset</button>
                                <button type="submit" class="btn btn-submit" name="submit" value="submit">Login</button>
                            </div>
                        </div>
                    </form>
                </div>
                <p class="sr-auth-help">Trouble signing in? Contact your SimpleRisk administrator.</p>
            </div>
        </main>
    </div>
    <!-- End Wrapper -->

        <script src='vendor/node_modules/toastr/build/toastr.min.js?20260828-001' defer id='script_toastr'></script>
        <script src='js/simplerisk/alert-helper.js?20260828-001' defer></script>
    
        <script>
            $('#script_toastr').on('load', function() {
                toastr.options.timeOut = 5000;
      .... Truncated ....
```

References: 
- https://github.com/dirtycoder0124/formcrawler

**CURL command**
```sh
curl -X 'GET' -d '' -H 'Accept: */*' -H 'Accept-Language: en' -H 'Referer: http://172.20.0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15' 'https://172.20.0.8/'
```

----

Generated by [Nuclei v3.11.1](https://github.com/projectdiscovery/nuclei)