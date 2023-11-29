# last_csv_email

This repository is an attempt at creating a script(s) for automating the process 
of parsing and sending login data from a Linux server. The project was created 
as part of my studies at Utbildning Nord and used to complete the 
"Työtehtävien automatisointi komentokielellä, 15 osp" study module.  

## Content	

### Setup the environment
The scripts use a Google email account to send emails. If you don't have a 
Google account, create one. Add the following environmental variables to 
/env/evironment on your Linux (Ubuntu) server or VM.

* EMAIL_FROM="Email address"
* EMAIL_AUTH="App password"
* EMAIL_TO="Email recepient / server admin"
* SMTP_SERVER="smtp.gmail.com"

### send_login_csv_email.py
The script parses the output of the last and lastb commands (since yesterday) 
as CSV files and sends them as email attachments to the given recipient. 

The lastb command requires sudo privileges. Be sure that the account (users) 
you execute the scripts on has been added to the list of sudoers. If you run 
in to problems with executing the scripts, try enabling passwordless sudo 
access. 

To automate (schedule) the execution of the script, add it to the scheduler of 
your choice.

#### Example using cron:
`0 6 * * * BASH_ENV=~/.bashrc bash -l –c "/usr/bin/python3 /home/user/send_login_csv_email.py"`

The example executes the script every day at 6 o'clock.

### parse_last_to_csv.py 
The script parses and saves the output of the last(b) command as a CSV-formatted 
plain text file. The script expects as arguments the command 'last' or 'lastb' 
and the duration for the switch 'since'.
 
#### Example:
`./parse_last_to_csv.py lastb yesterday`

Omitting both arguments will parse the output of the 'last' command since 
'yesterday'.

### send_email.py 
The script sends an email with or without attachments. The script expects the 
SMTP server (SMTP_SERVER), email sender (EMAIL_FROM), and apikey (EMAIL_AUTH) 
as environmental variables. 

To send an email, execute the script in a directory that contains the message 
(as a plain text file) and attachment(s). Give the recipient(s) (EMAIL_TO) as 
an argument, followed by the subject, message/body, and attachment(s).

#### Example: 
`./send_email.py 'email@email.com' 'subject' 'message.txt' 'attachment.jpg'`

When sending multiple attachments, separate filenames with a comma (,).

## Documentation (reference)
Listed below are links to documents and articles used in the development of 
this project. 
### Send email with Python
* [Read and Send Email with Python](https://www.devdungeon.com/content/read-and-send-email-python)
* [Sending Emails With Python](https://realpython.com/python-send-email/)
* [email:Examples](https://docs.python.org/3/library/email.examples.html)
### Linux last
* [Linux last Command](https://www.baeldung.com/linux/last-command)
### Setup environment
* [Setting Up Environment Variables on Ubuntu](https://tecadmin.net/setting-up-environment-variables-on-ubuntu/#:~:text=Environment%20variables%20are%20a%20crucial,store%20settings%20for%20various%20software.)
### Passwordless sudo access
* [Execute sudo without Password?](https://askubuntu.com/questions/147241/execute-sudo-without-password)
### Linux cron
* [How to Automate Tasks with cron Jobs in Linux](https://www.freecodecamp.org/news/cron-jobs-in-linux/)
* [How to Load Environment Variables in a Cron Job](https://www.baeldung.com/linux/load-env-variables-in-cron-job)
