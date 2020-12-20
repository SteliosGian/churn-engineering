########################################
######### Preprocessing Config #########
########################################

ENCODINGS_PATH = 'src/encodings'

DATASET_PATH = 'datasets/telco_churn.csv'

FEATURES = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
            'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
            'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
            'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
            'PaymentMethod', 'MonthlyCharges', 'TotalCharges']

CAT_VARS = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
            'PhoneService', 'MultipleLines', 'InternetService',
            'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
            'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
            'PaymentMethod']

NUMERICAL_VARS = ['tenure', 'MonthlyCharges', 'TotalCharges']

TARGET = 'Churn'

########################################
############# Train Config #############
########################################

TRACKING_URI = "http://0.0.0.0:5000/"

PARAMS_LOGISTIC = {'max_iter':  1000,
                   'penalty':  'l2',
                   'C':         1.0,
                   'solver':   'lbfgs'}

########################################
############# Predict Config ###########
########################################
