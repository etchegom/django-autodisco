# django-autodisco

Micro django lib that helps auto-loading app modules.

**Why this lib?**

I am used to grouping signal connectors and receivers in a module called `receivers.py`. I didn't want add the module import in the `ready` method of all the apps anymore.

---

## Installation

```
pip install django-autodisco
```
Or, for the latest git version
```bash
python -m pip install 'django-autodisco @ git+https://github.com/etchegom/django-autodisco.git'
```

---

## Usage

Add the `autodisco` django app:

```python
INSTALLED_APPS = [
    ...
    "autodisco",
]
```

Define the modules to auto-load in settings:

```python

AUTODISCO_MODULES = [
    "receivers",
    ...
]

```

---

## Run example

```bash
make example
```

---

## Run tests

```bash
make tests
```
