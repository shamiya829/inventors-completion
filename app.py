import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the dataset with caching
@st.cache_data
def load_data():
    # Replace with your actual file path or upload mechanism
    return pd.read_csv('completion.csv')

data_clean = load_data()

# Handle NaN values in 'Stages' (replace with 0 or another suitable value)
data_clean['Stages'] = data_clean['Stages'].fillna(0)

# Convert categorical variables into numerical codes
data_clean['Formation_Code'] = data_clean['Formation'].astype('category').cat.codes
data_clean['Compl_Type_Code'] = data_clean['Compl. Type'].astype('category').cat.codes

# Streamlit app title
st.title("Exploratory Data Analysis (EDA) - Well Data")

# Sidebar for options
st.sidebar.header("Choose Plot Type")
plot_type = st.sidebar.selectbox("Select Plot", ["2D Visualization", "3D Visualization"])

# Function for 2D scatter plots
def plot_2d():
    fig = make_subplots(
        rows=3, cols=2,
        subplot_titles=["Color by Formation", "Color by Completion Type", 
                        "Color by Best 1-Month BOPD", "Color by Fluid Volume",
                        "Color by Proppant Volume", "Color by Well Spacing"],
        vertical_spacing=0.1, horizontal_spacing=0.1,
        specs=[[{'type': 'scatter'}, {'type': 'scatter'}],
               [{'type': 'scatter'}, {'type': 'scatter'}],
               [{'type': 'scatter'}, {'type': 'scatter'}]]
    )

    # 1. Color by Formation
    trace1 = go.Scatter(
        x=data_clean['Longitude'],
        y=data_clean['Latitude'],
        mode='markers',
        marker=dict(
            size=data_clean['Stages'],
            color=data_clean['Formation_Code'],
            colorscale='Viridis',
            colorbar=dict(title='Formation')
        ),
        text=data_clean['Well Name'],
        hoverinfo='text'
    )

    # 2. Color by Completion Type
    trace2 = go.Scatter(
        x=data_clean['Longitude'],
        y=data_clean['Latitude'],
        mode='markers',
        marker=dict(
            size=data_clean['Stages'],
            color=data_clean['Compl_Type_Code'],
            colorscale='Blues',
            colorbar=dict(title='Completion Type')
        ),
        text=data_clean['Well Name'],
        hoverinfo='text'
    )

    # 3. Color by Best 1-Month BOPD
    trace3 = go.Scatter(
        x=data_clean['Longitude'],
        y=data_clean['Latitude'],
        mode='markers',
        marker=dict(
            size=data_clean['Stages'],
            color=data_clean['Best1 Mo BOPD'],
            colorscale='RdYlGn',
            colorbar=dict(title='Best 1-Month BOPD')
        ),
        text=data_clean['Well Name'],
        hoverinfo='text'
    )

    # Add all traces to the subplots
    fig.add_trace(trace1, row=1, col=1)
    fig.add_trace(trace2, row=1, col=2)
    fig.add_trace(trace3, row=2, col=1)

    # Update layout and title
    fig.update_layout(
        title="2D Well Visualizations: Different Color Groupings",
        height=800,
        width=1000,
        showlegend=False,
        title_x=0.5
    )

    st.plotly_chart(fig)

# Function for 3D scatter plots
def plot_3d():
    fig = make_subplots(
        rows=3, cols=2,
        subplot_titles=["Color by Formation", "Color by Completion Type", 
                        "Color by Best 1-Month BOPD", "Color by Fluid Volume",
                        "Color by Proppant Volume", "Color by Well Spacing"],
        vertical_spacing=0.1, horizontal_spacing=0.1,
        specs=[[{'type': 'scatter3d'}, {'type': 'scatter3d'}],
               [{'type': 'scatter3d'}, {'type': 'scatter3d'}],
               [{'type': 'scatter3d'}, {'type': 'scatter3d'}]]
    )

    # 1. Color by Formation
    trace1 = go.Scatter3d(
        x=data_clean['Longitude'],
        y=data_clean['Latitude'],
        z=data_clean['Lateral Length'],
        mode='markers',
        marker=dict(
            size=data_clean['Stages'],
            color=data_clean['Formation_Code'],
            colorscale='Viridis',
            colorbar=dict(title='Formation')
        ),
        text=data_clean['Well Name'],
        hoverinfo='text'
    )

    # 2. Color by Completion Type
    trace2 = go.Scatter3d(
        x=data_clean['Longitude'],
        y=data_clean['Latitude'],
        z=data_clean['Lateral Length'],
        mode='markers',
        marker=dict(
            size=data_clean['Stages'],
            color=data_clean['Compl_Type_Code'],
            colorscale='Blues',
            colorbar=dict(title='Completion Type')
        ),
        text=data_clean['Well Name'],
        hoverinfo='text'
    )

    # 3. Color by Best 1-Month BOPD
    trace3 = go.Scatter3d(
        x=data_clean['Longitude'],
        y=data_clean['Latitude'],
        z=data_clean['Lateral Length'],
        mode='markers',
        marker=dict(
            size=data_clean['Stages'],
            color=data_clean['Best1 Mo BOPD'],
            colorscale='RdYlGn',
            colorbar=dict(title='Best 1-Month BOPD')
        ),
        text=data_clean['Well Name'],
        hoverinfo='text'
    )

    # Add all traces to the subplots
    fig.add_trace(trace1, row=1, col=1)
    fig.add_trace(trace2, row=1, col=2)
    fig.add_trace(trace3, row=2, col=1)

    # Update layout and title
    fig.update_layout(
        title="3D Well Visualizations: Different Color Groupings",
        height=800,
        width=1000,
        showlegend=False,
        title_x=0.5
    )

    st.plotly_chart(fig)

# Display the corresponding plot based on the selected option
if plot_type == "2D Visualization":
    plot_2d()
elif plot_type == "3D Visualization":
    plot_3d()
