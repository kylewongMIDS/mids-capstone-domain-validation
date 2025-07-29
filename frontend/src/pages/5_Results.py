import streamlit as st
from app_utils import pred_to_df, df_to_download_buffer
import plotly.express as px


# plan
# show results overview
# highlight high risk domains
# allow full download or download of just high risk

st.set_page_config(page_title="Upload CSV", layout="wide")
st.markdown("""
    <style>
    .gold-text {
        font-size: 48px;
        font-weight: bold;
        color: #d4af37;
    }
    </style>

    <div class="gold-text">PhishFence</div>
""", unsafe_allow_html=True)
st.subheader("Step 4: Analyze Results")
# st.markdown(f"Prediction results for {st.session_state.file_name}")


df = pred_to_df(st.session_state.prediction_json)
high_risk_df = df[df['risk']=='high']

all_results, high_risk = st.tabs(['All Results','High Risk Domains'])

with all_results:
    
    risk_counts = df['risk'].value_counts().reindex(['low', 'medium', 'high']).fillna(0).reset_index()
    risk_counts.columns = ['risk', 'count']

    color_map = {
        'low': '#2ecc71',
        'medium': '#f39c12',
        'high': '#e74c3c'
    }

    fig = px.bar(
        risk_counts,
        x='count',
        y='risk',
        orientation='h',
        color='risk',
        color_discrete_map=color_map,
        text='count',
        category_orders={"risk": ["low", "medium", "high"]},  # enforce order
        title='Domain Count by Risk Level'
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(yaxis_title="Risk Level", xaxis_title="Number of Domains", showlegend=False)

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(df)
    
    all_data = df_to_download_buffer(df)
                    
    st.download_button(
        label = 'Download All Results',
        data = all_data,
        file_name = f'Phishfence_All_Results_{st.session_state.file_name}',
        mime='text/csv'
    )

with high_risk:
    
    st.dataframe(high_risk_df)
    high_risk_data = df_to_download_buffer(high_risk_df)
                    
    st.download_button(
        label = 'Download High Risk Domains',
        data = high_risk_data,
        file_name = f'Phishfence_High_Risk_Results_{st.session_state.file_name}',
        mime='text/csv'
    )


