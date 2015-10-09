import unittest

import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = party.app.test_client()

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("I'm having a party", result.data)

    def test_no_rsvp_yet(self):
        # FIXME: Add a test to show we haven't RSVP'd yet
        print "FIXME"

    def test_rsvp(self):
        result = self.client.post("/rsvp",
                                  data={'name': "Jane", 'email': "jane@jane.com"},
                                  follow_redirects=True)
        # FIXME: check that once we log in, we see party details -- and don't see form!
        print "FIXME"

    def test_rsvp_mel(self):
        # FIXME: write a test that mel can't invite himself
        pass
        print "FIXME"

if __name__ == "__main__":
    unittest.main()