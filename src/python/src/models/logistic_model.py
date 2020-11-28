from models.abstract_model import BaseModel
from sklearn.linear_model import LogisticRegression
import pickle


class LogisticModel(BaseModel):
    def __init__(self, **kwargs):
        self.model = LogisticRegression(**kwargs)

    def model_arch(self):
        pass

    def fit(self, x, y):
        self.model.fit(x, y)

    def predict(self, x):
        preds = self.model.predict(x)
        return preds

    def save_model(self, path):
        pickle.dump(self.model, open(f'{path}model', 'wb'))



