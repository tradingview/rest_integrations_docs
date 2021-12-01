.. links
.. _`/accounts`: https://www.tradingview.com/rest-api-spec/#operation/getAccounts
.. _`/authorize`: https://www.tradingview.com/rest-api-spec/#operation/authorize
.. _`/config`: https://www.tradingview.com/rest-api-spec/#operation/getConfiguration
.. _`/depth`: https://www.tradingview.com/rest-api-spec/#operation/getDepth
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory
.. _`/instruments`: https://www.tradingview.com/rest-api-spec/#operation/getInstruments
.. _`/logout`: https://www.tradingview.com/rest-api-spec/#operation/logout
.. _`/mapping`: https://www.tradingview.com/rest-api-spec/#operation/getMappin
.. _`/orders`: https://www.tradingview.com/rest-api-spec/#operation/placeOrder
.. _`/ordersHistory`: https://www.tradingview.com/rest-api-spec/#operation/getOrdersHistory
.. _`/permissions`: https://www.tradingview.com/rest-api-spec/#operation/getPermissions
.. _`/positions`: https://www.tradingview.com/rest-api-spec/#operation/getPositions
.. _`/quotes`: https://www.tradingview.com/rest-api-spec/#operation/getQuotes
.. _`/state`: https://www.tradingview.com/rest-api-spec/#operation/getState
.. _`/streaming`: https://www.tradingview.com/rest-api-spec/#operation/streaming
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo
.. _`streamingHistoryEquality`: https://github.com/tradingview-inspect/tests/wiki/streamingHistoryEquality

Data integration
****************

===
FAQ
===

How does *Symbol* differs to *Tickers*.
   *Symbol* --- the name of the instrument that will be shown to users.  *Ticker* --- the name of instrument that our
   data feed will use for requests to the server (for example ``/history?symbol= {ticker}``). Ticker is optional. If
   there is no *Ticker* then we will use *Symbol* for requests.

If the broker is satisfied with TradingView instruments, can we not send anything to `/symbol_info`_ and not implement `/streaming`_ and `/history`_?
   That’s right, the data integration is irrelevant when you are using only TradingView instruments.

How to set up session time for data integration?
   The session schedule is regulated in the `/symbol_info`_ with next paremeters: ``session-regular``, 
   ``session-premarket``, ``session-postmarket``, and ``session-extended``.

I added some new symbols but they don’t show in the chart. Do you call `/symbol_info`_ regularly or do you need to do it manually?
   We request `/symbol_info`_ every hour and automatically update it if everything is ok. But if we find some critical
   changes or invalid values, manual verification will be required.

We want to show to our users only our broker's symbols in the symbol search. How to set it up?
   After login into the brokerage account, a user has enabled filter in the symbol search. So the user can see the
   broker's symbols only. But this filter can be disabled. This behavior cannot be changed.

Followeing the `/symbol_info`_ specification a symbol should contain uppercase letters, numbers, a dot or an underscore. But our exchange symbols contain the slash symbol like ``BTC/USDT``. Is it allowed or we have to do a conversion to ``BTC_USDT``?
   You can add ticker field. We will use the ticker name for requests to API, it will be used prior to symbol filed.
   Ticker has no strict requirements. symbol is what we show on the chart. so, you can have two fields:

.. code-block:: javascript

   "ticker": [
      "BTC/USDT",
      "ETH/USDT",
      "LTC/USDT"
   ],
   "symbol": [
      "BTCUSDT",
      "ETHUSDT",
      "LTCUSDT"
   ],

Does ``has-no-volume`` parameter indicate whether we can report trading volume of the symbol?
   If you can provide trading volume, just set ``has-no-volume: false`` in the `/symbol_info`_.

Our trading session opens at 17:00-16:00 CT. And we have pre-market at 16:50 CT. Should we report about pre-market within the main session?
   It depends of the bar building. We build bars using the ``session-regular`` value. For example, we build all the
   resolutions (5 min, 1 hour, 4 hours etc.) for the session 17:00-16:00 from 17:00, even if ``session-premarket.``
   value recieved.

How to use fileds ``bar-source``, ``bar-transform``, and ``bar-fillgaps`` to build bars?
   * If you need to build bars from trades, use ``bar-source: trade``. If need to build from bids, use 
     ``bar-source: bid``.
   * ``bar-transform`` is required to align the bars. Its need for cases when open price is always equal to close price
     of the previous bar. If you dont have any alignments, just omit this field.
   * ``bar-fillgaps`` generate of degenerate bars in the absence of trades (bars with zero volume and equal 
     :term:`OHLC` values).

Is `/history`_ requested only for those instruments for which we supply our quotes?
   The `/history`_ is requested for all instruments represented in the symbol field of the `/symbol_info`_.

Which requests are going to the broker's server from the TradingView server, not from client?
   From the TradingView server, requests are sent that are responsible for the data integration: `/authorize`_,
   `/groups`_, `/symbol_info`_, `/history`_, `/streaming`_.

Should we implement the ``countback`` parameter? It is marked as optional in the API.
   Your server should operate both requests. The examples of such requests you can see in the 
   :doc:`History <../data/History>` section.

What time intervals you will send in the request to the `/history`_?
   We need 1-minute intervals only, and at some cases 1-day intervals. We are building interim resolution on our
   side.

How often do you request `/history`_ to update your database?
   We send request to the `/history`_ once for the deep history filling. Afteward, we update data twice a day. We
   request `/history`_ if we didn't recive data from `/streaming`_ (as a result of provider's server side issues).

What is the expected timestamp precision for the query params ``from`` and ``to``?
   The timestamp should be specified in seconds.

How do you get prices from the brokers? The price can change more than ten times per second for each instrument.
   Endpoint `/streaming`_ is a permanent connection through which we accept changes in quotes for all instruments.

The symbol id is required for the stream of prices response. Can we use ticker format instead. i.e. return ``BTC/USDT`` instead of ``BTCUSDT``?
   Yes, it will be the correct response format for the `/streaming`_. 

Should we send ``StreamingDailyBarResponse``? Or it can be calculated from our 1-minute history inteervals and live feed data?
   You do not need to send it. If there is ``has-daily: false`` in the `/symbol_info`_, we will skip the daily updates.
   But, when it is impossible to build a day bar out of minute bars, we need to request it daily.

Is it expected that the query to the `/history`_ should consider trades within the time interval, even for open and close prices?
   We build bar from the `/streaming`_ ticks. For verification, we use `streamingHistoryEquality`_ test.

Should we change the session schedule at the summer/winter time changes?
   You shouldn't change the session schedule without TradingView team confirmation. The transition to summer/winter
   time is carried out automatically following the ``timezone`` parameter in the `/symbol_info`_.

Should we change the session schedule during the holidays?
   You shouldn't change the session schedule without TradingView team confirmation. We don't consider holidays now.
   But will add their support in the future.

Is it possible to add breaks during the trading day?
   There is no such possibility now. The trading day is continuous.

How to set up a minimal price step (min tick size)?
   Minimal tick size is set by ``pricescale`` and ``minmovement`` parameters in the `/symbol_info`_:
   ``min tick size =  minmovement / pricescale``. For example, if you need to set a price step in ``0.01``, then you
   need to set ``pricescale: 100``, and ``minmovement: 1``.
