import os
import streamlit.components.v1 as components
import streamlit as st
import time
import pandas as pd
import streamlit_shadcn_ui as ui
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="AB Experiment",
    layout="wide"
)

@st.cache_data
def get_df() -> pd.DataFrame:
    return pd.read_csv("simulated_data.csv")

df = get_df()

st.title("ABA")

st.markdown("""<style>
            .appview-container .main .block-container{{padding-left: 0; padding-top: 0;}}
            </style>""", unsafe_allow_html=True)
col1, col2 = st.columns([1,2])
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(df, bins=20)

st.pyplot(fig)
# Take query and upload a file
col2.line_chart(data=df, x='variation', y='browse_time')
col1.markdown("# Welcome to AB Experiment")
input = col1.chat_input("Type your query")
output = {'Confidence Level': 0.95,
 'Minimum Detectable Effect (MDE)': 0.1,
 'Statistical Power': 0.8,
 'Test Type': 'Two-sided',
 'Sample Size': 392}
def change_csv_state():
    st.session_state["csv"]="done"

csv_file = col1.file_uploader("Upload a file", on_change= change_csv_state)
st.session_state["csv"]="none"

col2.markdown("# Statistics go here")
col2.metric(label="Confidence Level", value=output['Confidence Level'])
col2.metric(label="Minimum Detectable Effect (MDE)", value=output['Minimum Detectable Effect (MDE)'])
#col1.slider(label="power")
col2.scatter_chart(data=df, x='variation', y='browse_time')
#col2.plotly_chart(figure_or_data=plotly.graph_objs.Data)
#ui.table(data=df, maxHeight=300)

if st.session_state["csv"] == "done":
    progress_bar = col1.progress(0)
    for perc_completed in range(100):
        time.sleep(0.01)
        progress_bar.progress(perc_completed+1)
    col1.success("Uploaded successfully!")
    df = pd.read_csv(csv_file)
    col1.bar_chart(data=df, x='variation', y='browse_time')


#_RELEASE = False

def my_component(name, key=None):
    """Create a new instance of "my_component".

    Parameters
    ----------
    name: str
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        The number of times the component's "Click Me" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(name=name, key=key, default=0)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value

col2.markdown("# Statistics go here")
with col2.container():
    _component_func = components.declare_component(
        "my_component",
        url="http://localhost:3001",
    )

    # name_input = st.text_input("Enter a name", value="Streamlit")
    my_component(name = list(output.values()), key=list(output.keys()))
