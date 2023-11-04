# Social Media Backend

Well-structured pet project written on **Flask** using onion architecture (repository-service-api) which illustrates user's social media life through ability leaving posts and comments.

# Project Description

The **"SocialMedia"** project is a **Flask** project that aims to illustrate a user's social media life through the ability to create, view, like and dislike posts and comments. 
The application follows the **Onion Architecture** design pattern, which emphasizes the separation of concerns by dividing the application into layers: repository, service, and API. 
It also implements a robust authentication process using **JWT (JSON Web Tokens)** for secure user access and authorization. 
JWT tokens are located in Cookies. 
App has got an exception system for giving clear understanding of user's mistakes if such exist.

### **Technologies Used**:

* **Flask**: Flask was chosen as the web framework due to its simplicity, flexibility, and ease of use. It provides the foundation for building web APIs and serving web pages efficiently.
* **Onion Architecture**: This architectural pattern was selected to maintain a clear separation of concerns and to create a maintainable, testable, and scalable application. The repository layer handles data storage and retrieval, the service layer manages business logic, and the API layer exposes endpoints for client interaction.
* **JWT (JSON Web Tokens)**: JWT is used for authentication and authorization. It provides a secure and stateless way to manage user sessions and protect routes. They are located in Cookies right after the request for authentication. 
* **Marshmallow**: Marshmallow is used for data validation, serialization, and deserialization. It helps ensure that data transferred between the API and the database is in the correct format and structure.
* **SQLAlchemy**: SQLAlchemy is employed as an Object Relational Mapping (ORM) tool for database interaction. It simplifies database operations and ensures portability across various database systems.
* **PostgreSQL Database**: PostgreSQL serves as the database management system for storing and managing data. Its ACID compliance and support for complex data types make it an excellent choice for this project.

### **Challenges Faced**:

* **Authentication and Security**: Implementing JWT-based authentication and ensuring proper security measures were among the most significant challenges. It required careful validation and protection of routes and tokens.
* **Business Logic**: Implementing and managing business logic, including ensuring that users can only update or delete their own posts and comments, was a significant challenge. It required thorough validation and checks to prevent unauthorized actions.
* **Database Structure**: Designing the database schema for posts, comments, and user profiles while maintaining data integrity and efficiency presented challenges. SQLAlchemy helped address this, but it required careful planning.

* **Scalability**: The project was designed with scalability in mind, but future scaling challenges may arise as user data and interactions increase.


# Key Features

* **Custom JWT Authentication**: Authentication system based on JWT tokens realized from scratch
* **User Registration**: Allow users to register and create accounts, providing a seamless onboarding process.
* **User Profiles**: Enable users to create and manage their profiles, including bios and personalization options.
* **Posts**: Ability to leave, update or delete posts for authenticated users. All relationships checks are included.
* **Comments**: Ability to leave comments to posts and answers on comments for authenticated users
* **Likes**: Like/dislike system for posts and comments

# Exceptions

In Social Media App, was realized a good system of exceptions to enhance user experience and ensure smooth operation. 
These exceptions are designed to be informative and understandable, helping users quickly identify and resolve issues while interacting with the platform.
Whether it's notifying users about incorrect login credentials, handling unexpected errors gracefully, or providing clear feedback when accessing restricted content. 

You can see all provided exceptions in **"errors"** folder in source code.

# Requirements

* Python 3.10 (you can use virtual environment)
* Pip (v22.3)
* Docker (v20.10.21) and docker compose (v1.29.2) (for Postgres, if you already have Postgres you can skip this requirement)
* .env file in root project directory, which must contain secret key for tokens generating and name of database, port, user and password, like this:
  ```
  SECRET_KEY=your_secret_key
  DATABASE_NAME=your_database_name
  DATABASE_PORT=your_port
  DATABASE_USER=your_user
  DATABASE_PASSWORD=your_password
  ```
# Run Locally

Clone the project
 
```bash
  git clone --branch develop https://github.com/ash1vt/social-media-backend
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Create and launch Postgres docker container (you can set your own configuration in `docker-compose.yaml` file). 
Skip this if you already have Postgres running

```bash
  docker-compose up -d
```

Apply migrations for database

```bash
  flask db upgrade
```

Run server

```bash
  flask run
```

# Testing the API with Postman
To test the API of our Social Media App, it is recommended to use Postman, a popular and user-friendly API testing tool. 
A Postman collection have been provided in the **"documentation"** folder of this repository, which includes pre-configured requests to interact with various API endpoints.

### Prerequisites

Before you get started with Postman, please make sure you have the following prerequisites in place:

1) **Postman**: If you don't already have Postman installed, you can download it here.

2) **API Endpoint**: Ensure that your Social Media App API server is up and running and that you have the API's base URL.

### Importing the Postman Collection

1) Open Postman and click on **"Import"** in the top left corner.
2) In the **"Import"** window, select the **"Choose Files"** option.
3) Navigate to the folder **"documentation/postman"** in project repository and select the Postman collection file (socialmedia.postman_collection.json).
4) Click **"Open"** to import the collection.

### Running Requests

Now that you have the collection configured, you can start making API requests:

1) Open the Postman collection **"socialmedia"** from the left sidebar.
2) Navigate through the requests in the collection to interact with different API endpoints.
3) Click the **"Send"** button to make a request. 
4) Review the response to verify that your API is working as expected.

### Exceptions
As it was mentioned in [Exception](#Exceptions) section Social Media App has got understandable exceptions. 
If user make some mistakes in request he will get the text in the response telling what specifically went wrong.

### Authentication

Some API endpoints in the collection may require authentication using JWT tokens. 
You can obtain JWT tokens by passing right user credentials in the **login** request. 
It is automatically put in **Cookies**, so there is no need to provide it in authentication header.
After obtaining an access token, you can access protected endpoints.
