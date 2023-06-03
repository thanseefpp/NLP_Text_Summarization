import setuptools


with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()
    
    
    
__version__ = "0.0.0"

REPO_NAME = "NLP_Text_Summarization"
AUTHOR_USER_NAME = "thanseefpp"
SRC_REPO = "NLPTextSummarizer"
AUTHOR_EMAIL = "thanseefpp@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="small project for Text summarize Using NLP",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
    