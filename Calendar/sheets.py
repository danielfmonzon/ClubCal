# testing sheet reading here
# if pip installation is having trouble: https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command
# pip install gspread oauth2client

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("CourseCal_dataset").sheet1

data = sheet.get_all_records()
testcol = sheet.col_values(3)

print(testcol)
# print(data)