# Modules
import streamlit as st
import pandas as pd
import functions

class App:
    def __init__(self):
        self.left_column, self.middle_column, self.right_column = st.columns(3)
    @st.cache_data
    def nse_stocks(self):
        st.dataframe(functions.nse_stocks())

app = App()
app.nse_stocks()