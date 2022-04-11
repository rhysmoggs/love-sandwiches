import gspread
from google.oauth2.service_account import Credentials

"""
Every Google account has an IAM configuration.
IAM stands for Identity and Access Management. This configuration specifies what the user has access to.  
The scope (below) lists the APIs that the  program should access in order to run.
Since our scope variable value will not change, it's known as a constant, 
and in Python we  write constant variable names in capitals. 
"""

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)