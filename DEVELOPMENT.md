# Development

## Releasing a new version

Documentation is the first step on the road to automation. 😊

Follow these steps in order.

### Create new build on GitHub

1. Update `json-store/__init__.py` with new version.
1. Tag the commit

	```sh
	git tag -s v3.2
	```

1. Push commit and push tag

	```sh
	git push --atomic origin main v3.2
	```

### Release on GitHub

1. Download artifacts from GitHub: `rm -rf dist && ./download-artifact.sh <tag>`
This will create a `dist/` directory.
1. Create release from tag and write notes
1. Attach files in `/path/to/dist`
1. Publish

### Release on PyPI

1. Upload artifacts

	```sh
	uvx twine upload dist/*
	```

### Cleanup

```sh
rm -rf /path/to/dist
git clean -Xd -n  # check for the unexpected
git clean -Xd -f
```
