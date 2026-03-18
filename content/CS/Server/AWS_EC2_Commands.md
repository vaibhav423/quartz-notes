## Creating an EC2 Instance

Use the following command to create a new EC2 instance:
### Linux
```bash
aws ec2 run-instances \
  --image-id "ami-084568db4383264d4" \
  --instance-type "c7a.8xlarge" \
  --key-name "Fire" \
  --block-device-mappings '[
    {
      "DeviceName": "/dev/sda1",
      "Ebs": {
        "Encrypted": false,
        "DeleteOnTermination": true,
        "Iops": 3000,
        "SnapshotId": "snap-0edbe0f6601b2861c",
        "VolumeSize": 30,
        "VolumeType": "gp3",
        "Throughput": 125
      }
    }
  ]' \
  --network-interfaces '[
    {
      "SubnetId": "subnet-0a077e932c14b8583",
      "AssociatePublicIpAddress": true,
      "DeviceIndex": 0,
      "Groups": ["sg-010420643d3fe8ed1"]
    }
  ]' \
  --tag-specifications '[
    {
      "ResourceType": "instance",
      "Tags": [
        {
          "Key": "Name",
          "Value": "heavylinux"
        }
      ]
    }
  ]' \
  --metadata-options '{
    "HttpEndpoint": "enabled",
    "HttpPutResponseHopLimit": 2,
    "HttpTokens": "required"
  }' \
  --private-dns-name-options '{
    "HostnameType": "ip-name",
    "EnableResourceNameDnsARecord": false,
    "EnableResourceNameDnsAAAARecord": false
  }' \
  --count 1 \
  | jq -r '.Instances[0].InstanceId' 
```
### Windows
#### Launch instance
```bash
aws ec2 run-instances \
  --image-id "ami-0fa71268a899c2733" \
  --instance-type "t3.medium" \
  --key-name "Fire" \
  --block-device-mappings '{
    "DeviceName": "/dev/sda1",
    "Ebs": {
      "Encrypted": false,
      "DeleteOnTermination": true,
      "Iops": 3000,
      "SnapshotId": "snap-09507938b612a756b",
      "VolumeSize": 30,
      "VolumeType": "gp3",
      "Throughput": 125
    }
  }' \
  --network-interfaces '{
    "SubnetId": "subnet-0a077e932c14b8583",
    "AssociatePublicIpAddress": true,
    "DeviceIndex": 0,
    "Groups": ["sg-010420643d3fe8ed1"]
  }' \
  --credit-specification '{
    "CpuCredits": "unlimited"
  }' \
  --tag-specifications '{
    "ResourceType": "instance",
    "Tags": [
      {
        "Key": "Name",
        "Value": "ghhj"
      }
    ]
  }' \
  --metadata-options '{
    "HttpEndpoint": "enabled",
    "HttpPutResponseHopLimit": 2,
    "HttpTokens": "required"
  }' \
  --private-dns-name-options '{
    "HostnameType": "ip-name",
    "EnableResourceNameDnsARecord": false,
    "EnableResourceNameDnsAAAARecord": false
  }' \
  --count "1" \
  | jq -r '.Instances[0].InstanceId'
```
#### Password
```bash
aws ec2 get-password-data \
  --instance-id i-00b78372a51651129 \
  --priv-launch-key ~/Fire.pem
```

## Listing Instance IDs

To list the Instance ID(s) of instances with a specific tag (e.g., `Name=termux`):

```bash
aws ec2 describe-instances --filters Name=tag:Name,Values=termux --query 'Reservations[*].Instances[*].InstanceId' --output text
```

**Example Output:**

```
i-068a718798893320f
```

## Terminating an EC2 Instance

To terminate an EC2 instance, use the following command, replacing `i-068a718798893320f` with the actual instance ID:

```bash
aws ec2 terminate-instances --instance-ids i-02b81a273c6867d4c
```

**Important:** Terminating an instance is a permanent action.

## Getting the Public IP Address

To retrieve the public IP address of an instance with a specific tag (e.g., `Name=termux`):

```bash
aws ec2 describe-instances --filters "Name=tag:Name,Values=termux" --query "Reservations[*].Instances[*].PublicIpAddress" --output text
```