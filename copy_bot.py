import requests
import time

token = '6150442279:AAF_Op6lsUnpXMzDWs6J5MRMBMXOEKXTIRU'
BASE_URL = 'https://api.telegram.org/bot'
def work():
    file_id = ''
    caption = ''
    cnt_message = 0
    while True:
        time.sleep(0.5)
        response = requests.get(f'{BASE_URL}{token}/getUpdates').json()
        if cnt_message != len(response['result']):
            cnt_message = len(response['result'])
            message = response['result'][-1]['message']
            user_id = message['from']['id']
            user_name = message['from']['username']
            first_name = message['from']['first_name']
            keys = message.keys()
            try:
                if 'text' in keys:
                    text = message['text']
                    requests.get(f'{BASE_URL}{token}/sendMessage?chat_id={user_id}&text={text}')
                elif 'photo' in keys:
                    file_id = message['photo'][0]['file_id']
                    if 'caption' in keys:
                        caption = message['caption']
                    else:
                        caption = ''
                    requests.get(f'{BASE_URL}{token}/sendPhoto?chat_id={user_id}&photo={file_id}&caption={caption}')
                elif 'video' in keys:
                    file_id = message['video']['file_id']
                    if 'caption' in keys:
                        caption = message['caption']
                    else:
                        caption = ''
                    requests.get(f'{BASE_URL}{token}/sendVideo?chat_id={user_id}&video={file_id}&caption={caption}')
                elif 'document' in keys:
                    file_id = message['document']['file_id']
                    if 'caption' in keys:
                        caption = message['caption']
                    else:
                        caption = ''
                    requests.get(f'{BASE_URL}{token}/sendDocument?chat_id={user_id}&document={file_id}&caption={caption}')
                else:
                    requests.get(f'{BASE_URL}{token}/sendMessage?chat_id={user_id}&text=Такого пока не умею')
            except Exception:
                print('Error')
work()