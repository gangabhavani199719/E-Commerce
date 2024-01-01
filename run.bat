pytest -v -s -m "sanity" --html=./Reports/bat_reports.html  testCases/ --browser chrome

rem pytest -v -s -m "sanity and regression" --html=./Reports/bat_reports.html  testCases/ --browser chrome

rem pytest -v -s -m "sanity or regression" --html=./Reports/bat_reports.html  testCases/ --browser chrome

rem pytest -v -s -m "regression" --html=./Reports/bat_reports.html  testCases/ --browser chrome