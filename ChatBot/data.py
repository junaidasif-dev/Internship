import pandas as pd

dataset = [
    # section 1: Dashboard
    ('The dashboard is used for managing the whole system. It is used for managing branches, products, orders, tables, company theme, details and many more.'),
        # Category 1: Company Page
        ('The company page is used for managing the company details like logo, name, email, phone number, description and theme.'),
        ('To add/update/change logo, Goto Dashboard -> Company Page -> see at logo section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.' ),
        ('To add/update/change company name, Goto Dashboard -> Company Page -> see at company name section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.' ),
        ('To add/update/change company mail address, Goto Dashboard -> Company Page -> see at company mail section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.' ),
        ('To add/update/change company phone number, Goto Dashboard -> Company Page -> see at company phone number section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.' ),
        ('To add/update/change company description/details/information/bio/about, Goto Dashboard -> Company Page -> see at company description section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.' ),
        ('To add/update/change company color/theme, Goto Dashboard -> Company Page -> see at company choose theme section -> choose colors from the given section -> Click on update to save the changes.' ),
        ('The choose theme section is used for managing the theme of the company.'),
        # Category 2: Branch Page
        ('The branch page is used for managing the branch details like name, address, location, slider, opening/closing time and tax/delivery charges.' ),
        ('To add/update/change branch slider/slideshow/banner, Goto Dashboard -> Branch Page -> see at company slider section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.' ),
        ('To add/update/change branch name/title, Goto Dashboard -> Branch Page -> see at branch name section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.' ),
        ('To add/update/change branch address/location, Goto Dashboard -> Branch Page -> see at branch name, city & area section -> remove it if it exists already, otherwise fill those sections -> Click on update to save the changes.' ),
        ('To add/update/change tax/delivery charges/rate/price/cost, Goto Dashboard -> Branch Page -> see at tax & delivery charges section -> remove it if it exists already, otherwise fill those sections -> Click on update to save the changes.'),
        ('To add/update/change opening/closing time, Goto Dashboard -> Branch Page -> see at opening time & closing time section -> remove it if it exists already, otherwise fill those sections -> Click on update to save the changes.' ),
        # Category 3: Products Page
        ('The products page is used for managing the products details like name, description, price, quantity and photo/logo.'),
        ('To add new product/item/menu/deal/category, Goto Dashboard -> Products Page -> Click on "Add products and Category" button -> Choose category from the given ones otherwise Add New Category, then choose products from the given products otherwise add new product by using "Custom Product" section. After finalizing the product, a form will be open. Add product name, quantity, description & price and click on update to save the changes.' ),
        ('To roemove/delete product/menu/item/deal, Goto Dashboard -> Products Page -> You will see the bin icon in front of each product. Click on the bin icon to remove/delete the product.'),
        ('To add/update/change product/item/menu photo/logo, Goto Dashboard -> Products Page -> Choose the product that you want to update. -> Click on "Select photo here". Add photo. Click on update to save the changes.' ),
        ('To add/update/change product/item/menu price/cost, Goto Dashboard -> Products Page -> Choose the product that you want to update. -> Add price in "Product Price" section. Click on update to save the changes.' ),
        ('To add/update/change product/item/menu description/details, Goto Dashboard -> Products Page -> Choose the product that you want to update. -> Add description in "Description" section. Click on update to save the changes.' ),
        ('To add/update/change product/item/menu name, Goto Dashboard -> Products Page -> Choose the product that you want to update. -> Add name in "Product Name" section. Click on update to save the changes.' ),
        ('To add/update/change product/item/menu quantity, Goto Dashboard -> Products Page -> Choose the product that you want to update. -> Add quantity in "Product Quantity" section. Click on update to save the changes.' ),
        # Category 4: Tables Page
        ('The tables page is used for managing the tables details like table number, seats and barcode/qr code.'),
        ('To add new table, Goto Dashboard -> Table Page -> Click on "Add Table" button -> Fill "Table Seats" section. Click on "Add Table" button to save the changes.'),
        ('The barcode on the table is used for customer scanning purpose. It is used for booking an order by a customer without interaction of the waiter.'),
        ('To add/generate barcode/qr code, add/update a table.'),
        ('To remove/delete table, Goto Dashboard -> Table Page -> Choose the table that you want to delete. -> Click on "Delete" button. Then click on "Yes, Delete" for final confirmation'),
        ('To change/update table status/availability, Goto Dashboard -> Table Page -> Choose the table that you want to update. -> Choose status from "Table Availability". Click on "Update" button to save the changes.' ),
    
    # section 2: Orders Page
    ('The orders page is used for managing the orders details like adding new order, status and cancelation of order etc.'),
    ('To add/place new order, Goto Order Page -> Click on "Add Order" button -> Choose menu. Then add products in cart. You will see on the left side, a sale receipt will start creating. If you want to add any discount, click on "% Manage Discounts" button, fill those sections and click on submit. Then click on "Add Cash" button, enter amount that user had been paid, and click on submit. Then choose the delivery method by clicking on "Method" button. Click on "Place Order" button for confirming the order.' ),
    ('To search/track order, Goto Order Page -> Enter order id in search bar. If the order id is correct, you will see the order details.'),
    ('To check order status, Goto Order Page -> You will see the status column on the page and you can check the status of each order in drop down menu.'),
    ('To change/update order status, Goto Order Page -> Enter order id in search bar. If the order id is correct, you will see the order details. Then choose status from "Status" column. Click on "Apply" button to save the changes.'),
    ('To cancel the order, Goto Order Page -> Enter order id in search bar. If the order id is correct, you will see the order details. Then set its status "cancel" from "Status" column. Click on "Apply" button to save the changes.'),
    
    # section 3: POS Page
    ('The POS (Point of Sale) page is used for managing the orders, delivery methods and payments.'),
    ('To add/update/change discount, Goto POS (Point of Sale) Page -> Click on "% Manage Discounts" button -> Update the given sections and click on submit.'),
    ('To add/update cash, Goto POS (Point of Sale) Page -> Click on "Add Cash" button -> Enter amount that user had been paid, and click on submit.'),
    ('To add/change/update delivery method, Goto POS (Point of Sale) Page -> Click on "Method" button -> Choose the delivery method from the given ones.'),
   
   # section 4: Branches Page
    ('The branches page is used for managing the branches like monitor all branches, switch into different branch, add new branch and delete a branch etc.' ),
    ('To add new branch, Goto Branches Page -> Click on "Add Branch" button -> A new page will be open. Add branch name, city and area. Click on "Submit" for save the changes.'),
    ('To change/switch/update branch, Goto Branches Page -> Click on "Set Current Branch" button -> Choose the branch from the present branches.'),
    ('To delete/remove branch, Goto Branches Page -> You will see delete button in actions column. Click on it, then click on "Yes, Delete Branch" for final confirmation.'),
    ('To repeat/copy/same menu into different branches, Goto  Branches Page -> Click on "Sync Menu" button -> Fill the given sections and click on "Finalize Menu" button to save the changes.'),
    ('The sync menu button is used for syncing the menu into different branches.'),

    ("For support, please reach out to the Dassoft team: 0312-0000000")
]

# save data into json file
df = pd.DataFrame(dataset, columns=["Question"])
