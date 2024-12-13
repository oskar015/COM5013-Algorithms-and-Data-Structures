#tests for contacts app
#A data structure consisting of only zero or null values?
#still performs


#welcome message
print("Welcome to your contacts app.")

#this function is for searching the dictionary to find a contact.
#it searches by looping through the dictionary for the name of the contact [4], [1]
def search_contact(contacts, name):
  if name in contacts:
    return contacts[name]
  else:
    return "No contact found."

#this function is for adding a new contact, the user inputs details for the new contact [4]
def add_contact(contacts):
  name = input("Enter the contact's name: ")
  phone_number = input("Enter the contact's phone number: ")
  postal_address = input("Enter the contact's postal address: ")
  #adding the new contact to the dictionary
  contacts[name] = {
    "phone number": phone_number,
    "postal address": postal_address
  }
  print("Contact added.")

#a nested dictionary for the contact list with each sub dictionary's name as key and values as phone number and postal code [1], [2], [3]
contacts = {
#for this test i used of only zero or null values
    "Johnny Silverhand" : {
    "phone number" : None,
    "postal address" : 0
  },
    "Adam Smasher" : {
    "phone number" : None,
    "postal address" : 0
  }
  
}

#the program loops until the user 'end's. This is so that the user can add a contact and then view it, or view more than one contact. [4]
#based on user inputs, their 'choice' will determine the path of the program.
while True:
  choice = input("Here you can search for a contact or add a new one. (type search/add/end): ")
  #searching the dictionary for the contact
  if choice == 'search':
    name = input("Enter the name of the contact you are searching for: ")
    result = search_contact(contacts, name)
    print(result)
  #adding a contact to the dictionary
  elif choice == 'add':
    add_contact(contacts)
  #ending the program.
  elif choice == 'end':
    print("program ended.")
    break
  #if the user doesn't type a valid choice.
  else:
    print("choose 'search', 'add', or 'end'.")