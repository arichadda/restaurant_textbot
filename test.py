import json
import requests
import pprint


pp = pprint.PrettyPrinter(indent=4)


city = "san+francisco+restaurants"

js_ = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + city + "&radius=5000&key=AIzaSyDYwAFbxHqg9ZnZnl3cvqac32M7zJzRFl8").json()

pp.pprint(js_)

# parse = []
# rate = {}
# rate_val = {}

# avg_rank = {}
# class Restaurant:
#     def __init__(self, name, rating, user_ratings_count, open_):
#         self.name = name
#         self.rating = rating
#         self.user_ratings_count = user_ratings_count
#         self.open_ = open_
    
#     def __str__(self):
#         return self.name + " with a rating of " + str(self.rating) + " out of 5 and " + str(self.user_ratings_count) + " ratings"

    

# for restaurant in js_['results']:
#     name = restaurant['name']
#     rating = restaurant['rating']
#     user_ratings_count = restaurant['user_ratings_total']

#     try:
#         open_ = restaurant['opening_hours']['open_now']
#     except:
#         open_ = False

#     curr = Restaurant(name, rating, user_ratings_count, open_)
#     if open_ and user_ratings_count > 0:
#         parse.append(curr)

#         # rate[curr] = [user_ratings_count, rating]
#         if user_ratings_count not in rate:
#             rate[user_ratings_count] = [curr]
#         else:
#             rate[user_ratings_count].append(curr)
        
#         if rating not in rate_val:
#             rate_val[rating] = [curr]
#         else:
#             rate_val[rating].append(curr)


# sorted_rate = sorted(rate.keys(), reverse=True)
# sorted_rate_val = sorted(rate_val.keys(), reverse=True)

# # for i in sorted_rate:
# #     print(i)
# #     print(rate[i][0])


# # for i in sorted_rate:
# #     print(i)
# #     print(rate[i][0])


# for i in range(len(sorted_rate)):
#     for j in rate[sorted_rate[i]]:
#         avg_rank[j] = i / 4

# for i in range(len(sorted_rate_val)):
#     for j in rate_val[sorted_rate_val[i]]:
#         avg_rank[j] += i / 2

# sorted_avg_rank = sorted(avg_rank.items(), key=lambda x:x[1])

# for i in range(10):
#     print(sorted_avg_rank[i][0])

