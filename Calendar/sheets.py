# testing sheet reading here
# if pip installation is having trouble: https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command
# pip install gspread oauth2client

from calendar_class import Event
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("CourseCal_dataset").sheet1

# data = sheet.get_all_records()
# testcol = sheet.col_values(3)

still_receiving = True
col_i = 3
event_vec = []

while still_receiving:
    cur_col = sheet.col_values(col_i)

    # if len(cur_col) == 1 or len(cur_col) == 0:
    if len(cur_col) == 0:
        still_receiving = False

    else:
        while len(cur_col) < 6:
            cur_col.append('')

        event_vec.append(Event(cur_col[1], cur_col[2], cur_col[3], cur_col[4], cur_col[5]))
        col_i += 1


for z in range(len(event_vec)):

    print(f"Day {z}")
    event_vec[z].event_print()
    print()

# print(testcol)
# print(data)