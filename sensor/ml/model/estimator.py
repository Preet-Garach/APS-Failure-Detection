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

    def __init__(self,preprocessor, model):
        self.preprocessor = preprocessor
        self.model = model

    def predict(self,x):
        x_transform = self.preprocessor.transform(x)
        y_hat = self.model.predict(x_transform)
        return y_hat

class ModelResolver:

    def __init__(self,model_dir=SAVED_MODEL_DIR):
        self.model_dir = model_dir

    def get_best_model_path(self,)-> str:
        timestamps = list(map(int, os.listdir(self.model_dir)))
        latest_timestamp = max(timestamps)
        latest_model_path = os.path.join(self.model_dir, f"{latest_timestamp}", MODEL_FILE_NAME)
        return latest_model_path
    
    def is_model_exists(self,)-> str:
        if not os.path.exists(self.model_dir):
            return False
        
        timestamps = os.listdir(self.model_dir)
        if len(timestamps)==0:
            return False

        latest_model_path = self.get_best_model_path()
         
        if not os.path.exists(latest_model_path):
            return False
        
        return True
            


