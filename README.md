# Jira Github Integration

## To run the project locally (without docker)

1. Clone the repository and create a .env file (Refer `.env-sample` file)

2. Set the environment variables in the .env file

    ```bash
    export $(grep -v '^#' .env | xargs)
    ```

3. Create a virtual environment, activate it and install the dependencies

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    ```

4. Run the project and access it at `http://localhost:5000`

    ```bash
    python app.py
    ```

## To run the project with docker

1. Create a .env file (Refer `.env-sample` file) 

2. Run the container

    ```bash
    docker run -dit --env-file .env -p 5000:5000 prajwal3498/jira-github-integration:latest
    ```

## Contributing to the project

1. Fork the repository to your GitHub account.

2. Clone the forked repository to your local machine.

    ```bash
    git clone https://github.com/your-username/jira_github_automation.git
    ```

3. Create a new branch for your feature or bug fix.

    ```bash
    git checkout -b feature-or-bugfix-name
    ```

4. Make your changes and commit them with a descriptive commit message.

    ```bash
    git add .
    git commit -m "Description of the feature or bug fix"
    ```

5. Push your changes to your forked repository.

    ```bash
    git push origin feature-or-bugfix-name
    ```

6. Open a pull request from your forked repository to the main repository.

7. Wait for the pull request to be reviewed and merged.