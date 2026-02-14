import datetime
import webbrowser
from urllib.parse import quote

# ── Configuration ─────────────────────────────────────────────
PATRICK_PHONE  = "491738031349"   # His number, no + or spaces, with country code
SITE_URL       = "https://kulturtech.github.io/birthday-patrick/"

BIRTHDAY_DAY   = 10
BIRTHDAY_MONTH = 3  # March

# ── Message ───────────────────────────────────────────────────
MESSAGE = f"""🎂 Happy Birthday, Babuuu! 🎉

ich habe für dich was gebaut!  👇

{SITE_URL}

Ich lieb dich so dolle 💜✨"""

# ── Check & Open ──────────────────────────────────────────────
def is_birthday_today() -> bool:
    today = datetime.date.today()
    return today.day == BIRTHDAY_DAY and today.month == BIRTHDAY_MONTH


def send_wish():
    if not is_birthday_today():
        print("Today is not Patrick's birthday. No message sent.")
        return

    print("🎉 Today is Patrick's birthday! Opening WhatsApp...")

    url = f"https://wa.me/{PATRICK_PHONE}?text={quote(MESSAGE)}"
    webbrowser.open(url)
    print("✅ WhatsApp opened — just hit Send!")


# ── Entry point ───────────────────────────────────────────────
if __name__ == "__main__":
    send_wish()