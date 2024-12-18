from pyrogram import Client
import requests

app = Client("Insta-dl", api_id=28097331, api_hash="959b702688dac0613488a5c55e4b7472")

@app.on_message()
async def main(c, m):
    
    if 'instagram.com' in m.text:
        url = m.text
        json_api = requests.get(f"https://nativeig.vercel.app/api/video?postUrl={url}").json()
        video_url = json_api['data']['videoUrl']
        width = json_api['data']['width']
        height = json_api['data']['height']
        await app.send_video(chat_id = m.chat.id, video = video_url, caption = f"📹 {width} x {height}\n🪄 @TheCommit")

if __name__ == '__main__':
    app.run()