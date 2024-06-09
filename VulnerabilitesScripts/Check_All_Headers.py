import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import DB_V3
import requests
from time import sleep

class CheckHeaders(object):
	def __init__(self, scan_name, speed=0):
		super(CheckHeaders, self).__init__()
		self.scan_name  = scan_name
		self.speed      = speed
		self.scan_id    = DB_V3.get_scan_id_by_name(self.scan_name)
		self.urls       = DB_V3.get_urls_by_scan_id(self.scan_id)
		self.target     = DB_V3.get_target_by_scan_name(self.scan_name)
		self.target_id  = DB_V3.get_url_id_by_url(self.target)
		self.headers    = ['X-XSS-Protection','Referrer-Policy','Permissions-Policy', 'Content-Security-Policy', 'Content-Type', 'Cache-Control', 'X-Content-Type-Options', 'X-Frame-Options']
		self.vuln_names = ["TLS Version 1.0 Protocol Detection","HTTP TRACE / TRACK Methods Allowed","PHP Unsupported Version Detection","Web Server HTTP Dangerous Method Detection","HTTP Methods Allowed","Missing Content Security Policy","Missing Referrer Policy","Missing Referrer Policy","Duplicate HTTP Headers Detected","Missing 'X-XSS-Protection' Header","Missing 'Content-Type' Header","Missing 'Cache-Control' Header","Missing 'X-Content-Type-Options' Header","Missing 'X-Frame-Options' Header","Device Type 15"]

	def check_messing_headers(self):
		try:
			r = requests.get(self.target, timeout=15)
			for messing_header in self.headers:
				if messing_header not in r.headers:
					if messing_header == self.headers[0]:
						vulnerability_id = DB_V3.get_vulnerability_id_by_name(self.vuln_names[11])
						count = DB_V3.get_count_by_vulnerability_id(vulnerability_id)
						if count != None and count == 0:
							count += 1
							output = 'None'
							DB_V3.insert_scan_result(self.scan_id, vulnerability_id, self.target_id, count, output)
					if messing_header == self.headers[1]:
						vulnerability_id = DB_V3.get_vulnerability_id_by_name(self.vuln_names[6])
						count = DB_V3.get_count_by_vulnerability_id(vulnerability_id)
						if count != None and count == 0:
							count += 1
							output = 'None'
							DB_V3.insert_scan_result(self.scan_id, vulnerability_id, self.target_id, count, output)							
					if messing_header == self.headers[2]:
						vulnerability_id = DB_V3.get_vulnerability_id_by_name(self.vuln_names[7])
						count = DB_V3.get_count_by_vulnerability_id(vulnerability_id)
						if count != None and count == 0:
							count += 1
							output = 'None'
							DB_V3.insert_scan_result(self.scan_id, vulnerability_id, self.target_id, count, output)
					if messing_header == self.headers[3]:
						vulnerability_id = DB_V3.get_vulnerability_id_by_name(self.vuln_names[5])
						count = DB_V3.get_count_by_vulnerability_id(vulnerability_id)
						if count != None and count == 0:
							count += 1
							output = 'None'
							DB_V3.insert_scan_result(self.scan_id, vulnerability_id, self.target_id, count, output)
					if messing_header == self.headers[4]:
						vulnerability_id = DB_V3.get_vulnerability_id_by_name(self.vuln_names[10])
						count = DB_V3.get_count_by_vulnerability_id(vulnerability_id)
						if count != None and count == 0:
							count += 1
							output = 'None'
							DB_V3.insert_scan_result(self.scan_id, vulnerability_id, self.target_id, count, output)
					if messing_header == self.headers[5]:
						vulnerability_id = DB_V3.get_vulnerability_id_by_name(self.vuln_names[11])
						count = DB_V3.get_count_by_vulnerability_id(vulnerability_id)
						if count != None and count == 0:
							count += 1
							output = 'None'
							DB_V3.insert_scan_result(self.scan_id, vulnerability_id, self.target_id, count, output)
					if messing_header == self.headers[6]:
						vulnerability_id = DB_V3.get_vulnerability_id_by_name(self.vuln_names[12])
						count = DB_V3.get_count_by_vulnerability_id(vulnerability_id)
						if count != None and count == 0:
							count += 1
							output = 'None'
							DB_V3.insert_scan_result(self.scan_id, vulnerability_id, self.target_id, count, output)
					if messing_header == self.headers[7]:
						vulnerability_id = DB_V3.get_vulnerability_id_by_name(self.vuln_names[13])
						count = DB_V3.get_count_by_vulnerability_id(vulnerability_id)
						if count != None and count == 0:
							count += 1
							output = 'None'
							DB_V3.insert_scan_result(self.scan_id, vulnerability_id, self.target_id, count, output)

		except Exception as e:
			print('Error in check_messing_headers function ' + str(e))


	def get_vuln_details_with_id(self, vulnerability_id):
		data = DB_V3.get_vulnerability_by_id(vulnerability_id)
		return data
	def vuln_index(self):
		for i in range(len(self.vuln_names)):
			print(f"Vuln Index {i} of => ",self.vuln_names[i])
		print()
		print('#' * 80)
		print()
		for i in range(len(self.headers)):
			print(f"Vuln Index {i} of => ",self.headers[i])


# x = CheckHeaders('vulnweb')

# x.check_messing_headers()
# x.vuln_index()
# data = x.get_vuln_details_with_id(10)


# print(x.target)
# print(x.target_id)
# print()
# print(data['severity'])
# print()
# print(data['description'])
# print()
# print(data['impact'])
# print()
# print(data['solution'])
# print()
# print(data['see_also'])
# print()