.. contents::
   :depth: 5

Configuring
-----------
| There are three levels of configuration:

* *Broker level* --- applies to all subaccounts defined for the user.
  It's performed via the `/config <https://www.tradingview.com/rest-api-spec/#operation/getConfiguration>`_ request.
* *Subaccount level* --- extends to UI elements for a specific subaccount.
  It's performed via the `/accounts <https://www.tradingview.com/rest-api-spec/#operation/getAccounts>`_ request.
* *Instrument level* --- to configure UI elements for a specific instrument.
  It's performed via the `/instruments <https://www.tradingview.com/rest-api-spec/#operation/getInstruments>`_ request.

| All these requests are executed once when logging into the broker integration. The configuration priority of the same 
  UI elements is as follows: *broker*, *account*, *instrument*. Each subsequent configuration overrides the previous one.

Pulling intervals
.................
| Pulling intervals are configurable at the broker level only. They are designed to determine the frequency of requests
  to a specific endpoint. Consider the infrastructure when configuring the intervals to avoid dropping connections on 
  the broker's side. High values in requests can cause rate limit errors.
  
| TradingView does not strictly limit the amount of pulling intervals for requests, however, it is not recommended to 
  set their values higher than the maximum recommended. Because the TradingView UI can become unresponsive to the user 
  experience, which can lead to user complaints.

| Matching fields to requests:

* ``quotes`` --- the `/quotes <https://www.tradingview.com/rest-api-spec/#operation/getQuotes>`_ 
  and `/depth <https://www.tradingview.com/rest-api-spec/#operation/getDepth>`_ requests  (max 1000ms)
* ``accountManager`` --- the `/state <https://www.tradingview.com/rest-api-spec/#operation/getDepth>`_ request (max 1500ms)
* ``orders`` --- the `/orders <https://www.tradingview.com/rest-api-spec/#operation/getDepth>`_ request (max 1500ms)
* ``positions`` --- the `/positions <https://www.tradingview.com/rest-api-spec/#operation/getDepth>`_ request (max 1500ms)
* ``balances`` --- the `/balances <https://www.tradingview.com/rest-api-spec/#operation/getDepth>`_ request (max 1500ms)

Durations
.........
| `TradingView REST API <https://www.tradingview.com/rest-api-spec>`_ allows you to configure the duration 
  (or *Time In Force*) separately for each of the supported order types. By default, any item from the duration list will
  be shown in the *Order Ticket* only for *Limit*, *Stop*, *Stop-Limit* orders. If this list should be different from the 
  default for any Durations elements, you must submit it for this item in the ``supportedOrderTypes`` field.
  ``supportedOrderTypes`` must be an array of order types for which this duration will be available.
