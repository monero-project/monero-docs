# Monero Docs

This repository contains the source files to Monero Community documentation hosted at [docs.getmonero.org](https://docs.getmonero.org)

- [About](#about)
- [Contributing](#contributing)
- [Local Deployment](#run-the-documentation-server-locally)
- [License](#license)

## About

Monero Docs intends to be a Knowledge Base and User Guide for interacting with Monero.

## Contributing

Contributions are both encouraged and greatly appreciated.

To contribute content, fork this repo and make a pull request to the **`master`** branch including your changes.

1. On GitHub, fork the [monero-docs](https://github.com/monero-project/monero-docs) repo
2. Clone your newly created repo. (Note: replace `your-username` with your GitHub username)

via ssh:
```bash
git clone git@github.com:your-username/monero-docs
```
via https:
```bash
git clone https://github.com/your-username/monero-docs
```
3. Navigate to the repo and create a new topic branch
```bash
cd monero-docs
git checkout -b foobar
```
4. After making modifications, commit and push your changes to your topic branch
5. Open a PR against the monero-docs **`master`** branch

# Run the documentation server locally

- The build process for mkdocs utilizes Python
- It is recommended to install python pip dependencies inside of a Virtual Environment [(venv)](https://squidfunk.github.io/mkdocs-material/guides/creating-a-reproduction/#environment)

Note: You may need to first install `python3-venv` or the equivalent for your distribution
1. Navigate to your `monero-docs` repo
2. Create the python virtual environment
```bash
python3 -m venv .monero-docs-venv
source .monero-docs-venv/bin/activate
```
3. Install mkdocs dependencies to the venv
```bash
pip install --require-hashes -r requirements.txt
```
4. Run the documentation server locally
```bash
python3 -m mkdocs serve
```
5. View your changes at [http://localhost:8000](http://localhost:8000)

## License

The documentation is provided under the [MIT License](LICENSE).
