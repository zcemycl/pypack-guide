### pypack-guide

#### Setup
1. Git clone the repository.
    ```
    git clone https://github.com/zcemycl/pypack-guide.git
    ```
2. Add multiple remote repositories.
    ```
    git remote set-url origin --push --add https://github.com/zcemycl/pypack-guide.git
    git remote set-url origin --push --add https://leoleung0900@dev.azure.com/leoleung0900/pypack-guide/_git/pypack-guide
    git remote set-url origin --push --add https://leoleung0900@dev.azure.com/leoleung0900/dummy/_git/dummy
    ```
3. Install testing env.
    ```
    pip install -e '.[testing]'
    ```
4. Set up precommit hook.
    ```
    pip install pre-commit
    pre-commit install
    pre-commit run
    pre-commit run --all-files
    ```
5. Start contributing!!
    ```
    git add .
    git commit -m 'message'
    git push
    ```

#### Push to pypi package
1. Build the package.
    ```
    python setup.py sdist bdist_wheel
    ```
2. Upload to pypi website.
    ```
    python -m twine upload dist/*
    ```
