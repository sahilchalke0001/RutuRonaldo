import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import pickle
import os

def create_model(data):
    # Select only the 9 features for training
    selected_features = ['Age', 'Dribbling / Reflexes', 'Passing / Kicking', 'Shooting / Handling', 
                         'Total mentality', 'Shot power', 'Total power', 'Ball control', 'Finishing']

    # One-hot encode 'name' and other categorical columns if necessary
    if 'name' in data.columns:
        data = pd.get_dummies(data, columns=['name'], drop_first=True)

    # Ensure the selected features and target column exist in the data
    X = data[selected_features]  # Use only selected features
    y = data['Log Market Value']
    
    # Split the data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train the model
    forest = RandomForestRegressor()
    forest.fit(X_train, y_train)
    
    # Evaluate the model
    score = forest.score(X_train, y_train)
    print(f"Model score on training data: {score}")
    
    return forest  # Return the trained model

def get_clean_data():
    data_path = os.path.join(os.getcwd(), "data/data.csv")
    data = pd.read_csv(data_path)
    
    # Apply log transformation to 'Value' column where non-zero
    mask = data['Value'] > 0
    data.loc[mask, 'Log Market Value'] = np.log(data.loc[mask, 'Value'])
    
    # Drop rows where 'Log Market Value' is NaN (since log of 0 is undefined)
    data = data.dropna(subset=['Log Market Value'])
    
    return data

def main():
    data = get_clean_data()
    forest = create_model(data)  # Train the model with only the 9 selected features
    
    # Save the trained model to a .pkl file
    model_dir = 'forest'
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    
    with open(os.path.join(model_dir, 'forest.pkl'), 'wb') as f:
        pickle.dump(forest, f)
    
    print("Model saved successfully.")

if __name__ == '__main__':
    main()
