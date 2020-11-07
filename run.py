from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

def getReply(message):
    message = message.lower().strip()
    answer = ""

    if "open" in message:
        msg_list = message.split(" ")
        resturant = msg_list[1]
        city = msg_list[2]
        state = msg_list[3]

        try:
            answer = resturant + " in " + city + "," + state + " is open \n"
            # TODO: find some API to call... probably Google Places API to check if 
            # places are open for business/add query firebase and create 
            # interface for resturants to change if they are open or not - maybe use a 
            # different number that they can text 
        except:
            answer = "We do not have data on " + resturant

    else:
        answer = "Please use the format: 'is [RESTURANT_NAME] [CITY] [STATE ABREVIATION] open' for example: 'is Starbucks Hanover NH open'"

    if len(answer) > 1500:
        answer = answer[0:1500] + "..."

    return answer

app = Flask(__name__)

@app.route('/', methods=['POST'])
def sms():
    message_body = request.form['Body']
    resp = MessagingResponse()

    replyText = getReply(message_body)
    resp.message('Hi\n\n' + replyText )
    return str(resp)

if __name__ == '__main__':
    app.run()