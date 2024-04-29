import json
import boto3

# Initialiation of s3 buckets for translation
s3_client = boto3.client(service_name='s3')
translate = boto3.client('translate')

# Function to translate text
def translate_text(text, lang_code):
    result = translate.translate_text(
        Text=text,
        SourceLanguageCode='auto',
        TargetLanguageCode=lang_code
    )
    return result['TranslatedText']

# Lambda function handler
def lambda_handler(event, context):
    # Extract file name and bucket name from event
    file_name = event['Records'][0]['s3']['object']['key']
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    outfile = f"s3://ilori-translation-project-output-bucket/{file_name}"
    
    # Print event details
    print("Event details:", event)
    print("Input File Name:", file_name)
    print("Input Bucket Name:", bucket_name)
    print("Output File Name:", outfile)
    
    # Get S3 object
    result = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    
    # Read text file line by line
    final_document_array = ""
    for line in result["Body"].read().splitlines():
        each_line = line.decode('utf-8')
        print("Input Line:", each_line)
        if each_line != '':
            # Translate each line
            translated = translate_text(each_line, 'es')
            print("After translation:", translated)
            final_document_array += translated
            final_document_array += '\n\n'
    
    # Put translated document back to S3
    s3_client.put_object(Body=final_document_array, Bucket='ilori-translation-project-output-bucket', Key=file_name)
    print("Done")
