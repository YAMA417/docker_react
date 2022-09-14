FROM python:3.9                    
LABEL architecture="URI417"               

ENV PYTHONUNBUFFERD 1                        

COPY ./requirements.txt /requirements.txt   
RUN pip install -r /requirements.txt        

RUN mkdir /django-api                        
WORKDIR /django-api                          
# COPY ./django-api /django-api                                                  
