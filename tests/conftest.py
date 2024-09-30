import asyncio

import pytest

@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.mark.anyio
@pytest.fixture(scope="session", autouse=True)
async def afixture() -> int:
    await asyncio.sleep(5)
    return 1
