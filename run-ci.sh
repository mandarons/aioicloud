deleteDir() {
    if [ -d $1 ]; then rm -rf $1; fi
}
deleteFile() {
    if [ -f $1 ]; then rm -f $1; fi
}
echo "Cleaning ..."
deleteDir .pytest_cache
deleteDir allure-results
deleteDir allure-report
deleteDir htmlcov
deleteDir build
deleteDir dist
deleteDir aioicloud.egg-info
deleteFile .coverage
deleteFile coverage.xml

echo "Linting ..." &&
    ruff check --fix aioicloud/ tests/ &&
    echo "Formatting ..." &&
    ruff format aioicloud/ tests/ &&
    echo "Testing ..." &&
    pytest &&
    echo "Reporting ..." &&
    allure generate --clean &&
    echo "Building the distribution ..." &&
    python -m build &&
    echo "Done."
