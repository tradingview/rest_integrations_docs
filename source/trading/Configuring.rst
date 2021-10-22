.. links
.. _/accounts: https://www.tradingview.com/rest-api-spec/#operation/getAccounts
.. _/balances: https://www.tradingview.com/rest-api-spec/#operation/getBalances
.. _/config: https://www.tradingview.com/rest-api-spec/#operation/getConfiguration
.. _/depth: https://www.tradingview.com/rest-api-spec/#operation/getDepth
.. _/instruments: https://www.tradingview.com/rest-api-spec/#operation/getInstruments
.. _/orders: https://www.tradingview.com/rest-api-spec/#operation/placeOrder
.. _/positions: https://www.tradingview.com/rest-api-spec/#operation/getPositions
.. _/quotes: https://www.tradingview.com/rest-api-spec/#operation/getQuotes
.. _/state: https://www.tradingview.com/rest-api-spec/#operation/getState

Configuring
-----------

.. contents:: :local:
   :depth: 3

Configuration levels
....................
There are three configuration levels.

* *Broker level* applies to all subaccounts defined for the user. 
  It's performed via the `/config`_ request.
* *Subaccount level* extends to UI elements for a specific subaccount. 
  It's performed via the `/accounts`_ request.
* *Instrument level* uses to configure UI elements for a specific instrument. 
  It's performed via the `/instruments`_ request.

All these requests are executed once when logging into the broker integration. The configuration priority of the
same UI elements is as follows: *broker*, *account*, *instrument*. Each subsequent configuration overrides the
previous one.

Pulling intervals
.................
Pulling intervals are designed to determine the frequency of requests to a specific endpoint. They are configurable 
at the broker level only. Consider the infrastructure when configuring the intervals to avoid dropping
connections on the broker's side. High values in requests can cause rate limit errors.
  
TradingView does not strictly limit the amount of pulling intervals for requests, however, it is not recommended 
to set their values higher than the maximum recommended. Because the TradingView UI can become 
unresponsive to the user experience, which can lead to user complaints.

Matching fields to requests:

* ``quotes`` --- the `/quotes`_ and `/depth`_ requests (max 1000ms)
* ``accountManager`` --- the `/state`_ request (max 1500ms)
* ``orders`` --- the `/orders`_ request (max 1500ms)
* ``positions`` --- the `/positions`_ request (max 1500ms)
* ``balances`` --- the `/balances`_ request (max 1500ms)
