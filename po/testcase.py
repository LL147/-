from po import app
from po.app import App


def start(self):
    app = App()
    app.start()
    result = app.goto_main().goto_contact().add_connect().add_manully().add_information()
    assert result