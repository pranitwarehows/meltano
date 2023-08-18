
import streamlit as st
import pandas as pd
import sqlite3
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.title("Tables Data")
    # Fetch all table names in the database
    conn = sqlite3.connect("sqlite-sakila.db")
    table_query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = conn.execute(table_query).fetchall()
    tables = [table[0] for table in tables]

    # Sidebar for selecting tables
    selected_table = st.sidebar.selectbox("Choose a table", tables)

    # Display the selected table
    if selected_table:
        query = f"SELECT * FROM {selected_table}"
        data = pd.read_sql_query(query, conn)
        st.write(data)

with col2:
    st.title("Database Design Diagram")
    st.image("db_erd.png")

connection_string = "sqlite:///sqlite-sakila.db"
db = SQLDatabase.from_uri(connection_string)


st.text("Sample Questions")
st.text("1. Whos is our top customer?")
st.text("2. Which city has highest customers?")
st.text("3. Which Film has highest replacement cost?")
st.text("4. Which film category is rented a lot? ")


st.title("Ask me a Question")

name= st.text_input('Enter your question:')
# Construct the connection string using the parameters


if st.button("Fire Away"):
    llm= OpenAI(openai_api_key="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",temperature=0,model_name="gpt-3.5-turbo-16k", verbose= True)
    db_chain = SQLDatabaseChain.from_llm(llm,db,verbose=True)
    response = db_chain.run(name)
    st.write(response)
