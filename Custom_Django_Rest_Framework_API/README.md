<h1>Image Upload Custom API with Django and Django REST Framework!</h1>

Django App which has an API where someone can upload an image! Not all the files are here, you'd need to run setup for django and the database, I recommend you play around with GET and POST requests with 'Postman' for this app.

Try:

  First run the server using 'python manage.py runserver', it might also be a good idea to run the following commands as well:
  'python manage.py makemigrations' followed by 'python manage.py migrate' if the server fails to run.

  POST  localhost/file/upload/

  Select formdata, then include the keys: file, remark (timestamp is auto generated). Fill in their appropriate values (ie. for file, a photo, and for remark, some string. Be sure the boxes to the left of the keys are checked and the click SEND to send the request.

  You should notice that the database is now populated with your image/file and there is a new folder created called 'media' containing this file! 
