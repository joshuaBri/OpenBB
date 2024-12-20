"""Fund Router."""

from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.example import APIEx
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from openbb_core.app.router import Router

router = Router(prefix="", description="Exchange Traded Funds market data.")


# pylint: disable=unused-argument

@router.command(
    model="FundInfo",
    examples=[
        APIEx(parameters={"symbol": "000001.OF", "provider": "xiaoyuan"}),
    ],
)
async def info(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject:
    """Fund Information Overview."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="FundHoldings",
    examples=[
        APIEx(
            description="return the holdings of fund.",
            parameters={"symbol": "000001.OF", "provider": "xiaoyuan"},
        ),
    ],
)
async def holdings(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject:
    """Get the holdings for an individual Fund."""
    return await OBBject.from_query(Query(**locals()))
