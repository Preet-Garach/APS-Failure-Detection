from datetime import datetime
import os
from sensor.constant.training_pipeline import PIPELINE_NAME, ARTIFACT_DIR, DATA_INGESTION_COLLECTION_NAME,DATA_INGESTION_DIR_NAME, FILE_NAME
from sensor.constant.training_pipeline import DATA_INGESTION_FEATURE_STORE_DIR, DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO,DATA_INGESTION_INGESTED_DIR
from sensor.constant.training_pipeline import TRAIN_FILE_NAME, TEST_FILE_NAME
# from sensor.entity.artifact_entity import DataIngestionArtifact

class TrainingPipelineConfig:

    def __init__(self, timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name: str = PIPELINE_NAME
        self.artifact_dir: str = os.path.join(ARTIFACT_DIR, timestamp)
        timestamp: str = timestamp

class DataIngestionConfig:

    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME
        )

        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME
        )

        self.training_file_path:str = os.path.join(
            self.data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME
        )

        self.testing_file_path:str = os.path.join(
            self.data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME
        )

        self.train_test_split_ratio:float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name:str = DATA_INGESTION_COLLECTION_NAME