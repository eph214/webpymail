This is another attempt to make a webmail app in python. I aim on a first stage to build a standards compliant imap webmail client with the basic functionality we can find in squirrelmail without plugins. I'm not too worried about the user interface since it will be extremely easy to use the Django project templates to customize it.

## Contact / Support ##

If you which you can write to "hguerreiro at gmail dot com" if you have any comments about this project.

## What's done? ##

"simples" theme, a work in progress:

<img src='http://webpymail.googlecode.com/svn/wiki/img/webpymail-simples_theme-message_list-01.png' width='711' height='394'>

<h3>Django based webmail client</h3>

The implemented features are:<br>
<br>
<ul><li>Multiple IMAP and SMTP server support;<br>
</li><li>IMAP authentication, the Django built-in auth is only used for the superuser;<br>
</li><li>Auto creation of django users - if the user successfully authenticates against the IMAP server then a new django user is created '<user name>@<imap host>';<br>
</li><li>Mailbox List (subscribed mailboxes);<br>
</li><li>Folder List;<br>
</li><li>Message List (paginated);<br>
</li><li>Message view, only the TEXT/PLAIN parts, the others, including the html parts, may be viewed/downloaded from the message view;<br>
</li><li>Reply, Reply to All, Forward, Inline Forward;<br>
</li><li>Move and copy messages;<br>
</li><li>Message composing in plain text or using Markdown that's converted to html when the message is sent;<br>
</li><li>Simple address book application, it supports server, site and user level address books. The user can only edit and delete is own addresses. The server and site level addresses can be created from the admin interface;</li></ul>

Please note that I'm using Cyrus and Gmail to test, so if you try to use this on another kind of server the results may not be the same.<br>
<br>
Bug reports and patches are welcome!<br>
<br>
<h3>IMAP library - imaplib2</h3>

The IMAP proto is a bit complex, for me, the most difficult part in dealing with IMAP is to efficiently parse the server responses and within the IMAP responses the FETCH command ones are really complicated. Right now we parse to a useful format almost all the responses sent by the server.<br>
<br>
For instance:<br>
<br>
<ul><li>BODYSTRUCTURE FETCH responses are transformed in a class hierarchy, it's easy to get the part numbers for each part and then get only those message parts in which we're interested;<br>
</li><li>ENVEVELOPE FETCH responses are transformed in a dict;</li></ul>

Besides this, we can also get unasked for responses from the server, these are parsed correctly and stored on a response structure from where they can be read.<br>
<br>
Finally, the optional codes and tagged responses are also stored in a log, and callback functions can be defined to react to these responses.<br>
<br>
<h3>Higher Level IMAP library - hlimap</h3>

In order to have a more intuitive and simpler way to deal with the IMAP complexity, I've added an extra layer on top of imaplib2. Since this is being developed parallel to the Django webmail client, the result is that it's very easy to use from a Django template. For example to make a message list view, the Django view code to get the necessary information is:<br>
<br>
<pre><code>M = ImapServer('example.com')           # Connect to the server<br>
M.login('example user','example pass')  # Login<br>
folder = M.folders[folder].select()     # Get the folder and select it<br>
folder.messages.change_search(criteria) # Change the search criteria<br>
msg_len = folder.messages.len()         # To do the pagination<br>
[...]<br>
message_list = folder.messages[i:j]     # Get the message list <br>
</code></pre>

On the django template we do something like:<br>
<br>
<pre><code>{% for msg in message_list %}<br>
    &lt;p&gt;{{ msg.envelope.env_date }}<br>
    &lt;p&gt;{{ msg.envelope.env_subject }}<br>
{% endfor %}<br>
</code></pre>