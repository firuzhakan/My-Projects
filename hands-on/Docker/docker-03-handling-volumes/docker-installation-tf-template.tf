//This Template file creates a Docker machine on EC2 Instance.
//Docker Machine will run on Amazon Linux 2 EC2 Instance with
//custom security group allowing SSH connections from anywhere on port 22.

provider "aws" {
  region = "us-east-1"
  profile = "cw-training"
//  access_key = ""
//  secret_key = ""
//  If you have entered your credentials in AWS CLI before, you do not need to use these arguments.
}

data "aws_ami" "amazon-linux-2" {
  owners      = ["amazon"]
  most_recent = true

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "owner-alias"
    values = ["amazon"]
  }

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm*"]
  }
}

resource "aws_instance" "tf-docker-machine" {
  ami             = data.aws_ami.amazon-linux-2.id
  instance_type   = "t2.micro"
  key_name        = "oliver"
//  Write your pem file name
  security_groups = ["docker-sec-gr"]
  tags = {
    Name = "Docker"
  }
  user_data = <<-EOF
          #! /bin/bash
          yum update -y
          amazon-linux-extras install docker -y
          systemctl start docker
          systemctl enable docker
          usermod -a -G docker ec2-user
          curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" \
          -o /usr/local/bin/docker-compose
          chmod +x /usr/local/bin/docker-compose
          EOF
}

resource "aws_security_group" "tf-docker-sec-gr" {
  name = "docker-sec-gr"
  tags = {
    Name = "docker-sec-group"
  }
  ingress {
    from_port   = 80
    protocol    = "tcp"
    to_port     = 80
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    protocol    = "tcp"
    to_port     = 22
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    protocol    = -1
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}
output "ip" {
  value = aws_instance.tf-docker-machine.public_ip
}

output "account" {
  value = aws_instance.tf-docker-machine.arn
}