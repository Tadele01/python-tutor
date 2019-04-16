import re
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')#putting r in the parenthesis makes the escape chr as raw string
user_input = input("Enter your string : ")
phone_found = phone_num_regex.search(user_input)
if phone_found == None:
    print("sorry there is no phone number inserted")
else:
    print("The phone number found is : ", phone_found.group())
