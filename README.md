# Annotator

![Screenshot](https://github.com/zacharykitt/annotator/blob/assets/screenshot.png)

This repo contains a Django-based comment annotation system. 

## Getting Started

Create a sqlite database and populate it using the addcomments.py command (`python manage.py addcomments`). Comments must be in a CSV format with the following columns: text, code. The code column should be a UID. Tags can be added on the fly through the admin console or through the main interface.

Note that the current version has been secured with the django-registration-redux library to support user accounts, but solo users may be interested in removing this functionality. Make sure the **settings.py** file is customized for your unique needs.

Don't forget to add a **secrets.json** file that contains your unique Django key.
