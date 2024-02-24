import os
import streamlit.components.v1 as components
import streamlit as st
import time
import pandas as pd
import streamlit_shadcn_ui as ui

output = {'Confidence Level': 0.95,
 'Minimum Detectable Effect (MDE)': 0.1,
 'Statistical Power': 0.8,
 'Test Type': 'Two-sided',
 'Sample Size': 392}
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
# Take query and upload a file

col1.markdown("# Welcome to AB Experiment")
col1.chat_input("Type your query")
def change_csv_state():
    st.session_state["csv"]="done"
    st.session_state["log"]="done"

csv_file = col1.file_uploader("Upload a file", on_change= change_csv_state)


col2.markdown("# Statistics go here")
#col1.slider(label="power")

#col2.plotly_chart(figure_or_data=plotly.graph_objs.Data)
#ui.table(data=df, maxHeight=300)

#if st.session_state["csv"] == "done":
    #progress_bar = col1.progress(0)
    #for perc_completed in range(100):
        #time.sleep(0.01)
        #progress_bar.progress(perc_completed+1)
    #col1.success("Uploaded successfully!")
    #components.html(get_pyg_html(df), width=1300, height=1000, scrolling=True)
    #col3.metric(label="Temperature", value="60 °C", delta="3 °C") 
    #with st.expander("Click to read more"):
        #st.write("Hello, here are more details on this topic that you were interested in.")

# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
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

_RELEASE = False

if not _RELEASE:
    st.subheader("Component with variable args")
    _component_func = components.declare_component(
        "my_component",
        url="http://localhost:3001",
    )
    
    name_input = st.text_input("Enter a name", value="Streamlit")
    num_clicks = my_component(name = list(output.values()), key=list(output.keys()))
    st.markdown("You've clicked %s times!" % int(num_clicks))
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("my_component", path=build_dir)
