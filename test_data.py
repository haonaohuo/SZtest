import  pytest

class TestData:
    @pytest.mark.parametrize("a,b",[(10,20),(10,30)])
    def test_data(self,a,b):
        print(a+b)
