#summary Installation instructions
#labels Featured



# Warning #

Webpymail is still on its early development stages, it's not yet feature complete and could possibly cause damage to you data.

# Dependencies #

To test webpymail you need:

  1. Django svn
  1. Python 2.5 (>= 2.6 for SSL SMTP server support)
  1. Markdown library 2.0 (optional)

Please note that there is a bug that affected python versions 2.6 and 2.7 that makes SSL SMTP unusable, if you think you're affected by this consult:

> http://bugs.python.org/issue4066

The markdown library is used to compose html messages. The library can be obtained from:

> http://www.freewisdom.org/projects/python-markdown/

# Installation #

  * Get python and django working;
  * Choose a suitable folder and checkout webpymail source code:

```
svn checkout http://webpymail.googlecode.com/svn/trunk/ webpymail-source
```

  * Add the webpymail-source dir to your PYTHONPATH

```
cd webpymail-source
export PYTHONPATH=`pwd`:$PYTHONPATH
```

  * Create or edit the webpymail/local\_settings.py file according to your needs. The local\_settings.py is imported from the main settings file. This way you don't have to reconfigure each time you update you svn working copy.

> I'll try to shift all the needed configurations to the configuration files.

  * Edit the file servers.conf in webpymail/config/servers.conf and add your server. A server entry must be something like:

```
[example]

name = Example Server
host = imap.example.com
port = 993
ssl  = true
```

  * Define a smtp server use a [smtp](smtp.md) section. This can be done in webpymail/config/defaults.conf for a system wide configuration:

```
[smtp]

host   = smtp.example.com
port   = 25
user   = auser
passwd = apass
security = tls
```

> The security can be tls, ssl or none.

> If you wish to have different configurations by server you will have to define these settings in the specific server configuration file that lives in webpymail/config/servers/`<hostname>`.conf. Take a look at the next section for information about configuration file precedences.

> For the Google Mail IMAP server a pre-made configuration is shipped in webpymail/config/servers/imap.gmail.com.conf .

  * Go to the webpymail dir and create the data base:

```
$ cd webpymail
$ python manage.py syncdb
[... snip ...]
Creating table mailapp_userprofile

You just installed Django's auth system, which means you don't have
any superusers defined.
Would you like to create one now? (yes/no): yes
Username (Leave blank to use 'helder'):
E-mail address: helder@paxjulia.com
Password:
Password (again):
Superuser created successfully.
[... snip ...]
```

  * Start the Django included web server:

```
$ python manage.py runserver
```

  * Finally you can access the webmail app, just go to: http://127.0.0.1:8000/ . Login with a valid user on the IMAP server.