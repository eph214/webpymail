# -*- coding: utf-8 -*-

# WebPyMail - IMAP python/django web mail client
# Copyright (C) 2008 Helder Guerreiro

## This file is part of WebPyMail.
##
## WebPyMail is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## WebPyMail is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with WebPyMail.  If not, see <http://www.gnu.org/licenses/>.

#
# Helder Guerreiro <helder@paxjulia.com>
#
# $Id$
#

"""Actions on messages
"""

# Global Imports
import base64
# Django:
from django.http import Http404

# Local
from mailapp.forms import MessageActionForm

# System flags
DELETED = r'\Deleted'
SEEN = r'\Seen'
ANSWERED = r'\Answered'
FLAGGED = r'\Flagged'
DRAFT = r'\Draft'
RECENT = r'\Recent'

# Actions
MARK_READ = 1
MARK_UNREAD = 2
DELETE = 3
UNDELETE = 4

def message_change( request, message ):
    new_data = request.POST.copy()

    if new_data.has_key('delete'):
        message.set_flags(DELETED)
    elif new_data.has_key('undelete'):
        message.reset_flags(DELETED)

def batch_change(request, folder, message_list):
    new_data = request.POST.copy()
    if new_data.has_key('expunge'):
        folder.expunge()
        return

    if not new_data.getlist('messages'):
        # Do nothing if no messages are selected
        return

    # Validate the form
    form = MessageActionForm(new_data, message_list=message_list, server = folder.server)
    if not form.is_valid():
        # Do nothing if the form isn't valid
        return

    selected_messages = form.cleaned_data['messages']
    try:
        selected_messages = [ int(Xi) for Xi in selected_messages ]
    except:
        return

    action = int(form.cleaned_data['action'])

    if action == DELETE:
        folder.set_flags(selected_messages, DELETED)
    elif action == UNDELETE:
        folder.reset_flags(selected_messages, DELETED)
    elif action == MARK_READ:
        folder.set_flags(selected_messages, SEEN)
    elif action == MARK_UNREAD:
        folder.reset_flags(selected_messages, SEEN)

    if new_data.has_key('move') or new_data.has_key('copy'):
        if folder.url() == form.cleaned_data['folder']:
            return
        target_folder =  base64.urlsafe_b64decode(str(form.cleaned_data['folder']))
        folder.copy(selected_messages, target_folder)
        if new_data.has_key('move'):
            folder.set_flags(selected_messages, DELETED)
