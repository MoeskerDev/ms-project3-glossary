                                        Glossary Growing Fields
View the live project <a href="" target="_blank">here</a>

# UX
## Project Goals
Creating a jargon glossary for three growing fields in IT: Cyber Security, Data Analytics and Web Development. The idea is that visitors can find and share definitions by reading, creating, editing and deleting terms and definitions.

The final goal is to publish a book including the collection of good definitions for all three fields and in addition, a word cloud.

----
## User Stories
1. Anonymous Visitor Goals
    - As an anonymous user, I want to easily understand the main purpose of the site and scroll through all terms.
    - As an anonymous user, I want to easily navigate through the application to find and read terms relating to a specific field.
    - As an anonymous user, I want to be able to add new terms with their respective definition to add to the collection of important terms in the field.
    - As an anonymous user, I want to be able to edit the definition of terms to improve the quality of the site.
    - As an anonymous user, I want to be able to delete certain terms to ensure updated relevancy of the collection of terms.
    - As an anonymous user, I want to be able to see which terms are most frequently searched for.

2. Registered/logged in Visitor Goals
    - As a registered user, I want to see which terms are new on the site.
    -
    -


  
----
## Design choices
### Fonts
- Materialize uses Roboto 2.0 font and I proceeded with that font since it is a clear enough font for the purpose of my app. Therefore, I also did not add a backup font, like sans serif.
### Icons
- All icons have the purpose to add or explicitly visually show the purpose of the related elements.
### Colours
In essence, the idea was to keep it clean, but still play with a few colours. The colours of the buttons are in a way also related to their function.   
- The colour scheme is based on the following colours from Materialize:
    - #e0f2f1 teal lighten-5 for the overall background colour
    - #009688 teal for the headers, collapsible headers, card-titles, forms, flash messages and some text.
    - #00897b teal darken-1 for the 'submit' buttons, as in register, login, search and edit term button
    - #bf360c deep-orange darken-4 to make the (side)navbar stand out and for the delete buttons
    - #ff9e80 deep-orange accent-1 for the edit buttons
    - #ff5722 deep-orange for the reset, cancel edit and return back to homepage buttons
    - #9e9e9e grey for the card panel on the profile page
    - #546e7a blue-grey darken-1 for the card panels on the three separate field pages
    - #e0e0e0 grey lighten-2 for the collapsible body on the homepage
    - #ffffff white text in the sidenavbar, grey and blue-grey darken-1 card panels to make links and text stand out.

### Styling
- In order to recognize the term straight away I created stretched circle shapes around the term name on all pages to create consistency. At the same time, the reason to do this was also to create some schwung in order for the website not to look too rigid or clinical. 
- For the colour of the buttons I also took into account their function as mentioned above.
- The terms are also displayed in alphabetical order on all pages to make it easier to search for a term when scrolling instead of using the search bar. 

----
## Wireframes

All wireframes can be found <a href="" target="_blank">here</a>.

----
# Features
## Existing Features
- Web application where users can store and easily access definitions for terms regarding three different growing fields in IT.
- Backend code and frontend forms to allow logged-in users to add new definitions, edit them and delete them.
- Backend code and frontend functionality for all users to search for terms.
- A dropdown list and accordion element.
- Customized 404 error page.
- Interactive elements
- Responsive for the following screen sizes:
    - 320x568
    - 360x640
    - 375x667
    - 375x812
    - 411x731
    - 411x823
    - 414x736
    - 540x720
    - 768x1024
    - 1024x1366
    - 1366x768

----
## Left to implement
- Also fully responsive for 280x768 screen size
- More efficient responsive css coding
- Mongo DB word cloud
- Flask logging 

----
# Technologies Used
## Languages 
- <a href="https://en.wikipedia.org/wiki/HTML5" target="_blank"> HTML5 </a>
- <a href="https://en.wikipedia.org/wiki/CSS" target="_blank"> CSS3 </a>
- <a href="https://en.wikipedia.org/wiki/JavaScript" target="_blank"> JavaScript </a>
- <a href="https://en.wikipedia.org/wiki/Python_(programming_language)" target="_blank"> Python </a>
## External libraries and frameworks
- <a href="https://en.wikipedia.org/wiki/Flask_(web_framework)" target="_blank"> Flask: </a>
    - Mini Python web framework used to make creating web applications easier. It uses the Jinja templating language.
- <a href="https://www.mongodb.com/" target="_blank"> MongoDB: </a>
    - Used to create and store my database.
- <a href="https://materializecss.com/" target="_blank"> Materialize 1.0.0: </a>
    - Instead of Bootstrap, I used the frontend framework Materialize 1.0.0 to experience working with another frontend framework.
- <a href="https://fontawesome.com/" target="_blank"> Font Awesome: </a>
    - To import icons used in the application instead of the icons of Materialize 1.0.0.
- <a href="https://jquery.com/" target="_blank"> jQuery:  </a>
    - To support features and functions of Materialize.
- <a href="https://git-scm.com/" target="_blank"> Git: </a>
    - Used for version control by utilizing Gitpod terminal to commit to Git and Push to GitHub.
- <a href="https://github.com/" target="_blank"> GitHub: </a>
    - To document and store the development process.
