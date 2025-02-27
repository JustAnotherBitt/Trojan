# Python Trojan

## Overview
This is a trojan written in Python that establishes a persistent connection with a remote server and listens for incoming commands.

## Features
- Persistent connection attempts to the attacker's server.
- Remote command execution.
- Multi-threaded execution to handle commands asynchronously.

## Usage
1. Modify the IP (and, optionally, the port) of the code as needed.
   
2. Install the pyinstall library that will be used to generate the executable file:
```
pip install pyinstall
```

3. Generate the executable:
```
pyinstaller -F --clean -w trojan.py
```

Note: the file name can also be changed, as well as the icon. 

4. The attacker must leave a port listening on his machine to receive the connection:
```
nc -lvp 443
```

Once the connection is received, the attacker will have persistent access to the victim's machine, thanks to the `autorun()` function, which ensures that the program is executed automatically whenever the system is started.


## Security Notice
Use this script only in controlled environments such as penetration testing labs, with explicit permission. Misuse of this tool for unauthorized access to systems is illegal and may result in severe consequences. The risk is yours.

## Observation
The program has **low detectability** by antivirus software when run. But it is possible that, when generating the executable, the antivirus detects some suspicious activity, so I suggest disabling the antivirus/firewall when generating the executable to avoid errors.

