import tempfile

with tempfile.TemporaryFile() as myTempFile:
    myTempFile.write(b"Please save the special number : 54789654")
    myTempFile.seek(0)

    print(myTempFile.read())