.. links:
.. _/mapping: https://www.tradingview.com/rest-api-spec/#operation/getMapping
.. _`symbols.json`: https://s3.amazonaws.com/tradingview-symbology/symbols.json

Mapping symbols
---------------

What is mapping
...............
We call mapping symbols the mapping between the names of the broker's instruments and TradingView.
This mapping avoids the problem of matching TradingView and broker symbol names.

Mapping is necessary if the broker does not integrate its data in whole or in part on the TradingView servers but
uses the data already connected.

How to implement mapping
........................
Mapping is set with the `/mapping`_ endpoint implementation. This endpoint must be accessible without 
authorization. In TradingView production, it is automatically requested once a day. Based on the response to the 
request, a mapping of instruments is generated on the TradingView side. In TradingView staging, the ``/mapping`` 
request is made manually if necessary. At the development stage, you can set a partial mapping, i.e. not for all 
instruments supported by the broker.

How to match symbols
....................
You can use `symbols.json`_ with a complete list of all symbols to search for a TradingView symbol. This file is 
updated daily.

In response to the `/mapping`_ request, use the ``symbol-fullname`` field value as the TradingView symbol.
If the broker partially uses TradingView data and partially connects its own, the mapping must be implemented 
for all symbols.