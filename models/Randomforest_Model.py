from models.BaseModel import BaseModel
from sklearn.ensemble import RandomForestClassifier

class RandomForest_Model(BaseModel):
    
    def train(self, train_X, train_Y, validate_X=None, validate_Y=None, n_estimators=100, max_depth=None, random_state=42):
        train_X = train_X.dropna()
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=random_state
            

        )
        
        if validate_X is None or validate_Y is None:
            model.fit(train_X, train_Y)
        else:
            model.fit(train_X, train_Y)
        
        self.model = model
        return model

    def predict(self, test_X):
        y_pred = self.model.predict(test_X)
        return y_pred

    def predict_score(self, test_X):
        y_score = self.model.predict_proba(test_X)[:, 1]
        return y_score
