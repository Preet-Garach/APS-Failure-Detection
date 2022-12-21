from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys 
import logging
# from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline

# def test_exception():
#     try:
#         logging.info("We are diving 1 by 0")
#         x=1/0
#     except Exception as e:
#         raise SensorException(e,sys)

if __name__ == "__main__":
    # mongodb_cleint = MongoDBClient()
    # print(mongodb_cleint.database.list_collection_names())
    # training_pipeline_config = TrainingPipelineConfig()
    # data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    # print(data_ingestion_config.__dict__)
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        logging.exception(e)