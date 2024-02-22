# django-clerk

django-clerk is a Django library that integrates with the Clerk authentication platform. It provides seamless integration with Clerk's user authentication and authorization features, allowing you to easily authenticate and manage users in your Django application.

(or at least that's the goal - currently very alpha - thar be dragons)

[![PyPI - Version](https://img.shields.io/pypi/v/django-clerk.svg)](https://pypi.org/project/django-clerk)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-clerk.svg)](https://pypi.org/project/django-clerk)

---

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install django-clerk
```

Add to apps

```python
INSTALLED_APPS = [
    # other apps...
    'django_clerk',
]
```

Add Middleware which sets request.user

```python
MIDDLEWARE = [

# other middleware...

'django_clerk.middleware.ClerkMiddleware',
]
```

The following setting is required.
CLERK_JWT_PEM_PUBLIC_KEY = "your_public_key_here"

## License

`django-clerk` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
