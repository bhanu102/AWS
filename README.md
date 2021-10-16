# S3-Uploader

Uploading a image to s3 over the internet.

## Steps

1) Using the S3, IAM, Lambda, API Gateway we can achieve this.

2) Create a Lambda Function with the name **"getPresignedUrl"** and select NodeJs for execution using the **index.js** file.
3) Give the permissions for Lambda execution role with an IAM inline policy below:
```NodeJs
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
```
4) Add an API gateway with the HTTP api end point to invoke the lambda function
5) Upload **index.html** to s3 bucket to upload the image from the internet
