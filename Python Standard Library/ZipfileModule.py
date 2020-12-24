import zipfile

# open and list

zips = zipfile.ZipFile("Archive.zip", 'r')
print(zips.namelist())

# Metadata in the zip folder
for meta in zips.infolist():
    print(meta)

info = zips.getinfo("purchase.txt")
print(info)

# Access to file in the zip folder
print(zips.read("wishlist.txt"))

with zips.open("purchase.txt") as filezips:
    print(filezips.read())

# Extract files
zips.extract("wishlist.txt")
zips.extractall()