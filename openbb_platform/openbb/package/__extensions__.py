### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###


from openbb_core.app.static.container import Container


class Extensions(Container):
    # fmt: off
    """
Routers:
    /commodity
    /crypto
    /currency
    /derivatives
    /econometrics
    /economy
    /equity
    /etf
    /fixedincome
    /index
    /news
    /quantitative
    /regulators
    /technical

Extensions:
    - commodity@1.2.5
    - crypto@1.3.4
    - currency@1.3.4
    - derivatives@1.3.4
    - econometrics@1.4.4
    - economy@1.3.4
    - equity@1.3.4
    - etf@1.3.4
    - fixedincome@1.3.4
    - index@1.3.4
    - news@1.3.4
    - quantitative@1.3.4
    - regulators@1.3.4
    - technical@1.3.4

    - alpha_vantage@1.3.4
    - benzinga@1.3.4
    - biztoc@1.3.4
    - bls@1.0.2
    - cboe@1.3.4
    - cftc@1.0.2
    - ecb@1.3.4
    - econdb@1.2.4
    - federal_reserve@1.3.4
    - finra@1.3.4
    - finviz@1.2.4
    - fmp@1.3.4
    - fred@1.3.4
    - government_us@1.3.4
    - imf@1.0.1
    - intrinio@1.3.4
    - multpl@1.0.4
    - nasdaq@1.3.4
    - oecd@1.3.4
    - polygon@1.3.4
    - sec@1.3.4
    - seeking_alpha@1.3.4
    - stockgrid@1.3.4
    - tiingo@1.3.4
    - tmx@1.2.4
    - tradier@1.2.4
    - tradingeconomics@1.3.4
    - wsj@1.3.4
    - yfinance@1.3.5    """
    # fmt: on

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @property
    def commodity(self):
        # pylint: disable=import-outside-toplevel
        from . import commodity

        return commodity.ROUTER_commodity(command_runner=self._command_runner)

    @property
    def crypto(self):
        # pylint: disable=import-outside-toplevel
        from . import crypto

        return crypto.ROUTER_crypto(command_runner=self._command_runner)

    @property
    def currency(self):
        # pylint: disable=import-outside-toplevel
        from . import currency

        return currency.ROUTER_currency(command_runner=self._command_runner)

    @property
    def derivatives(self):
        # pylint: disable=import-outside-toplevel
        from . import derivatives

        return derivatives.ROUTER_derivatives(command_runner=self._command_runner)

    @property
    def econometrics(self):
        # pylint: disable=import-outside-toplevel
        from . import econometrics

        return econometrics.ROUTER_econometrics(command_runner=self._command_runner)

    @property
    def economy(self):
        # pylint: disable=import-outside-toplevel
        from . import economy

        return economy.ROUTER_economy(command_runner=self._command_runner)

    @property
    def equity(self):
        # pylint: disable=import-outside-toplevel
        from . import equity

        return equity.ROUTER_equity(command_runner=self._command_runner)

    @property
    def etf(self):
        # pylint: disable=import-outside-toplevel
        from . import etf

        return etf.ROUTER_etf(command_runner=self._command_runner)

    @property
    def fixedincome(self):
        # pylint: disable=import-outside-toplevel
        from . import fixedincome

        return fixedincome.ROUTER_fixedincome(command_runner=self._command_runner)

    @property
    def index(self):
        # pylint: disable=import-outside-toplevel
        from . import index

        return index.ROUTER_index(command_runner=self._command_runner)

    @property
    def news(self):
        # pylint: disable=import-outside-toplevel
        from . import news

        return news.ROUTER_news(command_runner=self._command_runner)

    @property
    def quantitative(self):
        # pylint: disable=import-outside-toplevel
        from . import quantitative

        return quantitative.ROUTER_quantitative(command_runner=self._command_runner)

    @property
    def regulators(self):
        # pylint: disable=import-outside-toplevel
        from . import regulators

        return regulators.ROUTER_regulators(command_runner=self._command_runner)

    @property
    def technical(self):
        # pylint: disable=import-outside-toplevel
        from . import technical

        return technical.ROUTER_technical(command_runner=self._command_runner)
