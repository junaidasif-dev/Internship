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

    # Keyword-based responses
    faq_responses = [
        # Logo-related
        (["change", "logo"], "To change the logo, go to the dashboard > company page. Remove the current logo, add a new one, and click on 'Update' to save."),
        (["update", "logo"], "To change the logo, go to the dashboard > company page. Remove the current logo, add a new one, and click on 'Update' to save."),
        (["add", "logo"], "To change the logo, go to the dashboard > company page. Remove the current logo, add a new one, and click on 'Update' to save."),
        (["upload", "logo"], "To change the logo, go to the dashboard > company page. Remove the current logo, add a new one, and click on 'Update' to save."),
        (["edit", "logo"], "To change the logo, go to the dashboard > company page. Remove the current logo, add a new one, and click on 'Update' to save."),

        # Company info
        (["company", "details"], "To add company details, go to dashboard > company page. Add the description and click 'Update'."),
        (["company", "info"], "To add company details, go to dashboard > company page. Add the description and click 'Update'."),
        (["company", "information"], "To add company details, go to dashboard > company page. Add the description and click 'Update'."),
        (["business", "description"], "To add company details, go to dashboard > company page. Add the description and click 'Update'."),
        (["organization", "details"], "To add company details, go to dashboard > company page. Add the description and click 'Update'."),

        # Branch address
        (["update", "address"], "To update branch address, go to dashboard > branch page. Add name, city, area, then click 'Update'."),
        (["add", "address"], "To update branch address, go to dashboard > branch page. Add name, city, area, then click 'Update'."),
        (["change", "location"], "To update branch address, go to dashboard > branch page. Add name, city, area, then click 'Update'."),
        (["branch", "location"], "To update branch address, go to dashboard > branch page. Add name, city, area, then click 'Update'."),
        (["edit", "address"], "To update branch address, go to dashboard > branch page. Add name, city, area, then click 'Update'."),

        # Timing
        (["opening", "closing", "time"], "To update opening & closing time, go to dashboard > branch page. Update time fields and save."),
        (["opening", "time"], "To update opening & closing time, go to dashboard > branch page. Update time fields and save."),
        (["closing", "time"], "To update opening & closing time, go to dashboard > branch page. Update time fields and save."),
        (["business", "hours"], "To update opening & closing time, go to dashboard > branch page. Update time fields and save."),
        (["working", "hours"], "To update opening & closing time, go to dashboard > branch page. Update time fields and save."),
        (["shop", "timing"], "To update opening & closing time, go to dashboard > branch page. Update time fields and save."),

        # Product/price
        (["price", "product"], "To update product price, go to dashboard > product page. Edit price and click 'Update'."),
        (["cost", "item"], "To update product price, go to dashboard > product page. Edit price and click 'Update'."),
        (["edit", "menu"], "To update product price, go to dashboard > product page. Edit price and click 'Update'."),
        (["update", "product", "price"], "To update product price, go to dashboard > product page. Edit price and click 'Update'."),
        (["price", "menu"], "To update product price, go to dashboard > product page. Edit price and click 'Update'."),
        (["menu", "price"], "To update product price, go to dashboard > product page. Edit price and click 'Update'."),
        (["add", "menu"], "To add a new product, go to dashboard > products page. Click 'Add Products and Category', select or create a category, then add your product."),
        (["update", "menu"], "To add a new product, go to dashboard > products page. Click 'Add Products and Category', select or create a category, then add your product."),

        # Delete product
        (["delete", "product"], "To delete a product, go to product page, click the bin icon, and confirm deletion."),
        (["remove", "product"], "To delete a product, go to product page, click the bin icon, and confirm deletion."),
        (["delete", "menu"], "To delete a product, go to product page, click the bin icon, and confirm deletion."),
        (["remove", "item"], "To delete a product, go to product page, click the bin icon, and confirm deletion."),

        # Table management
        (["add", "table"], "To add a table, go to dashboard > tables. Click 'Add Table', choose seats, and confirm."),
        (["create", "table"], "To add a table, go to dashboard > tables. Click 'Add Table', choose seats, and confirm."),
        (["insert", "table"], "To add a table, go to dashboard > tables. Click 'Add Table', choose seats, and confirm."),
        (["delete", "table"], "To delete a table, go to tables page, select the table, click delete, confirm action."),
        (["remove", "table"], "To delete a table, go to tables page, select the table, click delete, confirm action."),
        (["edit", "table", "status"], "To update table status, go to tables page, select table, update status, and click 'Update'."),
        (["table", "status"], "To update table status, go to tables page, select table, update status, and click 'Update'."),

        # Orders
        (["add", "order"], "To add an order, go to Orders > click 'Add Order'. Select products, add to cart, and click 'Place Order'."),
        (["create", "order"], "To add an order, go to Orders > click 'Add Order'. Select products, add to cart, and click 'Place Order'."),
        (["place", "order"], "To add an order, go to Orders > click 'Add Order'. Select products, add to cart, and click 'Place Order'."),
        (["track", "order"], "To track order status, go to Orders page. Check status column for updates."),
        (["order", "status"], "To track order status, go to Orders page. Check status column for updates."),
        (["where", "order"], "To track order status, go to Orders page. Check status column for updates."),

        # Branch management
        (["add", "branch"], "To add a branch, go to Branches > click 'Add Branch'. Enter info and click 'Submit'."),
        (["create", "branch"], "To add a branch, go to Branches > click 'Add Branch'. Enter info and click 'Submit'."),
        (["new", "branch"], "To add a branch, go to Branches > click 'Add Branch'. Enter info and click 'Submit'."),
        (["switch", "branch"], "To switch branch, go to Branches > click 'Set Current Branch'. Select branch and save."),
        (["change", "branch"], "To switch branch, go to Branches > click 'Set Current Branch'. Select branch and save."),
        (["set", "branch"], "To switch branch, go to Branches > click 'Set Current Branch'. Select branch and save."),
        (["delete", "branch"], "To delete a branch, go to Branches > click 'Delete' next to the branch. Confirm action."),
        (["remove", "branch"], "To delete a branch, go to Branches > click 'Delete' next to the branch. Confirm action."),

        # Menu sync
        (["sync", "menu"], "The 'Sync Menu' button synchronizes the menu with the selected branch."),
        (["synchronize", "menu"], "The 'Sync Menu' button synchronizes the menu with the selected branch."),
        (["same", "menu"], "The 'Sync Menu' button synchronizes the menu with the selected branch."),
    ]

    found = False
    for keywords, response in faq_responses:
        if all(word in user_query for word in keywords):
            print(response)
            found = True
            break

    if not found:
        print("Sorry, I couldn't find an answer. Please rephrase your question with appropriate keywords!")
