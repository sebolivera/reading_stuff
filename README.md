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

The ```zalgoify.py``` script in ./locale/LC_MESSAGES will fill the django.po translation file for the gibberish (zz) language.

To update the translations, type ```python3 manage.py makemessages -l XX``` where ```XX``` is one of the languages. Only English (default), French - 'fr' and Gibberish ('zz') are available right now.
Ignore the utf-8 codec error message.