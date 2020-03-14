from setuptools import setup

setup(
      name = 'tourist_translations',
      version = '1.0',
      description = 'Programming challenge on https://www.codechef.com/problems/TOTR',
      url = 'https://github.com/jprussoibanez/codechef',
      author = 'Juan Pablo Russo',
      author_email = 'jprussoibanez@gmail.com',
      license = 'MIT',
      packages = ['tourist_translations'],
      zip_safe = False,
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
          'console_scripts': [
              'tourist_translations = tourist_translations.__main__:main'
          ]
      }
)