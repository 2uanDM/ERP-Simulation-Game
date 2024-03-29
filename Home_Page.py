import json
import streamlit as st

from utils.common import product_info

st.set_page_config(
    page_title="ERP SIMULATION",
    page_icon=":shark:",
)


class HomePage():
    def __init__(self):
        st.header("ERP SIMULATION")

        # Init the UI
        self.init_ui()

        # Input the config of the simulation
        self.role = st.sidebar.radio("Your Role", options=['Admin', 'Client'], index=1)

        if self.role == 'Admin':
            self.input_config()

    def init_ui(self):
        st.write('---')

        # Table of Product
        st.markdown("### Product")

        # Show the table of product without the vertical index
        st.table(product_info().to_pandas().set_index('Code'))

    def save_config(self):
        new_config = {
            "round": self.sim_round,
            "day_per_round": self.day_per_round,
            "data_source_link": self.data_source_link,
            'username': self.username,
            'password': self.password,
            'auto_refresh': self.auto_refresh
        }

        print(f"==>> new_config: {new_config}")

        with open('configs/games.json', 'w') as f:
            json.dump(new_config, f, indent=4, ensure_ascii=True)

        st.toast("Saved successfully!", icon='✅')

    def input_config(self):
        st.sidebar.header("Simulation Config")

        # Load the value from the config file
        with open('configs/games.json', 'r') as f:
            config = json.load(f)

        self.sim_round = st.sidebar.number_input(
            "Round", min_value=1, max_value=100, value=config["round"], step=1, format="%d"
        )

        self.day_per_round = st.sidebar.number_input(
            "Day per round", min_value=1, max_value=100, value=config["day_per_round"], step=1, format="%d"
        )

        self.data_source_link = st.sidebar.text_input("Data source link", value=config["data_source_link"])

        self.username = st.sidebar.text_input("Username", value=config["username"])

        self.password = st.sidebar.text_input("Password", value=config["password"], type="password")

        self.auto_refresh = st.sidebar.number_input(
            "Refresh data after (s)", value=config["auto_refresh"], step=1, format="%d")

        print(f"==>> self.sim_round: {self.sim_round}")
        print(f"==>> self.day_per_round: {self.day_per_round}")
        print(f"==>> self.data_source_link: {self.data_source_link}")

        # Show the save button
        if st.sidebar.button("Save Config"):
            self.save_config()


if __name__ == '__main__':
    HomePage()