- <a href="https://heroku.com/" target="_blank"> Heroku: </a>
    - Used to deploy this full stack web application to a Cloud platform.
- <a href="https://balsamiq.com/" target="_blank"> Balsamiq:</a> 
    - During the design process, the wireframes were created by Balsamiq.
    
----
# Testing
## Validators
- [W3C Markup Validator](http://validator.w3.org/)
    - One warning left; section lacks heading. This is about the flash messages section.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - No errors found
- [JSHint Validator](https://jshint.com/) - [Results]()
    - Left with two undefined variables, $ and M, where $ is part of the jQuery code and M is of Materialize which also relies on jQuery. 
- Python code was checked via the command line by typing: ```pylint app.py```
    - Left with one unused-import error, W0611 for import env, which is okay. I am using it, pylint just cannot see that. 
## Testing User Stories
## Further testing
## Known Bugs
## Fixed Bugs
- Checking the HTML code from my templates gave many errors and warnings. Therefore I moved to the website, and with a rightclick selected "View page source". I copied that code and pasted it in the Markup validator. One warning came up; section lacks heading. 
    - My flash messages were inside a section element and placing an empty header was not working since that created the error of an empty header. So I replaced the section element with a div element. First testing my flash messages to see if it had any effect. They were still working so I checked my pages again and this time no errors or warnings at all!
- 280x653: still issues with line height header, search field, their buttons and sidenav logo.
----
# Deployment

## Deploy app to Heroku
To deploy Glossary Grow Fields to Heroku, take the following steps:

1. Create a requirements.txt file using the terminal command ```pip freeze > requirements.txt``` 
2. Create a Procfile with the terminal command ```echo web: python app.py > Procfile```
3. git add and git commit the new requirements and Procfile and then git push the project to GitHub.
4. Create a new app on the [Heroku website](https://signup.heroku.com/login) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.
5. Inside your newly created application, in the heroku dashboard, click on "Deploy" > "Deployment method" and select GitHub.
6. Confirm the link between the heroku app and the correct GitHub repository.
7. Now, in the heroku dashboard of your application, click on "Settings" > "Reveal Config Vars".
8. Set the following config vars:

Key|Value
---|-----
Debug|False
IP|0.0.0.0
MONGO_URI|mongodb+srv://<user_name>:<password>@<cluster_name>.vb0d4.mongodb.net/<database_name>?retryWrites=true&w=majority
PORT|5000
SECRET_KEY|<your_secret_key>

- To get your MONGO_URI read the [MongoDB Atlas documentation](https://docs.atlas.mongodb.com/).
9. Click "Deploy" in the heroku dashboard.
10. In the section "Manual Deploy" make sure the main branch is selected and then click on "Deploy Branch".
11. The site is now successfully deployed.
12. Click on "View" to view the app in your browser.

## Run this project locally
To clone this project into Gidpod you have to:

1. Have a GitHub account: create one [here](https://github.com/) if needed.
2. Use a Chrome Browser.
According to the steps below:
1. Install the [Gitpod Browser Extention for Chrome](https://www.gitpod.io/docs/browser-extension/).
2. After installing it, restart the browser.
3. Log into [Gitpod](https://www.gitpod.io/) with your Gitpod account.
4. Go to your project GitHub repository in GitHub under the tab "Repositories".
5. Click the green "Gitpod" button in the top right corner of the repository.
6. This will trigger a new Gitpod workspace, created from the code in GitHub, where you can work locally.

To work on the project code within a local IDE (Pycharm,VSCode, etc.):

1. Go to the [project GitHub repository](https://github.com/MoeskerDev/ms-project3-glossary).
2. Click on the "Code" button next to the green "Gitpod" button.
3. In the Clone section, make sure the HTTPS is selected, then copy the clone url of the repository.
4. Open the terminal in your local IDE.
5. Change the current working directory to the location where you want the cloned directory to be created.
6. Then, type ```git clone``` and paste the url that you copied in step 3 behind it:

```
git clone https://github.com/USERNAME/REPOSITORY
```

7. Press Enter for your local clone to be created.

- For further information about cloning a repository from GitHub, read [this](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository).
----
# Credits
## Code
1. For setting up the project I watched and copied most of the start-up of the mini-project videos of CI.
2. The custom validation for the dropdown in the add term form came from the mini-project and I copied it all.
3. 
## Acknowledgements
1. The terms that were inserted are from the following three pages:
- <a href="https://careerfoundry.com/en/blog/web-development/50-web-development-buzzwords-that-all-new-programmers-should-learn/" target="_blank">Web Development</a>
- <a href="https://devsdata.com/big-data-terms-every-manager-should-know/" target="_blank">Data Analytics</a>
- <a href="https://www.globalknowledge.com/us-en/topics/cybersecurity/glossary-of-terms/#gref" target="_blank">Cyber Security</a>
2. I had a look at the <a href="https://github.com/Code-Institute-Solutions/SampleREADME" target="_blank">sample READme</a> of CI.
3. A big thanks to tutor support, in particular Igor and Jo, who took the time to help me when needed. They both were very good at explaining and teaching more than the question asked for. Also thanks to my mentor for pushing me to learn more.

