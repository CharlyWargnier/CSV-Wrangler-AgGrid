import streamlit as st
import pandas as pd

###################################
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode

###################################
from functionforDownloadButtons import download_button

###################################

st.set_page_config(page_title="📊 CSV Wrangler", layout="wide")
st.title("📊 CSV Wrangler")

c29, c30, c31 = st.beta_columns([1, 6, 1])

with c30:

    uploaded_file = st.file_uploader("", key="1")

    if uploaded_file is not None:
        file_container = st.beta_expander("Check your uploaded CSV")
        shows = pd.read_csv(uploaded_file)
        uploaded_file.seek(0)
        file_container.write(shows)

    else:
        st.success(
            f"""
                👆 Upload a csv file
                """
        )
        st.stop()

from st_aggrid.shared import GridUpdateMode

gb = GridOptionsBuilder.from_dataframe(shows)
gb.configure_selection(selection_mode="multiple", use_checkbox=True)
gridOptions = gb.build()

data = AgGrid(
    shows,
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    allow_unsafe_jscode=True,
    update_mode=GridUpdateMode.SELECTION_CHANGED,
)

st.write(type(data))

df = pd.DataFrame(list(data.items()))

CSVButton = download_button(
    df,
    "File.csv",
    "✨ Download filtered to CSV",
)
