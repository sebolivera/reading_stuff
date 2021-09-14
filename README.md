# Reading Stuff

## Context
Just a small Django app to fuck around and learn some stuff.

## Setup
To install all the dependencies run :
```pip3 install -r requirements.txt```

Then migrate the database (psql by default) with :
```python3 manage.py makemigrations```
```python3 manage.py migrate```

Then simply start the server using :
```python3 manage.py runserver```

## Notes
If ckeditor (or the ap) doesn't work, run ```python3 manage.py collectstatic``` before setup.