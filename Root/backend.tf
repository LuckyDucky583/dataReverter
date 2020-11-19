terraform {
  required_version = ">=0.12.0"
  backend "s3" {
    region  = "eu-central-1"
    profile = "default"
    key     = "terraformstatefile"
    bucket  = aws_s3_bucket.terraform_state.id
  }

}