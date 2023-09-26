from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# ... your existing endpoints ...

# Supporting Document Endpoint
@app.route('/documentation', methods=['GET'])
def documentation():
    # Define the content of the supporting document with line breaks
    supporting_document = """
    # Flask Calculator API Documentation

    ## Overview

    The Flask Calculator API is a simple RESTful web service that allows users to perform basic mathematical operations such as addition, subtraction, multiplication, and division. It also provides a feature to retrieve user details. The API is built using the Flask framework in Python.

    ## Base URL

    The base URL for all API endpoints is http://localhost:5000. Replace localhost with the appropriate hostname or IP address if the API is deployed on a different server.

    ## Endpoints

    ### 1. Addition

    *Endpoint*: /add
    *HTTP Method*: POST

    *Description*: This endpoint allows users to perform addition. Users can provide two numbers, a and b, in the request body as JSON. The endpoint will return the sum of a and b as JSON.
    
    ... [The rest of your documentation here] ...
    
    """
    
    # Return the supporting document as formatted text
    return render_template_string('<pre>{{ document }}</pre>', document=supporting_document)

if __name__ == '__main__':
    app.run(host="localhost", debug=True)
