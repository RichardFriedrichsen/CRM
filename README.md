Project Name: CRM

The Customer Relations Management tool is designed to have integrated E-Mails which can be pulled from the imap servers of your choice. It features E-Mail customer communication (inbound/outbound) with and integrated to-do list.

Technologies:
  - Django => Server
  - SQLlite => DB
  - Celery => Task broker
  - RabbitMQ => message broker
  - HTML (with Django Templates)
  - CSS => styling

Table of Contents:

Installation & Usage

  Django:
    py manage.py runsever

  RabbitMQ:
    Open Docker and run the following in the terminal: 
      docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=richard -e RABBITMQ_DEFAULT_PASS=password rabbitmq:management

  Celery:
    Open another Terminal and run:
      celery -A A_Email worker --pool=solo -l info
      
Author:
Richard Friedrichsen
    
