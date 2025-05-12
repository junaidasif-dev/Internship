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
            st.info("Go to Dashboard > Branch page. Add branch name, city, area, and click 'Update' at the bottom-right.")
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
            st.info("Go to Dashboard > Product page. Select product, update price, and click 'Update'.")
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
            st.info("Go to Dashboard > Table page. Select table, update status, and click 'Update'.")
        elif question == "What is the purpose of barcode on the table?":
            st.success("Barcodes allow customers to scan and place orders directly, without a waiter.")
        elif question == "How can I delete a table?":
            st.success("Go to Dashboard > Table page. Select a table, click 'Delete', confirm when prompted.")

elif section in ["Orders", "POS", "Branches"]:
    st.warning(f"FAQ section for **{section}** is under development.")
