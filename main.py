from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest

# بيانات تسجيل الدخول (استبدلها ببياناتك)
api_id = 123456  # احصل عليه من https://my.telegram.org/apps
api_hash = "your_api_hash"
group_invite_link = "https://t.me/+yourGroupLink"  # رابط المجموعة

# تسجيل الدخول إلى Telegram
client = TelegramClient("session_name", api_id, api_hash)
client.start()

async def get_members():
    try:
        # الانضمام للمجموعة عبر الرابط
        chat = await client(ImportChatInviteRequest(group_invite_link.split("+")[1]))
        members = await client.get_participants(chat)

        # استخراج بيانات الأعضاء
        for member in members:
            print(f"ID: {member.id}, Username: {member.username}, Phone: {member.phone}")

    except Exception as e:
        print(f"حدث خطأ: {e}")

with client:
    client.loop.run_until_complete(get_members())