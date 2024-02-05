import pytest

import aioicloud


@pytest.mark.asyncio
async def test_hello_world():
    assert aioicloud.hello_world() == "Hello, World!"
