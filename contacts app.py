
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
  "Johnny Silverhand" : {
    "phone number" : '0191 226 8885',
    "postal address" : '18 Mitchcroft Road, Longstanton,CB24 3BE'
  },
  "Adam Smasher" : {
    "phone number" : '07802 481946',
    "postal address" : '10 Bispham Road, Nelson,BB9 0RX'
  },
  "Peter Griffin" : {
    "phone number" : '01268 730955',
    "postal address" : '56 Lampton Road, Hounslow,TW3 1JQ'
  },
  "Joe Swanson" : {
    "phone number" : '01782 823035',
    "postal address" : '6 Greenall Close, Cheshunt,EN8 9HY'
  },
  "Ichigo Kurosaki" : {
    "phone number" : '01947 602664',
    "postal address" : '31 Southgate Road, Southgate,SA3 2BY'
  },
  "Aizen Sosuke" : {
    "phone number" : '0191 222 7662',
    "postal address" : '1 Higher Devonshire Meadow, Grampound,TR2 4FS'
  },
  "Sasuke Uchiha" : {
    "phone number" : '01903 237707',
    "postal address" : '9 Castle Road, Cottingham,HU16 5JE'
  },
  "Kakashi Hatake" : {
    "phone number" : '01603 766137',
    "postal address" : '8 Fourview Close, Brixham,TQ5 9BR'
  },
  "Leonardo DiCaprio" : {
    "phone number" : '01582 413704',
    "postal address" : '126 Greenside Way, Walsall,WS5 4BH'
  },
  "Brad Pitt" : {
    "phone number" : '01978 351815',
    "postal address" : 'F1 The Lowry Designer Outlet The Quays, Salford,M50 3AH'
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