.. links
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo

.. _symbol-info-endpoint:

Symbol info
-----------

The `/symbol_info`_ endpoint returns a list of instruments and a set of rules for them.
This endpoint is requested every hour.

Response fields
................

The response body (JSON) must include an ``s`` field.
The response header must include the ``Content-Type`` header with the ``application/json`` value.

A ``symbol`` field is an array of strings. Each array item represents the name of the symbol that users will see. It must be unique. Symbol 
names are always displayed in uppercase. The symbol name is validated with a regex:

.. code-block:: none

  [A-Z0-9._]

Note that some optional fields in `/symbol_info`_ may be required depending on the instrument type:

- For CFDs, the ``is-cfd`` flag must be set to ``true``.
- For futures, the ``root`` and ``root-description`` fields are required.

Symbol groups
..............

If you have :ref:`groups <groups-endpoint>` implemented,
requests to `/symbol_info`_ can be either with or without the ``group`` parameter.
In the first case, TradingView expects to receive a list of only those symbols that belong to the group specified.
In the second case, TradingView expects to receive a list of all symbols from all groups.

Note that the symbol group ID must contain a broker name as a prefix to the group name.

If you :ref:`do not have groups implemented <groups-division>`,
your API must return symbols regardless of the parameters in the query to `/symbol_info`_.

Symbol naming rules
......................

Here are the symbol naming rules for different instrument types:

- `Stocks <#stocks>`__
- `Forex <#forex>`__
- `Futures <#futures>`__
- `Crypto <#crypto>`__

Stocks
~~~~~~

+---------------------------------+---------------------------------------+--------------------------------------------+
| Type                            | Format                                | Example                                    |
+=================================+=======================================+============================================+
| Stocks from one exchange        | ``<Exchange Ticker>``                 | ``AAPL`` — Apple stock                     |
+---------------------------------+---------------------------------------+--------------------------------------------+
| Stocks from different exchanges | ``<Exchange Code>_<Exchange Ticker>`` | ``NASDAQ_AAPL`` — Apple stock from Nasdaq  |
|                                 |                                       |                                            |
|                                 |                                       | ``ASX_AAPL`` — Apple stock from ASX        |
+---------------------------------+---------------------------------------+--------------------------------------------+

Forex
~~~~~~

+---------------------------------------+--------------------------------------------+
| Format                                | Example                                    |
+=======================================+============================================+
| ``<Base Currency><Quote Currency>``   | ``EURUSD`` — Euro to US Dollar             |
|                                       |                                            |
|                                       | ``USDGBP`` — US Dollar to British Pound    |
+---------------------------------------+--------------------------------------------+
	
Futures
~~~~~~~~

+-----------------------------------------------------+--------------------------------------------------------------------------+
| Type                                                | Format                                                                   |
+=====================================================+==========================================================================+
| Standard                                            | ``<Symbol Root><Month Code><Four-digit Year>``                           |
|                                                     |                                                                          |
|                                                     |                                                                          |
+-----------------------------------------------------+--------------------------------------------------------------------------+
| When more than one contract is expired in one month | ``<Symbol Root><Two-digit Expiration Day><Month Code><Four-digit Year>`` |
|                                                     |                                                                          |
|                                                     |                                                                          |
+-----------------------------------------------------+--------------------------------------------------------------------------+

The table below represents months and their corresponding codes:

+-----------+------------+
| Month     | Month Code |
+===========+============+
| January   | F          |
+-----------+------------+
| February  | G          |
+-----------+------------+
| March     | H          |
+-----------+------------+
| April     | J          |
+-----------+------------+
| May       | K          |
+-----------+------------+
| June      | M          |
+-----------+------------+
| July      | N          |
+-----------+------------+
| August    | Q          |
+-----------+------------+
| September | U          |
+-----------+------------+
| October   | V          |
+-----------+------------+
| November  | X          |
+-----------+------------+
| December  | Z          |
+-----------+------------+

Consider the examples below:

.. code-block:: cfg

	ESM2023       // S&P 500 future contract (June 2023)
	NQZ2023       // Nasdaq-100 future contract (December 2023)
	BTCUSD24M2022 // Bitcoin future contract quoted in US Dollar (June 24, 2022)
	BTCUSD30M2022 // Bitcoin future contract quoted in US Dollar (June 30, 2022)

Crypto
~~~~~~

