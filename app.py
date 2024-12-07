from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder

app = Flask(__name__)

# Load the model
model_filename = 'BRAIN_STROKE\Anand1.pkl'
with open(model_filename, 'rb') as f:
    model = pickle.load(f)

# Define feature names (13 features, excluding one-hot encoded features)
feature_names = ['age', 'avg_glucose_level', 'bmi', 'gender_Male', 'hypertension', 'heart_disease', 'ever_married_Yes', 'Residence_type_Urban',]

# Create one-hot encoders for 'work_type' and 'smoking_status'
work_type_encoder = OneHotEncoder(sparse_output=False)
work_type_encoder.fit([['work_type_Never_worked'], ['work_type_Private'], ['work_type_Self-employed'], ['work_type_children']])

smoking_status_encoder = OneHotEncoder(sparse_output=False)
smoking_status_encoder.fit([['smoking_status_formerly_smoked'], ['smoking_status_never_smoked'], ['smoking_status_smokes']])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')

@app.route('/predictAction', methods=['GET','POST'])
def predictAction():
    if request.method == 'POST':
        print("p1")
        form_data = request.form.to_dict()
        print("p2")

        # Create a list to store the feature values
        feature_values = []
        print("p3")

        # Extract feature values from form data
        age = float(form_data.get('age', 0))
        print(age)
        avg_glucose_level = float(form_data.get('avg_glucose_level', 0))
        print(avg_glucose_level)
        bmi = float(form_data.get('bmi', 0))
        print(avg_glucose_level)
        # Cholestrol = float(form_data.get('Cholestrol', 0))
        gender_Male = int(form_data.get('gender_Male', 0))
        print(gender_Male)
        ever_married_Yes = int(form_data.get('ever_married_Yes', 0))
        print(ever_married_Yes)
        Residence_type_Urban = int(form_data.get('Residence_type_Urban', 0))
        print(Residence_type_Urban)
        hypertension = int(form_data.get('hypertension_1', 0))
        print(hypertension)
        heart_disease = int(form_data.get('heart_disease_1', 0))
        print(heart_disease)
         # Alcohol_Yes = int(form_data.get('Alcohol_Yes', 0))

        # Get the values of 'work_type' and 'smoking_status' as strings
        work_type_value = form_data.get('work_type', '')
        print(work_type_value)
        smoking_status_value = form_data.get('smoking_status', '')
        print(smoking_status_value)
        
        work_type_Retired=0	
        work_type_Private=0
        work_type_Self_employed=0
        work_type_children=0

        smoking_status_formerly_smoked=0
        smoking_status_never_smoked=0
        smoking_status_smokes=0

        if work_type_value=='I have a private job':
            	
            work_type_Private=1	
            
        elif work_type_value=="I'm not working":
            work_type_Retired=1	
            
        elif work_type_value=="I'm self-employed":
            
            work_type_Self_employed=1
           
        elif work_type_value=="I'm a child":
           
            work_type_children=1




        if smoking_status_value == 'I used to smoke':
            smoking_status_formerly_smoked=1
            
        elif smoking_status_value == 'Yes, I smoke':
           
            smoking_status_smokes=1
        elif smoking_status_value == 'No, I never smoked':
            
            smoking_status_never_smoked=1
           


        input_features = [age	,avg_glucose_level,	bmi,gender_Male,hypertension,	heart_disease,ever_married_Yes,	work_type_Retired,	work_type_Private,	work_type_Self_employed, work_type_children,Residence_type_Urban,	smoking_status_formerly_smoked,smoking_status_never_smoked	,smoking_status_smokes]

        features_value = [np.array(input_features)]
        features_name = ['age'	,'avg_glucose_level','bmi','gender_Male'	,'hypertension',	'heart_disease','ever_married_Yes',	'work_type_Retired',	'work_type_Private',	'work_type_Self-employed',	'work_type_children'	,'Residence_type_Urban',	'smoking_status_formerly_smoked','smoking_status_never_smoked'	,'smoking_status_smokes']

        df = pd.DataFrame(features_value, columns=features_name)
        
        
        # Make prediction
        prediction = model.predict(df)
        

        # Process prediction result
        result_message = "you will not get stroke 😀" if prediction[0] == 0 else "you will get stroke 😔"
        name = form_data.get('name', 'Guest')
        result_message = f"{name}, {result_message}"

        return render_template('predict.html', a=result_message)

# @app.route('/predictAction', methods=['POST'])
# def predictAction():
#     try:
#         # Extract form data
#         form_data = request.form.to_dict()

#         # Extract feature values
#         age = float(form_data.get('age', 0))
#         avg_glucose_level = float(form_data.get('avg_glucose_level', 0))
#         bmi = float(form_data.get('bmi', 0))
#         gender_Male = int(form_data.get('gender_Male', 0))
#         hypertension_1 = int(form_data.get('hypertension_1', 0))  # Updated
#         heart_disease_1 = int(form_data.get('heart_disease_1', 0))  # Updated
#         ever_married_Yes = int(form_data.get('ever_married_Yes', 0))
#         Residence_type_Urban = int(form_data.get('Residence_type_Urban', 0))

#         # Work type
#         work_type = form_data.get('work_type', '').lower()
#         work_type_Private = 1 if work_type == 'private' else 0
#         work_type_Self_employed = 1 if work_type == 'self-employed' else 0
#         work_type_Retired = 1 if work_type == 'retired' else 0
#         work_type_children = 1 if work_type == 'children' else 0

#         # Smoking status
#         smoking_status = form_data.get('smoking_status', '').lower()
#         smoking_status_formerly_smoked = 1 if smoking_status == 'formerly smoked' else 0
#         smoking_status_never_smoked = 1 if smoking_status == 'never smoked' else 0
#         smoking_status_smokes = 1 if smoking_status == 'smokes' else 0

#         # Prepare input features
#         input_features = [
#             age, avg_glucose_level, bmi, gender_Male, hypertension_1, heart_disease_1,
#             ever_married_Yes, work_type_Private, work_type_Self_employed, work_type_Retired,
#             work_type_children, Residence_type_Urban, smoking_status_formerly_smoked,
#             smoking_status_never_smoked, smoking_status_smokes
#         ]

#         # Match with feature names used during training
#         features_name = [
#             'age', 'avg_glucose_level', 'bmi', 'gender_Male', 'hypertension_1',
#             'heart_disease_1', 'ever_married_Yes', 'work_type_Private',
#             'work_type_Self-employed', 'work_type_Retired', 'work_type_children',
#             'Residence_type_Urban', 'smoking_status_formerly smoked',
#             'smoking_status_never smoked', 'smoking_status_smokes'
#         ]

#         # Create DataFrame for prediction
#         input_df = pd.DataFrame([input_features], columns=features_name)

#         # Make prediction
#         prediction = model.predict(input_df)[0]

#         # Process result
#         result_message = (
#             "you will not get a stroke 😀" if prediction == 0 else "you will get a stroke 😔"
#         )
#         name = form_data.get('name', 'Guest')
#         result_message = f"{name}, {result_message}"

#         return render_template('predict.html', a=result_message)

#     except ValueError as e:
#         return f"Error in input values: {e}"
#     except Exception as e:
#         return f"An unexpected error occurred: {e}"


@app.route('/counsel')
def counsel():
    return render_template('counsel.html')

if __name__ == "__main__":
    app.run(debug=True)