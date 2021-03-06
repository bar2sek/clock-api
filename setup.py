import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="clock_api",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "clock_api"},
    packages=setuptools.find_packages(where="clock_api"),

    install_requires=[
        "aws-cdk.core==1.93.0",
        "aws_cdk.aws_lambda==1.93.0",
        "aws_cdk.aws_s3==1.93.0",
        "aws_cdk.aws_s3_deployment==1.93.0",
        "flask",
        "requests"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
