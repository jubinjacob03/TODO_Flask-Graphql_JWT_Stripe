# TODO_Flask-Graphql_JWT_Stripe
This is a Python Flask app ( TODO APP ) that uses JWT ( JSON Web Tokens ) for user-authentication &amp; for securing all GraphQL Endpoints, Uses the GraphQL  query language to handle all API calls &amp; connect with MySQL  Database, and Stripe (test mode) for payment integration.

# About the project
- This project was assigned by [Dendrite.ai](https://dendrite.ai/) as a short assignment for internship application short-listing.
- The project Details provided by Dendrite.ai are provided below :
<h3>Problem Statement:</h3>  
The objective of this python project is to create a To-Do List with Graphql API calls.
<h3>Description:</h3>  
A simple To-do Flask webapp that uses keycloak for Authentication to let the user log in and add a to-do with title, description and time. All the API calls must be handled by Graphql only. There will be a option to buy a Pro license that will enable user to upload images in To-Do as well.
<h3>Minimum Requirements:</h3> 
1.	Each of the To-Do will have 3 field:<br>
a.	Title<br>   
b.	Description<br>   
c.	Time<br> 
d.	Images (Pro license)<br> 
2.	There will Following operation that a user can do:<br> 
a.	List all To-Do.<br> 
b.	Add a To-Do.<br> 
c.	Delete a To-Do.<br> 
d.	Edit a To-Do.<br> 
3.	User must have to login with keycloak first to do any of the above operation.<br> 
4.	Every Graphql endpoint must be secured by keycloak.<br> 
5.	Option to buy a Pro license with Stripe payment.<br> 
6.	Stripe payment will done in testing mode only. Please read https://stripe.com/docs/testing<br> 
7.	Person with pro license only can upload images in To-Do<br> 
 <h3>Must have:</h3> 
1.	A very basic UI to perform the above-mentioned operations.<br> 
2.	Error-free, Readable, Simple & Clean code<br> 
3.	Let me stress the previous point - Readable, Simple & Clean code<br> 
4.	Minimum third-party dependencies <br> 
<h3>Bonus Points:</h3>
1.	UI is clean and beautiful.<br> 
2.	React used in frontend.<br> 
<h3>Few links for reference:</h3>
1.	Keycloak - https://www.keycloak.org/ & https://www.keycloak.org/getting-started/getting-started-docker<br> 
2.	Query - https://graphql.org<br> 

<h3>Note:</h3>
1.	PLEASE NOTE THAT, WE HAVE A ZERO TOLERANCE POLICY FOR PLAGIARISM. IF YOU PLAGIARIZE THE TEST, YOU WILL BE CAUGHT AND IMMEDIATELY TERMINATED.<br> 
2.	Please do not submit the code if code is not up to a standard.<br> 
3.	Please do not send LinkedIn Request to Connect!<br> 
4.	PLEASE MAKE SURE YOU SUBMIT EVERYTHING VIA A GITHUB LINK AND PLS UPLOAD ALL ASSETS AND FILES INCLUDING KEYCLOAK DOCKER ETC.<br> 

# Modifications to this project
- Due to <i><b>poor and limited documentation</b></i> <code>Keycloak intergration was aborted.</code>
- Docker was <i><b>crashing multiple times</b></i> and <i><b>back-end codes</b></i> for assigning role switch (*required as it is needed to integrate stripe payment which authorized the access of certain features as a premium member) <i><b>was not found</b></i> in documentation.
- Replacement of Keycloak was done with <code>JWT & Jsonify,</code> This was because I found that <i><b>Keycloak also uses JWT</b></i> to verify users.
- My <i><b>dearly apologies</b></i> for not using Keycloak afor Authentication , due to the above mentioned reasons.

# Running the project
- Install the requirement.txt
- Install GraphQl via npm
- To run and serve the project on LocalHost use this command in the terminal of IDE - <code>py src\main.py</code>.
