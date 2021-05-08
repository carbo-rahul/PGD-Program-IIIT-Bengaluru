from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset
from email.message import EmailMessage
# Importing the smtplib libaray for sending the email
import smtplib
import json
import re
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import numpy as np
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from threading import Thread
from time import sleep
from concurrent.futures import ThreadPoolExecutor

ZomatoData = pd.read_csv('zomato.csv',encoding= 'unicode_escape')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', "Delhi", "delhi",'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def RestaurantSearch(City,Cuisine):
    TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
    TEMP = TEMP.sort_values(by=['Aggregate rating'], ascending=False)
    return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]
## List of the cities in tier 1 and tier 2

operating_cities = [x.lower() for x in WeOperate]

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = int(tracker.get_slot('budget'))
        rangeMin = 0
        rangeMax = 100000
        if price == 1:
            rangeMax = 299
        elif price == 2:
            rangeMin = 300
            rangeMax = 699
        elif price == 3:
            rangeMin = 700
        elif price < 500:
            rangeMax = 299
        elif price < 700 and price >= 300:
            rangeMin = 300
            rangeMax = 699
        else:
            # default budget
            rangeMin = 300
            rangeMax = 699
        results = RestaurantSearch(City=loc, Cuisine=cuisine)
        response = ""
        if results.shape[0] < 5:
            response = "No Results. Please try a different location or cuisine"
        else:
           results = RestaurantSearch(City=loc, Cuisine=cuisine)
           restaurant_df = results[(results['Average Cost for two'] > rangeMin) & (results['Average Cost for two'] < rangeMax)]
           restaurant_df= restaurant_df.sort_values(by=['Aggregate rating'], ascending=False)
           for restaurant in restaurant_df.iloc[:5].iterrows():
                restaurant = restaurant[1]
                response = response + F"{restaurant['Restaurant Name']} in {restaurant['Address']} has been rated {restaurant['Aggregate rating']} \n\n"

        dispatcher.utter_message("-----"+response)
        return [SlotSet('location',loc)]

#  This is to check if Foodies operates in the given city or not.
class ActionValidateLocation(Action):
    def name(self):
        return 'action_validate_location'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        city = str(loc)
        if city.lower() in operating_cities:
            return [SlotSet('location_ok',"one")]
        else:
            return [SlotSet('location_ok',"zero")]

class SendMail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        recipient = tracker.get_slot('email')
        price = int(tracker.get_slot('budget'))
        rangeMin = 0
        rangeMax = 100000
        if price == 1:
            rangeMax = 299
        elif price == 2:
            rangeMin = 300
            rangeMax = 699
        elif price == 3:
            rangeMin = 700
        elif price < 500:
            rangeMax = 299
        elif price < 700 and price >= 300:
            rangeMin = 300
            rangeMax = 699
        else:
            # default budget
            rangeMin = 300
            rangeMax = 699

        results = RestaurantSearch(City=loc, Cuisine=cuisine)
        restaurant_df = results[(results['Average Cost for two'] > rangeMin) & (results['Average Cost for two'] < rangeMax)]
        restaurant_df= restaurant_df.sort_values(by=['Aggregate rating'], ascending=False)
        top_10_restaurant_details = restaurant_df[:10]

        if top_10_restaurant_details.shape[0] ==0:
            dispatcher.utter_message("No results found with this search criterion")
        else:
            try:
                mail_content = top_10_restaurant_details.to_html()
                print(top_10_restaurant_details)
                # HTML + CSS for body
                email_body = None

                email_body_header = ' '
                email_body_header = email_body_header + '<html><head></head><body>'
                email_body_header = email_body_header + '<style type="text/css"></style>'
                email_body_header = email_body_header + '<br><p>Hey there!!,<br><br>List of restaurnts is attached below.<br>'

                email_body_content = ' '
                email_body_content = email_body_content + mail_content


                email_body_footer = ' '
                email_body_footer = email_body_footer + '<br>Thank you'
                email_body_footer = email_body_footer + '<br>Foodie Support Bot<br>'

                email_body = str(email_body_header) + str(email_body_content) + str(email_body_footer)

			    #The mail addresses and password
                sender_address = 'ABCD@gmail.com'
                sender_pass = 'Password'
                receiver_address = str(recipient)

			    #Setup the MIME
                message = MIMEMultipart('alternative')
			    # message = MIMEMultipart()
                message['From'] = sender_address
                message['To'] = receiver_address

                message['Subject'] = 'List of Restaurants by Foodie'   #The subject line

			                #The body and the attachments for the mail
                message.attach(MIMEText(email_body, 'html'))

			                #Create SMTP session for sending the mail
                session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                session.starttls() #enable security
                session.login(sender_address, sender_pass) #login with mail_id and password
                text = message.as_string()
                session.sendmail(sender_address, receiver_address, text)
                dispatcher.utter_message("Have a great day! e-mail is sent")
                session.quit()
                return [AllSlotsReset()]
            except Exception as e:
                logger.error('Failed to upload to ftp: '+ str(e))
                dispatcher.utter_message("Foodie is unable to send Email, address is not valid ")