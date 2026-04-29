# python-mariadb-example
A sample Python Model-View-Controller project that pulls data from a Mariadb server and performs basic CRUD operations.

## How to Run

### Pre-requisites
- This project requires at least **Python 3.10** since it uses type hints.
- Mariadb installation (kindly refer to the posted mariadb installation guide on Google Classroom)
- Git Bash (if using Windows)
    - **DISCLAIMER**: If you are using Windows, execute all the commands in this tutorial inside Git Bash

### Step 0: Setting up Virtual Environment
- Execute the following command:
    ```sh
    python3 -m venv .venv
    ```
    - If it printed an error, delete the created `.venv` folder and try the command again. If the error persists, try updating your Python to the latest version.
- If you did not see a `(.venv)` before your terminal prompt, go inside the virtual environment using:
    ```sh
    source .venv/bin/activate
    ```
    - Some Windows users might have the activate the virtual environment using the `.venv/Scripts/activate` directory.
- If successful, you should now see the something similar on your terminal prompt:
    ```sh
    (.venv) username ~/directory $ >
    ```
### Step 1: Installing the Dependencies
- Execute the following command to install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
    - This project relies on the `pymysql` package which is a pure python MySQL/MariaDB client library. Previously, it used the `MariaDB Connector/Python` connector but it required additional setup on Windows machines compared to *nix machines. `pymysql` is mostly a "drop-in" replacement for the former. Only "mostly" since you still have to change some methods/type to `pymysql`, or you have to change your former parameter marker from `?` to `%s`.

### Step 2:
- Run the `main.py` file:
    ```sh
    python3 main.py
    ```
## Why are there a lot of folders? — The MVC Architecture
- You may have noticed that this *simple* Python terminal app consisted of multiple folders. It is true that this entire mini-project could've been done in a big `main.py` file, but the real reason is **separation of concerns**.
    - Yeah, yeah, this architecture is overkill for this project, but it is a good start since most modern application frameworks are based on the MVC architecture, or at least some derivatives of it. Learning the architecture allows you to easily adapt to any framework that imposes it, since they *all work the same*.
    - Anyways here is the relevand xkcd commic:
        ![Relevant XKCD Comic](https://imgs.xkcd.com/comics/the_general_problem.png)
### What is the MVC architecture?
![MVC Architecture](https://developer.mozilla.org/en-US/docs/Glossary/MVC/model-view-controller-light-blue.png)
- The **Model-View-Controller** architecture separates the data model (what your data looks like, for example our `emp` table from our class), your business logic (the things that you do on your data, say retrieve, edit, or add), and your view (the one that the user interacts with).
- The **Model** really is just the actual data model of our application. For example, if our application manages *traffic violation tickets*, our data model will consist of the attributes of the traffic violation ticket.
- Instead of our **View** sending raw SQL commands to our Mariadb server, we dedicate another entity to handle the connection to Mariadb, and that entity is the **Controller**. The controller usually contains the operations that your application will need to perform on the data model. Why do this?
    - It makes your codebase much more maintainable, you don't have to dig thru multiple function calls on your UI code to find your business logic. In a controller, **you know exactly where to look.**
    - Say you created a UI that fetches all the employees from the database, and you want to use the fetching logic on a different module of the application. You can't do that if your business logic is chained to your UI. With controllers, business logic is separated and can be used anywhere you need it.
- And lastly your **View** is now focusing on solely handling user interaction, which means a business logic error will not destroy the UI structure and **you finally have separation of concerns.**

### Model-View-Controller Interaction
- The view interacts with the controller, the controller interacts with the model usually thru a database API.

## The Code: MVC in Action
- Kindly click the individual folders as they contain their own README file explaining what each module do.