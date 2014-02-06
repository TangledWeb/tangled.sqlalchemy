from setuptools import setup


setup(
    name='tangled.sqlalchemy',
    version='0.1a2.dev0',
    description='Tangled SQLAlchemy integration',
    long_description=open('README.rst').read(),
    url='http://tangledframework.org/',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    packages=[
        'tangled.sqlalchemy',
    ],
    install_requires=[
        'tangled>=0.1.dev0',
        'SQLAlchemy',
    ],
    extras_require={
        'dev': [
            'tangled[dev]',
        ],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
