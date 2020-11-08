# Textbot for Top Resturants in a City 
### Ari Chadda and Suraj Srivats 
### Dartmouth College - 11/8/20

This project for the 2020 Mount Holyoke Hackathon involves using `twilio` and `Flask` to create and deploy a textbot which can be accessed at the number `202-866-2767`. 

The query syntax is simply: `[CITY] [STATE ABBREV] [MAX # RESULTS]`. For example: `Washington DC 10`. 

`[CITY]` is any US city name. E.g. San Francisco, Bethesda, Nashville.
`[STATE ABBREV]` is any US state abreviation. E.g. CA, MD, TN.
`[MAX # RESULTS]` is any number between 1 and 20 (max for to prevent bloated runtimes). 

An example output for Washington DC can be seen below. 
```
1. The Dabney with a rating of 4.8 out of 5 and 724 ratings

2. Bistro Aracosia with a rating of 4.9 out of 5 and 361 ratings

3. Maydan with a rating of 4.7 out of 5 and 903 ratings

4. Joe's Seafood, Prime Steak & Stone Crab with a rating of 4.7 out of 5 and 3054 ratings

5. Thip Khao Restaurant with a rating of 4.7 out of 5 and 982 ratings

6. Tail Up Goat with a rating of 4.7 out of 5 and 786 ratings

7. Old Ebbitt Grill with a rating of 4.6 out of 5 and 11188 ratings

8. Rooster & Owl with a rating of 4.8 out of 5 and 156 ratings

9. Keren Cafe & Restaurant with a rating of 4.7 out of 5 and 828 ratings

10. Le Diplomate with a rating of 4.6 out of 5 and 3712 ratings
```
