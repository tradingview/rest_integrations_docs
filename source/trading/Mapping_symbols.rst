.. links:
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups
.. _`/instruments`: https://www.tradingview.com/rest-api-spec/#operation/getInstruments
.. _`/mapping`: https://www.tradingview.com/rest-api-spec/#operation/getMapping
.. _`/permissions`: https://www.tradingview.com/rest-api-spec/#operation/getPermissions

Symbol mapping
---------------

What is mapping
...............

*Symbol mapping* is the matching between the names of the broker's and TradingView instruments.
It helps both brokers and TradingView operate with symbols in a convenient way and avoid symbol mismatching.

.. important::
    The mapping is necessary when you use Tradinview data available from a third-party source.

How to implement mapping
........................

To implement symbol mapping, use the `/mapping`_ endpoint 
This endpoint must be accessible without authorization.

In TradingView production, `/mapping`_ is automatically requested once a day. 
Based on the response to the request, instrument mapping is generated on the TradingView side. 
In TradingView staging, the `/mapping`_ request is made manually if necessary.
At the development stage, you can set a partial mapping, not for all instruments supported by the broker.

.. _trading-mapping-how-to-match-symbols:

How to match symbols
....................

You can use *symbols-brokers.json* (available upon request) with a complete list of all symbols to search for a 
TradingView symbol. This file is updated daily.

In response to a request to the `/mapping`_, use the ``symbol-fullname`` field value as the TradingView symbol.
If the broker partially uses TradingView data and partially connects its own, the mapping must be implemented 
for all symbols.

The ``symbol-type`` field in *symbols.json* aims to the market instrument type. A symbol can be traded on different
exchanges. In this case, the ``symbol`` fields will be the same, whereas the ``exchange-traded`` and ``exchange-listed`` fields will
differ. For example, the ``BLX`` symbol is traded on the NYSE and NASDAQ. But ``NYSE:BLX`` is a stock, and ``NASDAQ:BLX`` is
an index.

When the user's subscription has ended, they cannot trade on the broker's platform. But the user can see already opened
positions and orders on the TradingView platform. 
In this case, the broker should send these symbols to `/instruments`_ and return an error message when the user tries to send an order.

Use :doc:`our test <../trading_tests/index>` to check the accuracy of symbol mapping. The test will verify, that 
the symbols in the `/instruments`_ are matching with TradingView symbols.

How to restrict access to different symbols
............................................

If you need to manage symbol access for users, implement the following endpoints:

- `/groups`_ gets a list of symbols with different access level.
- `/permissions`_ gets a list of groups allowed for a user.

Restricting access is needed when you want to divide content for subscribed and free users.

.. note::
    Learn more about access restrictions in the :ref:`Permissions <permissions-endpoint>` and :ref:`Groups <groups-endpoint>` articles.