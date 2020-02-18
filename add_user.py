import os
import sys
try:
    import gspread
except ImportError:
    sys.path.append('/home/takeda1411123/.pyenv/versions/add_user_gcp/lib/python3.7/site-packages/')
    import gspread
try:
    from oauth2client.service_account import ServiceAccountCredentials
except ImportError:
    sys.path.append('/home/takeda1411123/.pyenv/versions/add_user_gcp/lib/python3.7/site-packages/')
    from oauth2client.service_account import ServiceAccountCredentials
import subprocess
def get_spreadsheet(wks):
     sheet = wks.get_all_values()
     add_list = []
     for i in range(1, len(sheet)):
         if sheet[i][6] == '1': continue
         if '@gmail.com' not in sheet[i][2]: continue
         add_list.append(sheet[i][2])
     return sheet,add_list

def add_user(list):
    added_list = []
    print(list)
    for i in range(len(list)):
        args = 'gcloud projects add-iam-policy-binding all-project-264506 --member=user:'+list[i]+ ' --role=roles/editor'
        print(args.split(" "))
        try:
            subprocess.check_call(args.split(" "))
            added_list.append(list[i])
        except:
            print("Error.")

    return added_list

def fix_spreadsheet(wks,sheet, added_list):

    for i in range(len(add_list)):
        for j in range(1,len(sheet)):
            if add_list[i] == sheet[j][2]:
                wks.update_cell(j+1,7,1)



if __name__ == "__main__":
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/takeda1411123/all-project-264506-6a264ae343d6.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open_by_key('1iTM88V9_Wm6vEQjGK4ivJHkLpyJ9NHqfJ3gZMM2iNiI').sheet1

    sheet, add_list = get_spreadsheet(wks)
    added_user = add_user(add_list)
    fix_spreadsheet(wks,sheet, added_user)

