from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
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
        

        try:
            # city = "mexican+restaurant+hanover"

            print(curr_str)
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

                    if open_ and rating and name and user_ratings_count and int(user_ratings_count) > 200:
                        curr = Restaurant(name, rating, user_ratings_count, open_)
                        parse.append(curr)

                    if user_ratings_count not in rate:
                        rate[user_ratings_count] = [curr]
                    else:
                        rate[user_ratings_count].append(curr)
                    
                    if rating not in rate_val:
                        rate_val[rating] = [curr]
                    else:
                        rate_val[rating].append(curr)

                except:
                    continue
            
            print(rate)
            print(rate_val)
            if rate and rate_val:
                sorted_rate = sorted(rate.keys(), reverse=True)
                sorted_rate_val = sorted(rate_val.keys(), reverse=True)


                for i in range(len(sorted_rate)):
                    for j in rate[sorted_rate[i]]:
                        avg_rank[j] = i / 4

                for i in range(len(sorted_rate_val)):
                    for j in rate_val[sorted_rate_val[i]]:
                        avg_rank[j] += i / 2

                sorted_avg_rank = sorted(avg_rank.items(), key=lambda x:x[1])

                
                answer = ""
                for i in range(int(max_num_returns)):
                    answer += str(i + 1) + ". "
                    answer += str(sorted_avg_rank[i][0])
                    answer += '\n\n'

            
        except:
            answer = "We do not have data on " + restaurant

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