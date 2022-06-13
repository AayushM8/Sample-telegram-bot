from datetime import datetime


def sample_responses (input_text):
    user_message = str(input_text).lower()
    if input_text=="padd":
        return"Enter the flat/house number"
        

    if input_text=="hno":
        return "Enter Building/House Name"
    
    if input_text=="hname":
        return "Enter the Street name"

    if input_text=="sname":
        return "Enter the name of your City"

    if input_text=="cname":
        return "Enter your pincode"

    if user_message in ("hello", "hi", "sup",):
        return "Hey! How's it going?"
    if user_message in ("who are you", "who are you?"):
        return "I am ABC bot!"
    if user_message in ("time", "time?"):
        now = datetime.now() 
        date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
        return str(date_time)
    return "Mehery Bot will be with you shortly"

