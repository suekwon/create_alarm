import streamlit as st
import time
from datetime import datetime, time as dt_time, timedelta


def create_alarm():
    # Page layout
    st.title("⏰ Smart Alarm Bot")
    st.write("---")

    col1, col2 = st.columns(2)

    with col1:
        # Preset times with icons
        preset_times = {
            "🌅 Morning (7:00 AM)": dt_time(7, 0),
            "☀️ Noon (12:00 PM)": dt_time(12, 0),
            "🌆 Evening (6:00 PM)": dt_time(18, 0)
        }

        if 'alarm_time' not in st.session_state:
            st.session_state.alarm_time = dt_time(7, 0)

        selected_preset = st.selectbox(
            "Choose preset time ⏱️",
            list(preset_times.keys())
        )

    with col2:
        # Custom time input with visual feedback
        alarm_time = st.time_input(
            "Or set custom time 🕒",
            value=preset_times[selected_preset],
            step=timedelta(minutes=1)
        )

        # Display selected time
        st.info(f"Selected alarm time: {alarm_time.strftime('%I:%M %p')}")

    # Center the alarm button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔔 Set Alarm", use_container_width=True):
            progress_text = "Monitoring time..."
            progress_bar = st.progress(0)

            while True:
                current_time = datetime.now().time()
                time_diff = (alarm_time.hour * 60 + alarm_time.minute) - \
                    (current_time.hour * 60 + current_time.minute)
                progress = 1 - (time_diff / 1440)  # 1440 minutes in a day
                progress_bar.progress(max(0, min(1, progress)))

                if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
                    st.balloons()
                    st.success("⏰ Time to wake up!")
                    break
                time.sleep(5)


if __name__ == "__main__":
    create_alarm()
