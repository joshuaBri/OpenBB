"""Price Router."""
from openbb_core.app.deprecation import OpenBBDeprecationWarning
# pylint: disable=unused-argument

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

router = Router(prefix="/price")


@router.command(
    model="CommoditySpotPrices",
    deprecated=True,
    deprecation=OpenBBDeprecationWarning(
        message="Xiao Yuan doesn't support this endpoint.Please ignore.",
        since=(4, 3),
        expected_removal=(4, 5),
    ),
    examples=[
        APIEx(parameters={"provider": "fred"}),
        APIEx(parameters={"provider": "fred", "commodity": "wti"}),
    ],
)
async def spot(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Commodity Spot Prices."""
    return await OBBject.from_query(Query(**locals()))
