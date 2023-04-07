import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("bank_prospects_3.csv")

# Sidebar
st.sidebar.title("Filters")
option = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2"])

# Main page
st.title("My Streamlit App")
st.write("Here is some data:")
st.dataframe(data)

if option == "Option 1":
    st.write("You selected Option 1")
else:
    st.write("You selected Option 2")

# Plot
fig, ax = plt.subplots()
ax.plot(data["x"], data["y"])
st.pyplot(fig)




# from sqlalchemy import create_engine

# # Execute code in Docker 
# conn_str = "postgresql+psycopg2://root:password@postgres_db:5434/database"

# # Execute code in local
# # conn_str = "postgresql+psycopg2://root:password@localhost:5434/database"

# engine = create_engine(conn_str)
# connection = engine.connect()


# row = connection.execute("SELECT * FROM public.users;").fetchall()

# print(row)

# connection.close()