FROM frolvlad/alpine-python3
ARG PROJECT_DIR

RUN echo $PROJECT_DIR

RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
COPY requirements.txt $PROJECT_DIR
RUN pip install -r requirements.txt

EXPOSE 5000