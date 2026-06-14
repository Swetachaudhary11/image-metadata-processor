# Automated Image Metadata Processor

## Project Overview

The Automated Image Metadata Processor is a serverless AWS solution that automatically extracts metadata from images uploaded to an Amazon S3 bucket.

When an image is uploaded, Amazon S3 triggers an AWS Lambda function. The Lambda function retrieves image metadata such as file name, file size, and upload timestamp, generates a metadata report, and stores the report in a separate S3 bucket.

The entire infrastructure is provisioned using Terraform, making the deployment reproducible, scalable, and Infrastructure-as-Code (IaC) compliant.

---

## Architecture

```text
Image Upload
      │
      ▼
+------------------+
| Input S3 Bucket  |
+------------------+
      │
      ▼
S3 Event Notification
      │
      ▼
+------------------+
| AWS Lambda       |
| Python Runtime   |
+------------------+
      │
      ▼
Metadata Extraction
      │
      ▼
+------------------+
| Output S3 Bucket |
+------------------+
      │
      ▼
Metadata Report
```

---

## Problem Statement

Organizations often upload large numbers of images to cloud storage.

Manually tracking image information such as:

- File Name
- File Size
- Upload Timestamp

is time-consuming and inefficient.

This project automates metadata extraction and report generation using AWS serverless services.

---

## Features

- Automated image processing
- Event-driven architecture
- Serverless execution
- Infrastructure as Code (Terraform)
- Metadata report generation
- AWS-native implementation
- Scalable and cost-effective design

---

## AWS Services Used

### Amazon S3

Used for:

- Storing uploaded images
- Storing generated metadata reports

### AWS Lambda

Used for:

- Processing uploaded images
- Extracting metadata
- Generating reports

### AWS IAM

Used for:

- Managing permissions
- Allowing Lambda access to S3

### Amazon CloudWatch

Used for:

- Monitoring Lambda execution
- Viewing logs and debugging

---

## Technology Stack

| Technology | Purpose |
|------------|----------|
| AWS S3 | Object Storage |
| AWS Lambda | Serverless Compute |
| IAM | Access Control |
| CloudWatch | Monitoring |
| Terraform | Infrastructure as Code |
| Python | Business Logic |
| GitHub Actions | CI/CD Automation |
| YAML | Workflow Definition |

---

## Project Structure

```text
image-metadata-processor/

├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── images/
│   └── sample.jpg
│
├── lambda/
│   ├── lambda_function.py
│   └── lambda.zip
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── terraform.tfvars
│   └── outputs.tf
│
├── README.md
└── .gitignore
```

---

## Workflow

### Step 1

Upload an image to the input S3 bucket.

### Step 2

Amazon S3 detects the upload event.

### Step 3

S3 automatically invokes the Lambda function.

### Step 4

Lambda retrieves image metadata.

### Step 5

A metadata report is generated.

### Step 6

The report is stored in the output S3 bucket.

---

## Example Input

```text
sample.jpg
```

---

## Example Output

```text
IMAGE METADATA REPORT

File Name: sample.jpg

File Size (Bytes): 125643

Upload Time: 2026-06-14 10:15:22
```

---

## Lambda Logic

The Lambda function performs the following tasks:

1. Receives an S3 event.
2. Retrieves bucket and object information.
3. Fetches metadata using Boto3.
4. Creates a formatted metadata report.
5. Stores the report in the output bucket.

### AWS SDK Method Used

```python
s3.head_object()
```

Used for retrieving object metadata without downloading the image.

---

## Terraform Resources Created

### S3 Buckets

- Input Bucket
- Output Bucket

### IAM

- Lambda Execution Role
- S3 Access Policy

### Lambda

- Image Metadata Processor Function

### Permissions

- S3 → Lambda Invocation Permission

### Event Notification

- S3 ObjectCreated Trigger

---

## Deployment Prerequisites

Install the following tools:

### Terraform

Verify installation:

```bash
terraform --version
```

### AWS CLI

Verify installation:

```bash
aws --version
```

### Python

Verify installation:

```bash
python --version
```

### Git

Verify installation:

```bash
git --version
```

---

## Deployment Steps

### Clone Repository

```bash
git clone <repository-url>
```

### Navigate to Project

```bash
cd image-metadata-processor
```

### Configure AWS Credentials

```bash
aws configure
```

Provide:

```text
AWS Access Key
AWS Secret Key
Region
Output Format
```

### Initialize Terraform

```bash
cd terraform

terraform init
```

### Validate Configuration

```bash
terraform validate
```

### Review Deployment Plan

```bash
terraform plan
```

### Deploy Infrastructure

```bash
terraform apply
```

Type:

```text
yes
```

when prompted.

---

## Upload Test Image

```bash
aws s3 cp images/sample.jpg s3://YOUR-INPUT-BUCKET/
```

Example:

```bash
aws s3 cp images/sample.jpg s3://sweta-image-input-2026-12345/
```

---

## Verify Output

List generated reports:

```bash
aws s3 ls s3://YOUR-OUTPUT-BUCKET/
```

Expected:

```text
sample.jpg_metadata.txt
```

Download report:

```bash
aws s3 cp s3://YOUR-OUTPUT-BUCKET/sample.jpg_metadata.txt .
```

View report:

```bash
cat sample.jpg_metadata.txt
```

---

## CI/CD Pipeline

The project includes GitHub Actions-based CI/CD.

### Workflow File

```text
.github/workflows/deploy.yml
```

### Automated Steps

1. Checkout Repository
2. Configure AWS Credentials
3. Terraform Init
4. Terraform Validate
5. Terraform Plan
6. Terraform Apply

### Trigger

Pipeline executes automatically on push to the main branch.

---

## Security Considerations

### IAM Least Privilege

Only required permissions are granted.

### No Public Buckets

Buckets remain private by default.

### Infrastructure as Code

All resources are version-controlled and auditable.

---

## Monitoring

Amazon CloudWatch is used for:

- Lambda execution logs
- Error monitoring
- Debugging
- Operational visibility

---

## Challenges Faced

- IAM permission management
- Lambda trigger configuration
- Terraform resource dependencies
- Global S3 bucket naming requirements

---

## Future Enhancements

### Image Analytics

- Image dimensions
- File format detection
- EXIF metadata extraction

### AI Integration

- AWS Rekognition
- Object detection
- Face detection
- Content moderation

### Data Storage

- DynamoDB integration
- Metadata catalog

### Notifications

- SNS email alerts
- Event-driven reporting

---

## Benefits

### Automation

No manual metadata extraction.

### Scalability

Automatically handles increasing workloads.

### Cost Efficiency

Pay only for actual Lambda executions.

### Reliability

AWS-managed infrastructure with high availability.

### Reproducibility

Terraform enables repeatable deployments.

---

## Learning Outcomes

This project demonstrates practical experience with:

- AWS S3
- AWS Lambda
- IAM
- CloudWatch
- Terraform
- Python (Boto3)
- Infrastructure as Code
- Event-Driven Architecture
- CI/CD using GitHub Actions
- YAML Workflows

---

## Author

**Sweta Chaudhary**

Cloud & DevOps Enthusiast

AWS | Terraform | Python | Docker | CI/CD

---

## License

This project is intended for educational, learning, portfolio, and hackathon purposes.