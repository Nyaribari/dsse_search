#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle

import dsse_c

if __name__ == "__main__":
    client = dsse_c.DSSEClient()
    client.Gen()
    pickle.dump(client.exportkeys(), open("key.json", "wb"))
