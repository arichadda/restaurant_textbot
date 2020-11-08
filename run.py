from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from Restaurant import Restaurant
import json
import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

def getReply(message):
    message = message.lower().strip()
    answer = ""

    if " " in message:
        msg_list = message.split(" ")
        
        curr_str = ""
        for i in range(len(msg_list) - 1):
            curr_str += msg_list[i] + "+"

        curr_str += "restaurants"
        max_num_returns = msg_list[-1]
        js_ = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + curr_str + "&radius=5000&key=AIzaSyDYwAFbxHqg9ZnZnl3cvqac32M7zJzRFl8").json()
        
        parse = []
        rate = {}
        rate_val = {}
        avg_rank = {}

        for restaurant in js_['results']:
            
            try:
                rating = restaurant['rating']
                open_ = restaurant['opening_hours']['open_now']
                name = restaurant['name']
                user_ratings_count = restaurant['user_ratings_total']

                if rating and name and user_ratings_count and int(user_ratings_count):
                    curr = Restaurant(name, rating, user_ratings_count, open_)
                    parse.append(curr)
                
                if curr not in rate.keys():
                    rate[curr] = user_ratings_count
                
                if curr not in rate_val.keys():
                    rate_val[curr] = rating

            except:
                continue
        
        if rate and rate_val:
            sorted_rate = {k: v for k, v in sorted(rate.items(), key=lambda item: item[1], reverse=True)}
            sorted_rate_val = {k: v for k, v in sorted(rate_val.items(), key=lambda item: item[1], reverse=True)}

            max = len(list(sorted_rate.keys()))
            for score in range(len(list(sorted_rate.keys()))):
                avg_rank[list(sorted_rate.keys())[score]] = (max - score) / 4
                    
            for rating in range(len(list(sorted_rate_val.keys()))):
                avg_rank[list(sorted_rate_val.keys())[rating]] += (max - rating) / 2 

            sorted_avg_rank = sorted(avg_rank.items(), key=lambda x:x[1], reverse=True)

            answer = ""
            for i in range(int(max_num_returns)):
                answer += str(i + 1) + ". "
                answer += str(sorted_avg_rank[i][0])
                answer += '\n\n'

    else:
        answer = "Please use the format: '[CITY] [STATE ABBREV] [MAX # RESULTS]' for example: 'Hanover NH 5'"

    if len(answer) > 1500:
        answer = answer[0:1500] + "..."

    return answer

app = Flask(__name__)

@app.route('/', methods=['POST'])
def sms():
    message_body = request.form['Body']
    resp = MessagingResponse()

    replyText = getReply(message_body)
    resp.message(replyText)

    return str(resp)

if __name__ == '__main__':
    app.run()