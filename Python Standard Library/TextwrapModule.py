# Text Wrap Module
import textwrap
websiteText = """   Learning can happen anywhere with our apps on your computer,
mobile device, and TV, featuring enhanced navigation and faster streaming
for anytime learning. Limitless learning, limitless possibilities."""

print("No Dedent : ")
print(textwrap.fill(websiteText))

print("Dedent : ")
dedentText = textwrap.dedent(websiteText).strip()
print(dedentText)

print("Fill")
print(textwrap.fill(dedentText, width=50))
print(textwrap.fill(dedentText, width=100))

print("Controlling Indent")
print(textwrap.fill(dedentText, initial_indent="  ", subsequent_indent="          "))


print("Shortening Text")
short = textwrap.shorten("LinkedIn is great!", width=15, placeholder="...")
print(short)