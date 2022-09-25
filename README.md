# Terminal
This Terminal contains multiple tools and commands to help with ethical network / and or pen testing.
Such tools:
  - SSH Bruteforce:
    - takes an IP , port , username , wordlist and timeout
    - loops through each word in the wordlist and tries it as a password
  
  - tcp client (tcp-client):
    - takes an IP and port (+ a connection timeout)
  
  - portscanner:
    - 3 different types of scanning (common, quick, full)
    - takes an IP and connection timeout
    - returns all open ports for that IP in the range it scanned
    
  - proxychecker:
    - takes a text file full of ips:ports & timeout
    - tries to connect to each ip:port combo to check if that port is open
  
  - more tools included
