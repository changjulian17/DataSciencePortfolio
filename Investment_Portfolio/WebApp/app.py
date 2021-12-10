# streaming
import streamlit as st
import streamlit.components.v1 as components
import webbrowser
# dataframe
import pandas as pd
# plotting
import plotly.express as px
import plotly.graph_objs as go
# streaming
import requests
# plotter
from plotter import overview_chart, strats_table, dist_returns, ppo_charts, portfolio_weights, histo_wts, returns_table

# set layout
st.set_page_config(layout = "wide")
# print header
st.header("AI Portfolio Allocator")

# set left sidebar
page = st.sidebar.selectbox('Select page',['Overview',
                                                'Background',
                                                'AI Models',
                                                'Table of Returns',
                                                'EDA',
                                                'PPO Model (External Link)',
                                                'Parameters (External Link)',
                                                'State, Action, Reward and Policy Gradient (External Link)',
                                                'Tensorboard (External Link)']) 

# set pages
if page == 'Overview':
        st.write('Welcome to the AI portfolio allocator!')
        st.write('The AI model used is a trained by Reinforcement Learning using Proximal Policy Optimisation (PPO). Read more in the Description page')
        st.header("AI Portfolio Outperformence in backtests")
        ## plot all 4 strategies
        overview_fig = overview_chart()
        st.plotly_chart(overview_fig,
                        use_container_width = True)

        st.table(strats_table())

        dist_ret_fig = dist_returns()
        st.plotly_chart(dist_ret_fig,
                        use_container_width = True)

elif page == 'AI Models':
        st.header("Compare AI models")
        st.write('Hyperparatmeter tuning is required. We see the more stable model PPO 5 perform better with more consistent portfolio allocations over time')
        # compare two PPO models
        ppo_chart = ppo_charts()
        st.plotly_chart(ppo_chart,
                        use_container_width = True)

        fig_ppo4, fig_ppo5, fig_drg = portfolio_weights()
        fig_hist_ppo4, fig_hist_ppo5 = histo_wts()

        # ppo 4 and 5 side by side
        l_fig, r_fig = st.columns((1, 1.02))
        with l_fig:
            st.plotly_chart(fig_ppo4,
                        use_container_width = True)
        with r_fig:
            st.plotly_chart(fig_ppo5,
                        use_container_width = True)

        st.write('PPO 5 allocates consistently for the most part, notably changing during periods of high volatility i.e. COVID-19 scare in March 2020')

        # ppo 4 and 5 side by side
        l_fig, r_fig = st.columns((1, 1.02))
        with l_fig:
            st.plotly_chart(fig_hist_ppo4,
                        use_container_width = True)
        with r_fig:
            st.plotly_chart(fig_hist_ppo5,
                        use_container_width = True)

        st.write('Dragon portfolio constant weighted is below for reference.')

        # dragon allocation
        st.plotly_chart(fig_drg,
                        use_container_width = True)

elif page == 'Table of Returns':
        st.header("Table of Returns")
        st.write('Values in percentage')
        df = returns_table()
        st.dataframe(df)

elif page == 'EDA':
        st.header("Exploratory Data Analysis")
        # display EDA from html
        HtmlFile = open("eda.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code, height = 9_900)

elif page == 'PPO Model (External Link)':
        st.header("Medium Article on PPO model (External Link)")
        # link to article opens automatically
        link = 'https://medium.com/@changjulian17/portfolio-allocation-reinforcement-learning-ppo-model-part-ii-56ecf76a941b'
        webbrowser.open(link)

elif page == 'Parameters (External Link)':
        st.header("Medium Article on model parameters (External Link)")
        # link to article open automatically
        link = 'https://medium.com/@changjulian17/reinforcement-learning-ppo-in-an-investment-environment-c18b1bac29c4'
        webbrowser.open(link)

elif page == 'State, Action, Reward and Policy Gradient (External Link)':
        st.header("Medium Article on model State, Action, Reward and Policy Gradient (External Link)")
        # link to article open automatically
        link = 'https://medium.com/@changjulian17/portfolio-allocation-reinforcement-learning-ppo-model-part-i-5cabd5aaaa93'
        webbrowser.open(link)

elif page == 'Tensorboard (External Link)':
        st.header("Tensorboard (External Link)")
        # link to tensorboard open automatically
        link = 'https://tensorboard.dev/experiment/z20zIbr6TmSQ3vqUBTpkAw/#scalars'
        webbrowser.open(link)

else:
        # display readme from github repo
        target_url = 'https://raw.githubusercontent.com/changjulian17/DataSciencePortfolio/main/Investment_Portfolio/README.md'
        response = requests.get(target_url)
        st.markdown(response.text, unsafe_allow_html=True)
