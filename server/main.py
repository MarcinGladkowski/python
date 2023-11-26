"""
Create web server using Python http module

python3 -m http.server 8001 - this run has security vulnerability! Everyone in the local network can talk you.

Consider this example:
python3 -m http.server -b 127.0.0.42 8080 - using Loopback interface only you can access to this address

As a default this command server files in current directory

CGI usage (Common Gateway Interface)

- Create directory cgi-bin
- Set permissions by: sudo chmod a+x cgi-bin
- Returned page is available at http://0.0.0.0:8001/cgi-bin/hello.py


"""