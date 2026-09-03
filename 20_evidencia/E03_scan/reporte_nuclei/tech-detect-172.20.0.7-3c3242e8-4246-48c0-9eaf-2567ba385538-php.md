### Wappalyzer Technology Detection (tech-detect:php) found on 172.20.0.7

----
**Details**: **tech-detect:php** matched at 172.20.0.7

**Protocol**: HTTP

**Full URL**: http://172.20.0.7/wp-admin/install.php

**Timestamp**: Thu Sep 3 05:43:03 +0000 UTC 2026

**Template Information**

| Key | Value |
| --- | --- |
| Name | Wappalyzer Technology Detection |
| Authors | hakluke, righettod, matejsmycka |
| Tags | tech, discovery |
| Severity | info |

**Request**
```http
GET / HTTP/1.1
Host: 172.20.0.7
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15
Accept: */*
Accept-Language: en
Accept-Encoding: gzip


```

**Response**
```http
HTTP/1.1 200 OK
Cache-Control: no-cache, must-revalidate, max-age=0, no-store, private
Content-Type: text/html; charset=utf-8
Date: Thu, 03 Sep 2026 05:42:56 GMT
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
<body class="wp-core-ui admin-color-modern">
<p id="logo">WordPress</p>

	<h1>Welcome</h1>
<p>Welcome to the famous five-minute WordPress installation process! Just fill in the information below and you&#8217;ll be on your way to using the most extendable and powerful personal publishing platform in the world.</p>

<h2>Information needed</h2>
<p>Please provide the following information. Do not worry, you can always change these settings later.</p>

		<form id="setup" method="post" action="install.php?step=2" novalidate="novalidate">
	<table class="form-table" role="presentation">
		<tr>
			<th scope="row"><label for="weblog_title">Site Title</label></th>
			<td><input name="weblog_title" type="text" id="weblog_title" size="25" value="" /></td>
		</tr>
		<tr>
			<th scope="row"><label for="user_login">Username</label></th>
			<td>
							<input name="user_name" type="text" id="user_login" size="25" aria-describedby="user-name-desc" value="" />
				<p id="user-name-desc">Usernames can have only alphanumeric characters, spaces, underscores, hyphens, periods, and the @ symbol.</p>
							</td>
		</tr>
				<tr class="form-field form-required user-pass1-wrap">
			<th scope="row">
				<label for="pass1">
					Password				</label>
			</th>
			<td>
				<div class="wp-pwd">
										<div class="password-input-wrapper">
						<input type="password" name="admin_password" id="pass1" class="regular-text" autocomplete="new-password" spellcheck="false" data-reveal="1" data-pw="ugBgbUuSWDDMPGv*Aj" aria-describedby="pass-strength-result admin-password-desc" />
						<div id="pass-strength-result" aria-live="polite"></div>
					</div>
					<button type="button" class="button wp-hide-pw user-new-password-toggle hide-if-no-js" data-start-masked="0" data-toggle="0" aria-label="Hide password">
						<span class="dashicons dashicons-hidden"></span>
						<span class="text">Hide</span>
					</button>
				</div>
				<p id="admin-password-desc"><span class="description important hide-if-no-js">
				<strong>Important:</strong>
								You will need this password to log&nbsp;in. Please store it in a secure location.</span></p>
			</td>
		</tr>
		<tr class="form-field form-required user-pass2-wrap hide-if-js">
			<th scope="row">
				<label for="pass2">Repeat Password					<span class="description">(required)</span>
				</label>
			</th>
			<td>
				<input type="password" name="admin_password2" id="pass2" autocomplete="new-password" spellcheck="false" />
			</td>
		</tr>
		<tr class="pw-weak">
			<th scope="row">Confirm Password</th>
			<td>
				<label>
					<input type="checkbox" name="pw_weak" class="pw-checkbox" />
					Confirm use of weak password				</label>
			</td>
		</tr>
				<tr>
			<th scope="row"><label for="admin_email">Your Email</label></th>
			<td><input name="admin_email" type="email" id="admin_email" size="25" aria-describedby="admin-email-desc" value="" />
			<p id="admin-email-desc">Double-check your email address before continuing.</p></td>
		</tr>
				<tr>
			<th scope="row">Search engine visibility</th>
			<td>
				<fieldset>
					<legend class="screen-reader-text"><span>Search engine visibility</span></legend>
											<label for="blog_public"><input name="blog_public" type="checkbox" id="blog_public" aria-describedby="privacy-desc" value="0"  />
						Discourage search engines from indexing this site</label>
						<p id="privacy-desc" class="description">It is up to search engines to honor this request.</p>
									</fieldset>
			</td>
		</tr>
	</table>
	<p class="step"><input type="submit" name="Submit" id="submit" class="button button-large" value="Install WordPress"  /></p>
	<input type="hidden" name="language" value="" />
</form>
	<script>var t = document.getElementById('weblog_title'); if (t){ t.focus(); }</script>
	<script id=".... Truncated ....
```


**CURL command**
```sh
curl -X 'GET' -d '' -H 'Accept: */*' -H 'Accept-Language: en' -H 'Referer: http://172.20.0.7' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15' 'http://172.20.0.7/wp-admin/install.php'
```

----

Generated by [Nuclei v3.11.1](https://github.com/projectdiscovery/nuclei)