<p><h1>Milestone 3 for Code Institute - A database web application.</h1><p>
<p><strong>MiDev Glossary</strong> app offers users/professionals like Project Managers or Product Owners the possibility to understand their development teams better by having a glossary of tech terms used within the project. It is important to understand each other in order to form a well-driven environment. Apart from tech teams there is the Marketing team which also benefits from this app.</p>
<p>You can find links to the application and github repository below:
<p>The application <a href="https://midevglossary.herokuapp.com/">live here.</a></p>
<p>The Github link <a href="https://github.com/VictoriaBC/midevglossary">here.</a></p>

<h2>UX</h2>
<p>Very often abbreviations are used within development teams and this app helps Managers to gather what they hear and also use this app as an internal dictionary. Developers, Designers, Marketing specialists also have a chance to help the team and create a better way of working. Users can add/edit words, also add/edit categories, they can search words and navigate according to the alphabet.</p>
<img src="https://github.com/VictoriaBC/midevglossary/blob/329e67974184560730ae8bc10cba485a8801d726/static/img/device_image.png">

<h2>Design process</h2>
<p>Discover (research focus groups and existing apps, platforms, code) > Define (define issues, brainstorm) > Deliver (create structure, user scenarios and user flow) > Develop (wireframes and prototype, tools: html, css, js, python, scss, mongodb and heroku, test: usability and collect feedback then update)</p>
<p><strong>Discover:</strong>researched the right focus group which are Project Managers and Product Owners, researched and gathered other glossary apps, that I later got inspired from. Decided which platform to code the app on and where to deploy, the database, which code language I should use.
Languages and platform - html, css, scss, javascript, python, gitpod. Database - MongoDB, Deployment platform - Heroku.</p>
<p><strong>Define:</strong>this process involve defining what the issues for our users and how we solve them, what is expected from an MVP (Minimum Viable Product) and what is expected from Product Owners and Project Managers who do not always have a full technical background.
This app offers them a place where they can search words they hear from development teams and also store words with a description to save for themselves or share with others. It important that everyone speaks the same language and understand eachother in a project.
Users search words differently, which is why both an input search field and alphabet navigation are good options.</p>
<p><strong>Deliver:</strong>before developing the app it is important to undertand it's structure and user flow. After I finished with the structure and user flow I continued with creating sketches, wireframes and even Hi-fidelity prototype. I collected feedback and iterated my design numerous times before I started developing. I used Adobe XD to create the wireframe and prototype.</p>
<p><strong>Develop:</strong>minor changes were performed in the UI (User Interface) before on prototypes and after being coded. I made sure I had the right structure and followed the UX/UI deliverables as close as possible. During this process I used html, css, js, python, scss, mongodb and heroku. I tested the on responsiveness and also with users. The code itself was tested on W3C HTML Validator, 
W3C CSS Validator, Pep8online to test app.py, ami.responsivedesign.is and Inspect to test for responsiveness.</p>
<p><strong>Note that the Design process is known as <a href="https://www.designcouncil.org.uk/news-opinion/what-framework-innovation-design-councils-evolved-double-diamond">Double Diamond</a>, normally used a framework within UX Designers. This project was not done by the book due to lack of time, but much of the methods in the process were included.</strong></p>
<p>To understand better how users interact with the app it is recommended to do evaluation after the app is launched in production. Gathering feedback surveys, contacting users for an interview and using tools like Hotjar, Google analytics, Google Tag Manager may be very useful.</p>
<img src="https://github.com/VictoriaBC/midevglossary/blob/1f0f3095138a1f555409748fefbf5c09056e1692/static/img/Screen%20Shot%202020-07-16%20at%2019.30.25.png"><p><i>Image above: Protoype environment in collaboration and prototyping tool <a href="https://www.adobe.com/se/products/xd.html">Adobe XD</a>.</i></p>

<p>Final thoughts for front-end: Creating a functional design system according to Atomic Design may be handful in the future.</p>

<h2>User Stories</h2>
<p>As a new User I would like to:</p>
<li>be able to understand how to navigate in the application. In order to that there is a main menu in the header suited for both mobile and desktop.</li>
<li>be able to find/search meaning of words and abbreviations. A search component has been implemented and search according to a letter, the results appear as an accordion and if there is not found the user sees the information and can go back to previous page with a created Back link.</li>
<li>be able to sort fast words with alphabet. Another way of searching is through the alphabet navigation which shows all letters that start with the letter and in alphabetical order. If the there is no word under the letter, the user sees a message and has a link to go back to landing page.</li>
<li>be able to see words in alphabetical order. All words are presented in alphabetical order.</li>
<li>be able to be warned about deleting a word or category if I clicked the button by mistake. Each word and category can be deleted, the user is asked if they are sure.</li>
<li>be able to create and edit words. User can create words through the menu and edit through the accordion. A user cannot submit a word if input fields are not filled, the user gets feedback if they have missed.  Pagination and Feedback that a word has been created should be implemented in the next phase.</li>
<li>be able to create and edit categories. User can create categories through the menu and edit under Manage categories. A user cannot submit a category if input fields are not filled, the user gets feedback if they have missed it. Each category can be deleted, the user is asked if they are sure. Pagination and Feedback that a category has been created should be implemented in the next phase.</li>

