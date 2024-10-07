# sync first fails

```python
import pytest

from src import __version__


def test_version() -> None:
    assert __version__ == "0.1.0"

# @pytest.mark.anyio
# async def test_version() -> None:
#     assert __version__ == "0.1.0"

@pytest.mark.anyio
async def test_afixture(afixture: int):
    print(afixture)
    assert afixture == 1
```

# async first passes

```python
import pytest

from src import __version__


# def test_version() -> None:
#     assert __version__ == "0.1.0"

@pytest.mark.anyio
async def test_version() -> None:
    assert __version__ == "0.1.0"

@pytest.mark.anyio
async def test_afixture(afixture: int):
    print(afixture)
    assert afixture == 1
```
