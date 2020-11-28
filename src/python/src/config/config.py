########################################
######### Preprocessing Config #########
########################################

ENCODINGS_PATH = 'src/python/src/encodings'

DATASET_PATH = 'src/python/src/datasets'

FEATURES = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
            'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
            'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
            'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
            'PaymentMethod', 'MonthlyCharges', 'TotalCharges']

CAT_VARS = ['MultipleLines',
            'InternetService',
            'OnlineSecurity',
            'OnlineBackup',
            'DeviceProtection',
            'TechSupport',
            'StreamingTV',
            'StreamingMovies',
            'Contract',
            'PaymentMethod']

NUMERICAL_VARS = ['tenure', 'MonthlyCharges', 'TotalCharges']

TARGET = 'Churn'
