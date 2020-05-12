import pytest

from src.person import Person

class TestPytestDemo(object):

    def setup_class(self):
        pass

    @pytest.mark.asserttest
    def test_str(self):
        b = "hello"
        assert "h" in b, "字符h期望在单词hello中出现"

    def test_person(self):
        testPerson = Person('Test')
        assert testPerson.sayHi() == "Hi, my name is Test"
