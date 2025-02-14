# Jira Github Integration

## To run the project locally (without docker)

1. Clone the repository and create a .env file (Refer `.env-sample` file)

2. Set the environment variables in the .env file

```bash
export $(grep -v '^#' .env | xargs)
```

## To run the project with docker

1. Create a .env file (Refer `.env-sample` file)

```bash
docker run -dit --env-file .env -p 5000:5000 prajwal3498/jira-github-integration:latest
```