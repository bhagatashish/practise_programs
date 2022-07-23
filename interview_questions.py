import math
# set does not add repeated numbers
import pytest as pytest

x = {1,2,3,4}
x.add(5)
x.add(7)
x.add(6)

print(x)

num = [1,2,3,4 ]
print (num [-2])

print(math.sin(10))


# split function usage

string = "ashs;tet;tete"
print(string.split(';'))
print(string.split())
print(string.split('t'))


@pytest.fixture(params=[{"name": "ashu", "email": "test@gmail.com", "gender": "male"}])
def forms(self, request):
    print(request.param)
    return request.param
@pytest.mark.usefixtures('forms')
def test_abc(self,forms):

    print(forms)





