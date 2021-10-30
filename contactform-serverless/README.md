# Contact form using Serverless

Contact form is an essential part of business to collect data from the visitors or customers to interact with them. It is hosted using AWS Lambda which is a serverless computing service helps in minimizing our costs and provide best business solutions in hosting simple dynamic web pages like user registration, contact us form, and survey form.

## Usage

1. Create an IAM role with AWS service Lambda to invoke other services and give PowerUserAccess permission policy.
2. Create a DynamoDB table contactform with email as primary key.
3. Create a Lambda function contactform_function and select Python3.9 for run time and select the IAM role created in step 1 and click on create function.
4. Upload the "lambdafunction" ZIP file that consists of contactus.html, confirm.html, and lambda_function.html. Now our function is ready.
5. Create an API gateway with REST API and create a GET and POST methods , for each of this method use lambda proxy integration and select the function created in step 3 & 4. Finally deploy the api with a new stage dev. It gives the invoke url which is our contact form.
6. This invoke url can be attached to a custom domain with api mappings and route53 configuration.

## License
[MIT](https://choosealicense.com/licenses/mit/)