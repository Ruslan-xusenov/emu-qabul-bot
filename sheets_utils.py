import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging
import traceback

def connect_sheet(sheet_key_or_name, by_key=True):
    try:
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)

        if by_key:
            sheet = client.open_by_key(sheet_key_or_name).get_worksheet(0)
        else:
            sheet = client.open(sheet_key_or_name).sheet1

        return sheet
    except Exception:
        logging.error("Google Sheetga ulanishda xatolik:\n%s", traceback.format_exc())
        raise

def ensure_headers(sheet, headers: list):
    existing_headers = sheet.row_values(1)
    if existing_headers != headers:
        sheet.insert_row(headers, 1)

def append_user_to_sheet(user_data: dict):
    try:
        sheet = connect_sheet("1-JmxZx6_UBIptOc4-KtbizI-Rc7O4Yh7x4M68NP6Eng")
        values = [
            user_data.get("id", ""),
            user_data.get("username", ""),
            user_data.get("full_name", ""),
            user_data.get("phone", ""),
            user_data.get("passport", ""),
            user_data.get("passport_given_by", ""),
            user_data.get("jshshir", ""),
            user_data.get("address", ""),
            user_data.get("shape", ""),
            user_data.get("direction", ""),
            user_data.get("test_score", ""),
            user_data.get("joined", "")
        ]
        sheet.append_row(values)
    except Exception:
        logging.error("Sheetsga yozishda xatolik:\n%s", traceback.format_exc())
        raise

def append_partial_user_to_sheet(user_data: dict, completed: bool = False):
    try:
        sheet = connect_sheet("1gMQeBrM1AkIb9aJ-odg6rk4bRA0cILu4Vx99EfoZ4c8")
        values = [
            user_data.get("id", ""),
            user_data.get("username", ""),
            user_data.get("full_name", ""),
            user_data.get("phone", ""),
            user_data.get("passport", ""),
            user_data.get("passport_given_by", ""),
            user_data.get("jshshir", ""),
            user_data.get("address", ""),
            user_data.get("shape", ""),
            user_data.get("direction", ""),
            user_data.get("test_score", ""),
            user_data.get("joined", ""),
            "✅" if completed else "❌"
        ]
        headers = ["ID", "Username", "F.I.Sh", "Tel", "Passport", "Kim tomonidan", "JSHSHIR", "Manzil", "Shakl", "Yo'nalish", "Ball", "Vaqt", "To'liq"]
        ensure_headers(sheet, headers)
        sheet.append_row(values)
    except Exception:
        logging.error("Qisman foydalanuvchini sheetsga yozishda xatolik:\n%s", traceback.format_exc())
        raise