import streamlit as st

# Session state setup
if "messages" not in st.session_state:
    st.session_state.messages = []

# Default FAQ
default_questions = [
    {
        "question": "What is the purpose of color theme section?",
        "answer": "The color theme section allows you to customize the appearance of your company's dashboard."
    },
    {
        "question": "How can I add tax & delivery charges?",
        "answer": "To add tax & delivery charges, go to the dashboard > branch page. Fill in the tax & delivery charges section, then click 'Update' to save."
    },
    {
        "question": "How can I add a new product?",
        "answer": "To add a new product, go to dashboard > products page. Click 'Add Products and Category', select or create a category, then add your product."
    },
    {
        "question": "What is the purpose of barcode on the table?",
        "answer": "The barcode on the table lets customers scan it to place orders without waiter interaction."
    },
    {
        "question": "How can I manage discounts?",
        "answer": "To manage discounts, go to POS > click 'Manage Discounts' in the top-right. Adjust values and click 'Submit' to save."
    }
]

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

# App title
st.title("💬 Dassoft FAQ Chatbot")

# Show previous messages in chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Show default question buttons ---
st.markdown("### 💡 Frequently Asked Questions:")
for q in default_questions:
    if st.button(q["question"]):
        # Add user question and bot answer to chat history
        st.session_state.messages.append({"role": "user", "content": q["question"]})
        st.session_state.messages.append({"role": "assistant", "content": q["answer"]})
        st.rerun()

# --- Always-visible chat input field ---
user_input = st.chat_input("Ask your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    user_query = user_input.lower()
    found = False
    for keywords, response in faq_responses:
        if all(word in user_query for word in keywords):
            bot_reply = response
            found = True
            break

    if not found:
        bot_reply = "❌ Sorry, I couldn't find an answer. Please try rephrasing your question."

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
        
# --- End of the app ---
