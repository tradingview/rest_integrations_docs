.. links
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo

🎾 Symbol info
--------------

A *symbol* is an array of strings. It is a name of the symbol that users will see. It must be unique. Symbol names are
always in uppercase. The symbol name is validated with a regex: 

.. code-block:: none

  ^[A-Z0-9!&*+\-./\\_|=;]+$

The `/symbol_info`_ endpoint is a list of instruments and a set of rules for them. This endpoint is requested every 
hour. The answer must include a ``"s": "ok"`` field, and a ``"Content-Type": "application/json"`` header.

With :ref:`division into symbol groups <groups-division>`, API must return symbols regardless of the parameters in the 
query to the `/symbol_info`_.

If the symbol groups exist, their names should have a perfix as broker's name. In this case, a request to the 
`/symbol_info`_ without ``groups`` parameter must return and error.

Rules of symbol naming
......................

The symbols names, which are sending to the `/symbol_info`_  side are converted differently for different types of 
instruments on the TradingView side. But all names must be specified in one piece, uppercase, without special 
characters.

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
``<Traded Exchange>:<Symbol>.<Exchange suffix>``

.. code-block:: cfg

	CFD at NASDAQ:AAPL → EXCHANGENAME:AAPL.NASDAQ
	CFD at ASX:AAPL → EXCHANGENAME:AAPL.ASX
	
Indexes
~~~~~~~
``<Index>:<Symbol>``

.. code-block:: cfg

	$MYLX → INDEX:MYLX
	.MYLX → INDEX:MYLX
	$TXDV → INDEX:TXDV
	.TXDV → INDEX:TXDV
	
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

+-----------+-------+
| Month     | Code  |
+===========+=======+
| January   | ``F`` |
+-----------+-------+
| February  | ``G`` |
+-----------+-------+
| March     | ``H`` |
+-----------+-------+
| April     | ``J`` |
+-----------+-------+
| May       | ``K`` |
+-----------+-------+
| June      | ``M`` |
+-----------+-------+
| July      | ``N`` |
+-----------+-------+
| August    | ``Q`` |
+-----------+-------+
| September | ``U`` |
+-----------+-------+
| October   | ``V`` |
+-----------+-------+
| November  | ``X`` |
+-----------+-------+
| December  | ``Z`` |
+-----------+-------+

Crypto
~~~~~~
``<Exchange>:<Root><2 Digit Day(optional)><Month Code><4 Digit Year>``

.. code-block:: cfg

	BTCUSD → OKEX:BTCUSD // crypto pair
	BTCUSDTPERP → OKEX:BTCUSDTPERP // perpetual swap contract
	BTCUSDT25H2022 → BITMEX:BTCUSDT25H2022 // futures contract