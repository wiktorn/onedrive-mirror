from onedrivemirror import MirrorClient, create_session_file

import unittest


class MirrorTests(unittest.TestCase):

    @unittest.skip
    def test_create_session_file(self):
        create_session_file("test.session")

    def test_mirror(self):
        client = MirrorClient("test.session")

        client.mirror("visualvm_139", "copy")