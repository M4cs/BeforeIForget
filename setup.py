from setuptools import find_packages, setup

with open('./README.md', 'r') as readme:
    long_desc = readme.read()

setup(
    name='beforeiforget',version='1.0',description='Simple Git Auto Commit Command Line Tool',
    long_description=long_desc, long_description_content_type='markdown', author='Max Bridgland',
    author_email='mabridgland@protonmail.com', url='https://github.com/M4cs/BeforeIForget',
    packages=find_packages(), maintainer_email='mabridgland@protonmail.com', license='MIT',
    install_requires=['gitpython'], zip_safe=True, entry_points={'console_scripts': 'bif = beforeiforget.__main__:main'}
)