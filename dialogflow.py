import apiai
import json

token = 'your_bot_token'


def bot_answer(message):
    request = apiai.ApiAI(token).text_request()
    request.lang = 'ru'
    request.query = message
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    return response

message = ''
while(message!='стоп'):
    message = input('Введите сообщение:')
    print(bot_answer(message))

