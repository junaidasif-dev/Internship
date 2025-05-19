import streamlit as st

st.title("💬 Dassoft FAQ Bot")
st.write("Welcome to the Dassoft FAQ Bot! Please select a section below:")

# Sections
section = st.selectbox("Select a section:", ["", "Dashboard", "Orders", "POS", "Branches"])

if section == "Dashboard":
    st.subheader("Dashboard Categories")
    category = st.selectbox("Choose a category:", ["", "Company", "Branch", "Products", "Tables"])

    if category == "Company":
        question = st.radio("How can I help you?", [
            "How can I change the logo?",
            "What is the purpose of color theme section?",
            "I want to tell my customers about my company, but I don't know how to do it?"
        ])
        if question == "How can I change the logo?":
            st.success("To change the logo, go to Dashboard > Company page. Remove the current logo, add a new one, and click 'Update' at the bottom-right.")
        elif question == "What is the purpose of color theme section?":
            st.info("The color theme section allows you to customize the appearance of your company's dashboard.")
        elif question == "I want to tell my customers about my company, but I don't know how to do it?":
            st.success("Go to Dashboard > Company page. Add details in the description section and click 'Update' at the bottom-right.")

    elif category == "Branch":
        question = st.radio("How can I help you?", [
            "How can I add tax & delivery charges?",
            "How can I set or update the address of my restaurant branch?",
            "I want to update opening & closing time of my restaurant, please guide me?"
        ])
        if question == "How can I add tax & delivery charges?":
            st.success("Go to Dashboard > Branch page. Add tax & delivery charges in the respective section and click 'Update' at the bottom-right.")
        elif question == "How can I set or update the address of my restaurant branch?":
            st.success("Go to Dashboard > Branch page. Add branch name, city, area, and click 'Update' at the bottom-right.")
        elif question == "I want to update opening & closing time of my restaurant, please guide me?":
            st.success("Go to Dashboard > Branch page. Set opening & closing times and click 'Update' at the bottom-right.")

    elif category == "Products":
        question = st.radio("How can I help you?", [
            "How can I add a new product?",
            "How can I update the price of a product?",
            "How can I delete a product?"
        ])
        if question == "How can I add a new product?":
            st.success("Go to Dashboard > Product page. Click 'Add Products and Category', choose or create category, then add product.")
        elif question == "How can I update the price of a product?":
            st.success("Go to Dashboard > Product page. Select product, update price, and click 'Update'.")
        elif question == "How can I delete a product?":
            st.success("Go to Dashboard > Product page. Click the bin icon next to a product, confirm deletion.")

    elif category == "Tables":
        question = st.radio("How can I help you?", [
            "How can I add a new table?",
            "How can I update the status of a table?",
            "What is the purpose of barcode on the table?",
            "How can I delete a table?"
        ])
        if question == "How can I add a new table?":
            st.success("Go to Dashboard > Table page. Click 'Add Table', set number of seats, and click 'Add Table'.")
        elif question == "How can I update the status of a table?":
            st.success("Go to Dashboard > Table page. Select table, update status, and click 'Update'.")
        elif question == "What is the purpose of barcode on the table?":
            st.info("Barcodes allow customers to scan and place orders directly, without a waiter.")
        elif question == "How can I delete a table?":
            st.success("Go to Dashboard > Table page. Select a table, click 'Delete', confirm when prompted.")

elif section == "Orders":
    question = st.radio("How can I help you?", [
            "How can I add a new order?",
            "How can I monitored the order has been delivered or not?"
        ])
    if question == "How can I add a new order?":
        st.success("To add a new order, 1st go to the orders section, you'll see a button \"Add Order\" on the top right corner, click on it, now you're on Point of Sale section. Choose a product from the menu, add to cart all products, then you'll see a sale receipt on left side, select method, add cash amount, and then click on \"Place Oder\" button. The order has been added.")
    elif question == "How can I monitored the order has been delivered or not?":
        st.success("To monitor the order has been delivered or not, 1st go to the Orders page, you'll see a status column on that page. All orders are mentioned and there status too that the order has been delivered or pending or cancelled. You can also update the status when the order has been delivered or cancelled.")

elif section == "POS":
    st.radio("How can I help you?", [
            "How can I manage discounts?"
    ])
    st.success("To manage discounts, go to the POS section, on the top right corner, you'll see a \"Manage Discounts\" button. Click on it, adjust discounts, and then click on \"Submit\" button to save the changes.")


elif section == "Branches":
    question = st.radio("How can I help you?", [
            "How can I add a new branch?",
            "How can I switch into another branch?",
            "What is the purpose of \"Sync Mneu\" button on Branches page?",
            "How can I delete a branch?"
        ])
    if question == "How can I add a new branch?":
        st.success("To add a new branch, 1st go to the branches section, you'll see a button \"Add Branch\" on the top right side, click on it. Enter branch name, select city and select area and then click on \"Submit\" button.")
    elif question == "How can I switch into another branch?":
        st.success("To switch into another branch, 1st go to the branches section, you'll see a button \"Set Current Branch\" on the top right side, click on it. The list of all branches will be shown. Choose the branch from the list and then click on \"Save\" button.")
    elif question == "What is the purpose of \"Sync Mneu\" button on Branches page?":
        st.info("The \"Sync Menu\" button is used to synchronize the menu of your restaurant with the selected branch.")
    elif question == "How can I delete a branch?":
        st.success("To delete a branch, 1st go to the branches section, all branches of your restaurant will be shown. In action column, you will see a \"Delete\" button, click on it. It'll ask confirmation, click on \"Yes, delete branch\". Branch has been deleted.")

