# Loan Approval Application

Deployed link:
- Heroku: https://loan-approval-app.herokuapp.com/
- Azure: https://loan-approval-app.azurewebsites.net/

This app was made as the final assignment of [DPhi's Online Machine Learning Bootcamp](https://dphi.tech/bootcamps/machine-learning-online-bootcamp/). The objective of this Machine Learning project is to build a model and web application that the bank can use to classify if a user can be granted a loan or not.

## Project Structure

- Folders:
    - `dev`: development scripts
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

The app is built using Python 3.7.9, with the following dependencies:

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
- Create an API endpoint for the prediction
- Create new page for batch prediction, using upload and download file
- Create new page for explainable results, using LIME or SHAP