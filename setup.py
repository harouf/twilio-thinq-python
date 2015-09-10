from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='twilio_with_thinq',
      version='0.1',
      description='Twilio Wrapper Library For thinQ LCR integration.',
      long_description=readme(),
      keywords='twilio thinq wrapper',
      url='https://github.com/harouf/twilio-thinq-python',
      author='Fujio Harou',
      author_email='harouf@outlook.com',
      license='MIT',
      packages=['twilio_with_thinq'],
      install_requires=[
          'twilio'
      ],
      include_package_data=True,
      zip_safe=False)