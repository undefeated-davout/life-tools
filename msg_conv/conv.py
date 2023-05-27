import os
import extract_msg

msg = extract_msg.Message("test.msg")

# Get the email body
body = msg.body
print(body)

# Get attachments
attachments = msg.attachments

# Create a directory for the attachments if it does not exist
if not os.path.isdir("attachments"):
    os.makedirs("attachments")

# Save all attachments in the directory
for attachment in attachments:
    with open(f"attachments/{attachment.longFilename}", "wb") as fp:
        fp.write(attachment.data)
