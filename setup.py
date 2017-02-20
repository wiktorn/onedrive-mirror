from distutils.core import setup

setup(
    name='onedrive-mirror',
    version='0.1',
    packages=['onedrivemirror'],
    url='',
    license='MIT',
    author='w',
    author_email='',
    description='',
    entry_points= {
            'console_scripts': ['onedrivemirror=onedrivemirror.__main__:main'],
    }
)
