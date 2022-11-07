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

#### Push package
1. Build the package.
    ```
    python setup.py sdist bdist_wheel
    ```
2. Upload to pypi website.
    ```
    python -m twine upload dist/*
    twine upload dist/* -u** -p**
    ```
3. Upload to azure devops.
    ```
    python -m twine upload -r leoleung0900 --config-file .pyazrc dist/*
    ```

#### Install package
1. Install from public pypi package.
    ```
    pip install pypack-guide
    ```
2. Install from private azure package.
    ```
    pip install pypack-guide2==0.1.dev23 \
        --index-url https://pkgs.dev.azure.com/leoleung0900/_packaging/leoleung0900/pypi/simple
    ```
