## ML project with front end

- front end
- js
- html
- css
- python
- FastAPI

---

![screenshot](https://github.com/RGGH/API-1/blob/main/Full_Project/ss_neural_net_ratings.png)

see https://stackoverflow.com/questions/68645378/how-to-deploy-fastapi-to-google-cloud-run
for Dockerfile details

    FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

    COPY . /app
    ENV APP_HOME /app

    WORKDIR $APP_HOME
    COPY . ./

    RUN pip install -r requirements.txt

    CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app
---
    gcloud builds submit --tag gcr.io/PROJECT-ID/countries_fastapi
---
    gcloud run deploy --image gcr.io/bitnami-oyzgng8y5a/countries_fastapi --platform managed
    
