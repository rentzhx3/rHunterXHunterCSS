#!/usr/bin/python
import re


pattern = r".*(https://localhost/hunter/(.*)(\.png|\.jpg)).*";
files = []
with open("style.css","r") as f:
    with open("reddit.css","w") as out:
        for line in f:
            match = re.match(pattern,line)
            if(match):
                if match.group(2) not in files:
                    files.append(match.group(2))
                line = line.replace(match.group(1),"%%"+match.group(2)+"%%")
            out.write(line)

print files