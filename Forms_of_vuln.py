def SSL_TLS_Form():
	vuln_name = '''
TLS Version 1.0 Protocol Detection
	'''
	vuln_sev  = '''
MEDIUM
	'''
	vuln_Description_form = '''
These vulnerabilities could compromise the confidentiality and integrity of data transmitted over secure connections.
	'''
	vuln_Impactes_form = '''
Data Breaches: Vulnerabilities can allow attackers to steal sensitive data like passwords and financial info.
Privacy Risks: Your private information might not stay private if attackers can listen in on supposedly secure communications.
Data Tampering: Attackers could change data being sent, leading to potential manipulation of important information.
Trust Issues: Users might lose trust in websites and services, impacting their reputation and causing financial losses.
Legal Trouble: Violating data security regulations could lead to fines and legal consequences.
Financial Losses: Dealing with security incidents can be expensive, from investigating breaches to compensating affected parties.
Service Disruptions: Attacks could disrupt normal operations, causing downtime and chaos.
Reputation Damage: Publicizing security breaches can harm an organization's reputation, driving away customers and partners.
	'''
	vuln_Soluation_form = '''
Enable support for TLS 1.2 and 1.3, and disable support for TLS 1.0.
	'''
	vuln_See_Also_form = '''
https://tools.ietf.org/html/draft-ietf-tls-oldversions-deprecate-00
	'''
	vuln_Output_form = '''
	'''
	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form

def TRACE_TRACK_Mathod_Form():
	vuln_name = '''
HTTP TRACE / TRACK Methods Allowed
	'''
	vuln_sev  = '''
MEDIUM
	'''
	vuln_Description_form = '''
The TRACE and/or TRACK method in web servers allows clients to see the request as received by the server. Essentially, when a client sends a TRACE request to the server, the server echoes back the received request, which can include sensitive information such as authentication credentials or cookies.
	'''
	vuln_Impactes_form = '''
Allowing the TRACE method on a web server can lead to security risks such as Cross-Site Tracing (XST), information disclosure, vulnerabilities, unpredictable proxy behavior, and non-compliance with security best practices and standards.
	'''
	vuln_Soluation_form = '''
To mitigate risks, disable the TRACE method on the web server unless essential for debugging. This reduces the attack surface and minimizes security vulnerabilities.
	'''
	vuln_See_Also_form = '''
http://www.apacheweek.com/issues/03-01-24
https://download.oracle.com/sunalerts/1000718.1.html
	'''
	vuln_Output_form = '''
	'''
	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form

def PHP_Unsupported_Version_Detection():
	vuln_name = '''
PHP Unsupported Version Detection
	'''
	vuln_sev  = '''
CRITICAL
	'''
	vuln_Description_form = '''
According to its version, the installation of PHP on the remote host is no longer supported.

Lack of support implies that no new security patches for the product will be released by the vendor. As a result, it is likely to contain security vulnerabilities.
	'''
	vuln_Impactes_form = '''
Security Vulnerabilities: Unsupported versions of PHP may contain known security vulnerabilities that have not been patched by the vendor. Hackers actively scan for and exploit these vulnerabilities to compromise systems.

No Security Updates: Without vendor support, there will be no official security updates or patches released to fix any vulnerabilities discovered in the unsupported version. This leaves the system exposed to potential attacks and compromises.

Compliance Issues: Running unsupported software may violate regulatory or compliance requirements, leading to potential legal consequences or fines.

Compatibility Issues: Unsupported PHP versions may not be compatible with newer software or libraries, limiting the ability to update or integrate with other systems.

Performance and Stability: Unsupported software may lack performance optimizations and bug fixes, leading to potential performance issues or instability in production environments.
	'''
	vuln_Soluation_form = '''
Upgrade to a version of PHP that is currently supported.
	'''
	vuln_See_Also_form = '''
http://php.net/eol.php
https://wiki.php.net/rfc/releaseprocess
	'''
	vuln_Output_form = '''
	'''
	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form

