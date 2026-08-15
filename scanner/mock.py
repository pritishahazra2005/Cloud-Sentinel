MOCK_S3_BUCKETS = [
    {"name": "my-public-bucket", "public_access_blocked": False, "encryption": False},
    {"name": "private-logs", "public_access_blocked": True, "encryption": True},
]

MOCK_SECURITY_GROUPS = [
    {"id": "sg-001", "rules": [{"port": 22, "source": "0.0.0.0/0"}]},  # SSH open!
    {"id": "sg-002", "rules": [{"port": 443, "source": "10.0.0.0/8"}]},
]

MOCK_IAM_USERS = [
    {"name": "admin-user", "policies": ["AdministratorAccess"]},
    {"name": "dev-user", "policies": ["AmazonS3ReadOnlyAccess"]},
]