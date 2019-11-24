FROM python:3


COPY quiz_execution.py quiz_execution.py
COPY quiz_data.json quiz_data.json

CMD [ "python", "./quiz_execution.py" ]