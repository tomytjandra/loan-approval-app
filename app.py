from flask import Flask, render_template, url_for, flash, request, Markup, jsonify
from forms import PredictionForm
from pandas import DataFrame
import joblib

app = Flask(__name__)

# Secret key protect against modifying cookies and cross-site request forgery attacks
app.config['SECRET_KEY'] = '686ae18682ce71b6e620dfea8995d735'

# Load trained model
model = joblib.load("models/loan_model_logreg.pkl")

# Home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# Prediction page
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    form = PredictionForm()
    field_list = ["SelectField", "DecimalField", "IntegerField"]

    if form.validate_on_submit():
        # convert input data as dataframe and run through pipeline
        new_data = dict([(field.id, field.data)
                            for field in form
                            if field.type in field_list])
        new_df = DataFrame([new_data])
        new_df['Credit_History'] = new_df['Credit_History'].astype('float')

        # predict
        pred_prob = model.predict_proba(new_df)[0, 1]
        if pred_prob > 0.5:
            conclusion = 'APPROVED :)'
            category = 'success'
        else:
            conclusion = 'REJECTED :('
            category = 'danger'

        message = Markup(
            f'''
            <b>Probability of loan approval</b>: {pred_prob*100:.2f}% <br>
            <b>Conclusion</b>: Loan is {conclusion}
            '''
        )

        flash(message, category=category)      
        
        # return redirect(url_for('home'))
    return render_template('prediction.html', title='Predict', form=form, field_list=field_list)

# API
@app.route('/result', methods=['POST'])
def result():

    new_data = request.get_json(force=True)
    new_df = DataFrame([new_data])
    new_df['Credit_History'] = new_df['Credit_History'].astype('float')

    # predict
    pred_prob = model.predict_proba(new_df)[0, 1]
    pred_class = 'approved' if pred_prob > 0.5 else 'rejected'

    return jsonify((pred_prob, pred_class))

if __name__ == '__main__':
    app.run(debug=True, port=5000)