def PUT_DELETE_Mathod_Form():
	vuln_name = '''
Web Server HTTP Dangerous Method Detection
	'''
	vuln_sev  = '''
HIGH
	'''
	vuln_Description_form = '''
The PUT method enables an attacker to upload any web pages onto the server. If the server is set up to handle scripts such as ASP, JSP, or PHP, this could empower the attacker to run code using the web server's privileges.
The DELETE method allows an attacker to delete arbitrary content from the web server.
	'''
	vuln_Impactes_form = '''
<span style="font-weight:600;">Increased functionality</span>: By allowing PUT and DELETE requests, web servers can support more complex interactions with clients, enabling them to update or delete resources on the server.
<br><span style="font-weight:600;">RESTful API support</span>: PUT and DELETE are commonly used in RESTful APIs to create, update, and delete resources. Allowing these methods enables developers to build RESTful APIs on top of the web server.
<br><span style="font-weight:600;">Data modification</span>: PUT requests are typically used to update existing resources, while DELETE requests are used to remove resources. Allowing these methods means clients can modify the server's data directly.
<br><span style="font-weight:600;">Security concerns</span>: Allowing PUT and DELETE requests requires careful consideration of security implications. Without proper authentication and authorization mechanisms in place, malicious users could potentially modify or delete sensitive data on the server.
<br><span style="font-weight:600;">Idempotent operations</span>: Both PUT and DELETE operations are idempotent, meaning that making the same request multiple times will have the same effect as making it once. This property can simplify error handling and make it easier to design robust client-server interactions.
<br><span style="font-weight:600;">HTTP method semantics</span>: By adhering to HTTP method semantics, web servers can improve interoperability and consistency across different clients and servers. This can lead to more predictable behavior and easier debugging.
	'''
	vuln_Soluation_form = '''
To allow PUT and DELETE methods on a web server securely:

1.Implement strong authentication and authorization.
2.Validate input to prevent security vulnerabilities.
3.Log requests for auditing and troubleshooting.
4.Handle errors gracefully.
5.Test thoroughly.
6.Document usage for clarity.
or 
Disable the PUT and/or DELETE method in the web server configuration.
	'''
	vuln_See_Also_form = '''
https://tools.ietf.org/html/rfc7231#section-4.3.4

https://tools.ietf.org/html/rfc7231#section-4.3.5
	'''
	vuln_Output_form = '''
	'''

	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form


def OPTIONS_Mathod_Form():
	vuln_name = '''
HTTP Methods Allowed
	'''
	vuln_sev  = '''
INFO
	'''
	vuln_Description_form = '''
The OPTIONS method in HTTP lets a client check which HTTP methods and capabilities a web server supports. Enabling OPTIONS provides clarity and helps clients understand how they can interact with the server.
	'''
	vuln_Impactes_form = '''
Allowing the OPTIONS method on a web server has several impacts:

Interoperability: Enhances communication between clients and servers by clarifying supported HTTP methods.
Security: Supports CORS, aiding in preventing cross-origin attacks and ensuring safe data transfers.
API Documentation: Facilitates documentation of API endpoints and methods available on the server.
Resource Discovery: Helps clients discover available resources and their supported methods.
Compliance: Ensures adherence to HTTP standards, promoting consistency and compatibility across systems.
	'''
	vuln_Soluation_form = '''
Ensure security by configuring CORS properly.
Utilize OPTIONS for comprehensive API documentation.
Implement access controls to manage OPTIONS requests.
Test server responses to OPTIONS requests.
Ensure compliance with relevant standards.
Monitor server logs for any unusual activity.
	'''
	vuln_See_Also_form = '''
https://www.owasp.org/index.php/Test_HTTP_Methods_(OTG-CONFIG-006)
	'''
	vuln_Output_form = '''
	'''

	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form

