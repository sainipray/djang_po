from setuptools import find_packages, setup

import django_po

setup(
    name=django_po.__name__,
    version=django_po.__version__,
    packages=find_packages(),
    url='https://github.com/sainipray/django_po',
    author=django_po.__author__,
    author_email=django_po.__author_email__,
    description=django_po.__description__,
    license='MIT',
    include_package_data=True,
    platforms=['any'],
    install_requires=[
        "xlsxwriter"
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
    ],
)
