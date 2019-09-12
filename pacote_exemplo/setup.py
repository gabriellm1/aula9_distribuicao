from setuptools import setup

setup(name='my_hello_gabrielm',
      version='0.1',
      author="Gabriel Monteiro",
      packages=['my_hello'],
      python_requires='>=3.6',
      plataforms=['posix','nt'],
      install_requires=[
        'pandas'
      ],
      scripts=['scripts/hello.py']
      )