def Content_Security_Policy_Header_Missing():
	vuln_name = '''
Missing Content Security Policy
	'''
	vuln_sev  = '''
LOW
	'''
	vuln_Description_form = '''
This website lacks a Content Security Policy (CSP), which is a crucial web security standard aimed at thwarting various attacks such as cross-site scripting (XSS),clickjacking, and mixed content issues. 
CSP enables websites to define rules restricting what content browsers are permitted to load. The absence of a CSP header has been noted on this host, with the provided URL serving as an illustrative example.
	'''
	vuln_Impactes_form = '''
The absence of a Content Security Policy (CSP) on a website exposes it to various security risks such as XSS attacks and data breaches. 
This can result in loss of user trust, legal issues, negative SEO effects, and compromised website security. 
Implementing a CSP is crucial for safeguarding the website and its users against these threats.
	'''
	vuln_Soluation_form = '''
Set up Content Security Policy (CSP) for your website either through the addition of the 'Content-Security-Policy' HTTP header or by inserting a meta tag with 'Content-Security-Policy' specified as the http-equiv attribute.
	'''
	vuln_See_Also_form = '''
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
	'''
	vuln_Output_form = '''
	'''

	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form

def Permissions_Policy_Header_Missing():
	vuln_name = '''
Missing Referrer Policy
	'''
	vuln_sev  = '''
INFO
	'''
	vuln_Description_form = '''
The Permissions Policy offers websites the ability to control the utilization of browser functionalities within their own framework and within embedded iframes.	
No Referrer Policy header or metatag configuration has been detected.
'''
	vuln_Impactes_form = '''
The absence of a Permissions Policy on websites can result in security vulnerabilities, privacy risks, negative user experiences, compliance issues, and interoperability challenges.
Implementing a robust Permissions Policy is crucial for safeguarding user data and ensuring secure browsing experiences.
	'''
	vuln_Soluation_form = '''
Adjust the Referrer Policy of your website either by including the 'Referrer-Policy' HTTP header or by implementing the meta tag for referrer within your HTML code.
	'''
	vuln_See_Also_form = '''
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy
https://scotthelme.co.uk/goodbye-feature-policy-and-hello-permissions-policy/
	'''
	vuln_Output_form = '''
	'''

	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form

def Referrer_Policy_Header_Missing():
	vuln_name = '''
Missing Referrer Policy
	'''
	vuln_sev  = '''
INFO
	'''
	vuln_Description_form = '''
The website lacks a Referrer Policy, which typically allows sites to control the information browsers send in the "referer" header.
There's no evidence of any Referrer Policy header or metatag configuration.
	'''
	vuln_Impactes_form = '''
The absence of a Referrer Policy on a website can lead to privacy concerns, security risks, data leakage, SEO and analytics issues, and vulnerabilities in handling cross-origin requests.
Implementing a Referrer Policy is crucial for maintaining user privacy, enhancing security, and ensuring data integrity.
	'''
	vuln_Soluation_form = '''
You can implement Referrer Policy on your website either by including the 'Referrer-Policy' HTTP header or by using the meta tag 'referrer' in your HTML code.
	'''
	vuln_See_Also_form = '''
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
	'''
	vuln_Output_form = '''
	'''

	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form

def Duplicate_HTTP_Headers():
	vuln_name = '''
Duplicate HTTP Headers Detected
	'''
	vuln_sev  = '''
INFO
	'''
	vuln_Description_form = '''
Multiple occurrences of HTTP headers with identical names have been identified. According to RFC 7230, a server should not produce multiple header fields sharing the same name 
unless either the entire value for that header is specified as a comma-separated list or the header field is a recognized exception.
If strings are divided across multiple instances of the header, unexpected outcomes may occur, as additional elements like commands and whitespace could be introduced during recombination,
beyond the control of the initial serializer.
	'''
	vuln_Impactes_form = '''
	'''
	vuln_Soluation_form = '''
Make sure that each HTTP header or meta tag with http-equiv declarations has a unique name.
	'''
	vuln_See_Also_form = '''
https://tools.ietf.org/id/draft-ietf-httpbis-header-structure-15.html
https://www.rfc-editor.org/rfc/rfc7230#section-3.2.2
	'''
	vuln_Output_form = '''
	'''

	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form

