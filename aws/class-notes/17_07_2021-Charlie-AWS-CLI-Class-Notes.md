Clarusway
AWS&DevOps-08

Lesson starts at 1500

* AWS CLI
- https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

* What-Why-How

- Open source tool to reach and manipulate AWS resources from command line of your operating system.

- Currently there are 2 versions. We will use version 2.

* Install AWS CLI (MS-Lınux-MacOS)

- https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
 
  https://graspingtech.com/install-and-configure-aws-cli/

    $ aws --version
    
    For MS Windows
    https://awscli.amazonaws.com/AWSCLIV2.msi

    You should also install CLI if you are using a virtual machine like WSL in your Windows system.

    For Linux (On Ubuntu)
    
    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ aws --version
    $ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    $ sudo apt install unzip
    $ unzip awscliv2.zip
    $ sudo ./aws/install

    $ aws s3 ls

    So you have to configure according to your credentials.



* Configure AWS CLI

- AWS requires that all incoming requests are cryptographically signed. The AWS CLI does this for you. The "signature" includes a date/time stamp. Therefore, you must ensure that your computer's date and time are set correctly. If you don't, and the date/time in the signature is too far off of the date/time recognized by the AWS service, AWS rejects the request.

- After installation and configuration regardless of your operating system AWS CLI works with same commands.

- Connection to IAM
When you created an IAM user you check the programatic access.
Connect to console open your security credendials from the drop down menu by clicking your name or from IAM service.
You can have max 2 Access Keys correspond to access IDs. Once created, download csv file do not lose.


- $ aws configure
  AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
  AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
  Default region name [None]: us-west-2
  Default output format [None]: json

- For Windows 
  C:\Users\User_Name\.aws

  For Linux
  /.aws 
  
  $ cat config
  $ vi config

You can see the values if you "aws configure" again. If you want to change you can type the new values.

  $ aws s3 ls

- Named Profiles

https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html

Imagine you have multiple accounts or different users for an account. You can use "profiles" to use AWS CLI. to different different profiles we have 2 options. first is manipulating the config file with editors. second is with CLI commands by adding required parameters. (this is only for once)
  
  $ aws configure --profile new-user
  $ cat credentials
  $ cat config
  $ aws s3 ls --profile new-user

If you want to use the profile during the session, you have to export a variable;
  
  for linux and macOS
  $ export AWS_PROFILE=new-user
  
  for Windows
  $ setx AWS_PROFILE new-user

  $ aws sts get-caller-identity



* Basic Examples

- Structure of AWS CLI commands
  $ aws
  $ aws help
  
  aws command subcommand help
  $ aws s3 cp help

  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-services.html

  https://docs.aws.amazon.com/cli/latest/index.html

- Examples

  Go on with the pre class

  $ aws iam create-user --user-name Levo <br>
  $ aws iam list-users

  $ aws s3 ls <br>
  $ aws s3 ls s3://<bucket name>


  $ aws ec2 run-instances --generate-cli-skeleton > demo.json

  Change the demo.json file as below.
 <br>
{<br>
    "ImageId": "ami-0dc2d3e4c0f9ebd18",<br>
    "InstanceType": "t2.micro",<br>
    "KeyName": "levo",<br>
    "SecurityGroupIds": [<br>
        "sg-0de0b09f2cb3c31d5"<br>
    ]<br>
}<br>
<br>
  $ aws ec2 run-instances --cli-input-json file://demo.json

  When it is done, stop and/or terminate the newly created instance either by using CLI or Console. 
