from django.conf import settings


def pytest_configure():
    settings.configure(
        ROOT_URLCONF='rest_assured.tests.urls',

        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'test'
            }
        },

        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',

            'rest_framework',
            'rest_assured.tests',
        ]
    )


try:
    import django

    django.setup()
except AttributeError:
    pass