def X_XSS_Header_Missing():
	vuln_name = '''
Missing 'X-XSS-Protection' Header
	'''
	vuln_sev  = '''
INFO
	'''
	vuln_Description_form = '''
The absence of the 'X-XSS-Protection' header in the server configuration exposes this website to potential Cross-Site Scripting (XSS) vulnerabilities.
Without this header, modern browsers lack control over their XSS auditors, putting pages at risk. To mitigate this risk, consider implementing Content-Security-Policy, 
disallowing unsafe-inline scripts, especially if legacy browser support isn't a requirement.
	'''
	vuln_Impactes_form = '''
The absence of the 'X-XSS-Protection' header on a website can lead to Cross-Site Scripting (XSS) vulnerabilities, exposing users to various risks such as data theft,
session hijacking, malware distribution, defacement, financial losses, reputation damage, and regulatory non-compliance.
Implementing proper security measures like the 'X-XSS-Protection' header and Content-Security-Policy is crucial to mitigate these risks and safeguard both the website and its users.
	'''
	vuln_Soluation_form = '''
Set up your web server to incorporate an 'X-XSS-Protection' header with the setting '1; mode=block' across all pages.
	'''
	vuln_See_Also_form = '''
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection
https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#xxxsp
	'''
	vuln_Output_form = '''
	'''

	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form

