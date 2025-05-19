# 🗞️ News Category Classifier

A **Streamlit web app** that classifies news **headlines** and **articles** into categories:  
**World**, **Business**, **Sports**, and **Sci/Tech**.  
Built using a **Sentence Transformer** for semantic embeddings and an **LSTM model** for classification.

---

## 🔍 Features

- 🔎 **Predict Headline**: Classify a single headline into a news category.
- 📄 **Analyze Article**: Split a full article into sentences and categorize each sentence.
- 🎯 **Extract by Category**: Filter sentences from a paragraph based on a selected category.

---

## 📁 Repository Structure

├── app.py # Streamlit web app  
├── lstm_model.keras # Trained LSTM classification model  
├── requirements.txt # All dependencies for the app  
├── Model-training.ipynb # Jupyter notebook used to train and evaluate the model  
├── X_train.npy # Preprocessed training features  
├── X_test.npy # Preprocessed test features  
├── y_train.npy # Training labels  
├── y_test.npy # Test labels  

.npy files had been ignored because of larger size.

---

## 🧠 How It Works

1. **Embedding**:
   - Text is converted to 384-dimensional vectors using `all-MiniLM-L6-v2` from `sentence-transformers`.

2. **Reshaping**:
   - Each vector is reshaped into a 3D array (`24x16`) to fit LSTM input requirements.

3. **Prediction**:
   - A trained **Keras-based LSTM** model returns a category and its confidence score.

4. **Sentence Splitting**:
   - Articles are split into individual sentences using regular expressions for fine-grained classification.

---
