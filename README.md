# AWS Simple Document Language Translator

## Overview
This project aims to provide a straightforward solution for translating languages within documents using various AWS services.

## AWS Services Utilized

- **Amazon Simple Storage Service (S3):** Utilized for storing documents requiring translation.
- **AWS Lambda:** Used to translate documents within the S3 bucket upon invocation.
- **AWS IAM:** To leverage least privileges to the different Aws services used for best security practices.

## Architecture
<img src="https://i.imgur.com/4VgwVkm.png" height="80%" width="80%" alt="Code commit permissions"/>
<br />
<br />

### 1.) Setting up the S3 Buckets
The initial step involved setting up two separate S3 buckets: one for input files and another for output files. The latter would host the translated documents following Lambda's translation process.

### 2.) Setting up the Lambda Function for Document Language Translation
Lastly, a Lambda function was created to facilitate the translation of documents stored within the input S3 bucket.

### 3.) Testing
<img src="https://i.imgur.com/dRAMlsH.png" height="80%" width="80%" alt="Code commit permissions"/>
<br />
<br />



