import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Page config set karna
st.set_page_config(page_title="Decision Tree GUI", layout="wide")

st.title("🛍️ Customer Purchase Prediction Dashboard")
st.write("Is application me aap customer attributes select karke purchase behavior predict kar sakte hain aur trained Decision Tree dekh sakte hain.")

# ==========================================
# 1. DATA LOAD AUR MODEL TRAINING (Cached)
# ==========================================
@st.cache_data
def load_and_train_model():
    # Dataset read karna
    df = pd.read_excel("Decision_Tree_Large_Practice_Dataset.xlsx")
    
    X = df.drop(columns=['Customer_ID', 'Made_Purchase'])
    y = df['Made_Purchase'].map({'Yes': 1, 'No': 0})
    
    # Preprocessing ke columns ka backup rakhne ke liye taaki alignment sahi rahe
    X_encoded = pd.get_dummies(X, drop_first=True)
    
    # Model configuration (Fixed for simplicity or can be tuned)
    model = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=42)
    model.fit(X_encoded, y)
    
    return model, X_encoded.columns, X

model, encoded_columns, original_X = load_and_train_model()

# Layout ko do parts me divide karna (Sidebar for inputs, Main panel for results)
st.sidebar.header("🎯 Customer Features Select Karein")

# ==========================================
# 2. GUI INPUT ELEMENTS (Sidebar)
# ==========================================
# Original dataset ke values ke unique options nikal kar dropdowns banana
age_group = st.sidebar.selectbox("Age Group", original_X['Age_Group'].unique())
annual_income = st.sidebar.selectbox("Annual Income", original_X['Annual_Income'].unique())
time_spent = st.sidebar.selectbox("Time Spent (Mins)", original_X['Time_Spent_Mins'].unique())
device = st.sidebar.selectbox("Device Used", original_X['Device_Used'].unique())
items_cart = st.sidebar.selectbox("Items in Cart", original_X['Items_in_Cart'].unique())
discount = st.sidebar.selectbox("Discount Available", original_X['Discount_Available'].unique())

# ==========================================
# 3. USER INPUT KO MODEL FORMAT ME BADALNA
# ==========================================
# Ek khali row banana original encoded structure ke sath
input_data = pd.DataFrame(0, index=[0], columns=encoded_columns)

# Jo options users ne select kiye hain, unke dummy columns ko 1 karna
if f"Age_Group_{age_group}" in encoded_columns: input_data[f"Age_Group_{age_group}"] = 1
if f"Annual_Income_{annual_income}" in encoded_columns: input_data[f"Annual_Income_{annual_income}"] = 1
if f"Time_Spent_Mins_{time_spent}" in encoded_columns: input_data[f"Time_Spent_Mins_{time_spent}"] = 1
if f"Device_Used_{device}" in encoded_columns: input_data[f"Device_Used_{device}"] = 1
if f"Items_in_Cart_{items_cart}" in encoded_columns: input_data[f"Items_in_Cart_{items_cart}"] = 1
if f"Discount_Available_{discount}" in encoded_columns: input_data[f"Discount_Available_{discount}"] = 1

# ==========================================
# 4. PREDICTION AUR GUI DISPLAY
# ==========================================
st.subheader("🔮 Prediction Result")

if st.sidebar.button("Predict Purchase"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]
    
    if prediction == 1:
        st.success(f"🎉 **Yes!** Customer purchase karega. (Probability: {probability[1]*100:.2f}%)")
    else:
        st.error(f"❌ **No!** Customer purchase nahi karega. (Probability: {probability[0]*100:.2f}%)")
else:
    st.info("Sidebar me values select karke 'Predict Purchase' button par click karein.")

st.markdown("---")

# ==========================================
# 5. DECISION TREE VISUALIZATION IN GUI
# ==========================================
st.subheader("🌳 Trained Decision Tree Structure")
with st.spinner("Tree visual taiyar ho raha hai..."):
    fig, ax = plt.subplots(figsize=(18, 8))
    plot_tree(
        model, 
        feature_names=encoded_columns, 
        class_names=['No', 'Yes'], 
        filled=True, 
        rounded=True, 
        fontsize=9,
        ax=ax
    )
    st.pyplot(fig)