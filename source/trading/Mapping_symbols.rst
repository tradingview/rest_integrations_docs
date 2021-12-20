.. links:
.. _`/instruments`: https://www.tradingview.com/rest-api-spec/#operation/getInstruments
.. _`/mapping`: https://www.tradingview.com/rest-api-spec/#operation/getMapping
.. _`/orders`: https://www.tradingview.com/rest-api-spec/#operation/placeOrder
.. _`/positions`: https://www.tradingview.com/rest-api-spec/#operation/getPositions

Mapping symbols
---------------

What is mapping
...............
We call *mapping symbols* the matching between the names of the broker's instruments and TradingView.
This mapping solves the problem of TradingView and broker symbol names mimatching.

Mapping is necessary if the broker does not integrate its data in whole or in part on the TradingView servers but
uses the data already connected.

How to implement mapping
........................
Mapping is set with the `/mapping`_ endpoint implementation. This endpoint must be accessible without 
authorization. In TradingView production, it is automatically requested once a day. Based on the response to the 
request, a mapping of instruments is generated on the TradingView side. In TradingView staging, the `/mapping`_ 
request is made manually if necessary. At the development stage, you can set a partial mapping, i.e. not for all 
instruments supported by the broker.

How to match symbols
....................
You can use *symbols.json* (available upon request) with a complete list of all symbols to search for a 
TradingView symbol. This file is updated daily.

In response to a request to the `/mapping`_, use the ``symbol-fullname`` field value as the TradingView symbol.
If the broker partially uses TradingView data and partially connects its own, the mapping must be implemented 
for all symbols.

The ``symbol-type`` field in *symbols.json* aims to the market instrument type. A symbol can be traded on the different
exchanges. In this case, ``symbol`` fields will be the same, and fields ``exchange-traded``, ``exchange-listed`` will
differ. For example, *BLX* symbol is traded on the NYSE and NASDAQ. But ``NYSE:BLX`` is a stock, and ``NASDAQ:BLX`` is
an index.

When the user's subscription has ended, he cannot trade on the broker's platform. But the user can see already opened
positions and order on the TradingView platform. In this case broker should send these symbols at `/instruments`_.
And when a user tries to send an order, return an error message.
