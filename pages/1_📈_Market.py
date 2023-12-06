import os
import sys
import pandas as pd
sys.path.append(os.getcwd())  # NOQA

import streamlit as st
import json
import sqlite3

st.set_page_config(
    page_title="Market 📈",
    page_icon="📈",
)


class Market():
    def __init__(self) -> None:
        # Load system config
        with open('configs/system.json', 'r') as f:
            self.system_cfg = json.load(f)

        # Connect to the database
        self.conn = sqlite3.connect(self.system_cfg['db_name'])

        # Init UI
        self.init_ui()

    def init_ui(self):
        st.title("Market 📈")

        st.write('---')

        self.refresh_button = st.sidebar.button('Refresh', use_container_width=True)

        if self.refresh_button:
            self.refresh_ui()

    """-----------------------------Query SQL commands-----------------------------"""

    def _query_revenue(self):
        result = self.conn.execute("""
            WITH CTE1 AS (
            SELECT 
                SIM_PERIOD AS week,
                SUM(NET_VALUE) AS company_revenue
            FROM Market
            WHERE SALES_ORGANIZATION = 'Company'
            GROUP BY SIM_PERIOD
        ), CTE2 AS (
            SELECT 
                SIM_PERIOD AS week,
                SUM(NET_VALUE) AS market_revenue
            FROM Market
            WHERE SALES_ORGANIZATION = 'Market'
            GROUP BY SIM_PERIOD
        )
        SELECT 
            CTE1.week,
            CTE1.company_revenue,
            CTE2.market_revenue,
            CAST(ROUND(CTE1.company_revenue * 1.0 / CTE2.market_revenue * 100, 2) AS TEXT) || "%" AS Percentage
        FROM CTE1
        JOIN CTE2 ON CTE1.week = CTE2.week
        ORDER BY CTE1.week ASC;
    """)

        return result.fetchall()

    """-----------------------------UI Elements-----------------------------"""

    def market_revenue(self):
        data = self._query_revenue()
        df = pd.DataFrame(data, columns=['Week', 'Company Revenue', 'Market Revenue', 'Percentage'])
        df.set_index('Week', inplace=True)
        df.index = df.index.astype(int)

        st.markdown("### Market Revenue")
        st.dataframe(df, use_container_width=True)
        st.write('---')
        st.line_chart(
            data=df[['Company Revenue', 'Market Revenue']],
            color=['#FF0000', '#00FF00'],
            width=1,
            use_container_width=True
        )

    def market_unit_sold(self):
        pass

    def market_average_price(self):
        pass

    """-----------------------------Refresh UI-----------------------------"""

    def refresh_ui(self):
        self.market_revenue()


if __name__ == "__main__":
    market = Market()
