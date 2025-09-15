docker build -f api-test -t api-test .
docker run --rm api-test pytest test_main.py
docker rmi api-test
