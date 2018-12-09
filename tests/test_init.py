import src as app


def test_get_input():
    assert app.get_input('hi "2017/02/10 5:00"') == {'filename': 'hi', 'start_time': '2017/02/10 05:00'}
    assert app.get_input('hi hi  hi  ') is None
