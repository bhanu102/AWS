#!/bin/bash
aws ec2 run-instances --image-id ami-xxxxxxxxxxxxxxxxxxx --count 1 --instance-type t2.micro --key-name xxxxxxxxx --security-group-ids sg-xxxxxxxxxxxxxxxxxxx --subnet-id subnet-xxxxxxxxxxxxxxxxxxx --output text
INSTANCE_ID=$(aws ec2 describe-instances --filters Name=instance-state-name,Values=pending --query Reservations[].Instances[].InstanceId --region us-east-1 --output json)
id=$(echo $INSTANCE_ID |awk '{print substr($0, 4, 19)}')
aws ec2 create-tags --resources $(echo $id) --tags Key=Name,Value=Testing