+-------------------------------------------------------+------------------------------------------------------------------------------+
| Type                                                  | Format                                                                       |
+=======================================================+==============================================================================+
| Base crypto pair                                      | ``<Base Currency><Quote Currency>``                                          |
+-------------------------------------------------------+------------------------------------------------------------------------------+
| Leveraged crypto ETF's                                | ``<Base Currency><Quote Currency>.<Leverage Size><Long or Short Direction>`` |
|                                                       |                                                                              |
|                                                       |                                                                              |
+-------------------------------------------------------+------------------------------------------------------------------------------+
| Future contracts                                      | See the `Futures <#futures>`__ section.                                      |
+-------------------------------------------------------+------------------------------------------------------------------------------+
| Perpetual swap contracts                              | ``<Base Currency><Quote Currency>.P``                                        |
+-------------------------------------------------------+------------------------------------------------------------------------------+
| Decentralized exchanges (DEX)                         | ``<Base Currency><Quote Currency>_<First Six Hash Numbers of the Pair>``     |
+-------------------------------------------------------+------------------------------------------------------------------------------+
| DEX for pairs converted to USD or other fiat currency | ``<Base Currency><Quote Currency>_<First Six Hash Numbers of the Pair>.USD`` |
+-------------------------------------------------------+------------------------------------------------------------------------------+

The corresponding examples are added below:

.. code-block:: cfg

	BTCUSD            // Bitcoin / US Dollar crypto pair
	BTCUSDT.3L        // Bitcoin 3× Long 
	BTCUSDT.3S        // BTC 3× Short
	BTCUSDT.P         // Bitcoin perpetual swap contract
	ETHUSD_7380E1     // Ethereum / BTCB on BSC in US Dollar
	ETHUSD_7380E1.USD // Ethereum / BTCB on BSC in US Dollar (converted to USD)

Price display
......................

To manage how the price is displayed on the chart, use the following parameters in `/symbol_info`_.

-  ``minmovement`` indicates the number of units that make one price tick.
-  ``pricescale`` indicates how many decimal places a security price has.
-  ``minmovement2`` indicates the pip size for Forex prices or how to separate the main and additional fractions for fractional prices.

The parameter values depend on the price format chosen. 
There are two ways to display a security price:

-  The `decimal <#decimal-format>`__ format is used for most instruments, such as stocks, indices, and futures.
-  The `fractional <#fractional-format>`__ format is used only for futures traded on the CBOT (Chicago Board of Trade), 
   including futures on bulk commodities (grains, etc.) and US Federal Reserve Government bonds. 
   This format also has a variety — that is a fractional format of the fractional price.

Decimal format
~~~~~~~~~~~~~~

For the decimal format:

-  The ``minmovement`` value depends on the price tick chosen: 1, 5, etc.
-  The ``pricescale`` value must always be ``10^n``, where *n* is the number of decimal places. 
   For example, if the price has two decimal places ``300.01``, ``pricescale`` must be ``100``. 
   If it has three decimal places ``300.001``, ``pricescale`` must be ``1000``, etc. 
   If the price doesn't have decimals, ``pricescale`` must be ``1``.
-  The ``minmovement2`` value must always be ``0``, except for `Forex symbols <#forex-symbols>`__.

Forex symbols
^^^^^^^^^^^^^

Forex symbols have the decimal price format, however, the ``minmovement2`` value must differ from ``0``.
In this case, ``minmovement2`` indicates the pip size on the chart and the value must be ``10^n``, where ``n`` is the number of pips. 
A pip is the smallest whole unit measurement of the spread.
On the chart, the pip is displayed smaller than the price digits.

.. image:: ../../images/Data_SymbolInfo_PriceDisplay_ForexSymbols.png
   :scale: 100 %
   :alt: Order Dialog
   :align: center

.. note::
	If ``minmovement2`` is ``0`` for Forex symbols, the spread is displayed in ticks, not pips.

Fractional format
~~~~~~~~~~~~~~~~~

The price in the fractional format is displayed as ``76'27``.
A single quote is used as a delimiter.

For the fractional format:

-  The ``minmovement`` value depends on the price tick chosen: 1, 5, etc.
-  The ``pricescale`` value must always be ``2^n``.
   It indicates the number of fractions.
   For example, if ``minmovement: 1`` and ``pricescale: 32``, the fraction numerator values can vary from 0 to 31.
-  The ``minmovement2`` value must always be ``0``, except for the fraction of fractional format.

Fractional format of the fractional price
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The fractional format of the fractional price is a particular case of the fractional price format. 
In this case, ``minmovement2`` indicates the part of the fraction and can differ from ``0``.

For example, for the ``76'27'2`` price: 76 is an integral part of the price, 27 is a fractional part of the price,
and 2 is a fractional part of the first fractional part (27).
To display such a price, you can specify the parameters in the following way: ``minmovement: 1``, ``pricescale: 128``, and ``minmovement2: 4``.

Tick size
...........

Tick size (minimum price step) is the minimum price amount a security can move in exchange. 
The tick size is calculated as ``minmovement``/ ``pricescale``.
For example, if you need a price step to be ``0.25``:

-  Set ``minmovement: 25`` and ``pricescale: 100`` for the decimal format.
-  Set ``minmovement: 1`` and ``pricescale: 4`` for the fractional format.
