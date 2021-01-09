# Selenium Walmart Shopping Bot

This is a very simple shopping bot written in Selenium binding. It aims to speed up click through on websites dramatically and might help you get that new release! 

##### Set-up

Execute the following command in your IDE terminal after pulling the files:

`python -m venv tutorial-env`

Then execute the two statements in your command, omit this step if you use PyCharm:

`Set-ExecutionPolicy RemoteSigned` 

`tutorial-env\Scripts\activate.bat` 

Your virtual environment should be up and running.

Now install selenium in your virtual environment:

`pip install selenium`

##### Usage

Enter your Walmart account information in the correct input area indicated in the code. Run the setup.py to save your login cookie as stated in comment in the code. Now the program will automatically dumps the cookie when you run the main program. Depending on which product you are buying you will have to grab the class name of the buttons of your specific page and switch that with what's in the program, when you run main it should click through to the purchase page fast. 

It's possible to adapt the program to other shopping websites by changing the url and adapting the click through steps as per the design of the website.

`python3 <name>.py`

##### Motivations

- I was originally inspired to make a shopping bot from trying to help my friend secure a PS5 and XBox on release, and afterwards finding out that it was extremely difficult for genuine customers to secure one because of all the scalpers. I wanted to make a shopping bot that would be fast enough to compete with the scalper bot but also only allows the user to buy the allotted quantity of the limited good.
- Before that I had been interested in automations and thought it was a good opportunity to get some hands-on experience building an automated program. 
- Eventually I hope to figure out the tools scalpers use to their advantage and invent protocols to counteract their attempts. 

##### Limitations

- ReCAPTCHA! After all they ARE designed to counter bots. It significantly slows down the speed and discourages true automation with primitive bots.
- Due to the need to identify the specific visual elements on the webpage, the code is highly specific to the site and will require major revamp adapting to different sites.
- Dumping cookie does not work due to security design on the website. While testing my app I found that the Walmart site would ask me to log in again even though when my program start up the site it appears that I am logged in. 

##### Next-Steps

- I learned from one of my mentor to configure the user agent with selenium, this could reduce the  chance of ReCAPTCHA popping up 
- Pupeteer and Playwright offered more powerful functionalities and moving the code base there could be a next step 
- To program it so that it recognizes which buttons to press for log in and purchase given the url 



