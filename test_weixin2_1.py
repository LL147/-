from po.app import App
import pytest

class TestCase:
    def test(self):
        app1 = App()
        app1.start()
        result = app1.goto_main().goto_contact().add_connect().add_manully().add_information()
        assert result

