from setuptools import setup

setup(
      name = 'bst_operations',
      version = '0.1',
      description = 'Programming challenge on https://www.codechef.com/problems/BSTOPS',
      url = 'https://github.com/jprussoibanez/codechef',
      author = 'Juan Pablo Russo',
      author_email = 'jprussoibanez@gmail.com',
      license = 'MIT',
      packages = ['bst_operations'],
      zip_safe = False,
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
          'console_scripts': [
              'bst_operations = bst_operations.__main__:main'
          ]
      }
)