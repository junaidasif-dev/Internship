import streamlit as st

# Define FAQ data as a nested dictionary
faq_data = {
    "Dashboard": {
        "Company Page": {
            "What is the company page used for?": "The company page is used for managing the company details like logo, name, email, phone number, description and theme.",
            "How to update the company logo?": "Goto Dashboard -> Company Page -> see at logo section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.",
            "How to update the company name?": "Goto Dashboard -> Company Page -> see at company name section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.",
            "How to update the company mail address?": "Goto Dashboard -> Company Page -> see at company mail section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.",
            "How to update the company phone number?": "Goto Dashboard -> Company Page -> see at company phone number section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.",
            "How to update company description or about info?": "Goto Dashboard -> Company Page -> see at company description section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.",
            "How to change the company color or theme?": "Goto Dashboard -> Company Page -> see at company choose theme section -> choose colors from the given section -> Click on update to save the changes.",
            "What is the choose theme section used for?": "The choose theme section is used for managing the theme of the company."
        },
        "Branch Page": {
            "What is the branch page used for?": "The branch page is used for managing the branch details like name, address, location, slider, opening/closing time and tax/delivery charges.",
            "How to update the branch slider?": "Goto Dashboard -> Branch Page -> see at company slider section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.",
            "How to update the branch name?": "Goto Dashboard -> Branch Page -> see at branch name section -> remove it if it exists already, otherwise add it in the given section -> Click on update to save the changes.",
            "How to update the branch address or location?": "Goto Dashboard -> Branch Page -> see at branch name, city & area section -> remove it if it exists already, otherwise fill those sections -> Click on update to save the changes.",
            "How to update tax or delivery charges?": "Goto Dashboard -> Branch Page -> see at tax & delivery charges section -> remove it if it exists already, otherwise fill those sections -> Click on update to save the changes.",
            "How to update opening and closing times?": "Goto Dashboard -> Branch Page -> see at opening time & closing time section -> remove it if it exists already, otherwise fill those sections -> Click on update to save the changes."
        },
        "Products Page": {
            "What is the products page used for?": "The products page is used for managing the products details like name, description, price, quantity and photo/logo.",
            "How to add a new product or menu item?": "Goto Dashboard -> Products Page -> Click on 'Add products and Category' button -> Choose category or add a new one -> choose or add product -> Fill form with name, quantity, description, price -> Click update to save.",
            "How to delete a product?": "Goto Dashboard -> Products Page -> Click bin icon in front of the product to remove/delete it.",
            "How to update product photo or logo?": "Goto Dashboard -> Products Page -> Choose product -> Click 'Select photo here' -> Add photo -> Click update.",
            "How to update product price?": "Goto Dashboard -> Products Page -> Choose product -> Enter new value in 'Product Price' section -> Click update.",
            "How to update product description?": "Goto Dashboard -> Products Page -> Choose product -> Update 'Description' section -> Click update.",
            "How to update product name?": "Goto Dashboard -> Products Page -> Choose product -> Update 'Product Name' section -> Click update.",
            "How to update product quantity?": "Goto Dashboard -> Products Page -> Choose product -> Update 'Product Quantity' section -> Click update."
        },
        "Tables Page": {
            "What is the tables page used for?": "The tables page is used for managing the tables details like table number, seats and barcode/qr code.",
            "How to add a new table?": "Goto Dashboard -> Table Page -> Click on 'Add Table' -> Fill 'Table Seats' section -> Click 'Add Table' to save.",
            "What is the table barcode used for?": "The barcode on the table is used for customer scanning purpose. It is used for booking an order by a customer without interaction of the waiter.",
            "How to generate a barcode for a table?": "To add/generate barcode/qr code, add or update a table.",
            "How to delete a table?": "Goto Dashboard -> Table Page -> Choose table -> Click 'Delete' -> Confirm with 'Yes, Delete'.",
            "How to change table status or availability?": "Goto Dashboard -> Table Page -> Choose table -> Set 'Table Availability' -> Click 'Update'."
        }
    },
    "Orders Page": {
        "What is the orders page used for?": "The orders page is used for managing the orders details like adding new order, status and cancelation of order etc.",
        "How to place a new order?": "Goto Order Page -> Click on 'Add Order' -> Choose menu -> Add products to cart -> Apply discount -> Add cash -> Choose delivery method -> Click 'Place Order'.",
        "How to search an order?": "Goto Order Page -> Enter order ID in search bar.",
        "How to check order status?": "Goto Order Page -> View status column to check current status.",
        "How to update order status?": "Goto Order Page -> Search by order ID -> Set new status from 'Status' column -> Click 'Apply'.",
        "How to cancel an order?": "Goto Order Page -> Search by order ID -> Set status to 'cancel' -> Click 'Apply'."
    },
    "POS Page": {
        "What is the POS page used for?": "The POS (Point of Sale) page is used for managing the orders, delivery methods and payments.",
        "How to apply or update a discount in POS?": "Goto POS Page -> Click on '% Manage Discounts' -> Update details -> Click Submit.",
        "How to add or update cash in POS?": "Goto POS Page -> Click on 'Add Cash' -> Enter amount -> Click Submit.",
        "How to change delivery method in POS?": "Goto POS Page -> Click on 'Method' -> Choose delivery method."
    },
    "Branches Page": {
        "What is the branches page used for?": "The branches page is used for managing the branches like monitor all branches, switch into different branch, add new branch and delete a branch etc.",
        "How to add a new branch?": "Goto Branches Page -> Click on 'Add Branch' -> Fill branch name, city, area -> Click Submit.",
        "How to switch branches?": "Goto Branches Page -> Click 'Set Current Branch' -> Choose desired branch.",
        "How to delete a branch?": "Goto Branches Page -> Click delete button in actions -> Confirm with 'Yes, Delete Branch'.",
        "How to sync menu into different branches?": "Goto Branches Page -> Click on 'Sync Menu' -> Fill the sections -> Click 'Finalize Menu'.",
        "What is the sync menu button used for?": "The sync menu button is used for syncing the menu into different branches."
    }
    #"Support": {
     #   "How to get support?": "For support, please reach out to the Dassoft team: 0312-0000000"
    #}
}

# Streamlit app logic
st.set_page_config(page_title="Dassoft Assistant", layout="centered")
st.title("🤖 DASSOFT Chatbot")
st.markdown("### 💬 Hello, how can I help you?")

selected_section = st.selectbox("Choose section", list(faq_data.keys()))

if selected_section:
    categories = faq_data[selected_section]
    if isinstance(categories, dict) and all(isinstance(v, dict) for v in categories.values()):
        selected_category = st.selectbox("Choose category", [""] + list(categories.keys()))
        if selected_category:
            question = st.selectbox("Choose your question", [""] + list(categories[selected_category].keys()))
            if question:
                st.info(categories[selected_category][question])
    else:
        question = st.selectbox("Choose your question", [""] + list(categories.keys()))
        if question:
            st.info(categories[question])

# --- footer ---
st.markdown("---")
st.markdown("📞 For support, contact Dassoft team: **0312-0000000**")