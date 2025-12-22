name: Sync Usage Data to Google Drive

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  sync-to-drive:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      
      - name: Install dependencies
        run: |
          pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
      
      - name: Sync data to Google Drive
        env:
          GOOGLE_CREDENTIALS: ${{ secrets.GOOGLE_DRIVE_CREDENTIALS }}
          DRIVE_FOLDER_ID: ${{ secrets.DRIVE_FOLDER_ID }}
        run: |
          python sync_to_drive.py
