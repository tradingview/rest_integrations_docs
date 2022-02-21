.. links
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo

Symbol info
-----------

A ``symbol`` field is an array of strings. It is a name of the symbol that users will see. It must be unique. Symbol 
names are always displayed in uppercase. The symbol name is validated with a regex:

.. code-block:: none

  ^[A-Z0-9!&*+\-./\\_|=;]+$

The `/symbol_info`_ endpoint returns a list of instruments and a set of rules for them. This endpoint is requested
every hour. The response body (JSON) must include an ``s`` field. The response header must include ``Content-Type`` 
header with ``application/json`` value.

With :ref:`division into symbol groups <groups-division>`, API must return symbols regardless of the parameters in the 
query to the `/symbol_info`_.

If the symbol groups exist, their names should have a prefix as broker\'s name. In this case, a request to the 
`/symbol_info`_ without groups parameter must return and error.

Rules of symbol naming
......................

Here are the rules of symbol naming for different types of instruments on the TradingView\'s side.

Stocks
~~~~~~
``<Traded Exchange>:<Symbol>``

.. code-block:: cfg

	AAPL → NASDAQ:AAPL
	IBM → NYSE:IBM
	AAA → TSX:AAA
	ADW-B → TSX:ADW-B
	AAN → TSXV:AAN
	AFLT → MICEX:AFLT

Stocks from the different exchanges under one prefix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``<Traded Exchange>:<Exchange suffix>_<Symbol>``

.. code-block:: cfg

	CFD at NASDAQ:AAPL → EXCHANGENAME:NASDAQ_AAPL
	CFD at ASX:AAPL → EXCHANGENAME:ASX_AAPL
	
Forex
~~~~~
``<FX>:<Currecny><Currency>``

.. code-block:: cfg

	EURUSD → FX:EURUSD
	USDEUR → FX:USDEUR
	
Features
~~~~~~~~
``<Exchange>:<Root><2 Digit Day(optional)><Month Code><4 Digit Year>``

.. code-block:: cfg

	IMH2 → LIFFE:IMH2012
	MAH2 → EUIDX:MAH2012
	AVU2 → EUREX:AVU2012

If more than one contract is expired in one month, the expiration day is added to the name after the root.

.. code-block:: cfg

	BTCUSD → OKEX:BTCUSD24M2020
	ETHBTC → BITMEX:ETHBTC30U2020

Crypto
~~~~~~
``<Exchange>:<Root><2 Digit Day(optional)><Month Code><4 Digit Year>``

.. code-block:: cfg

	BTCUSD → OKEX:BTCUSD // crypto pair
	BTCUSDTPERP → OKEX:BTCUSDTPERP // perpetual swap contract
	BTCUSDT25H2022 → BITMEX:BTCUSDT25H2022 // futures contract