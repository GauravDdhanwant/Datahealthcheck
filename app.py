import streamlit as st
from modules import data_ingestion, eda, insights, nlp_interface
from PIL import Image

# Load settings and configurations
from config.settings import PAGE_TITLE, LOGO_PATH, THEME_COLOR

# Set up the page
st.set_page_config(page_title=PAGE_TITLE, page_icon=":bar_chart:", layout="wide", initial_sidebar_state="expanded")

# Load and display the logo
logo = Image.open(LOGO_PATH)
st.sidebar.image(logo, use_column_width=True)

# Sidebar for data upload
st.sidebar.title("Upload your Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx", "parquet"])

# Main page content
st.title(PAGE_TITLE)

if uploaded_file is not None:
    # Data ingestion
    df = data_ingestion.load_data(uploaded_file)

    # Display initial data preview
    st.write("### Data Preview")
    st.dataframe(df.head())

    # EDA and data health check
    st.write("### Data Health Check")
    eda.display_data_health(df)

    # Insights and Use Cases
    st.write("### Insights and Suggested Use Cases")
    insights.display_insights(df)

    # Conversational interface
    st.write("### Ask Questions About the Data")
    user_input = st.text_input("Enter your query")
    if user_input:
        response = nlp_interface.handle_query(df, user_input)
        st.write(response)
else:
    st.info("Please upload a data file to proceed.")
