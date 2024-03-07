bump: 
  hatch version patch
  git add src/django_clerk/__about__.py
  
  git ci -m "Bump version to $(grep __version__ src/django_clerk/__about__.py)"

build:
  hatch build

publish: bump build
  hatch publish
