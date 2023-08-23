# last_csv_email

This repository is an attempt at creating a script for automating the process 
of parsing and sending login data from a Linux server.

## Content	

### send_login_csv_email.py
The script parses the output of the last and lastb commands (since yesterday) 
as csv files and sends them as email attachments to the given recipient.

To automate (schedule) the execution of the script, add it to the scheduler of 
your choice.

#### Example using cron:
`0 6 * * * BASH_ENV=~/.bashrc bash -l –c "/usr/bin/python3 /home/user/send_login_csv_email.py"`

The example executes the script every day at 6 o'clock.

### parse_last_to_csv.py 
The script parses and saves the output of the last(b) command as a csv-formated 
plain text file. The script expects as arguments the command 'last' or 'lastb' 
and the duration for the switch 'since'.

#### Example:
`./parse_last_to_csv.py lastb yesterday`

Omitting both arguments will parse the output of the 'last' command since 
'yesterday'.

### send_email.py 
The script sends an email with or without attachments. The script expects 
the SMTP server (SMTP_SERVER), email sender (EMAIL_FROM), and apikey 
(EMAIL_AUTH) as environmental variables. 

To send an email, execute the script in a directory that contains the message 
(as a plain text file) and attachment(s). Give the recipient(s) (EMAIL_TO) 
as an argument, followed by the subject, message/body, and attachment(s).

#### Example: 
`./send_email.py 'email@email.com' 'subject' 'message.txt' 'attachment.jpg'`

When sending multiple attachments, separate filenames with a comma (,).

## Documentation
