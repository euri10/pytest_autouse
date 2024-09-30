import pytest

from src import __version__


# using this test first the afixture in conftest is executed fine,
# tests takes the 5s sleep of the fixture and prints 1
# @pytest.mark.anyio
# async def test_version() -> None:
#     assert __version__ == "0.1.0"

# using this test 1st instead, the afixture in conftest is not called
# and the print returns coroutine...
def test_version() -> None:
     assert __version__ == "0.1.0"


@pytest.mark.anyio
async def test_afixture(afixture: int):
    print(afixture)
    assert True
