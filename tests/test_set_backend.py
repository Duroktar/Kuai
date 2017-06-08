from kuai import Kuai, set_backend


def test_set_backend():
    set_backend('simple')
    assert Kuai.which_backend == 'simple'
    set_backend('priority')
    assert Kuai.which_backend == 'priority'
    set_backend('simple')
    assert Kuai.which_backend == 'simple'
