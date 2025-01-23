# sre-worktest

# Important notes

- Do not fork this repository. Clone it, and push the solution to your personal private GitHub repository. Once finished, send us your solution as a zip archive of your Git repository along with clear execution instructions.
- Your solution should assume that this is a production-grade system expected to handle thousands of requests per second with an uptime of at least 99.99% (~4.38 minutes of downtime per month).
- You do not need to deploy the Terraform code on GCP. This is a test exercise, and there is no need to spend money on provisioning infrastructure.
- Feel free to use public Terraform modules (e.g., [terraform-google-modules](https://github.com/terraform-google-modules)).
- We explicitly do not expect you to spend more than 4 hours on this task. The requirements are designed to provide enough scope to challenge candidates. If you're unable to complete all tasks within that time, focus on showcasing your proficiency across all four objectives (e.g., 2 hours on Terraform, 1 hour on Helm charts, and 1 hour on pipelines) and comment on what would do if more time was allowed.

## app.py

This is a Flask application that allows you to write, delete, and list key-value pairs in a Redis database.

Endpoints:

    GET /:
        A test endpoint to verify the Redis connection.
        Writes a sample key-value pair ("test_key": "Hello Redis!") to the Redis database, retrieves it, and returns the value as a response.

    POST /write:
        Adds a new key-value pair to the Redis database.
        You can provide the key and value as a JSON payload, e.g., {"key": "<your-key>", "value": "<your-value>"}.
        If no payload is provided, the app generates random key-value pairs and writes them to Redis.

    DELETE /delete:
        Deletes a key-value pair from the Redis database.
        Requires a query parameter key=<key> to specify the key to delete.
        Returns a success message if the key was deleted or an error if the key doesn’t exist.

    GET /list:
        Fetches all key-value pairs stored in the Redis database.
        Returns the data in JSON format.

## Objective

Your task is to deliver a complete solution for deploying this application in a production environment. Testing environments are not required. Specifically, you need to provide:
1. A pipeline to build and push the Docker image.
2. Terraform code to provision all necessary cloud resources (e.g., VPC, Kubernetes cluster) in GCP.
3. Helm chart or deployment scripts for deploying Kubernetes-related components.
4. Automation for deployment (GitOps approach preferred).
