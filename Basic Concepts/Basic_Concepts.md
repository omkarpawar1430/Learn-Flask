# Basic Concepts from Flask 
----------------------------------

![Alt text](Images/flask%20logo.png)

-------------------------------
## Required Libraries: 
### flask:  
Flask is a WSGI (Web Server Gateway Interface) framework for Python. WSGI is a specification for a universal interface between web servers and web applications or frameworks written in Python. In simpler terms, WSGI allows Python web applications like Flask to communicate with web servers like Apache or Nginx. WSGI acts as a bridge between the web server and the web application, handling requests from the web server and passing them on to the application, and then returning the response back to the web server.
#### Classes from flask module: 
1. Flask: This is the main class of the Flask web framework. It is used to create a new Flask application instance.
1. render_template: This function is used to render a template file (usually an HTML file) using the Jinja2 template engine. It takes the name of the template file as its first argument and any additional keyword arguments that should be available in the template context.
1. request: This is an object that represents an incoming HTTP request. It contains information about the request, such as the HTTP method, headers, form data, and URL parameters.

-------------------------

## Decorator: 
```python
app.route('/', methods=['GET'])
```
Here we are giving root URL as `"/"`. Which is going to act as our landing page or default page. Whatever code we write after this decorator, will be executed when we try to open our webpage using root URL.
endpoint: The name of the endpoint for the route, which can be used to generate URLs to the route.

### `methods`: 
types of different requests

We can give arguments in `methods` as list of these:  
`GET`: Used to retrieve data from the server.

`POST`: Used to submit data to the server.

`PUT`: Used to update an existing resource on the server.

`DELETE`: Used to delete a resource from the server.

`PATCH`: Used to make a partial update to an existing resource.

`OPTIONS`: Used to retrieve information about the communication options available for a resource.

`HEAD`: Similar to GET, but only retrieves the HTTP headers for a resource and not the content.

similar to `methods` we can give argument to decoder like: 

### `defaults`:
 A dictionary of default values to be used when building a URL for the route.

### `host`:
 The hostname for the route.

### `port`: 
The port for the route.

### `subdomain`: 
The subdomain for the route.

### `strict_slashes`: 
Whether or not the route should match URLs with trailing slashes.

### `redirect_to`: 
The URL to redirect to if the route is requested without the correct HTTP method.

---------------------

## Debugger = True 

Debug mode provides helpful features during development, such as automatic reloading of the application when changes are made, a debugger that displays useful information about errors, and a more verbose output of server logs.

When debug mode is enabled, the server will also display detailed information about any errors that occur during application execution, including a traceback of the error and the line number in the source code where the error occurred. This makes it easier to identify and fix issues during development.

It is important to disable debug in production to avoid security risks. 

----
## Why we use `__name__`?
In this case, `__name__` would be set to the string `"__main__"`, which is the name of the module that Python executes when the script is run. This tells Flask that the application is defined in the current file, and Flask can locate other files and resources relative to the location of the app.py file.

---


