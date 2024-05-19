FROM public.ecr.aws/lambda/python:3.11

RUN yum update -y && yum install -y gcc-c++
RUN yum install java-1.8.0-openjdk-devel -y

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

RUN pip install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.handler" ]