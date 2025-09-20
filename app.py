import webbrowser

toolSelector = {
    "1": "Whitepage",
    "2": "DNS Lookup",
    "3": "Google Search",
    "4": "LinkedIn Search",
    "5": "Email Search",
    "6": "Phone Number Search",
    "7": "Address Search",
    "8": "IP Address Search",
    "9": "Social Media Search",
      
}

print("Select a tool:")
for key, value in toolSelector.items():
    print(f"{key}. {value}")

choice = input("Enter the number of your choice: ")

if choice in toolSelector:
    print(f"You selected: {toolSelector[choice]}")
    # Implement tool functionality here1


if choice == "1":
    # Implement Whitepage functionality here
    
    # Select a name or phone number to search
    whitepage_choice = input("Search by (1) Name or (2) Phone Number? Enter 1 or 2: ")
    
    if whitepage_choice == "1":
        name = input("Enter a name to search: ")
        print(f"Searching for {name} in Whitepages...")
        # Implement Whitepages search functionality here
        webbrowser.open(f"https://www.whitepages.com/name/{name.replace(' ', '%20')}")


    elif whitepage_choice == "2":
        phone_number = input("Enter a phone number to search: ")
        print(f"Searching for {phone_number} in Whitepages...")
        # Implement Whitepages search functionality here
        webbrowser.open(f"https://www.whitepages.com/phone/{phone_number}")
    else:
        print("Invalid choice. Please enter 1 or 2.")


elif choice == "2":
    print("Running DNS Lookup tool...")
    # Implement DNS Lookup functionality here
    domain_name = input("Enter a domain name to look up: ")
    print(f"Looking up DNS records for {domain_name}...")
    webbrowser.open(f"https://www.whois.com/whois/{domain_name}")
elif choice == "3":
    print("Running Google Search...")
    # Implement WHOIS functionality here
    first_name = input("Enter a first name: ")
    last_name = input("Enter last name: ")
    birthdate = input("Enter a birthday if known: ")
    if birthdate:
        webbrowser.open(f"https://www.google.com/search?q={first_name}+{last_name}") 
    elif birthdate is True:
        webbrowser.open(f"https://www.google.com/search?q={first_name}+{last_name}+%3A+{birthdate}")
  
elif choice == "4":
    print("Running Linkedin Search")
    # Implement Linkedin Search functionality here
elif choice == "5":
    print("Running Phone Number Search tool...")
    # Implement Phone Number Search functionality here
elif choice == "6":
    print("Running Address Search tool...")
    # Implement Address Search functionality here
elif choice == "7":
    print("Running IP Address Search tool...")
    # Implement IP Address Search functionality here
elif choice == "8":
    print("Running Social Media Search tool...")
    # Implement Social Media Search functionality here

else:
    print("Invalid choice. Please select a valid tool number.")
    
# Add your tool implementation here based on the user's choice
# For example:

