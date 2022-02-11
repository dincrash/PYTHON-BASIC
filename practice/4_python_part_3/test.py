import mock

from mymodule import main


@mock.patch('mymodule.process')
def test_main(process):
    main([])
    process.assert_call_once_with(a=None)


@mock.patch('foo.process')
def test_main_a(process):
    main(['-a', '1'])
    process.assert_call_once_with(a='1')