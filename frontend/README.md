# Streamlit Frontend

1. Start docker engine by opening Docker Desktop
2. Build docker image
    ```
    docker build -t streamlit-app .
    ```
3. Run docker container and specify the aws permissions

    Windows:
    ```
    docker run -e AWS_ACCESS_KEY_ID=<aws_access_key_id_goes_here> `
            -e AWS_SECRET_ACCESS_KEY=<aws_secret_access_key_id_goes_here> `
            -e AWS_DEFAULT_REGION=<aws_region_goes_here> `
            -p 8501:8501 `
            streamlit-app
    ```

    Mac/Linux:
    ```
    docker run -e AWS_ACCESS_KEY_ID=<aws_access_key_id_goes_here> \
            -e AWS_SECRET_ACCESS_KEY=<aws_secret_access_key_id_goes_here> \
            -e AWS_DEFAULT_REGION=<aws_region_goes_here> \
            -p 8501:8501 \
            streamlit-app
    ```

4. Access the locally hosted website from the browser
    ```
    http://localhost:8501
    ```


general notes:
- batch prediction workflow:
    - user submits csv to streamlit app
        - done
    - service account writes csv to s3 input folder with unique identifier name
        - done
    - s3 writing triggers lambda job
        - need to start
    - lambda job performs preprocessing to transform domains into model inputs
        - in progress: preprocessing added in mode.preprocessing
        need to formalize lambda job
    - batch transformation job predicts on model inputs in bulk
        - need to start
    - lambda job writes model inputs as csv to s3 output folder with same unique identifier name
        - need to start
    - streamlit app polls for unique identifier name in output folder
        - need to start
    - when available, streamlit app enables user to download results via presigned url
        - need to start