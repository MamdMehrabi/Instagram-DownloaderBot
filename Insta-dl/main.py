from pyrogram import Client
import requests

app = Client("Insta-dl", api_id=28097331, api_hash="959b702688dac0613488a5c55e4b7472")

@app.on_message()
async def main(c, m):
    
    if 'instagram.com' in m.text:
        url = m.text
        proccessing = await m.reply("در حال پردازش...", reply_to_message_id=m.id)
        json_api = requests.get(f"https://nativeig.vercel.app/api/video?postUrl={url}").json()
        if json_api['status'] == 'success':
            video_url = json_api['data']['videoUrl']
            width = json_api['data']['width']
            height = json_api['data']['height']
            await app.send_video(chat_id = m.chat.id, video = video_url, caption = f"📹 {width} x {height}\n🪄 @TheCommit", reply_to_message_id = m.id)
            await app.delete_messages(chat_id=m.chat.id, message_ids=proccessing.id)
        elif json_api['status'] == 'error':
            await m.reply(f"❌ به مشکل خوردیم\n❗{json_api['message']}", reply_to_message_id = m.id)
            await app.delete_messages(chat_id=m.chat.id, message_ids=proccessing.id)
        else:
            await m.reply("🤔ارور ناشناخته", reply_to_message_id = m.id)
            await app.delete_messages(chat_id=m.chat.id, message_ids=proccessing.id)

if __name__ == '__main__':
    app.run()