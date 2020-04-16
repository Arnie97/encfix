from setuptools import setup

setup(
    name='encfix',
    description='Guess and fix character encodings of garbled filenames',
    url='https://github.com/Arnie97/encfix',
    author='Arnie97',
    author_email='arnie97@gmail.com',
    license='GPLv3+',
    py_modules=['encfix'],
    entry_points=dict(console_scripts=['encfix = encfix:main']),
    python_requires='>=3.0',
    install_requires=['chardet'],
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
    ],
)
