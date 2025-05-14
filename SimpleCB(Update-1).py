import string

print("Welcome to the Dassoft FAQ Bot!")
default_Question = [
    "a. What is the purpose of color theme section?",
    "b. How can I add tax & delivery charges?",
    "c. How can I add a new product?",
    "d. What is the purpose of barcode on the table?",
    "e. How can I manage discounts?"
]

print("\n".join(default_Question))
dq = input("Please select a question (Type a, b, c, d or e): ").lower()

# Default Questions Responses
if dq == "a":
    print("The color theme section allows you to customize the appearance of your company's dashboard.")
elif dq == "b":
    print("To add tax & delivery charges, 1st go to the dashboard section, then go to branch's page. Add the tax & delivery charges in the respective section and then at the right bottom, click on updated to save the changes.")
elif dq == "c":
    print("To add a new product, 1st go to the dashboard section, then go to product's page. Click on \"Add Products and Category\" button, choose category from the given ones or add a new category. Choose product from the given ones or add a new product.")
elif dq == "d":
    print("The barcode on the table is used for customer scanning purpose. It is used for booking an order by a customer without interaction of the waiter.")
elif dq == "e":
    print("To manage discounts, go to the POS section, on the top right corner, you'll see a \"Manage Discounts\" button. Click on it, adjust discounts, and then click on \"Submit\" button to save the changes.")

else:
    # Take free-text user input
    user_query = input("How can I help you? ").lower()

    # Define keyword-based responses
    faq_responses = [
        (["change", "logo"], "To change the logo, go to the dashboard > company page. Remove the current logo, add a new one, and click on 'Update' to save."),
        (["update", "logo"], "To change the logo, go to the dashboard > company page. Remove the current logo, add a new one, and click on 'Update' to save."),
        (["add", "logo"], "To change the logo, go to the dashboard > company page. Remove the current logo, add a new one, and click on 'Update' to save."),
        (["company", "details"], "To add details about your company, go to the dashboard > company page. Add the description and click on 'Update'."),
        (["company", "info"], "To add details about your company, go to the dashboard > company page. Add the description and click on 'Update'."),
        (["company", "information"], "To add details about your company, go to the dashboard > company page. Add the description and click on 'Update'."),
        (["update", "address"], "To update your restaurant branch address, go to dashboard > branch page. Add branch name, city, and area, then click on 'Update'."),
        (["add", "address"], "To update your restaurant branch address, go to dashboard > branch page. Add branch name, city, and area, then click on 'Update'."),
        (["opening", "closing", "time"], "To update opening & closing time, go to dashboard > branch page and update the time fields, then save changes."),
        (["opening", "time"], "To update opening & closing time, go to dashboard > branch page and update the time fields, then save changes."),
        (["closing", "time"], "To update opening & closing time, go to dashboard > branch page and update the time fields, then save changes."),
        (["price", "product"], "To update the price of a product, go to dashboard > product page. Edit the price and click 'Update'."),
        (["delete", "product"], "To delete a product, go to product page, click the bin icon beside the product, confirm deletion."),
        (["add", "table"], "To add a new table, go to dashboard > tables page. Click 'Add Table', choose seats, and confirm."),
        (["status", "table"], "To update table status, go to tables page, select the table, update its status, and click 'Update'."),
        (["delete", "table"], "To delete a table, go to tables page, choose the table, click delete, confirm action."),
        (["add", "order"], "To add an order, go to Orders > click 'Add Order'. Select products, add to cart, and click 'Place Order'."),
        (["track", "order"], "To track order status, go to Orders page. Check status column for delivered, pending, or cancelled."),
        (["add", "branch"], "To add a new branch, go to Branches > click 'Add Branch'. Enter info and click 'Submit'."),
        (["switch", "branch"], "To switch branch, go to Branches > click 'Set Current Branch'. Select branch and click 'Save'."),
        (["change", "branch"], "To switch branch, go to Branches > click 'Set Current Branch'. Select branch and click 'Save'."),
        (["sync", "menu"], "The 'Sync Menu' button synchronizes the menu with the selected branch."),
        (["delete", "branch"], "To delete a branch, go to Branches > click 'Delete' next to the branch. Confirm action.")
    ]


    found = False
    for keywords, response in faq_responses:
        if all(word in user_query for word in keywords):
            print(response)
            found = True
            break

    if not found:
        print("Sorry, I couldn't find an answer. Please rephrase your question with appropriate keywords!")
