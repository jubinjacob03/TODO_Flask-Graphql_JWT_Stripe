# TODO_Flask-Graphql_JWT_Stripe
This is a Python Flask app ( TODO APP ) that uses JWT ( JSON Web Tokens ) for user-authentication &amp; for securing all GraphQL Endpoints, Uses the GraphQL  query language to handle all API calls &amp; connect with MySQL  Database, and Stripe (test mode) for payment integration.

# Assignment Details
- This assignment was assigned by [Dendrite.ai](https://dendrite.ai/) as a short assignment for internship application short-listing.
- The assignment details provided by Dendrite.ai is attached as a .docx file :
[Python_Assignment - internship.docx](https://github.com/jubinjacob03/TODO_Flask-Graphql_JWT_Stripe/files/12196722/Python_Assignment.-.internship.docx)

# Running the project
- Install the requirement.txt
- Install GraphQl via npm
- To run and serve the project on LocalHost use this command in the terminal of IDE - <code>py src\main.py</code>.

# Modifications to this project
- Due to <i><b>poor and limited documentation</b></i> <code>Keycloak intergration was aborted.</code>
- Docker was <i><b>crashing multiple times</b></i> and <i><b>back-end codes</b></i> for assigning role switch (*required as it is needed to integrate stripe payment which authorized the access of certain features as a premium member) <i><b>was not found</b></i> in documentation.
- Replacement of Keycloak was done with <code>JWT & Jsonify,</code> This was because I found that <i><b>Keycloak also uses JWT</b></i> to verify users.
- My <i><b>dearly apologies</b></i> for not using Keycloak afor Authentication , due to the above mentioned reasons.


