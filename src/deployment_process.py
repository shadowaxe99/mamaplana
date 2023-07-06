```python
import os
from datetime import datetime

class DeploymentProcess:
    def __init__(self):
        self.version = "1.0.0"
        self.release_date = datetime.now()

    def releaseVersion(self):
        print(f"Releasing version {self.version} on {self.release_date}")
        self.version = self.incrementVersion(self.version)
        self.release_date = datetime.now()

    def deployVersion(self, deployment_type):
        if deployment_type == "online":
            self.deployOnline()
        elif deployment_type == "local":
            self.deployLocal()
        else:
            print("Invalid deployment type. Choose 'online' or 'local'.")

    def deployOnline(self):
        print("Deploying online version...")
        # Code for online deployment goes here

    def deployLocal(self):
        print("Deploying local version...")
        # Code for local deployment goes here

    def incrementVersion(self, version):
        major, minor, patch = map(int, version.split('.'))
        patch += 1
        if patch > 9:
            patch = 0
            minor += 1
        if minor > 9:
            minor = 0
            major += 1
        return f"{major}.{minor}.{patch}"

if __name__ == "__main__":
    dp = DeploymentProcess()
    dp.releaseVersion()
    dp.deployVersion("online")
```