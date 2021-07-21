import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='flask-faas',
    packages=setuptools.find_packages(),
    package_dir = {'': 'flask_faas'},
    version='0.1.0',
    license='MIT',
    description='flask serverless decorator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Shivanjan Chakravorty',
    author_email='schakravorty846@gmail.com',
    url='https://github.com/Glitchfix/flask-faas',
    project_urls={                                # Optional
        "Bug Tracker": "https://github.com/Glitchfix/flask-faas/issues"
    },
    install_requires=['flask', 'pytest'],
    keywords=["flask", "serverless", "faas", "flask-serverless", "lambda",
              "cloud function", "flask serverless"],  # descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],

    download_url="https://github.com/Glitchfix/flask-faas/archive/refs/tags/0.1.tar.gz",
)
