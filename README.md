Uploading a image to s3 through a web page:
Using the S3,IAM,Lambda,API Gateway we can achieve this.
Create a Lambda Function with the name "getPresignedUrl" and select NodeJs for execution using the index.js file.
Give the permissions for Lambda execution role with an IAM inline policy below:

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:PutObjectAcl"
            ],
            "Resource": "arn:aws:s3:::bhanu-uploads/*"
        }
    ]
}

Add an API gateway with the HTTP api end point to invoke the lambda function
Upload index.html to s3 bucket to upload the image from the internet
