FROM python:3.10.0-alpine3.14
RUN python3 -m pip install requests
COPY . .
CMD python3 orka_sdk.py