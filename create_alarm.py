import streamlit as st
import time
from datetime import datetime, time as dt_time, timedelta


def create_alarm1():
    st.title("Simple Alarm Bot")
    alarm_time = st.time_input(
        "Set alarm time", step=timedelta(minutes=1))

    if st.button("Set Alarm"):
        while True:
            current_time = datetime.now().time()
            if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
                st.balloons()  # Using Streamlit's built-in notification
                st.success("Time to wake up!")
                break
            time.sleep(5)


def create_alarm2():
    st.title("Simple Alarm Bot")

    # Preset times for dropdown
    preset_times = {
        "Morning (7:00 AM)": dt_time(7, 0),
        "Noon (12:00 PM)": dt_time(12, 0),
        "Evening (6:00 PM)": dt_time(18, 0)
    }

    # Initialize session state for time input [[3](https://docs.streamlit.io/develop/concepts/architecture/session-state)]
    if 'alarm_time' not in st.session_state:
        st.session_state.alarm_time = dt_time(7, 0)

    # Dropdown for preset times
    selected_preset = st.selectbox(
        "Choose preset time", list(preset_times.keys()))

    # Time input with default value from dropdown [[1](https://docs.streamlit.io/develop/api-reference/widgets/st.time_input)]
    alarm_time = st.time_input(
        "Or set custom alarm time", value=preset_times[selected_preset],
        step=timedelta(minutes=1))  # Set time step to 1 minute)

    if st.button("Set Alarm"):
        while True:
            current_time = datetime.now().time()
            if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
                st.balloons()
                st.success("Time to wake up!")
                break
            time.sleep(5)


if __name__ == "__main__":
    create_alarm2()
