# Python-Project
This project allows users to create, update, share, and delete project information, including details and attached documents. It supports authentication, access control, and document management using AWS S3 and Lambda for image processing.

Stack:
Python3.10
FastAPI
PostgreSQL + Optional ORM (SQLAlchemy, etc)
Docker
AWSS3 (file storage)
AWS Lambda functions (for image processing on s3 event)
CI/CD:  GitHub Actions/Gitlab CI (testing/linting/building/pushing to registry/deploy to cloud on merge request)



Desired functionality:
User login/auth
Create/Delete projects
Add/Update project’s info/details - name, description
Add/Update/Remove projects documents (docx, pdf)
Share project with other users to access

