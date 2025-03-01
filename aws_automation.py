import boto3
import pandas as pd
import os

# AWS S3 Configuration
S3_BUCKET_NAME = "your-s3-bucket-name"
S3_FILE_KEY = "data/football_players_data.csv"
LOCAL_FILE_PATH = "data/football_players_data.csv"

# Initialize S3 Client
s3 = boto3.client('s3')

def download_data_from_s3():
    """Download the latest dataset from S3"""
    try:
        s3.download_file(S3_BUCKET_NAME, S3_FILE_KEY, LOCAL_FILE_PATH)
        print("Data downloaded successfully from S3!")
    except Exception as e:
        print(f"Error downloading file: {e}")

def upload_processed_data_to_s3():
    """Upload the processed dataset to S3"""
    processed_file_path = "data/processed_data.csv"
    try:
        s3.upload_file(processed_file_path, S3_BUCKET_NAME, "data/processed_data.csv")
        print("Processed data uploaded successfully to S3!")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    # Step 1: Download latest data
    download_data_from_s3()
    
    # Step 2: Process Data
    df = pd.read_csv(LOCAL_FILE_PATH)
    df.fillna(method='ffill', inplace=True)
    df.to_csv("data/processed_data.csv", index=False)
    print("Data processing completed!")
    
    # Step 3: Upload processed data
    upload_processed_data_to_s3()
