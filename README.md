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
    twine upload -r pypack-guide --config-file .pyazrc dist/*
    ```

#### Install package
1. Install from public pypi package.
    ```
    pip install pypack-guide
    ```
2. Install from private azure package.
    ```
    pip install pypack-guide==0.1.dev23 \
        --index-url https://<your-feed-name>:<pat-key>@pkgs.dev.azure.com/leoleung0900/_packaging/leoleung0900/pypi/simple
    # or
    pip install pypack-guide --extra-index-url=https://<your-feed-name>:<pat-key>@pkgs.dev.azure.com/leoleung0900/pypack-guide/_packaging/leoleung0900/pypi/simple/
    ```

#### Release and Publish Package
1. Create new release.
    ```
    git tag v0.0.0
    git push origin v0.0.0
    ```
2. Update the release with specific tag.
    ```
    git checkout v0.0.0
    # make changes
    git commit -am 'commit messages'
    git tag -f v0.0.0
    git push origin --delete v0.0.0
    git push origin v0.0.0
    ```


#### References
1. [Twine Documentation](https://twine.readthedocs.io/en/stable/)
2. [Get started with Python packages in Azure Artifacts](https://learn.microsoft.com/en-us/azure/devops/artifacts/quickstarts/python-packages?view=azure-devops)
3. [Automate PyPi releases with Github Actions](https://medium.com/@VersuS_/automate-pypi-releases-with-github-actions-4c5a9cfe947d)
4. [“tag already exists in the remote" error after recreating the git tag](https://stackoverflow.com/questions/19298600/tag-already-exists-in-the-remote-error-after-recreating-the-git-tag)
5. [GitHub Action Automatic Releases](https://github.com/marketplace/actions/automatic-releases#supported-parameters)
6. [How to Publish a Python Package from GitHub Actions](https://www.seanh.cc/2022/05/21/publishing-python-packages-from-github-actions/)
7. [Git tag](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-tag)
8. [Publish Python packages with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/pypi?view=azure-devops&tabs=yaml)
9. [Publish and download pipeline Artifacts](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/pipeline-artifacts?view=azure-devops&tabs=yaml)
