<p><h1>Milestone 3 for Code Institute - A database web application.</h1><p>
<p><strong>MiDev Glossary</strong> app offers users such as professionals like Project Managers or Product Owners the possibility to understand their development teams better.</p>
<p>You can find links to the application and github repository below:
<p>The application <a href="https://tmfmdb.herokuapp.com/">live here.</a></p>
<p>The Github link <a href="https://github.com/VictoriaBC/miniprojectpy/">here.</a></p>

<h2>UX</h2>
Very often abbreviations are used within development teams and this app helps Managers to gather what they hear and also use this app as an internal dictionary. Developers, Designers, Marketing specialists also have a chance to help the team and create a better way of working. Users can add/edit words, also add/edit categories, they can search words and navigate according to the alphabet.

<h2>User Stories</h2>
As a new User I would like to:
<li>be able to understand how to navigate in the application.</li>
<li>be able to find/search meaning of words and abbreviations.</li>
<li>be able to sort fast words with alphabet.</li>
<li>be able to create and edit words.</li>
<li>be able to create and edir categories.</li>

<h2>Wireframes</h2>
<p>Wireframes are attached in my github repository as <a href="https://github.com/VictoriaBC/miniprojectpy/blob/master/MiDev_Glossary_Victoria.pdf">MiDev_Glossary_Victoria.pdf</a></p> 
<p>The document contains the app structure, mobile and desktop wireframes.</p>

<h2>Features</h2>
<h3>Layout</h3>
<p>This is a multi-page layout designed as minimalistic and functional as possible, also responsive and pleasing for the user. The home page displays short information about this app, search input, alphabetical navigation and accordions containing words in the clossary with their description. Each accordion can be deleted and edited.</p>

<h3>Colors</h3>
<p>Colors are taken from <a href="https://materializecss.com/color.html">Sass in materialize</a> to make the it easier to change without risking to have multiple colors of the same tone.</p>
<li>Background color: #f5f5f5 grey lighten-4</li>
<li>Primary button color: #004d40 teal darken-4</li>
<li>Secondary button color: #26a69a teal lighten-1</li>
<li>Header and Footer color: #004d40 teal darken-4</li>
<img src="https://github.com/VictoriaBC/miniprojectpy/blob/master/tmfmdb/static/img/Screen%20Shot%202020-07-09%20at%2023.01.38.png">

<h3>Buttons</h3>
<p>Buttons in this application are from component library <a href="https://materializecss.com/">Materialize</a>.</p>

<h3>Font</h3>
<p>One font set is used from google fonts, called "Roboto". It gives a modern appeal, simplicity and most important easy to read.</p>

<h3>Existing Features</h3>
<p>Header and footer - The header contains a linked to home logo, menus: Home, New Word, Manage Catergory. The footer below repeats the name of the app and the author. Both the Header and Footer are components from <a href="https://materializecss.com/">Materialize</a>.</p>
<p>Button "Edit" - This button is found in the accordion with hex color: #004d40 teal darken-4.</p>
<p>Button "Delete/Del" - This button is found in the accordion with hex color: #26a69a teal lighten-1.</p>
<p>Buttons Add Category and Add Word - These buttons are found Add Word and Manage Category pages. Button colors: #004d40 teal darken-4.</p>
<p>Form - The forms are taken from materialize and contain input fields and category dropdown. Forms are found at Add Word page and Manage Category page.</p>

<h3>Features Left to Implement</h3>
<li>Authentication</li>
<li>Login and Register</li>
<li>Images</li>

<h3>Main Technologies Used</h3>
For this project I used Python, HTML, CSS, Sass and Javascript programming languages.

<h3>Tools used</h3>
<li>Used Heroku for uploading the app and Mongo DB for keeping database.</li>
<li>PIP3 for installation of tools needed in this project.</li>
<li>Github to handle version control</li>
<li>Gitpod to code</li>

<h3>Other technologies and libraries used:</h3>
<li>Jinja to simplify data displaying from the backend.</li>
<li>PyMongo - containing tools for working with MongoDB.</li>
<li>Materialize for components and to make the website responsive easily. https://materializecss.com/
<li>Fontawesome to provide icons from it's library. https://fontawesome.com/</li>
<li>Google Fonts to easily use simple and recognizable fonts on the internet https://fonts.google.com/.</li>

<h3>Testing</h3>
<li>User Testing - people were are asked to visit the app and test. REason is to collect feedback and improve the app.</li>
<li>Tested browser lists: Google Chrome, Chrome Lighthouse for audit of website, Safari.</li>

<h3>HTML, CSS and JS code</h3>
<li>W3C HTML Validator.</li>
<li>W3C CSS Validator.</li>
<li>Pep8online to test app.py</li>

<h3>Meeting the needs of the user stories (described  earlier in the UX section of this README file)</h3>
<li>
<p>As a new User I want to be able to understand how to navigate around the web application.</p>
<p>On landing page, the user is welcomed with a welcome text and information about this app, imediately followed below by search, alphabet navigation and common glossary.</p> 
<p>Navigation in the header at the top of the page. The Logo, when clicked, redirects the user to Landing page</p>
</li>

<li>
<p>As a user I would like to be able to add words, edit them and also add, edit categories.</p>
</li>

<li>
<p>As a user I would like this application to be responsive.</p>
</li>

<h3>Deployment</h3>
<p>heroku - git - PIP - Python 3 - Flask - A MongoDB Atlas account</p>

<h3></h3>Instructions for Installation</h3>

<p>Make your folders and navigate to it on the terminal. Enter the following in the terminal:</p>
<li>$ git clone https://github.com/haydal810/Milestone-Project-3.git</li>
<li>$ pip3 install </li>
$ pip install -r requirements.txt
To run the app locally:
$ python -m flask run
Heroku Deployment
The code was also pushed from git to heroku for live deployment: https://www.heroku.com/

To Deploy using Heroku Git, use git in the command line:

Install the Heroku CLI. If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
$ heroku login
Clone the repository. Use Git to clone the projects source code to your local machine.
$ heroku git:clone -a kerry-rivers-ms3
$ cd kerry-rivers-ms3
create your requirements.txt file
$ pip freeze --local > requirements.txt

create your procfile file
$ echo web: python app.py > Procfile

Deploy your changes. Make some changes to the code you just cloned and deploy them to Heroku using Git.
$ git add .
$ git commit -am "commit message"
$ git push heroku master
In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

Set the following config vars:

IP : 0.0.0.0
PORT: 5000
MONGO_URI: mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
To get your MONGO_URI read the MongoDB Atlas documentation: HERE

In the heroku dashboard, click on the button "Open App".
The app should open in a new tab.

Credits
Content
All text in this project was written by the developer.

Media
The background image was sourced from https://www.pexels.com/
Acknowledgements
I'd like to thank my mentor, Antonija Šimić, for her useful and constructive feedback throughout the Milestone Project
The content of this website is for educational purposes only.
Thank you.
