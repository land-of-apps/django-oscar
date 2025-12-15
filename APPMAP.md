# AppMap Installation and Configuration Notes


## Setup procedure

```bash
nvm use 22
virtualenv venv --python=python3.11
. ./venv/bin/activate
pip install appmap
make sandbox
appmap-python sandbox/manage.py runserver
```

## appmap.yml

Note the one important function exclusion:

```yaml
appmap_dir: tmp/appmap
language: python
name: django-oscar_nov_2025
packages:
- path: sandbox
- path: oscar
  exclude: 
  - apps.catalogue.abstract_models.AbstractCategory.get_ancestors_and_self
```