#!/bin/python3

def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, remaining = s.split("@")
        website, extension = remaining.split(".")
    except:
        return False
    return all( [ ( username.replace( "-","").replace( "_","").isalnum()),\
              website.isalnum(), len( extension) <= 3])