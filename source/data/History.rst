.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory
.. _`/streaming`: https://www.tradingview.com/rest-api-spec/#operation/streaming

History
-------

TradingView needs the `/history`_ endpoint to:

* fill the database with deep history,
* compensate data from `/streaming`_ in case of problems.

After initial filling of the database, TradingView makes regular requests to `/history`_ endpoint to keep the data relevant.
TradingView data feed requests 1-minute bars for the whole day per request.
Requests are made sequentially from the current time to the past. 

Data requirements
..................

Your data should meet the following requirements:

- The data must be real, from the production environment preferably. Otherwise, integration tests will fail.
- Real-time data obtained from the `/streaming`_ endpoint must match the historical data obtained from `/history`_. The allowed count of mismatched bars (candles) must not exceed 5% for frequently traded symbols. Otherwise, integration into TradingView is not possible.
- The data must not include unreasonable price gaps, historical data gaps on 1-minute, daily resolutions (temporal gaps), and incorrect prices (adhesions).
- The daily bar time should be 00:00 UTC and expected to be a trading day, not a day when the session starts.
- The monthly bar time should be 00:00 UTC and be the first trading day of the month.

.. important::
  If there is no data in the requested period, consider the following:
    - Set the status code to ``no_data`` or return an empty response in case there is no historical data in the previous periods.
    - Return an empty response in case there is historical data in the previous periods.

TradingView requests `/history`_ until the date that the broker reported in the **Data requirements form**. Without this
date, TradingView requests history up to 1800 year.

Example
........

.. code-block:: json

  {
    "s": "ok",
    "t": [],
    "o": [],
    "h": [],
    "l": [],
    "c": [],
    "v": []
  }

Request to `/history`_ consists of ``from`` and ``to`` parameters. TradingView expects to receive all bars inside the given interval,
including the border ones.

.. code-block:: bash

  /history?symbol=BTCUSDT&resolution=1&from=1637502014&to=1637502267

The response will be:

.. code-block:: json

  {
    "s": "ok",
    "t": [
      1637502060,
      1637502180,
      1637502240
    ],
    "o": [
      58905.5,
      58907.5,
      58889
    ],
    "h": [
      58908,
      58908,
      58893.5
    ],
    "l": [
      58905.5,
      58888.5,
      58869
    ],
    "c": [
      58907.5,
      58889,
      58893
    ],
    "v": [
      5.365,
      2.288,
      17.36
    ]
  }
