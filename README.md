## AWS Lambda Integration with PostgreSQL 

This repository will help in creating the AWS Lambda Function in Python, which will connect to PostgreSQL DB over SSL.

### Tech Stack
      Python 3.6
      AWS Lambda 
      PostgreSQL
      Psycopg2(Postgres connector)
      SSL


### Assumption
      DB is already created with some table and access on AWS cloud. 
      
### Steps Required for Project Setup
      1- Install Python3.6 or 3.8
      2- Create a lambda project in python
      3- Add psycopg2 dependency in your project root. (Add Image) (Reference)
      3- Get SSL certificate from AWS (), add this SSL Certificate to your project directory. (Add Image)
      4- Access this certificate in your code and use it in your psycopg2.connect() as sslMode and ssl_ca.(Add Image)
      5- Zip it and upload it in AWS lambda (Note: Zip name and lambda name should be same, and lambda_funcation.py should be on root of zip)

### Steps Required for Project Deployment
    1- Create Lambda furcation (Image) with same name as project zip.
    2- Create Lambda a Role, which should have RDSAccess Permission. 
    3- Lambda should be in same VPC and subnets as PostgreSQL
    4- Lambda should have a Security Group, this security group should have permission in PostgreSQL. So there should be a inbound rule in PostgreSQL Security Group for Lambda Security Group 
    
 ### Step Run 
 
 ### Steps to upload ZIP file to AWS Lambda
 
 
# References
 
   [SSL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) 
   
  [SSL MODE  ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.SSL.html#PostgreSQL.Concepts.General.SSL.Connecting)
   
   [postgresql-and-python]( https://gist.github.com/pfigue/3440e2bc986550a6b8ec)
   
  [awslambda-psycopg2]( https://gist.github.com/pfigue/3440e2bc986550a6b8ec) 
  
  [SSL Issue]( https://gist.github.com/pfigue/3440e2bc986550a6b8ec)
 




