from distutils.core import setup
setup(
  name = 'pylenium',
  packages = ['pylenium'],
  version = '0.01-alpha',
  license='MIT',
  description = 'Web application test automation made easy',
  author = 'Simon Kerr',
  author_email = 'jackofspaces@gmail.com',
  url = 'https://github.com/symonk/pylenium',
  download_url = 'https://github.com/symonk/pylenium/archive/v0.1.tar.gz',
  keywords = ['test, automation, selenium'],
  install_requires=[
          'selenium',
          'webdriver-manager',
          'requests',
          'urllib3'
      ],
  classifiers=[
    # Stage of the project -> Currently in VERY early alpha
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers, Test Automation Engineers, QA Engineers',
    'Topic :: Software Development :: Test Automation',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 3.7',
  ],
)
