# Reading Stuff

## Français

### Contexte
Reading Stuff est en quelques mots un prototype d'application de type blogging/e-reading. Le but est de permettre à des utilisateurs et/ou auteurs de publier des articles ou des chapitres de livres.

>Note : le site n'est pas fini et n'a pas prétention à l'être. C'est simplement un bac à sable pour tester des choses.

À travers cette app, j'ai essayer d'implémenter un maximum de fonctionnalités intéressantes en Django, telles que : 
- Un système de traductions (zalgo)
- Quelques manipulations de l'UX/UI
- Un système de 'Dark Mode' géré via les cookies & les préférences utilisateurs (beaucoup plus coupliqué que ça ne devrait l'être...)
- Un système de favoris
- Une bibliothèque d'écriture (CKEditor) pour agrémenter les postes de plus de fonctionnalités
- Une pseudo-implémentation du polymorphisme en utilisant `PolymorphicModel`

### Installation
Pour installer les dépendances, lancez :
```pip3 install -r requirements.txt```

Migrez la base de données (psql par défaut) avec :
```python3 manage.py makemigrations```
```python3 manage.py migrate```

(Optionnel) vous pouvez générer un jeu de données de départ avec :
```python3 manage.py seed```
Note : les emails et mots de passes générés pour les comptes factices sont rangés dans le fichier `dummy_passwords.txt`.

Ensuite, lancez le serveur avec :
```python3 manage.py runserver```

### Notes
Si CKEditor (ou toute autre partie de l'app) ne fonctionne pas, lancez ```python3 manage.py collectstatic``` avant l'instllation.

Le script ```zalgoify.py``` dans `./locale/LC_MESSAGES` remplira le fichier de traduction `django.po` avec le langage (charabia) zalgo.


Pour mettre à jour les traductions, lancez ```python3 manage.py makemessages -l XX``` où ```XX``` est l'un des langages. Seuls l'Anglais (default), le Français - 'fr' et  Charabia ('zz') sont disponibles.
Vous pouvez ignorer les messages d'erreurs liés au codec UTF-8.

Lancez ```python3 manage.py compilemessages``` pour générer les fichiers de traductions.


## English

### Context
Reading Stuff is basically a blog/e-writing plateform prototype. It lets users and authors post articles and book chapters.

>Note : the website is not currently 'finished', nor does it ever needs to be. It's end job is just being what it is.

Through it I tried to work on as many interesting things as I could, worth mentionning are : 
- A translation system, that also has a custom language implementation (zalgo)
- Some UI/UX manipulations
- A cookie/user preference setting for dark mode (this was insanely more convoluted than it needed to be...)
- A 'favourite' system
- A writing oriented library (through CKEditor)
- A pseudo implementation of polymorphism in classes using `PolymorphicModel`

### Setup
To install all the dependencies run :
```pip3 install -r requirements.txt```

Then migrate the database (psql by default) with :
```python3 manage.py makemigrations```
```python3 manage.py migrate```

Then simply start the server using :
```python3 manage.py runserver```

### Notes
If CKEditor (or the app overall) doesn't work, run ```python3 manage.py collectstatic``` before setup.

The ```zalgoify.py``` script in `./locale/LC_MESSAGES` will fill the django.po translation file for the gibberish (zz) language.


To update the translations, type ```python3 manage.py makemessages -l XX``` where ```XX``` is one of the languages. Only English (default), French - 'fr' and Gibberish ('zz') are available right now.
Ignore the utf-8 codec error message.

Then run ```python3 manage.py compilemessages``` to generate the rendered files.