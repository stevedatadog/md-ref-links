FROM python:3-alpine

COPY ref-links-to-inline.py /ref-links-to-inline.py

ENTRYPOINT ["python3", "/ref-links-to-inline.py"]
