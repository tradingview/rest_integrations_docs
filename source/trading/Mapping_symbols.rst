.. links:
.. _`/instruments`: https://www.tradingview.com/rest-api-spec/#operation/getInstruments
.. _`/mapping`: https://www.tradingview.com/rest-api-spec/#operation/getMapping

Symbol mapping
---------------

*Symbol mapping* is the matching between the broker's and TradingView symbols.
It helps both brokers and TradingView operate with symbols in a convenient way and avoid symbol mismatching.

When to implement
..................

The mapping is necessary when you use TradingView data available from a third-party source.
If you plan to use your symbols *only*, you don't need to implement mapping.
However, if you decide to use both TradingView (available from a third-party source) and your own data, you must implement mapping for all symbols, including yours.

How to implement
.................

To implement symbol mapping, use the `/mapping`_ endpoint.

.. note::
  `/mapping`_ must be accessible without authorization.

The endpoint must return an object in the following format:

.. code:: 
  {
    "symbols": [
      {
        "f": ["EURUSD"],
        "s": "FX_IDC:EURUSD"
      },
      {
        "f": ["AAPLE"],
        "s": "NASDAQ:AAPLE"
      }
    ],
    "fields": ["brokerSymbol"]
  }

Here, ``symbols`` is an array of objects describing symbols. Every object contains two required properties:

- ``f`` is a broker symbol name. Note that the ``f`` value must always consist of an array with only one string element.
- ``s`` is a TradingView symbol name with a prefix. Refer to the `broker-symbols.json file <#how-to-match-symbols>`__ to find the TradingView symbols corresponding to the broker ones.

The ``fields`` property must always contain an array with a ``brokerSymbol`` value.

.. _trading-mapping-how-to-match-symbols:

How to match symbols
....................

To match symbols properly, refer to the *broker-symbols.json* file which contains a list of symbols available on TradingView.
This file is updated daily.

.. note::
  The *broker-symbols.json* file is available upon request. Ask your TradingView manager to get access to it.

In the file, each symbol has its own meta-data such as full name and description.
The ``symbol-fullname`` property contains the full symbol name with a prefix.
As response to a request, use ``symbol-fullname`` value in the ``symbols.s`` property as the TradingView symbol name.

How often requests are made
............................

In TradingView production and staging, `/mapping`_ is requested twice a day.
Based on the response, mapping is generated on the TradingView side.
During development, you can implement partial mapping, not for all supported instruments.

How to test the endpoint
..........................

Use the :doc:`trading integration test <../trading_tests/index>` to check the accuracy of symbol mapping. 
The test verifies that symbols in the `/instruments`_ match the TradingView symbols.
