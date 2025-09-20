import webbrowser

toolSelector = {
    "1": "Whitepage",
    "2": "DNS Lookup",
    "3": "WHOIS",
    "4": "Google Search",
    "5": "LinkedIn Search",
    "6": "Email Search",
    "7": "Phone Number Search",
    "8": "Address Search",
    "9": "IP Address Search",
    "10": "Social Media Search",
      
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
        #https://www.whitepages.com/name/{name}
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
elif choice == "3":
    print("Running WHOIS tool...")
    # Implement WHOIS functionality here
elif choice == "4":
    print("Running Google Search tool...")
    # Implement Google Search functionality here
elif choice == "5":
    print("Running LinkedIn Search tool...")
    # Implement LinkedIn Search functionality here
elif choice == "6":
    print("Running Email Search tool...")
    # Implement Email Search functionality here
elif choice == "7":
    print("Running Phone Number Search tool...")
    # Implement Phone Number Search functionality here
elif choice == "8":
    print("Running Address Search tool...")
    # Implement Address Search functionality here
elif choice == "9":
    print("Running IP Address Search tool...")
    # Implement IP Address Search functionality here
elif choice == "10":
    print("Running Social Media Search tool...")
    # Implement Social Media Search functionality here

else:
    print("Invalid choice. Please select a valid tool number.")
    
# Add your tool implementation here based on the user's choice
# For example:

