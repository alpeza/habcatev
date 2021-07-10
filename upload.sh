git add .
git commit -m "update"
git push
cp README.md habcatev/README.md
cd habcatev
python3 setup.py build sdist bdist_wheel
python3 setup.py install
#python3 -m twine upload --skip-existing --verbose dist/*