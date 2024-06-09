import Extracted_Data.ExtractURLS as ExU
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import DB_V3
import Login as L
import requests
from time import sleep


def get_urls_from_target(scan_name, speed=0):
	target = DB_V3.get_target_by_scan_name(scan_name)
	if target != None:
		is_saved, errorMessage =  ExU.save_urls(scan_name, target, speed)
		if not is_saved:
			print(errorMessage)
			return False, errorMessage
		else:
			return True, is_saved
	else:
		errorMessage = "target Not Found!!"
		print(errorMessage)
		return False, errorMessage

def get_forms_from_urls(scan_name, speed=0):
	is_saved, errorMessage = ExU.save_forms(scan_name, speed)
	return is_saved, errorMessage 

def get_data():
	try:
		errorMessage = 'Data Extracted Successfully from DB'
		return True , DB_V3.get_all_forms_with_url()
	except Exception as e:
		errorMessage = f'Error in get_data function whilte get all froms from db {e}'
		return False, errorMessage

def RunScan(scan_name, speed=0):
	try:
		DB_V3.clear_urls_and_forms()
		is_get_data, errorMessage = get_urls_from_target(scan_name, speed)
		
		if not is_get_data:
			return False, errorMessage

		is_get_form, errorMessage = get_forms_from_urls(scan_name, speed)

		if not is_get_form:
			return False, errorMessage

		is_login_sc , errorMessage = L.Login(scan_name, 'test', 'test', 0).login()
		print("The Scan Finshed !!")
		return is_login_sc, errorMessage
	except Exception as e:
		errorMessage = f'Unkown error in RunScan function {e}'
		print(errorMessage)
		return False, errorMessage

status, errorMessage = RunScan('vulnweb')

print(status, " ",errorMessage)