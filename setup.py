from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='jenkins-backup-s3',
    version='0.1.9',
    description="Backup Jenkins to S3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/artsy/jenkins-backup-s3",
    author='Walid Boussafa',
    author_email='boussaffa.walid@outlook.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jenkins-backup=jenkins_backup_s3.jenkins_backup:main'
        ]
    },
    install_requires=(
        'boto3',
        'click',
        'colorama',
        'python-dateutil',
        'termcolor'
    )
)
