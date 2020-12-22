import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("sheetcreds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("SampleXeroChecklist").sheet1
data = sheet.get_all_records()



#We will probably need a dedicated google account as our credentials will be tied to us

def countRows() -> int:
    """Return total number of actual rows"""
    name_column = sheet.col_values(1)
    rows = name_column
    return len(rows)

print(countRows())

"""sheet.update_cell(8,1, "CHANGED")  #Update a given cell, row/column/variable""