from guerrillamail import GuerrillaMailSession
from guerrillamail import *

session = GuerrillaMailSession()
session.set_email_address('sanumolu')
print(session.get_session_state()['email_address'])
print(session.get_email_list()[0].guid)
print(session.get_email_list())
emaillist = session.get_email_list()
for email in emaillist:
    print(email.guid)
    emailattr = session.get_email(email.guid)
    print(emailattr.sender)
    print(emailattr.body)

