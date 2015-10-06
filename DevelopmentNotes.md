#summary Notes about the development environment



# Configuration #

In my development environment I have a 'local\_settings.py' similar to the following:

```
import os.path

# Use the factory configuration from SVN:
FACTORYCONF   = '<svn co path>/webpymail/config/factory.conf'

# Define every other configuration file outside the checked out 
# directory. This way I'm able to preserve my configuration changes
# between updates
CONFIGDIR     = '<config directory>'
USERCONFDIR   = os.path.join(CONFIGDIR, 'users')
SERVERCONFDIR = os.path.join(CONFIGDIR, 'servers')
DEFAULTCONF   = os.path.join(CONFIGDIR,'defaults.conf')
SYSTEMCONF    = os.path.join(CONFIGDIR,'system.conf')

SERVERCONF    = os.path.join(CONFIGDIR,'servers.conf')


# Debug the IMAP connection

import imaplib2.imapll

D_SERVER = 1        # Debug responses from the server
D_CLIENT = 2        # Debug data sent by the client
D_RESPONSE = 4      # Debug obtained response

# Uncomment the following line to get the client/server conversations:
# imaplib2.imapll.Debug = D_SERVER | D_CLIENT
```