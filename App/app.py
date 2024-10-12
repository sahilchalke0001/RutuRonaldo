import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go

def load_model():
    with open('forest/forest.pkl', 'rb') as f:
        model = pickle.load(f)
    return model


def preprocess_input(age, dribbling_reflexes, passing_kicking, shooting_handling, total_mentality, 
                     shot_power, total_power, ball_control, finishing):
    
    input_features = np.array([[age, dribbling_reflexes, passing_kicking, shooting_handling, 
                                total_mentality, shot_power, total_power, ball_control, finishing]])
    return input_features

def get_radar_chart(input_data):
    categories = ['Age', 'Dribbling / Reflexes', 'Passing / Kicking', 'Shooting / Handling', 
                  'Total Mentality', 'Shot Power', 'Total Power', 'Ball Control', 'Finishing']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[input_data['age'], input_data['dribbling_reflexes'], input_data['passing_kicking'],
          input_data['shooting_handling'], input_data['total_mentality'], input_data['shot_power'],
          input_data['total_power'], input_data['ball_control'], input_data['finishing']],
        theta=categories,
        fill='toself',
        name='Player Attributes'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]  
            )),
        showlegend=True
    )
    
    return fig

def main():
    st.set_page_config(
        page_title="Football Transfer Market",
        page_icon="⚽",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    
    model = load_model()

    with st.container():
<<<<<<< HEAD
        st.title("⚽⚽⚽Football⚽Transfer⚽⚽⚽")
        st.subheader("This app predicts the transfer values of football players")
=======
        st.title("⚽⚽⚽Rutu⚽Ronaldo⚽⚽⚽")
        st.subheader("Ronaldo is far better than Messi because he has scored more goals and has more UCL trophies.")
>>>>>>> b0bae99 (Your commit message)
        st.subheader("Predict a player's market value using advanced ML techniques.")

    with st.container():
        buff, col, buff2 = st.columns([1, 3, 1])
        
        
        with col.form("player_form"):
            
            player_name = st.text_input("Enter the player's name:")
            age = st.number_input("Enter the Age(min value=16, max value=45):", min_value=16, max_value=45, step=1)
            dribbling_reflexes = st.number_input("Enter the Dribbling / Reflexes(max value=100):", min_value=0, max_value=100, step=1)
            passing_kicking = st.number_input("Enter the Passing / Kicking(max value=100):", min_value=0, max_value=100, step=1)
            shooting_handling = st.number_input("Enter the Shooting / Handling(max value=100):", min_value=0, max_value=100, step=1)
            total_mentality = st.number_input("Enter the Total mentality (max value=500):", min_value=0, max_value=500, step=1)
            shot_power = st.number_input("Enter the Shot power(max value=100):", min_value=0, max_value=100, step=1)
            total_power = st.number_input("Enter the Total power (max value=500):", min_value=0, max_value=500, step=1)
            ball_control = st.number_input("Enter the Ball control (max value=100):", min_value=0, max_value=100, step=1)
            finishing = st.number_input("Enter the Finishing(max value=100):", min_value=0, max_value=100, step=1)

            # Submit button for the form
            submit_button = st.form_submit_button("Predict Market Value")

            if submit_button:
                # Check if any input is empty
                if player_name == "":
                    st.warning("Your input is empty")
                else:
                    # Preprocess the input data to match the model
                    features = preprocess_input(age, dribbling_reflexes, passing_kicking, shooting_handling, 
                                                total_mentality, shot_power, total_power, ball_control, finishing)

                    # Predict the log market value and convert it to millions
                    try:
                        log_market_value = model.predict(features)[0]
                        predicted_market_value = np.exp(log_market_value) / 1_000_000

                        # Display the predicted value
                        st.success(f"Predicted Market Value for {player_name}: ${predicted_market_value:.2f} million")
                    except ValueError as e:
                        st.error(f"Prediction error: {e}")
        
        # Prepare input data for radar chart
        input_data = {
            'age': age,
            'dribbling_reflexes': dribbling_reflexes,
            'passing_kicking': passing_kicking,
            'shooting_handling': shooting_handling,
            'total_mentality': total_mentality,
            'shot_power': shot_power,
            'total_power': total_power,
            'ball_control': ball_control,
            'finishing': finishing
        }

    # Display the radar chart
    radar_chart = get_radar_chart(input_data)
    st.plotly_chart(radar_chart)

    # Load custom CSS
    with open("Assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Set background image
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("https://i.ytimg.com/vi/bR0wUBxlGt0/hq720.jpg?sqp=-oaymwE7CK4FEIIDSFryq4qpAy0IARUAAAAAGAElAADIQj0AgKJD8AEB-AH-CYAC0AWKAgwIABABGH8gIigTMA8=&rs=AOn4CLBji98FmjYxvHxKxITfKpsTy5q2Nw");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
