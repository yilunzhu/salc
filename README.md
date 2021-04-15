# salc
Website for the SALC corpus, supported by Georgetown University

### Supported features
#### User management
1. To manage users, please go to /admin/
superuser: admin
password: 123
2. The registration function is not supported (since it's not a public website). To add users, please ask the admin to add username, password, and email.
3. Anonymous users can visit the *Home* page, but only **logged-in users** can visit the *Corpus* page and do query.

#### Corpus searching
- TBD

### Restore locally
Currently the website runs locally. To restore the web in your local environment, please do as follows:
1. python manage.py makemigrations
2. python manage.py migrate
3. Rename the file `settings_example.py` to `settings.py` and add your *SECRET_KEY*.
