import pytest
class TestDemo():
    def test_answer(self):
        assert 3 == 5


if __name__ == '__main__':
    pytest.main("-v -x TestDemo")