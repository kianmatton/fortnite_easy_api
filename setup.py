from distutils.core import setup
setup(
  name = 'fortnite-easy-api',
  packages = ['fortnite-easy-api'],
  version = '0.1',
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = "A simple python library for developers and beginners to easily use difficult api's"
  author = 'OsOmE1',
  author_email = 'gamerosome@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/OsOmE1/fortnite-easy-api',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['python', 'fortnite', 'api'],   # Keywords that define your package best
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 4 - Beta', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)