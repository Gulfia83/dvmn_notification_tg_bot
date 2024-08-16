import requests
import telegram
from time import sleep
import os
from dotenv import load_dotenv
import logging


logger = logging.getLogger('check_results')


def send_message(bot, chat_id, results):
    if results['is_negative']:
        text = f'''У Вас проверили работу: {results["lesson_title"]}.
               К сожалению, в работе нашли ошибки.' \
               Ссылка на урок: {results["lesson_url"]}'''
    else:
        text = f'''У Вас проверили работу: {results["lesson_title"]}.
               Преподавателю все понравилось. Вам открыт следующий урок.'''

    bot.send_message(chat_id=chat_id, text=text)


def main():
    load_dotenv()

    dvmn_token = os.getenv('DVMN_API_TOKEN')
    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')

    bot = telegram.Bot(tg_bot_token)

    logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s")
    logger.setLevel(logging.INFO)
    logger.info('Бот запущен')

    while True:
        try:
            url = 'https://dvmn.org/api/long_polling/'

            headers = {
                'Authorization': f'Token {dvmn_token}'
            }
            params = {}
            response = requests.get(url,
                                    headers=headers,
                                    params=params,
                                    timeout=60)
            response.raise_for_status
            verification_results = response.json()
            if verification_results['status'] == 'found':
                params['timestamp'] = verification_results['last_attempt_timestamp']
                for result in verification_results['new_attempts']:
                    send_message(bot, tg_chat_id, result)
            elif verification_results['status'] == 'timeout':
                params['timestamp'] = verification_results['timestamp_to_request']

        except requests.exceptions.ReadTimeout:
            pass
        except ConnectionError as err:
            logger.exception(err)
            sleep(5)
        except Exception as err:
            logger.exception(err)


if __name__ == '__main__':
    main()
