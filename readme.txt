RUN UNIT TEST
docker-compose run app python src/tests/test_cjsonimport.py
RUN INTEGRATION TEST
docker-compose run app python src/tests/test_chartcreation.py