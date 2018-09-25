from setuptools import setup

setup(name="perseus",
      version="0.0.UNKNOWN",
      packages=['perseus', 'perseus.routes', 'perseus.constants', 'perseus.util'],
      install_requires=[
          'bottle==0.12.7',
          'requests==2.4.3',
          'uwsgi==2.0.15',
          'pytest == 3.2.3',
          'awscli',
          'six == 1.11.0',
          'freezegun == 0.3.9',
          'webargs==1.6.0',
          'webtest',
          'mock'
      ]
      )
