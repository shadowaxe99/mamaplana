```python
import unittest
from src import deployment_process

class TestDeploymentProcess(unittest.TestCase):

    def setUp(self):
        self.deployment = deployment_process.DeploymentProcess()

    def test_deployOnline(self):
        result = self.deployment.deployOnline()
        self.assertEqual(result, "Online deployment successful")

    def test_deployLocal(self):
        result = self.deployment.deployLocal()
        self.assertEqual(result, "Local deployment successful")

    def test_releaseVersion(self):
        result = self.deployment.releaseVersion()
        self.assertTrue(isinstance(result, str))
        self.assertTrue(result.startswith("Version"))

    def test_deployVersion(self):
        version = self.deployment.releaseVersion()
        result = self.deployment.deployVersion(version)
        self.assertEqual(result, f"Version {version} deployed successfully")

if __name__ == '__main__':
    unittest.main()
```