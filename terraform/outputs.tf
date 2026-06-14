output "input_bucket_name" {
  value = aws_s3_bucket.input_bucket.bucket
}

output "output_bucket_name" {
  value = aws_s3_bucket.output_bucket.bucket
}

output "lambda_name" {
  value = aws_lambda_function.image_metadata_processor.function_name
}