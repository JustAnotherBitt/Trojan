# Python Trojan

## Overview
This is a trojan written in Python that establishes a connection with a remote server and listens for incoming commands. It executes the received commands and returns the output to the attacker. The script has been modified to accept the attacker's IP and port as user inputs for better flexibility.

## Features
- Persistent connection attempts to the attacker's server.
- Remote command execution.
- Multi-threaded execution to handle commands asynchronously.
- Dynamic input for IP and Port.

## How It Works
1. The script prompts the user to input the attacker's IP address and port.
2. It then attempts to connect to the provided IP and port.
3. If the connection is successful, it listens for commands from the attacker.
4. Commands received are executed on the target machine, and the output is sent back to the attacker.
5. If the connection fails, the script retries after a short delay.

## Requirements
- Python 3.x

## Usage
Run the script on the target machine:
```sh
python trojan.py
```

Enter the attacker's IP and port when prompted:
```sh
Attacker's IP: 192.x.x.x
Port: 443
```

On the attacker's machine, set up a listener using Netcat:
```sh
nc -lvnp 443
```

## Security Notice
Use this script only in controlled environments such as penetration testing labs, with explicit permission. Misuse of this tool for unauthorized access to systems is illegal and may result in severe consequences.

## Observation
Upgrade is comming!

