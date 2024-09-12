# Releasing a new version

Notes from the last release process. Documentation is the first step on the road to automation. 😊

### 1. Create new build on GitHub

1. Update `json-store/__init__.py` with new version.
1. Tag the commit
	```sh
	git tag -s v3.2
	```
1. Push commit and push tag
	```sh
	git push --atomic origin main v3.2
	```

### 2. Release on GitHub

1. Download artifacts from [GitHub workflow](https://github.com/brainsik/json-store/actions/workflows/main.yml). This will create a `dist/` directory.
1. Create release from tag and write notes
1. Attach files in `/path/to/dist`
1. Publish

### 3. Release on PyPI

1. Upload artifacts
	```sh
	uvx twine upload /path/to/dist/*
	```

### 4. Cleanup

```sh
rm -rf /path/to/dist
git clean -Xd -n  # check for the unexpected
git clean -Xd -f
```
