heart.route('/predict', methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    
    column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 
                    'fbs', 'restecg', 'thalach', 'exang', 
                    'oldpeak', 'slope', 'ca', 'thal']

    input_data = pd.DataFrame([input_features], columns=column_names)

    output = model.predict(input_data)

    if output == 1:
        res_val = "The Patient Have Heart Disease, please consult the Doctor"
    else:
        res_val = "The Patient is Normal"

    return render_template('index1.html', prediction_text='Result - {}'.format(res_val))
