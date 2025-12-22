import os
import json
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Load credentials from GitHub secrets
CREDENTIALS_JSON = os.environ.get('GOOGLE_CREDENTIALS')
DRIVE_FOLDER_ID = os.environ.get('DRIVE_FOLDER_ID')

def upload_to_drive():
    """Upload usage data and logs to Google Drive"""
    
    # Parse credentials
    creds_dict = json.loads(CREDENTIALS_JSON)
    credentials = service_account.Credentials.from_service_account_info(
        creds_dict,
        scopes=['https://www.googleapis.com/auth/drive.file']
    )
    
    # Build Drive API service
    service = build('drive', 'v3', credentials=credentials)
    
    # Create log entry
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_data = {
        'timestamp': timestamp,
        'sync_type': 'automated',
        'status': 'active'
    }
    
    # Create log file
    log_filename = f'dynamo_sync_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    with open(log_filename, 'w') as f:
        json.dump(log_data, f, indent=2)
    
    # Upload to Drive
    file_metadata = {
        'name': log_filename,
        'parents': [DRIVE_FOLDER_ID]
    }
    
    media = MediaFileUpload(log_filename, mimetype='application/json')
    
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    
    print(f'Sync completed. File ID: {file.get("id")}')
    
    # Clean up local file
    os.remove(log_filename)

if __name__ == '__main__':
    upload_to_drive()
