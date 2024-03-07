bump: 
  hatch version patch
  git add src/django_clerk/__about__.py
  git ci -m "Bump version"

build:
  hatch build

publish: bump build
  hatch publish
