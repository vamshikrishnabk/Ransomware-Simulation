CSCE 5550 Ransomware Simulation Project


# Required Softwares

1. Python 3.6+
2. Oracle VM Box
3. Linux os

# Libraries

1. Watchdog
2. SMTP 
3. pandas


# Steps to run 

1. Place a folder containing subdirectories and files in a linux machine.
2. To simulate the ransomware we will attack the folder place in linux.
3. A program called send_email when run will ask for an email address, after which it will send an malicious code which can capable of encrypting the directory will sent as an executable.
4. Once the executable file is downloaded and ran, it encrypts the directory.
5. Now we can demand money for decrypting the files.
6. After ransom is paid, we can use decrypt code for decrypting the files.


# Monitoring

1. Run monitor.py. It will enable the monitor logs for the specified directories.


# Detection

1. Run detection.py. It will detect the changes and tells whether a ransom is happening.

# Mitigation

1. Run mitigation.py. It will identify process on which ransom is happening, and it will terminate the process,and send an email to admin regading this.
