import boto3


def scan_security_groups():

    findings = []

    ec2 = boto3.client("ec2")

    try:

        response = ec2.describe_security_groups()

        for group in response.get(
            "SecurityGroups",
            []
        ):

            group_id = group["GroupId"]
            group_name = group.get(
                "GroupName",
                "Unknown"
            )

            for permission in group.get(
                "IpPermissions",
                []
            ):

                from_port = permission.get(
                    "FromPort"
                )

                to_port = permission.get(
                    "ToPort"
                )

                protocol = permission.get(
                    "IpProtocol"
                )

                for ip_range in permission.get(
                    "IpRanges",
                    []
                ):

                    cidr = ip_range.get(
                        "CidrIp"
                    )

                    if cidr != "0.0.0.0/0":
                        continue

                    # SSH
                    if from_port == 22:

                        findings.append({
                            "service": "EC2",
                            "resource": group_id,
                            "severity": "CRITICAL",
                            "title": "SSH Exposed to Internet",
                            "description": (
                                f"Security group '{group_name}' "
                                "allows SSH from 0.0.0.0/0."
                            ),
                            "port": "22",
                            "protocol": protocol
                        })

                    # RDP
                    elif from_port == 3389:

                        findings.append({
                            "service": "EC2",
                            "resource": group_id,
                            "severity": "CRITICAL",
                            "title": "RDP Exposed to Internet",
                            "description": (
                                f"Security group '{group_name}' "
                                "allows RDP from 0.0.0.0/0."
                            ),
                            "port": "3389",
                            "protocol": protocol
                        })

                    # Other ports
                    else:

                        findings.append({
                            "service": "EC2",
                            "resource": group_id,
                            "severity": "HIGH",
                            "title": "Internet-Exposed Security Group",
                            "description": (
                                f"Security group '{group_name}' "
                                "allows inbound traffic from "
                                "0.0.0.0/0."
                            ),
                            "port": (
                                str(from_port)
                                if from_port
                                else "All"
                            ),
                            "protocol": protocol
                        })

    except Exception as error:

        findings.append({
            "service": "EC2",
            "resource": "AWS Account",
            "severity": "HIGH",
            "title": "Security Group Scanner Error",
            "description": str(error)
        })

    return findings