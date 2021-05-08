## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location_ok": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"email": "rahuloct311990@gmail.com"}
    - slot{"email": "rahuloct311990@gmail.com"}
    - action_send_email
    - utter_goodbye

## Cuisine and Location 
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "Bangalore"}
	- slot{"location": "Bangalore"}
	- action_validate_location
	- slot{"location_ok": true}
    - slot{"location": "Bangalore"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"email": "rahuloct311990@gmail.com"}
    - slot{"email": "rahuloct311990@gmail.com"}
    - action_send_email
    - utter_goodbye
	
## Cuisine and Location 
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "delhi"}
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location_ok": true}
    - slot{"location": "delhi"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "2"}
    - slot{"budget": "2"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"email": "rahuloct311990@gmail.com"}
    - slot{"email": "rahuloct311990@gmail.com"}
    - action_send_email
    - utter_goodbye

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_validate_location
    - slot{"location_ok": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "lucknow"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"email": "rahuloct311990@gmail.com"}
    - slot{"email": "rahuloct311990@gmail.com"}
    - action_send_email
    - utter_goodbye

## complete path 2
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "2"}
    - slot{"budget": "2"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"email": "rahuloct311990@gmail.com"}
    - slot{"email": "rahuloct311990@gmail.com"}
    - action_send_email
    - utter_goodbye


## complete path 3
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "budget": "2"}
    - slot{"budget": "2"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* dont_send_email
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "budget": "2"}
    - slot{"budget": "2"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"email": "rahuloct311990@gmail.com"}
    - slot{"email": "rahuloct311990@gmail.com"}
    - action_send_email

## complete path 5
* greet
    - utter_greet
* restaurant_search{"location": "palakkad"}
    - slot{"location": "palakkad"}
    - action_validate_location
    - slot{"location_ok": "zero"}
    - utter_no_operation
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "2"}
    - slot{"budget": "2"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email
* dont_send_email{"dont_send_email": "no"}
    - utter_goodbye

## complete path 6
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "2"}
    - slot{"budget": "2"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"email": "rahuloct311990@gmail.com"}
    - slot{"email": "rahuloct311990@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* action_search_restaurants{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* action_search_restaurants{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop
    
## happy_path
* restaurant_search{"location": "dandeli"}
    - slot{"location": "dandeli"}
    - action_validate_location
    - slot{"location_ok": "zero"}
    - utter_no_operation
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "dharwad", "budget": "2"}
    - slot{"budget": "2"}
    - slot{"location": "dharwad"}
    - action_validate_location
    - slot{"location_ok": "zero"}
    - utter_no_operation
    - utter_ask_location
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "2"}
    - slot{"budget": "2"}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"email": "talrejarahul_ism@hotmail.com"}
    - slot{"email": "talrejarahul_ism@hotmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "goa"}
    - slot{"cuisine": "italian"}
    - slot{"location": "goa"}
    - action_validate_location
    - slot{"location_ok": "one"}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "goa"}
    - utter_ask_email
* dont_send_email{"dont_send_email": "no"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_validate_location
    - slot{"location_ok": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "2"}
    - slot{"budget": "2"}
    - action_search_restaurants
    - slot{"location": "kanpur"}
    - utter_ask_email
* dont_send_email
    - utter_goodbye
	
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbaim"}
    - slot{"location": "mumbaim"}
    - action_validate_location
    - slot{"location_ok": "zero"}
	- utter_no_operation
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "1"}
    - slot{"budget": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"email": "talrejarahul_ism@hotmail.com"}
    - slot{"email": "talrejarahul_ism@hotmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
