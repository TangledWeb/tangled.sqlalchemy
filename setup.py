from setuptools import setup, PEP420PackageFinder


setup(
    name='tangled.sqlalchemy',
    version='1.0a6.dev0',
    description='Tangled SQLAlchemy integration',
    long_description=open('README.rst').read(),
    url='https://tangledframework.org/',
    download_url='https://github.com/TangledWeb/tangled.sqlalchemy/tags',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    packages=PEP420PackageFinder.find(include=['tangled*']),
    install_requires=[
        'tangled>=1.0a12',
        'SQLAlchemy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
