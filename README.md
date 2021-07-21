                                        Glossary Growing Fields
View the live project <a href="" target="_blank">here</a>

![Mockup home](https://github.com/MoeskerDev/ms-project3-glossary/blob/main/static/css/images/home_mockup.png)
![Mockup field](https://github.com/MoeskerDev/ms-project3-glossary/blob/main/static/css/images/field_mockup.png)
![Mockup error](https://github.com/MoeskerDev/ms-project3-glossary/blob/main/static/css/images/error_mockup.png)
# UX
## Project Goals
Creating an open jargon glossary for three growing fields in IT: Cyber Security, Data Analytics and Web Development. The idea is that visitors can find and share definitions by reading, creating, editing and deleting terms and definitions. The target audience is anyone who is interested, but more focused will be for newbies in these fields and even the more experienced since they can share there knowdledge with the newbies. At the same time, newbies can add new terms as well while they learn and come across certain terms often.

The final goal is to publish a book including the collection of good definitions for all three fields and in addition, a word cloud.

----
## User Stories
1. Anonymous Visitor Goals
    - As an anonymous user, I want to easily understand the main purpose of the site and to scroll through all terms to get a quick overview.
    - As an anonymous user, I want to easily navigate through the application to find and read terms relating to a specific field to have a focused elaborate search.
    - As an anonymous user, I want to be able to quickly search for a term to see if that term exists on this site and to learn the meaning of it.
    - As an anonymous user, I want to receive feedback that a term I searched for does not exist on this site and then to easily return to the homepage with all terms to attain good user experience.
    - As an anonymous user, After I searched for a term that exists, I want to easily see all results so that I can also scroll through the terms available to learn even more. 
    - As an anonymous user, I want to easily navigate back to the homepage if I end up at the 404 error page to not get lost.

2. Registered/logged in Visitor Goals
    - As a registered/logged in user, I want to be able to add new terms with their respective definition to add to the collection of important terms in the field.
    - As a registered/logged in user, I want to get a confirmation message before editing or deleting one of my terms on one of the field pages to prevent accidental deletion. 
    - As a registered/logged in user, I want to be able to easily edit my previous added definition of terms to improve the quality of the site.
    - As a registered/logged in user, I want to be able to easily delete certain terms to ensure updated relevancy of the collection of terms.
    - As a registered/logged in user, I want to have my own page where I can see an overview of all the terms that I added in alphabetical order.
    - As a registered/logged in user, I want to be able to cancel the editing of one of my terms before I saved it to not (accidently) lose a good part of the definition.
 
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
- Also fully responsive for 280x768 screen size; somehow my css for width 280 is not being picked up..
- More efficient responsive css coding
- Mongo DB word cloud which shows terms most viewed/searched for
- Flask logging 
- New terms to show as new for a certain time
- Voting regarding quality of definition
- Create even better custom error pages

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
    - No errors or warnings found.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - No error found.
- [JSHint Validator](https://jshint.com/)
    - Left with two undefined variables, $ and M, where $ is part of the jQuery code and M is of Materialize which also relies on jQuery. 
- Python code was checked via the command line by typing: ```pylint app.py``` and via the online [Python validator](http://pep8online.com/)
    - Pylint left me with one unused-import error, W0611 for import env, which is okay. I am using it, pylint just cannot see that. 
    - The PEP8 requirements results were: all right.
## Testing User Stories
The most common path through the website for an anonymous user will be the Homepage and then search for a particular term via the search bar or scrolling down. The separate field pages were added to have a collection of terms in a particular field attainable using only one click, since the index for the search bar is based on the term name and term definition. Another frequent path would be from Homepage to the Register page.

1. As an anonymous user:
* I want to easily understand the main purpose of the site and to scroll through all terms to get a quick overview.

    - When I land on any page I will see the logo which clearly mentions glossary of certain fields. The navbar contains three particular fields showing the focus fields of the site. 
    - The big header on the homepage show terms are the main focus of this site.
    - On the homepage I am able to scroll quickly down to get an overview of all the terms and if wanted I can check the definition as well.

* I want to easily navigate through the application to find and read terms relating to a specific field to have a focused elaborate search.

    - No matter what page the user lands on, they can easily find and use the navigation bar.
    - To easily get an overview of all terms of a specific field, the field specific page is just one click away via the navbar. 

* I want to be able to quickly search for a term to see if that term exists on this site to learn the meaning of it.

    - On the homepage, at the top, a search bar is presented for the user to search for any term they want.
    - On the homepage, the user can also scroll through the existing terms, ordered alphabetically, to see if a particular term is there or perhaps find a new term to learn even more.

* I want to receive feedback that a term I searched for does not exist on this site and then to easily return to the homepage with all terms to attain good user experience.

    - A flash message appears with the text "No Results Found" when a term does not exist in the name or in the definition.
    - To return to the homepage with all terms displaying, you only have to click the reset button to reset your search. 

* After I searched for a term that exists, I want to easily see all results so that I can also scroll through the terms available to learn even more. 

    - When I search for a term, all terms or definitions that contain that term are displayed as the search result.
    - The terms are collapsible to have a quick overview of all terms, and with one click you can read the definition as well to learn more than only the specific term I searched for. 

* I want to easily navigate back to the homepage if I end up at the 404 error page to not get lost.

    - Once I am on the custom error page, there is a button below the error message which says "Return to homepage" and redirects the user back to the homepage with all terms. 
    - Another option would be to use the navbar, either click home or glossary frow fields.

The most common path for a registered user is from the homepage to the login page which leads to the profile page (from now on logged in user). From there you can either delete a term which then takes you back to the homepage or you edit a term which leads to the edit term page. By cancelling the edit term you go back to the homepage. By editing a term, you stay on the edit term page to see your changes. Another frequent path from the profile page could be the add term page. Once you have added a term you are redirected to the homepage with all terms, including your newly added term. 

2. As a registered/logged in user:
* I want to be able to add new terms with their respective definition to add to the collection of important terms in the field.

    - Starting on the profile page, one click on the add term link in the navbar and you are guided to the add term form 
    - Via the form you can choose one of the fields via dropdown menu and type the term name and definition.
    - The add term button adds your new term and definition to the database and redirects you to the homepage where the new term can be found, as well as on your own profile page.

* I want to get a confirmation message before editing or deleting one of my terms on one of the field pages to prevent accidental deletion. 

    - The edit and delete button on all pages request the user for a confirmation if they really want to edit or delete the term.

* I want to be able to easily edit my previous added definition of terms to improve the quality of the site.

    - No matter which page you can find your term; homepage, profile page or one of the field pages, you are able to edit it with the edit button.
    - Confirm that you want to edit your term and you are redirected to a filled out edit term form.
    - Change what you want to change and click the edit term button which creates a feedback message and your changes are changed. 

* I want to be able to easily delete certain terms to ensure updated relevancy of the collection of terms.

    - Everywhere you term is shown, you are able to click the delete button.
    - Confirm you really want to delete this term and the term with definition is removed, redirecting you to the homepage with all current terms.

* I want to have my own page where I can see an overview of all the terms that I added in alphabetical order to see my contribution to the site.

    - Once you are registered you are redirected to the profile page with a message saying that you have not added any terms yet.
    - Once you are logged in and have added terms before, you are also redirected to you profile page which lists, in alphabetical order the collapsible terms that you have created and added to the site.

* I want to be able to cancel the editing of one of my terms before I saved it to not (accidently) lose a good part of the definition.

    - After clicking on the edit button of one of the terms you created, confirmed your choice and are on the edit term form, you can click on the cancel edit button to undo your changes.
    - It leads you back to the homepage where you can still decide to edit the term by searching for it there or leave it and perhaps edit it at a later moment. 

## Further testing
- The website was tested on Google Chrome, Microsoft Edge and Mozilla Firefox. 
- The website was viewed on several devices, Laptop, Moto G4, Galaxy S5, Pixel 2, Pixel 2 XL, Iphone 5/SE, Iphone 6/7/8, Iphone 6/7/8 Plus, Iphone x, Ipad, Ipad Pro, Surface Duo and Galaxy Fold. 
- The Lighthouse report for mobile can be found [here]().
- The Lighthouse report for desktop can be found [here]().
## Known Bugs
- 280x653: still issues with line height header, search field, their buttons and sidenav logo.
- edit term page buttons are not positioned side by side correctly in Ipad and some mobile views.
## Fixed Bugs
- Issue: in mobile view my register and login button were not placed in the center of the form.
    - Fix: first I tried to fix this with additional css, but this was not successful. Perhaps due to Materialize. However, removing the offset-m2 class in my html and converting it to a percentage in css worked just fine. 
- Issue: I created my favicon and added all files that are mentioned on the website. This included the site.webmanifest:1 file. In the console I had a syntax and 404 error relating to site.webmanifest:1.
    - Fix: First I checked line 1 of the syntax, since that error was mentioned. I had no idea what was not correct, so I first deleted the file to add it again later. It turned out that my favicon was still there and the error was gone so I left it out. 
- Issue: checking JavaScript with the JSHint gave an unused variable, var instance =. First I commented out the whole code snippet, but then my collapsible items would not work anymore. After that it turned out that just removing the part of "var instance =" already did the trick.
- Issue: the pylint error W0613 unused-argument 'e'.
    - Fix: it turned out you can just add print(e) inside the function with parameter 'e' to get rid of the error. 
- Issue: my pylint check gave me multiple times the error E0102; function-redefined, function already defined. A function named terms and several variables called terms as well. Also, I imported login_required from Flask and created a function with the same name according to documentation.
    1. Fix: first I tried to change the name of the function, but that was more tricky, since it is also the route() decorator. Instead I decided to adapt the names of the variables. That worked just fine. 
    2. Fix: it turned out that, after commenting out the code of the function and checking on the website if the login_required would still work, it did not. Then, commenting out the code of the import and checking on the website, there was no issue at all. Interesting conclusing was that I could delete my import of login_required and the error was gone.
- Issue: a CO103 error; invalid-name, does not conform to snake_case naming about my e parameter in a function came up with the pylint check.
    - Fix: first I checked to add an underscore before e; _e and that worked but I did not really like it, so I checked online. I found out that you can add a [.pylintrc file](https://stackoverflow.com/questions/22448731/how-do-i-create-a-pylintrc-file) and add e to the list of [good-names](https://stackoverflow.com/questions/14233867/pylint-ignore-specific-names). This is what I did and it worked!
- Issue: after checking my python code, the error CO114; missing-module-docstring came up.
    - Fix: I tried to add a docstring below the line, like with a function, however this created more errors. So I checked [online](https://stackoverflow.com/questions/65949325/how-do-you-fix-missing-module-docstringpylintmissing-module-docstring) and found that you have to create one above the module. This worked.
- Issue: checking the HTML code from my templates gave many errors and warnings. Therefore I moved to the website, and with a rightclick selected "View page source". I copied that code and pasted it in the Markup validator. One warning came up; "section lacks heading". 
    - Fix: my flash messages were inside a section element and placing an empty header was not working since that created the error of an empty header. So I replaced the section element with a div element. First testing my flash messages to see if it had any effect. They were still working so I checked my pages again and this time no errors or warnings at all!

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
2. The custom validation Javascript for the dropdown in the add term form came from the mini-project and I copied it all.
3. The other Javascript/jQuery code came from the [Materialize](https://materializecss.com/collapsible.html) website.
4. The login_required function and everyting related, like import and using it on functions, came from [here](https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator).
5. As part of the refactoring three functions into one, my mentor taught me something new with changing the url as well. 
## Content
1. The terms that were inserted came from the following three pages:
- <a href="https://careerfoundry.com/en/blog/web-development/50-web-development-buzzwords-that-all-new-programmers-should-learn/" target="_blank">Web Development</a>
- <a href="https://devsdata.com/big-data-terms-every-manager-should-know/" target="_blank">Data Analytics</a>
- <a href="https://www.globalknowledge.com/us-en/topics/cybersecurity/glossary-of-terms/#gref" target="_blank">Cyber Security</a>
2. I had a look at the <a href="https://github.com/Code-Institute-Solutions/SampleREADME" target="_blank">sample READme</a> of CI.
3. In order to create the mockups I used this [website](http://ami.responsivedesign.is).
4. To create images from screenshot I used [Paste Pics](https://paste.pics/).
## Acknowledgements
- A big thanks to tutor support, in particular Igor and Jo, who took the time to help me when needed. They both were very good at explaining and teaching more than the question asked for.
- And thanks to my mentor for pushing me to learn more!

