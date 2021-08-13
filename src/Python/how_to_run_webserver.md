# How to run a WebServer in Python

Make use of ```http.server``` library.

Simply:

```python

import os
import webbrowser
from http.server import HTTPServer, CGIHTTPRequestHandler
# Make sure the server is created at current directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Create server object listening the port 80
server_object = HTTPServer(server_address=('', 8080), RequestHandlerClass=CGIHTTPRequestHandler)
# Start the web server
server_object.serve_forever()
```



## References

[3 Lines of Python Code to Write A Web Server](https://towardsdatascience.com/3-lines-of-python-code-to-write-a-web-server-46a109666dbf)
