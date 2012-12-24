from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='loremipsum.workflow',
      version=version,
      description='Prodotto di esempi di worfklow e sicurezza per libro '
                  '"Plone: worfklow e sicurezza"',
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        ],
      keywords='plone workflow security example',
      author='keul',
      author_email='luca@keul.it',
      url='https://github.com/keul/loremipsum.workflow',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['loremipsum'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
