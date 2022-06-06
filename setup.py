from distutils.core import setup

setup(
  # Application name:
  name="cryptojsaesdecrypt",

  # Version number (initial):
  version="0.0.3",

  # Application author details:
  author="Aleem Isiaka",
  author_email="aleemisiaka@gmail.com",

  # Packages
  packages=["aesdecrypt"],

  # Include additional files into the package
  include_package_data=True,

  # Details
  url="https://github.com/limistah/cryptojs-decrypt",

  license="MIT",
  python_requires='>=3',
  description="Decrypt cryptojs encrytped ciphers",


  # Dependent packages (distributions)
  install_requires=[
      "pycryptodome"
  ],

  classifiers=[
    # 'Development Status :: 3 - Alpha',   
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],

)