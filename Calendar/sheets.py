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
event_dict = {}

while still_receiving:
    cur_col = sheet.col_values(col_i)

    # if len(cur_col) == 1 or len(cur_col) == 0:
    if len(cur_col) == 0:
        still_receiving = False

    elif len(cur_col) != 1:
        event_dict[col_i-2] = []
        chunk_i = 1

        # COOKING SECTION

        while len(cur_col) % 5 != 1:
            cur_col.append('')

        while chunk_i < len(cur_col):
            event_dict[col_i - 2].append(Event(cur_col[chunk_i], cur_col[chunk_i + 1], cur_col[chunk_i + 2], cur_col[chunk_i + 3], cur_col[chunk_i + 4]))
            chunk_i += 5

        # COOKING SECTION

        '''while chunk_i < len(cur_col): # len(cur_col) is 9

            # chunk =
            while chunk_i % 5 != 0:
                cur_col.append('')
                chunk_i += 1

            event_dict[col_i - 2].append(Event(cur_col[chunk_i - 4], cur_col[chunk_i - 3], cur_col[chunk_i - 2], cur_col[chunk_i - 1], cur_col[chunk_i]))
            # chunk_i += 5'''

    col_i += 1


'''for z in range(len(event_dict)):

    print(f"Day {z}")
    event_dict[z].event_print()
    print()

# print(testcol)
# print(data)'''