import os


def mpath_file_locations(configs):
    bindings_file = None
    wwids_file = None
    prkeys_file = None
    for conf in configs:
        bindings_file = conf.bindings_file or bindings_file
        wwids_file = conf.wwids_file or wwids_file
        prkeys_file = conf.prkeys_file or prkeys_file
    return (bindings_file, wwids_file, prkeys_file)
