.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory
.. _`/streaming`: https://www.tradingview.com/rest-api-spec/#operation/streaming

History
-------

We need the `/history`_ endpoint to:

* fill the database with deep history,
* compensate data from the `/streaming`_ in case of problems.

After initial filling of the database we make regular requests to `/history`_ endpoint to keep the data relevant. Our 
data feed requests 1-minute bars for the whole day per request. Requests are made sequentially from the current time 
to the past. 

If there is no data in the requested and previous time periods then you should set the status code to ``no_data``. The
API should respond with an empty response in case of requesting the range containing no historical data.

We will request `/history`_ until the date that the broker reported in the **Data requirements from**. Without this
date, we will request a history up to 1800 year.

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

There can be two types of request to `/history`_:

* with ``from`` and ``to`` parameters,
* with ``countback`` and ``to`` parameters.

In the first case we expect to receive all bars inside the given interval, including the border ones.

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

In the second case, we expect to receive exactly 3 bars when the ``countback`` is specified. The ``from`` parameter is 
ignored. 

.. code-block:: bash

  /history?symbol=BTCUSDT&resolution=1&from=1637502014&to=1637502267&countback=3

The response will be:

.. code-block:: json

  {
    "s": "ok",
    "t": [
      1585132560,
      1585133820,
      1585134120
    ],
    "o": [
      6500,
      6588,
      6591.5
    ],
    "h": [
      6500,
      6591.5,
      6603.5
    ],
    "l": [
      6500,
      6588,
      6591.5
    ],
    "c": [
      6500,
      6591.5,
      6603.5
    ],
    "v": [
      0.001,
      0.001,
      0.001
    ]
  }
