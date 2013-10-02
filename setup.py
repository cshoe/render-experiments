from setuptools import setup

required = ['django==1.4', 'jinja']

setup(
    name='render-experiments',
    version='0.0.1alpha',
    description='Experiments in template rendering, focusing on Django and Jinja.',
    long_description=open('README.rst').read(),
    author='Chris Schomaker',
    author_email='schomaker.c@gmail.com',
    license='WTFPL',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
