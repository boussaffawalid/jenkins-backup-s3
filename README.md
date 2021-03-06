# jenkins-backup-s3

A collection of scripts to backup Jenkins configuration to S3, as well as manage and restore those backups. By default
runs silently (no output) with proper exit codes. Log Level option enables output.

## Setup

`pip3 install git+https://github.com/boussaffawalid/jenkins-backup-s3.git`

### Configure S3 and IAM

- Create an S3 bucket to store backups.

- Create an IAM role with STS:AssumeRole and a trust Service ec2.amazonaws.com.  The IAM role must have the `GetObject`, `DeleteObject`, `PutObject` and `ListBucket` S3 permissions for that bucket.

## Usage

Setup with cron for ideal usage.

`jenkins-backup {OPTIONS} {COMMAND} {COMMAND_OPTIONS}`

Options can be set directly or via and environment variable.

The only required option is your S3 bucket:
  - `jenkins-backup --bucket={BUCKET_NAME}`
  Or set it via the envirment variable
  - `JENKINS_BACKUP_BUCKET`

Other available options are:

Bucket prefix (defaults to "jenkins-backups"):
  - `jenkins-backup --bucket-prefix={BUCKET_PREFIX}`

Bucket region (defaults to "us-east-1"):
  - `jenkins-backup --bucket-region={BUCKET_REGION}`

Available commands:
  - `create`
  - `restore`
  - `list`
  - `delete`
  - `prune`

Run `jenkins-backup {COMMAND} --help` for command-specific options.

## Running a daily backup on Jenkins

Create a new item in Jenkins and configure a build of this repository.

Set the shell / virtualenv builder (if you have it installed) to run `jenkins-backup create`.

Set the build on a daily CRON schedule.