def webserver_name_Form(serverName):
	vuln_name = ''
	vuln_sev = ''
	vuln_Description_form = ''
	vuln_Impactes_form = ''
	vuln_Soluation_form = ''
	vuln_See_Also_form = ''
	vuln_Output_form = ''

	if serverName == "Apache":
		vuln_name = f'''
{serverName} HTTP Server Installed (Linux)
		'''
		vuln_sev  = '''
INFO
		'''
		vuln_Description_form = f'''
The remote host has {serverName} HTTP Server software installed, indicating that {serverName} HTTP Server, a widely used web server software, is present on the Linux system.
		'''
		vuln_Impactes_form = '''
		'''
		vuln_Soluation_form = '''
		'''
		vuln_See_Also_form = '''
https://httpd.apache.org/
		'''
	elif serverName == "Nginx":

		vuln_name = f'''
{serverName} Unit HTTP Server Detection
		'''
		vuln_sev  = '''
INFO
		'''
		vuln_Description_form = f'''
The NGINX Unit HTTP server was detected on the remote host by examining the HTTP banner, as determined by CyberScope.
		'''
		vuln_Impactes_form = '''
		'''
		vuln_Soluation_form = '''
		'''
		vuln_See_Also_form = '''
https://nginx.org/
		'''
	elif serverName == "Microsoft-IIS":
		vuln_name = f'''
Microsoft Internet Information Services (IIS) Installed
		'''
		vuln_sev  = '''
INFO
		'''
		vuln_Description_form = f'''
The script checks Windows registry keys and executables for the presence of a Microsoft Internet Information Services (IIS) installation, indicating the detection of IIS on the remote Windows host.
		'''
		vuln_Impactes_form = '''
		'''
		vuln_Soluation_form = '''
		'''
		vuln_See_Also_form = '''
https://www.iis.net/
		'''
	elif serverName == "LiteSpeed":
		vuln_name = f'''
{serverName} HTTP Server Installed
		'''
		vuln_sev  = '''
INFO
		'''
		vuln_Description_form = f'''
The remote host has {serverName} HTTP Server software installed, indicating that {serverName} HTTP Server, a widely used web server software.
		'''
		vuln_Impactes_form = '''
		'''
		vuln_Soluation_form = '''
		'''
		vuln_See_Also_form = '''
https://www.litespeedtech.com/products/litespeed-web-server
		'''
	elif serverName == "OpenResty":
		vuln_name = f'''
{serverName} HTTP Server Installed
		'''
		vuln_sev  = '''
INFO
		'''
		vuln_Description_form = f'''
The remote host has {serverName} HTTP Server software installed, indicating that {serverName} HTTP Server, a widely used web server software.
		'''
		vuln_Impactes_form = '''
		'''
		vuln_Soluation_form = '''
		'''
		vuln_See_Also_form = '''
https://openresty.org/
		'''
	elif serverName == "Tomcat":
		vuln_name = f'''
Apache {serverName} Installed (Windows)
		'''
		vuln_sev  = '''
INFO
		'''
		vuln_Description_form = f'''
Apache Tomcat, a web server, is installed on the remote Windows host, indicating the presence of this software.
		'''
		vuln_Impactes_form = '''
		'''
		vuln_Soluation_form = '''
		'''
		vuln_See_Also_form = '''
https://tomcat.apache.org/
		'''
	elif serverName == "Gunicorn":
		vuln_name = f'''
{serverName} HTTP Server Installed
		'''
		vuln_sev  = '''
INFO
		'''
		vuln_Description_form = f'''
The remote host has {serverName} HTTP Server software installed, indicating that {serverName} HTTP Server, a widely used web server software.
		'''
		vuln_Impactes_form = '''
		'''
		vuln_Soluation_form = '''
		'''
		vuln_See_Also_form = '''
https://gunicorn.org/
		'''
	elif serverName == "Node.js":
		vuln_name = f'''
{serverName} HTTP Server Installed
		'''
		vuln_sev  = '''
INFO
		'''
		vuln_Description_form = f'''
The remote host has {serverName} HTTP Server software installed, indicating that {serverName} HTTP Server, a widely used web server software.
		'''
		vuln_Impactes_form = '''
		'''
		vuln_Soluation_form = '''
		'''
		vuln_See_Also_form = '''
https://nodejs.org/docs/latest/api/
		'''
	elif serverName == "IBM HTTP Server":
		vuln_name = f'''
{serverName} HTTP Server Installed (Linux)
		'''
		vuln_sev  = '''
INFO
		'''
		vuln_Description_form = f'''
The IBM HTTP Server is installed on the remote Linux/Unix host.
		'''
		vuln_Impactes_form = '''
		'''
		vuln_Soluation_form = '''
		'''
		vuln_See_Also_form = '''
https://www.ibm.com/docs/en/ibm-http-server
		'''
	elif serverName == "Jetty":
		vuln_name = f'''
Eclipse Jetty Web Server Detection
		'''
		vuln_sev  = '''
INFO
		'''
		vuln_Description_form = f'''
The remote host has been identified as running the Eclipse Jetty web server.
		'''
		vuln_Impactes_form = '''
		'''
		vuln_Soluation_form = '''
		'''
		vuln_See_Also_form = '''
https://eclipse.dev/jetty/
		'''
	vuln_Output_form = '''
	'''

	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form


def Content_Type_Header_Missing():
	vuln_name = '''
Missing 'Content-Type' Header
	'''
	vuln_sev  = '''
LOW
	'''
	vuln_Description_form = '''
The absence of the 'Content-Type' header in HTTP responses prevents clients from identifying the appropriate method to render data. 
This omission poses a risk as it can enable MIME sniffing attacks, where browsers attempt to interpret data in unintended ways, potentially compromising security.
	'''
	vuln_Impactes_form = '''
Rendering Ambiguity: Without the 'Content-Type' header, clients may struggle to correctly interpret data, leading to rendering errors or improper display of content.
Security Vulnerabilities: Omission of the header opens doors to MIME sniffing attacks, where malicious actors exploit browser behavior to execute scripts or access sensitive information.
Compatibility Issues: Lack of clear data type indication can cause compatibility issues across different platforms and applications, disrupting user experience and functionality.
	'''
	vuln_Soluation_form = '''
Set up your web server to incorporate a 'Content-Type' header containing the appropriate Content-Type specification.
	'''
	vuln_See_Also_form = '''
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type
https://www.iana.org/assignments/media-types/media-types.xhtml
https://www.w3.org/Protocols/rfc1341/4_Content-Type.html
	'''
	vuln_Output_form = '''
	'''

	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form


