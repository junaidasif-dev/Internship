import string 

print("Welcome to the Dassoft FAQ Bot!")

section = ["1. Dashboard", "2. Orders", "3. POS", "4. Branches"]
print("\n".join(section))
sec = input("Please select a section: ")

if sec == "1":
    print("Dashboard page handled queries!")
    category = ["1. Company", "2. Branch", "3. Products", "4. Tables"]
    print("\n".join(category))
    cat = input("Please select a category: ")

    if cat == "1":
        print("You have selected Company!")
        FAQ = ["a. How can I change the logo?", "b. What is the purpose of color theme section?", "c. I want to tell my customers about my company, but I don't know how to do it?"]
        print("\n".join(FAQ))
        FAQ_cat1= input("How can I help you? (Type a, b or c): ")
        if FAQ_cat1 == "a":
            print("To change the logo, 1st go to the dashboard section, then go to company's page. 1st remove the current logo and then add new logo. On the right bottom, click on update to save the changes.")
        elif FAQ_cat1 == "b":
            print("The color theme section allows you to customize the appearance of your company's dashboard.")
        elif FAQ_cat1 == "c":
            print("To add details about your company, 1st go to the dashboard section, then go to company's page. Add the details in description section and then at the right bottom, click on updated to save the changes.")
        else:
            pass

    elif cat == "2":
        print("Branch page handled queries!")
        FAQ = ["a. How can I add tax & delivery charges?", "b. How can I set or update the address of my restaurant branch?", "c. I want to update opening & closing time of my restaurant, please guide me?"]
        print("\n".join(FAQ))
        FAQ_cat2= input("How can I help you? (Type a, b or c): ")
        if FAQ_cat2 == "a":
            print("To add tax & delivery charges, 1st go to the dashboard section, then go to branch's page. Add the tax & delivery charges in the respective section and then at the right bottom, click on updated to save the changes.")
        elif FAQ_cat2 == "b":
            print("To set or update the address of your restaurant branch, 1st go to the dashboard section, then go to branch's page. Add the address by adding branch name, enter city in the city's section & add are in the respective section, and then at the right bottom, click on updated to save the changes.")
        elif FAQ_cat2 == "c":
            print("To update opening & closing time of your restaurant, 1st go to the dashboard section, then go to branch's page. Add the opening & closing time in the respective section and then at the right bottom, click on updated to save the changes.")
        else:
            pass

    elif cat == "3":
        print("Products page handled queries!")
        FAQ = ["a. How can I add a new product?", "b. How can I update the price of a product?", "c. How can I delete a product?"]
        print("\n".join(FAQ))
        FAQ_cat3= input("How can I help you? (Type a, b or c): ")
        if FAQ_cat3 == "a":
            print("To add a new product, 1st go to the dashboard section, then go to product's page. Click on \"Add Products and Category\" button, choose category from the given ones or add a new category. Choose product from the given ones or add a new product.")
        elif FAQ_cat3 == "b":
            print("To update the price of a product, 1st go to the dashboard section, then go to product's page. Choose the product of which you want to update the price. Update the price in the respective section and then click on update to save the changes.")
        elif FAQ_cat3 == "c":
            print("To delete a product, 1st go to the dashboard section, then go to product's page. You'll see a bin icon in front of each product. Click on it, it will ask the confirmation, click on ok. The product has been deleted.")
        else:
            pass
        
    elif cat == "4":
        print("Tables page handled queries!")
        FAQ = ["a. How can I add a new table?", "b. How can I update the status of a table?", "c. What is the purpose of barcode on the table?", "d. How can I delete a table?"]
        print("\n".join(FAQ))
        FAQ_cat4= input("How can I help you? (Type a, b, c or d): ")
        if FAQ_cat4 == "a":
            print("To add a new table, 1st go to the dashboard section, then go to table's page. Click on \"Add Table\" button, then fixed the number of seats, then click on add table.")
        elif FAQ_cat4 == "b":
            print("To update the status of a table, 1st go to the dashboard section, then go to table's page. Choose the table of which you want to update the status. Update the status (available/booked) in the respective section and then click on update to save the changes.")
        elif FAQ_cat4 == "c":
            print("The barcode on the table is used for customer scanning purpose. It is used for booking an order by a customer without interaction of the waiter.")
        elif FAQ_cat4 == "d":
            print("To delete a table, 1st go to the dashboard section, then go to table's page. Choose a table that you want to delete, click on delete button. It'll ask confirmation, click on \"Yes, delete\". Table has been deleted.")
    else:
        pass

elif sec == "2":
    print("You have selected Orders!")
    FAQ = ["a. How can I add a new order?", "b. How can I monitored the order has been delivered or not?"]
    print("\n".join(FAQ))
    FAQ_sec2= input("How can I help you? (Type a or b): ")
    if FAQ_sec2 == "a":
        print("To add a new order, 1st go to the orders section, you'll see a button \"Add Order\" on the top right corner, click on it, now you're on Point of Sale section. Choose a product from the menu, add to cart all products, then you'll see a sale receipt on left side, select method, add cash amount, and then click on \"Place Oder\" button. The order has been added.")
    elif FAQ_sec2 == "b":
        print("To monitor the order has been delivered or not, 1st go to the Orders page, you'll see a status column on that page. All orders are mentioned and there status too that the order has been delivered or pending or cancelled. You can also update the status when the order has been delivered or cancelled.")
    else:
        pass

elif sec == "3":
    print("You have selected POS!")
    FAQ = "a. How can I manage discounts?"
    print(FAQ)
    FAQ_sec3= input("How can I help you? (Type a): ")
    if FAQ_sec3 == "a":
        print("To manage discounts, go to the POS section, on the top right corner, you'll see a \"Manage Discounts\" button. Click on it, adjust discounts, and then click on \"Submit\" button to save the changes.")
    else:
        pass


elif sec == "4":
    print("You have selected Branches!")
    FAQ = ["a. How can I add a new branch?", "b. How can I switch into another branch?", "c. What is the purpose of \"Sync Mneu\" button on Branches page?", "d. How can I delete a branch?"]
    print("\n".join(FAQ))
    FAQ_sec4= input("How can I help you? (Type a, b, c or d): ")
    if FAQ_sec4 == "a":
        print("To add a new branch, 1st go to the branches section, you'll see a button \"Add Branch\" on the top right side, click on it. Enter branch name, select city and select area and then click on \"Submit\" button.")
    elif FAQ_sec4 == "b":
        print("To switch into another branch, 1st go to the branches section, you'll see a button \"Set Current Branch\" on the top right side, click on it. The list of all branches will be shown. Choose the branch from the list and then click on \"Save\" button.")
    elif FAQ_sec4 == "c":
        print("The \"Sync Menu\" button is used to synchronize the menu of your restaurant with the selected branch.")
    elif FAQ_sec4 == "d":
        print("To delete a branch, 1st go to the branches section, all branches of your restaurant will be shown. In action column, you will see a \"Delete\" button, click on it. It'll ask confirmation, click on \"Yes, delete branch\". Branch has been deleted.")
else:
    pass