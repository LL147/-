from test_xueqiu.po.app import App

class TestCase:
    def test(self):
        app = App()
        app.start()
        app.goto_main().main().search().content()