def Cache_Control_Header_Missing():
	vuln_name = '''
Missing 'Cache-Control' Header
	'''
	vuln_sev  = '''
LOW
	'''
	vuln_Description_form = '''
Missing 'Cache-Control' Header and this HTTP header is used to specify directives for caching mechanisms.
	'''
	vuln_Impactes_form = '''
The absence or misconfiguration of the 'Cache-Control' header can lead to significant impacts. Sensitive information, including passwords, credit card details, personal data, or social security numbers, may inadvertently reside on the client-side disk.
Consequently, unauthorized individuals could access this data, potentially leading to breaches of privacy and security. This URL serves as a tangible illustration of the risks associated with such oversight.
	'''
	vuln_Soluation_form = '''
Set up your web server to incorporate a 'Cache-Control' header with relevant directives. 
When the page contains sensitive information, set the 'Cache-Control' value to 'no-store', and ensure that the 'Pragma' header value is set to 'no-cache'.
	'''
	vuln_See_Also_form = '''
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control
https://www.owasp.org/index.php/Testing_for_Browser_cache_weakness_(OTG-AUTHN-006)
	'''
	vuln_Output_form = '''
	'''

	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form


def X_Content_Type_Options_Header_Missing():
	vuln_name = '''
Missing 'X-Content-Type-Options' Header
	'''
	vuln_sev  = '''
LOW
	'''
	vuln_Description_form = '''
When a website fails to include the 'X-Content-Type-Options' header in its HTTP response, it opens itself up to potential security vulnerabilities. 
This header is crucial as it prevents browsers from MIME-sniffing responses away from the declared content type. Without it, browsers may incorrectly interpret content, leaving the site susceptible to attacks like Cross-Site Scripting (XSS).
	'''
	vuln_Impactes_form = '''
The impact of missing this header is significant. Without proper enforcement of content types, malicious actors could manipulate the browser into executing script content as if it were from a trusted source. 
This could lead to various security breaches, including the injection of harmful scripts that steal sensitive user information or hijack user sessions.
	'''
	vuln_Soluation_form = '''
To mitigate this risk and ensure the security of the website and its users, it's imperative for web developers to include the 'X-Content-Type-Options' header with the appropriate value (e.g., "nosniff") in their HTTP responses.
This simple measure can significantly enhance the site's security posture and protect against potential XSS attacks.
	'''
	vuln_See_Also_form = '''
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options
https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#xcto
	'''
	vuln_Output_form = '''
	'''

	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form


def X_Frame_Options_Header_Missing():
	vuln_name = '''
Missing 'X-Frame-Options' Header
	'''
	vuln_sev  = '''
LOW
	'''
	vuln_Description_form = '''
By analyzing the remote operating system, one can discern the type of remote system, whether it's a printer, router, general-purpose computer, or otherwise.
	'''
	vuln_Impactes_form = '''
	'''
	vuln_Soluation_form = '''
	'''
	vuln_See_Also_form = '''
	'''
	vuln_Output_form = '''
	'''

	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form


def webserver_name_Form():
	vuln_name = '''
Device Type
	'''
	vuln_sev  = '''
INFO
	'''
	vuln_Description_form = '''
By analyzing the remote operating system, one can discern the type of remote system, whether it's a printer, router, general-purpose computer, or otherwise.
	'''
	vuln_Impactes_form = '''
	'''
	vuln_Soluation_form = '''
	'''
	vuln_See_Also_form = '''
	'''
	vuln_Output_form = '''
	'''

	return vuln_name, vuln_sev, vuln_Description_form, vuln_Impactes_form, vuln_Soluation_form, vuln_See_Also_form, vuln_Output_form


