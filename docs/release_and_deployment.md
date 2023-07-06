# Release and Deployment Process

The AI Scheduling Assistant follows a robust release and deployment process to ensure smooth and efficient deployments. This process includes versioning, testing, and CI/CD pipelines.

## Versioning

We use semantic versioning for the AI Scheduling Assistant. Each release is tagged with a unique version number that follows the format `MAJOR.MINOR.PATCH`. The `releaseVersion()` function in `src/deployment_process.py` handles the versioning process.

## Testing

Before each release, we run a comprehensive suite of tests to ensure the functionality and stability of the AI Scheduling Assistant. The tests are located in the `src/tests/` directory. The `testFunctionality()` function in each test file is responsible for running the tests.

## CI/CD Pipelines

We use Continuous Integration (CI) and Continuous Deployment (CD) pipelines to automate the testing and deployment process. The `deployVersion()` function in `src/deployment_process.py` is responsible for deploying new versions.

## Deployment

There are two deployment options for the AI Scheduling Assistant:

1. **Online Deployment**: The AI Scheduling Assistant is hosted on a dedicated website, enabling user access through web browsers. The `deployOnline()` function in `src/web_interface.py` handles the online deployment.

2. **Downloadable Version**: We provide a downloadable version for local installation, ensuring compatibility with major operating systems. The `deployLocal()` function in `src/local_version.py` handles the local deployment.

For both deployment options, we ensure that the latest version of the AI Scheduling Assistant is always available to users.