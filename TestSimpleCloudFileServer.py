#!/usr/bin/python

"""
Copyright 2017 Ben Wheatley

This is what needs to be tested, but I don't know how to write and run Python server unit tests yet.
"""

# name: url -> status, result (optional)

load_index: url=="http://localhost:8000/index.json" -> status==200

upload_file: <how?> -> status==200, result==<json with number>

download_file: url=="http://localhost:8000/<result of upload_file>" -> status==200, result==<identical image data to that which was uploaded>

download_nonexistent_file: url=="http://localhost:8000/<value not in load_index>" -> status==404

injection_attack_python: url=="http://localhost:8000/print(\"hello\")" -> status==404
# Anything more than this level of injection-proof testing should be done with Metasploit, which will know more server failure modes than I've heard of