<h2>Wireframes</h2>
<p>Wireframes are attached in my github repository as <a href="https://github.com/VictoriaBC/midevglossary/blob/10ee1f98f087c61390dbec702b31081d0c8fc779/MiDev_Glossary_Victoria.pdf">MiDev_Glossary_Victoria.pdf</a></p> 
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
<img src="https://github.com/VictoriaBC/midevglossary/blob/master/static/img/Screen%20Shot%202020-07-09%20at%2023.01.38.png?raw=true">

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
<li>Flash messages</li>
<li>Pagination</li>
<li>Search under Manage Categories</li>
<li>Separate field for links in Add New Word</li>

<h3>Main Technologies Used</h3>
<p>For this project I used Python, HTML, CSS, javascript and Sass programming languages.</p>

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
<li>User Testing - people were asked to visit the app and test. Reason is to collect feedback and improve. After collected feedback I fixed the alphabet navigation that did not work, search was not noticed at first so I added an icon, the app was not responsive due to issues in Materialize, but I fixed that by adding: meta name=“viewport” content=“width=device-width, initial-scale=1.0" in the html code under head and using media queries in css. </li>
<li>Tested browser lists: Google Chrome, Chrome Lighthouse for audit of website, Safari. Everything worked fine. In Chrome audit result are mixed, no less than 79 in both mobile and desktop, which means improvement can be made: Best practice scored 79, SEO scored 90, Accessibility 100 and overall performance 89.</li>
<img src="https://github.com/VictoriaBC/midevglossary/blob/93fbfd2c831f8974800eadfaf6b009014bcbaa1f/static/img/lighthouse_audit.png"><p><i>Lighthouse performance Audit test in inspect.</i></p>

<h3>HTML, CSS and JS code</h3>
<li>W3C HTML Validator.</li>
<li>W3C CSS Validator.</li>
<li>Pep8online to test app.py.</li>
<li>ami.responsivedesign.is and Inspect to test for responsiveness.</li>

<h3>Meeting the needs of the user stories (described  earlier in the UX section of this README file)</h3>
<p>As a new User I want to be able to understand how to navigate around the web application.</p>
<p>On landing page, the user is welcomed with a welcome text and information about this app, imediately followed below by search, alphabet navigation and common glossary.</p> 
<p>Navigation in the header at the top of the page. The Logo, when clicked, redirects the user to Landing page</p>
<p>As a user I would like to be able to add words, edit them and also add, edit categories.</p>
<p>As a user I would like this application to be responsive.</p>

<h3>Deployment</h3>
<p>heroku - git - PIP - Python 3 - Flask - A MongoDB Atlas account</p>
<p>The app is designed in Gitpod environment and committed to GitHub. Issues occured when I deployed manually, the tried to this through gitpod. Recommendation: Do not deploy manually, only through gitpod terminal.</p>

<h3>The following steps were taken to deploy this project to Github:</h3>
<li>created a master branch in Github repository through <a href="https://github.com/Code-Institute-Org/gitpod-full-template">Gitpod fulltemplate.</a></li>
<li>Committed files using bash terminal commands: git status; git add (specify directory); git commit -m "Initial commit"</li>
<li>Commited and pushed files to the working environment with commands git push, which updates the repository.</li>

<h3>To set .gitignore environment variables:</h3>
<li>Create file env.py in the root directory of your project. You will then define your variables there because you do not want to expose your MONGODB password and credentials to public.</li>
<li>Create .gitignore in the root directory of your project.</li>
<li>You will nedd to stop git from pushing this file to github, and so keep your environment variables secret. Open .gitignore file add the following text: env.py</li>
<li>Type import os at the top of your env.py file. Once added, type underneath your environment variables using the following syntax:
os.environ["Variable Name Here"] = "Value of Variable Goes Here"</li>
<li>Now your environment variables are set in your env.py file. After this you can use them using the following syntax:
MONGODB_NAME = os.environ.get('MONGODB_NAME')</li>

<h3>To deploy the project to Heroku :</h3>
<li>Create a Heroku account</li>
<li>Create requirements.txt file in Gitpod workspace for Heroku to understand installation files to run app.</li> 
<li>Then from CLI type pip3 freeze --local > requirements.txt.</li>
<li>Type in terminal Heroku login.</li>
<li>To get the application running create a Procfile that istructs Heroku which file is the entry point.</li> 
<li>Follow these commands to create this: echo web: python app.py</li>
<li>To push from Github to Heroku use following CLI commands: git add ., git commit -m "fist Heroku commit", git push</li>
<li>To scale dynos and run the app in Heroku, use commands: heroku ps:scale web=1</li>
<li>We will need to run our Flask application in Heroku, so we need to specify IP and Port in Heroku. To do this go to Settings tab > Config Variables and input: IP Address: 0.0.0.0; Port: 8080</li>

<h3>To Deploy using Heroku Git, use git in the command line:</h3>

<li>Deploy your changes. Make some changes to the code you just cloned and deploy them to Heroku using Git.</li>
<li>$ git add .</li>
<li>$ git commit -am "commit message"</li>
<li>$ git push heroku master</li>
<li>Go to Heroku. In the heroku dashboard, click on the button "Open App".</li>

<h3>Credits</h3>
<p>The content is all from the developer, also inspired from Code Institute lessons, <a href="https://github.com/RobSimons1/ocean-dictionary">RobSimons1</a> and <a href="https://github.com/haydal810/Milestone-Project-3">David Hayden</a>.</p>
