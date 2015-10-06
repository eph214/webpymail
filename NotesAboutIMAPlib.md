# Whats inside the imaplib2 package? #

The main components of the imaplib2 package are:

  * **Class IMAP4** - very simple IMAP client;
  * **Class IMAP4\_SSL** - very simple IMAP client, SSL version;
  * **Class IMAP4P** - parsed IMAP client;

Besides this we have some auxiliary stuff:

  * Parser modules:
    * parsefetch module:
      * BODYSTRUCTURE response:
        * **Class BodyPart** - generic body part;
        * **Class Multipart** - <MULTIPART/**>
        ***Class Single**- generic non multipart;
        ***Class Message**- <MESSAGE/RFC822>
        ***Class SingleTextBasic**- generic non multipart;
        ***Class SingleText**- <TEXT/**>
        * **Class SingleBasic** - <**/**>
        * **load\_structure** - factory for the BODYSTRUCTURE class hierarchy.
      * ENVELOPE response:
        * **Class Envelope**
    * parselist module:
      * **Class ListParser** - container for the mailbox list;
      * **Class Mailbox** - mailbox;
    * sexp module:
      * **scan\_sexp** - scans a string containing a symbolic expression and transforms it in a nested python list.

  * utils module:
    * **getUnicodeHeader** - unicode string with the content of the header string;
    * **getUnicodeMailAddr** - returns an address list with the mail addresses;
    * **Int2AP** - Convert integer to A-P string representation (from imaplib);
    * **makeTagged** - composes a string with the tagged response;
    * **unquote**
    * **envelopedate2datetime** - converts the envelope env\_date response (from teh FETCH command) to python's datetime;
    * **Internaldate2tuple** - converts the internal date response (from the FETCH command) to python's datetime;
    * **shrink\_fetch\_list** - takes a list of message IDs or UIDs and returns a shrinked list using IMAP's ranges;
    * **Class ContinuationRequests** - handle continuation requests from teh server.

# Why do another IMAP library? #

Strictly speaking there is no need for us to have a new IMAP lib in python. True, the standard lib is not very pythonic, and could use some love, but overall it does its job fairly well.

I went the way of making a new lib simply because it made things easier for me on the parsing side. For instance, in imaplib, if I invoque a fetch command I might get something like:

```
>>> M.fetch('1', '(BODY[1] BODY[2])')
('OK',
 [('1 (BODY[1] {5}', 'Test1'),
  (' BODY[2] {879}',
   "...snip 879 chars..."),
  ')'])
```

While in imaplib2 using the low level library I get:

```
>>> M.send_command('FETCH 1 (BODY[1] BODY[2])')
('KPDE003',
{'untagged':
["* 1 FETCH (BODY[1] {5}\r\nTest1 BODY[2] {879}\r\n...snip 879 chars..."], 'tagged': {'KPDE003':
            {'status': 'OK',
             'message': 'Completed (0.000 sec)',
             'tag': 'KPDE003',
             'command': 'FETCH 1 (BODY[1] BODY[2])'}}})
```

The untagged responses come in a list, with a complete response per list item, the tagged responses are clearly layed out in a dictionary, identifying each response with the associated tag.

Naturaly I could have wrapped imaplib to get the same result, but in that case I would have to live also with all the other stuff in there. Instead I borrowed the socket code, and went from there.

BTW for the same example as above with the parsed library I get:

```
>>> M.fetch( 1, '(BODY[1] BODY[2])' )
{1: {'BODY[1]': 'Test1', 'BODY[2]': "...snip 879 chars..."}}
```