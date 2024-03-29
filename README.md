# Loan Approval Application

Deployed link: https://loan-approval-app-facb8c5d72fa.herokuapp.com/

This app was made as the final assignment of [DPhi's Online Machine Learning Bootcamp](https://dphi.tech/bootcamps/machine-learning-online-bootcamp/). The objective of this Machine Learning project is to build a model and web application that the bank can use to classify if a user can be granted a loan or not.

## Endpoints

1. `/home`: Home page
2. `/prediction`: Prediction form
3. `/result`: API
    - Return: `[pred_prob, pred_class]`
    - See `guide/API_Example.ipynb` for minimal example

## Project Structure

- Folders:
    - `dev`: development scripts
    - `guide`: notebook for usage examples
    - `models`: pickled pre-trained model (scikit-learn pipeline)
    - `static`: css files
    - `template`: html files

- Application Files:
    - `app.py`: main application
    - `forms.py`: wtforms class

- Deployment Files:
    - `requirements.txt`: package dependencies
    - `runtime.txt`: Python version
    - `Procfile`: commands for app's dynos on Heroku

## Dependencies

The app is built using Python 3.12.1, with the following dependencies:

- `Flask`: web framework
- `Flask-WTF`: forms validation
- `pandas`: data analysis
- `scikit-learn`: model pipeline
- `gunicorn`: HTTP server

List of dependencies and its version can be found on `requirements.txt`.

## References

- [DPhi Datathon 54](https://dphi.tech/practice/challenge/54)
- [Bootstrap v5.0](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Corey Schafer's Code Snippets](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog)

## Future Improvement Ideas

- Improve classifier performance
- Create new page for batch prediction, using upload and download file
- Create new page for explainable results, using LIME or SHAP