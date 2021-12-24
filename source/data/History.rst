.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory
.. _`/streaming`: https://www.tradingview.com/rest-api-spec/#operation/streaming

🎾 History
----------

We need the `/history`_ endpoint to:

* fill the database with deep history,
* compensate data from the `/streaming`_ in case of problems.

After filling our database, make regular requests to `/history`_ in the shallow history to keep the data up to date.
Per request out data feed requests 1-minute bars per day. Requests are made sequentially from the current time to the 
past. When we reach the date that you specify as the history depth, we will stop sending requests. It means here is no 
deeper data for this symbol.

So, if a request arrives in `/history`_ for a period without data, an empty value should be sent in the response:

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

The request to `/history`_ can be of two types: 
* with ``from`` and ``to`` parameters,
* with ``countback`` and ``to`` parameters.

In the first case, we wait to recieve all bars inside ``from`` and ``to`` interval:

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

In the second case, when the ``countback`` specifies, we wait to receive exactly 3 bars. The ``from`` parameter is
ignored. When a symbol has fewer bars history, an answer may contain less than 3 bars.

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
