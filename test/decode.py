import base64

encoded_url = b'aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQUlwUUxTZHpldmE0Zl9JbTBMTUowMUtRa1dEX05iV1N1YjRrcVRLM19rRG1LcXdQcGlxbUN3L3ZpZXdmb3JtP2VkaXQyPTJfQUJhT251ZXQzS3Mwdk90X0JhNE51WU9sWUgyT3paMlB6QjhUZmp6MFU0NWRaWHlDWExENF9JQ1NLZHBSd2xyUXNJNGVzT3M='

print(base64.urlsafe_b64decode(encoded_url.decode()))
