# Email notification

Simple but practical notification scheme. 

### Install: 
- Create a new email address, so you don't have to store your important password in plain text. 
- Save the file to your machine, and add it to your python path.
  - on Linux, add `export PYTHONPATH="${PYTHONPATH}:/my_path_to/email_me_statement.py"` to `~/.bashrc` 
  - (do not forget to subsequently run `source ~/.bashrc`)

### Use:
- add the following code to any file: 

```python
from email_me_statement import send_msg
send_msg("This is my test message", "The is my test Subject")
```
  
- You can leave the Subject blank, however leaving the message blank will cause an error. 

### Note:
 - If you create a new Gmail address you may have to authorize dangerous access to it. A notification should appear if you run the script once. 
