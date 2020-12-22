from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired 
from wtforms.widgets import html5

class PredictionForm(FlaskForm):

    '''
    Parameter for each field:
    - id: column name that the model recognize
    - label: text that will appear on the form
    - description: tooltip of input field, on hover
    '''

    gender = SelectField(
        id='Gender',
        label='Gender',
        description=['Gender of the applicant'],
        choices=['Male', 'Female'])

    married = SelectField(
        id='Married',
        label='Married',
        description=['Marital status of the applicant'],
        choices=['No', 'Yes'])

    dependents = SelectField(
        id='Dependents',
        label='Number of Dependents',
        description=['No. of people dependent on the applicant'],
        choices=['0', '1', '2', '3+'])

    education = SelectField(
        id='Education',
        label='Education',
        description=['Education level of the applicant'],
        choices=['Not Graduate', 'Graduate'])

    self_employed = SelectField(
        id='Self_Employed',
        label='Self Employed',
        description=['If the applicant is self-employed or not'],
        choices=['No', 'Yes'])

    applicant_income = DecimalField(
        id='ApplicantIncome',
        label='Applicant Income',
        default=0,
        places=2,
        description=['USD', 'The amount of income the applicant earns'],
        validators=[DataRequired('Value must be greater than zero!')],
        widget=html5.NumberInput(min=0, max=999999, step=0.01)
    )

    coapplicant_income = DecimalField(
        id='CoapplicantIncome',
        label='Co-applicant Income',
        default=0,
        places=2,
        description=['USD', 'The amount of income the co-applicant earns'],
        validators=[DataRequired('Value must be greater than zero!')],
        widget=html5.NumberInput(min=0, max=999999, step=0.01)
    )

    loan_amount = DecimalField(
        id='LoanAmount',
        label='Loan Amount',
        default=0,
        places=2,
        description=['USD', 'The amount of loan the applicant has requested for'],
        validators=[DataRequired('Value must be greater than zero!')],
        widget=html5.NumberInput(min=0, max=999999, step=0.01)
    )

    loan_amount_term = IntegerField(
        id='Loan_Amount_Term',
        label='Loan Amount Term',
        default=0,
        description=['days', 'The no. of days over which the loan will be paid'],
        validators=[DataRequired('Value must be greater than zero!')],
        widget=html5.NumberInput(min=0, max=9999)
    )

    credit_history = SelectField(
        id='Credit_History',
        label='Credit History',
        description=['A record of a borrower\'s responsible repayment of debts'],
        choices=[(0.0, 'Not paid'), (1.0, 'All debts paid')])

    property_area = SelectField(
        id='Property_Area',
        label='Property Area',
        description=['The type of location where the applicant’s property lies'],
        choices=['Rural', 'Semiurban', 'Urban'])

    submit = SubmitField(label='Predict!')