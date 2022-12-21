from sensor.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME
import os

class TargetValueMapping:

    def __init__(self,):
        self.neg: int = 0
        self.pos: int = 1
    
    def to_dict(self):
        return self.__dict__
    
    def reverse_mapping(self):
        mapping_response = self.to_dict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))

#Write a code to train model and check the accuracy.

class SensorModel:

    def __init__(self):
        self.preprocessor = preprocessor
        self.model = model

    def predict(self,x):
        x_transform = self.preprocessor.transform(x)
        y_hat = self.model.predict(x_transform)
        return y_hat