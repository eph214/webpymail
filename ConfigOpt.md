#summary Configuration options



# Configuration #

The client configuration is stored in plain text files.

There are a number of configuration files:

  * **FACTORYCONF** - this configuration file stores the factory settings, it should not be changed by the user;
  * **DEFAULTCONF** - here we can define settings that are valid system wide and can be overridden by the user or at the server level. The settings defined here override the factory settings;
  * **USERCONFDIR/`<user name>@<host>.conf`** - user settings. The settings defined here override the DEFAULTCONF settings on a per user base;
  * **SERVERCONFDIR/`<host>.conf`** - server settings. The settings defined here override all the other files except for the ones defined in **SYSTEMCONF**;
  * **SYSTEMCONF** - system wide settings. The settings defined here override all the ones defined in any other file.

This arrangement affords extreme flexibility when customizing the system.

Additionally we have also the configuration file **SERVERCONF** where the connection settings to the IMAP servers are defined.

The paths to these files are defined on the settings.py file. You can change this paths according to your needs.

# Configuration Options #

## General ##

  * **theme** - (default: default) theme to be used please read ThemesApplication
  * **login\_page** - (default: /mail/FOLDER\_SU5CT1g=/) by default we use the message list view on the INBOX folder. Note that you must change this if Webpymail isn't installed on the webserver root
  * **logout\_page** - (default: /) This can be a relative or a complete URL

## Identities ##

The user can customize one or more identities. Usually these are defined on the per user configuration file in **USERCONFDIR/`<user name>@<host>.conf`**. Each identity must have its own section. The identity section must be named in the form **identity-##** where ## is an integer. Right now the available configuration parameters are:

  * **user\_name**
  * **mail\_address**

An identity configuration example might be:

```
[identity-00]

user_name       = Helder Guerreiro
mail_address    = helder@example.com

[identity-01]

user_name       = Helder Guerreiro
mail_address    = postmaster@example.com
```

## smtp ##

Define the SMTP server to connect to in order to send mail. The available options are:

  * **host** - SMTP server
  * **port** - (default: 25)
  * **user** - If specified an attempt to login will be made
  * **passwd** - password for the SMTP server
  * **security** - the available options are:
    * TLS
    * SSL
    * none
  * **use\_imap\_auth** - (default: False) - if true the imap user/pass pair will be used to authenticate against the smtp server.

For example we may have:

```
[smtp]

host = smtp.googlemail.com
port = 465
user = a_user@gmail.com
passwd = XXXXXXXXXX
security = SSL
```

Or (SSL support):

```
[smtp]

host = smtp.googlemail.com
port = 465
security = SSL
use_imap_auth = True
```

Or (TLS support):

```
[smtp]

host = smtp.gmail.com
port = 587
security = TLS
use_imap_auth = True
```

## Message ##

Message related settings:

  * **css** - (default: empty) you can define here CSS to be used on Markdown generated messages.

CSS definition example:

```
[message]

css = body {
	color: black;
	background: whitesmoke; }
```

  * **show\_images\_inline** - (default: False) if true the images attached are displayed in-line.