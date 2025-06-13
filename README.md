# Running the App

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