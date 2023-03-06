.. links
.. _`/accounts`: https://www.tradingview.com/rest-api-spec/#operation/getAccounts
.. _`/balances`: https://www.tradingview.com/rest-api-spec/#operation/getBalances
.. _`/config`: https://www.tradingview.com/rest-api-spec/#operation/getConfiguration
.. _`/depth`: https://www.tradingview.com/rest-api-spec/#operation/getDepth
.. _`/instruments`: https://www.tradingview.com/rest-api-spec/#operation/getInstruments
.. _`/orders`: https://www.tradingview.com/rest-api-spec/#operation/placeOrder
.. _`/positions`: https://www.tradingview.com/rest-api-spec/#operation/getPositions
.. _`/quotes`: https://www.tradingview.com/rest-api-spec/#operation/getQuotes
.. _`/state`: https://www.tradingview.com/rest-api-spec/#operation/getState

Configuration
--------------

.. .. contents:: :local:
..    :depth: 1

Configuration levels
....................
There are three configuration levels.

* *Broker level* applies to all sub-accounts defined for the user. 
  It's performed via the `/config`_ request.
* *Sub-account level* extends to UI elements for a specific sub-account. 
  It's performed via the `/accounts`_ request.
* *Instrument level* uses to configure UI elements for a specific instrument. 
  It's performed via the `/instruments`_ request.

All these requests are executed once when logging into the broker integration. The configuration priority of the
same UI elements is as follows: *broker*, *account*, *instrument*. Each subsequent configuration overrides the
previous one.

.. _trading-configuration-pulling-intervals:

Pulling intervals
.................

Pulling intervals are designed to determine the frequency of requests to a specific endpoint.
It is the only way TradingView can track if anything was changed on the user's account.
If your integration doesn't comply with the request frequency,
TradingView UI can become unresponsive and display outdated information to users.
This may lead to user complaints.

Pulling intervals must be configurable at the broker's level only and defined in the ``pullingInterval`` object of `/config`_.
Consider the infrastructure when configuring the intervals to avoid dropping connections on the broker's side.
High values in requests can cause rate-limit errors.

The ``pullingInterval`` object has the following fields:

+--------------------+--------------------------------------------+---------------+-----------+
| Field              | Description                                | Default value | Max value |
+====================+============================================+===============+===========+
| ``quotes``         | For the `/quotes`_ and `/depth`_ requests. | 500 ms        | 1000 ms   |
+--------------------+--------------------------------------------+---------------+-----------+
| ``orders``         | For the `/orders`_ requests.               | 500 ms        | 1000 ms   |
+--------------------+--------------------------------------------+---------------+-----------+
| ``accountManager`` | For the `/state`_ requests.                | 500 ms        | 1500 ms   |
+--------------------+--------------------------------------------+---------------+-----------+
| ``positions``      | For the `/positions`_ requests.            | 1000 ms       | 1500 ms   |
+--------------------+--------------------------------------------+---------------+-----------+
| ``balances``       | For the `/balances`_ requests.             | 1000 ms       | 1500 ms   |
+--------------------+--------------------------------------------+---------------+-----------+

.. important::
  TradingView does not strictly limit the number of pulling intervals for requests, however,
  it is not recommended to set their values higher than the maximum recommended.
