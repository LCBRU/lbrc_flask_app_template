# NIHR Leicester BRC Flask Application Template

## Running Jobs

This application uses background tasks to connect to the external
systems using the python Celery library with Redis as the backend.

### Redis Server

To run redis, use the command:

```
redis-server
```

### Run Celery Worker

To run the celery work, use the command:

```
celery -A celery_worker.celery worker -l 'INFO'
```
