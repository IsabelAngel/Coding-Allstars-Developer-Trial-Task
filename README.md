# WebScrapping and Language detector

I read the CSV file with pandas, skipping the bad lines and using the ";" separator because of my PC configuration. after that I created a for loop, that looks into each of the URLS of the dataframe "df" that contains the CSV read. 

It uses a try-except-finally to control four exception types used from the urllib, urllib3 and ssl modules for those pages that could not be opened due to different reasons. For the pages that can be opened I used the urlopen and BeautifulSoup for the webscrapping and then with the soup.get_text() I got the text of the page, which I cleaned with the funcion, making a join with the linejumps and the repeated spaces.

In the list "IdentifiedLanguage" I saved the result of PASS or FAIL of each page and later in the line 51 I insert the column with the result, so the user can export the dataframe "df" with the asked results. 

I configured the Dockerfile with the installation of python, its modules, requirements of the different packages and main files for the deployment in RailWay but RailWay for some reason didn't trust in my github repository, so I couldn't build and deploy it.  

I created a function that with the langdetect module detects what is the language of the visited page.  

I made the commitments to Github to the latest version of this program and I couldn't reach the image and bar assesment

## 💁‍♀️ How to use

- Download the CSV and python files
- Execute the code with F5
- In the df dataframe variable you will find the results

## 📝 Notes

- To learn about how to use FastAPI with most of its features, you can visit the [FastAPI Documentation](https://fastapi.tiangolo.com/tutorial/).
- FastAPI provides automatic documentation to call and test your API directly from the browser. You can access it at `/docs` with [Swagger](https://github.com/swagger-api/swagger-ui) or at `/redoc` with [Redoc](https://github.com/Rebilly/ReDoc).
- Selenium Webdriver is an automation library designed to enable testing and scraping of websites. Learn more about [Selenium](https://www.selenium.dev/documentation/webdriver/getting_started/)
- Thank you to the original [FastAPI Template](https://github.com/railwayapp-templates/fastapi)