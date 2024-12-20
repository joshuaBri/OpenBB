"""Fundamental Analysis Router."""

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

router = Router(prefix="/fundamental")

# pylint: disable=unused-argument


@router.command(
    model="IndexTrailingDividendYield",
    examples=[
        APIEx(parameters={"symbol": "000001.SS", "provider": "akshare"}),
    ],
)
async def trailing_dividend_yield(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get the trailing dividend yield for a given company over time."""
    return await OBBject.from_query(Query(**locals()))
