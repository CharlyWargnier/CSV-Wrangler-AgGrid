# import pandas as pd
# import streamlit as st
# from st_aggrid import AgGrid
#
# st.set_page_config(page_title="Netflix Shows", layout="wide")
# st.title("Netlix shows analysis")
#
# shows = pd.read_csv("../data/netflix_titles.csv")


import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

from st_aggrid.shared import JsCode

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

st.set_page_config(page_title="Netflix Shows", layout="wide")

st.subheader(
    "Article: https://towardsdatascience.com/7-reasons-why-you-should-use-the-streamlit-aggrid-component-2d9a2b6e32f0"
)

st.title("Netlix shows analysis")

st.file_uploader("File uploader")


c29, c30, c31 = st.beta_columns([1, 6, 1])

with c30:

    uploaded_file = st.file_uploader("", key="1")

    if uploaded_file is not None:
        file_container = st.beta_expander("Check your uploaded CSV")
        shows = pd.read_csv(uploaded_file)
        uploaded_file.seek(0)
        file_container.write(shows)
        # dfNew

    else:
        st.warning(
            f"""
                👹 **Oh! What the Fuzz!**
                """
        )
        st.stop()


# GSCDf = GSCDf.fillna(value="")

#  st.set_page_config(page_title="Netflix Shows", layout="wide")
# st.title("Netlix shows analysis")


#   shows = pd.read_csv("Datasets\Fraud dataset\DescriptiveFile1KRows.csv")
# shows = pd.read_csv("../data/netflix_titles.csv")

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

data

st.stop()

# loaded_data = pd.DataFrame(
#     {"Fruit": ["Grape", "Apple"], "Vegetable": ["Carrot", "Green Bean"]}
# )
gb = GridOptionsBuilder.from_dataframe(loaded_data)
#
# gb.configure_default_column(
#     groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True
# )
#
#
# gb.configure_pagination(enabled=True)
# gridOptions = gb.build()
#
# main_grid_response = AgGrid(
#     loaded_data,
#     gridOptions=gridOptions,
#     height=400,
#     width="100%",
#     # data_return_mode=DataReturnMode.AS_INPUT,
#     # update_mode=GridUpdateMode.MODEL_CHANGED,
#     fit_columns_on_grid_load=True,  # automatically fits all columns to be displayed in the grid in one view
#     allow_unsafe_jscode=True,  # Set it to True to allow jsfunction to be injected
#     reload_data=True,
#     enable_enterprise_modules=True,
#     key="main_grid",
# )

# st.stop()

st.set_page_config(page_title="Netflix Shows", layout="wide")
st.title("Netlix shows analysis")


shows = pd.read_csv("Datasets\Fraud dataset\DescriptiveFile1KRows.csv")


gb = GridOptionsBuilder.from_dataframe(shows)

gridOptions = gb.build()

data = AgGrid(
    shows,
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    allow_unsafe_jscode=True,
)


# shows = pd.read_csv("../data/netflix_titles.csv")

gb.configure_pagination()
gb.configure_side_bar()
gb.configure_default_column(
    groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True
)

data = AgGrid(
    shows,
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    allow_unsafe_jscode=True,
)

cellsytle_jscode = JsCode(
    """
function(params) {
    if (params.value.includes('United States')) {
        return {
            'color': 'white',
            'backgroundColor': 'darkred'
        }
    } else {
        return {
            'color': 'black',
            'backgroundColor': 'white'
        }
    }
};
"""
)

# gridOptions = gb.build()
# AgGrid(shows, gridOptions=gridOptions, enable_enterprise_modules=True)
# gb.configure_column("country", cellStyle=cellsytle_jscode)

from st_aggrid.shared import GridUpdateMode


def display_table(df: pd.DataFrame) -> AgGrid:
    # Configure AgGrid options
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection("single")
    return AgGrid(
        df,
        gridOptions=gb.build(),
        # this override the default VALUE_CHANGED
        update_mode=GridUpdateMode.MODEL_CHANGED,
    )


# gb.configure_selection(selection_mode="multiple", use_checkbox=True)

gb.configure_selection(
    "multiple", use_checkbox=True, groupSelectsChildren=True, groupSelectsFiltered=True
)


data = AgGrid(
    shows,
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    allow_unsafe_jscode=True,
    update_mode=GridUpdateMode.SELECTION_CHANGED,
)

# st.write(data)


display_table(data)