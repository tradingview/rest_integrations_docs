.. links
.. _`/accounts`: https://www.tradingview.com/rest-api-spec/#operation/getAccounts
.. _`/authorize`: https://www.tradingview.com/rest-api-spec/#operation/authorize
.. _`/config`: https://www.tradingview.com/rest-api-spec/#operation/getConfiguration
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory
.. _`/instruments`: https://www.tradingview.com/rest-api-spec/#operation/getInstruments
.. _`/logout`: https://www.tradingview.com/rest-api-spec/#operation/logout
.. _`/mapping`: https://www.tradingview.com/rest-api-spec/#operation/getMappin
.. _`/orders`: https://www.tradingview.com/rest-api-spec/#operation/placeOrder
.. _`/permissions`: https://www.tradingview.com/rest-api-spec/#operation/getPermissions
.. _`/positions`: https://www.tradingview.com/rest-api-spec/#operation/getPositions
.. _`/quotes`: https://www.tradingview.com/rest-api-spec/#operation/getQuotes
.. _`/state`: https://www.tradingview.com/rest-api-spec/#operation/getState
.. _`/streaming`: https://www.tradingview.com/rest-api-spec/#operation/streaming
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo
.. _`PasswordBearer`: https://www.tradingview.com/rest-api-spec/#section/Authentication/PasswordBearer
.. _`OAuth2Bearer`: https://www.tradingview.com/rest-api-spec/#section/Authentication/OAuth2Bearer
.. _`ServerOAuth2Bearer`: https://www.tradingview.com/rest-api-spec/#section/Authentication/ServerOAuth2Bearer

FAQs
====

.. contents:: :local:
   :depth: 2

Authentication
--------------

🎾 What about error handling when an error occurs? Should we respond with error code 400 (Bad Request) or 200 (OK)?
   In response to an error, return the code 200. Send the error message to the ``errmsg`` parameter.

🎾 Are there any restrictions on the lifetime of tokens? What is the optimal lifetime?
   Max lifetime is a 32-bit signed integer --- ``2147483647``. It's about 24.8 of a day. Furthermore, you can make it
   never-ending if you don't send ``expired_in`` parameter. But we think this is unsafe.
   For the optimal functioning, the token lifetime should not exceed 20 minutes. 

🎾 There is no ``prompt`` parameter in the OAuth specification? How is it used?
   This parameter is a flag for prompting for user credentials.
   On your side, everything should be simple.
   * When you received ``prompt: login`` in the authorization request, ask the user for credentials.
   * If successful, redirect him (with an access token) to our ``redirect url``.
   * If you received a request for authorization with ``prompt: none``, then immediately redirect with the token.

🎾 Will the ``scope`` parameter be sent on authorization? What about its values? How do we deal with them?
   Upon authorization, you will receive a ``scope`` in the request. When refreshing a token, no.
   This parameter is optional. We don't process it on our side.

🎾 Do we have to implement all 4 types of authorization system?
   Integration is divided into 2 parts: data integration and trading integration. Data Integration supports
   `PasswordBearer`_, `ServerOAuth2Bearer`_ authorization types. Integration of the trading part supports 
   `PasswordBearer`_, `OAuth2Bearer`_ (Implicit Flow), `OAuth2Bearer`_ (Code Flow) authorization types.
   The types of authorization for each part of the integration (data and trading) may differ.

🎾 Are the data integration API being requested by the user`s browser or by TradingView server?
   Data integration API is requested only by TradingView servers. Authorization is optional function.
   You can implement this or skip it.

🎾 Can you talk more about the flow of `PasswordBearer`_?
   In general, the flow is:

   1. The user selects a broker in the Trading Panel on the TradingView website.
   2. A popup for entering credentials is opened for the user.
   3. The user enters credentials and presses the "Connect" button (submits the form).
   4. Your REST server receives a POST request to `/authorize`_ endpoint with credentials inside.
   5. Your REST server validates the credentials and, if successful, gives a response with a token. 
   6. Then you get this token in all other requests to your REST server in the ``Authorization`` header.

🎾 Can we use the same Client ID in both staging and production environments?
   The Сliend IDs for each of the 6 environments connections must be unique, this is a requirement of our security team.
   The TradingView website in the sandbox or production can be connected to only 1 brokerage environment at a time. 

🎾 Are you able to support the OAuth2 Client Credentials Grant for authorizing to our server? 
   Our client uses OAuth 2.0 JWT Bearer Flow. Please check out `ServerOAuth2Bearer`_ section in our specs. We need
   X.509 cert to sign the JWT. Our client forms the JWT, signs it and sends it in the body of the POST request as
   assertion field and expects to get a token in response.

Authorization
-------------

Authorize
.........

Logout
......

🎾 Should we implement `/authorize`_ and `/logout`_ endpoints for Implicit Flow?
   There is no need for an `/authorize`_ endpoint when using the `OAuth2Bearer`_ (Implicit Flow).
   Implementation of `/logout`_ is optional. Use it if you need to know when a user is logging out of his session.

Broker Configuration
--------------------

Configuration
.............

🎾 What about the ``locale`` argument in Configuration, do we need to support all the languages?
   With this argument, we provide information about locale used by the user entering the integration.
   You can use this information to create a more comfortable UX for a user.

🎾 How can I modify the tabs in the "Positions panel"?
   For these needs, you can use the ``positionCustomFields`` in the `/config`_ endpoint. If you want to use different
   custom columns for different accounts, use the ``positionCustomFields`` of the `/accounts`_ endpoint.

Mapping
.......

🎾 How can I map Forex symbols?
   You cannot map your Forex to any other exchange. The prices are different. If you want to support Forex, you need
   to connect your Forex data feed to TradingView using `/symbol_info`_, `/history`_, `/streaming`_ endpoints.
   You don't need to provide `/mapping`_ for Forex. So, you don't need to implement it in case of Forex.
   `/mapping`_ is used for exchange based instruments.

Account
-------

🎾 Can a user login multiple times simultaneously (login with the same account from two browsers for example)?
   That's quite possible. Usually brokers limit number of concurrent session. For example, user can be connected from
   desktop and mobile.

Accounts
........

🎾 Where the user can see if his account is *live* or *demo*?
   The account type can be specified in the ``name`` parameter in the `/accounts`_ endpoint. A user can see this 
   information when selecting an account in the extra menu.

.. image:: ../images/accounts-menu.png
   :alt: Names in the account menu.
   :align: center

🎾 What happens if an account on the TradingView platform gets disabled/deleted on the broker side during trading session?
   If the account has expired and it happened while the broker session was connected, you should return error responses
   for that account. After 20 consecutive error responses, the user will be disconnected. After that, the user will try
   to login again, and the broker will send the list of accounts without expiring.
   
   If it was the user's only active account, you will send an error message in the ``errMsg`` to `/accounts`_. Login
   dialog will not occur and the user will be shown that message.

🎾 How to implement orders with brackets?
   :ref:`Brackets<section-concepts-brackets>` are Stop-Loss and Take-Profit orders. To place orders with brackets, set
   flags ``supportOrderBrackets``, ``supportMarketBrackets``, ``supportPositionBrackets`` to ``true``.
   
   After setting the ``supportOrderBrackets`` flag to ``true``, Stop-Loss and Take-Profit section will automatically
   appear in the :ref:`Order Ticket<section-uielements-orderticket>`. If you send brackets to `/orders`_ with the
   suitable ``type`` and ``status`` values, they will automatically appear in 
   :ref:`Positions<section-concepts-positions>`. The value of the ``parentId`` field must fit order's or position's id
   to which they are attached.

Instruments
...........

🎾 Should we implement all the required fields (pipSize, pipValue, minTick) for all the instruments?
   These fields can have different values for the different brokers. We expect the broker's values in the 
   `/instruments`_ endpoint.

🎾 Should ``pipValue`` be returned in the `/instruments`_ in the instrument's currency or customer account currency?
   You should send it in the currency of the customer's account.

State
.....

🔥 For the /state, there is a parameter “unrealizedPl” which only presents in future contract. Does it mean that for TradingView, it only supports future market but not spot market?
   We support both crypto spot and crypto derivatives trading. Some brokers show unrealizedPL even for spot trading, for example against the dollar.

🔥 We have 2 assets in trading account which is BTC and USDT. So for the /state, what is the value of “balance”  that we are supposed to return in this case?
   You can fully customize both the *Account Summary Row* and the *Account Summary Tab* and display the information you deem necessary there.

🎾 How often are quoted parameters (equity, margin level) recalculated?
   You provide this data (already calculated) in the `/state`_. The request interval is defined in the `/config`_ in the
   ``pullingInterval`` field.

Orders
......

🎾 How to define the ``accountId`` for the oders?
   We get the ``accountId`` in the `/accounts`_ and then send your ``id`` of the account selected by the user (active)
   during the request.

🔥 Is the Last Updated field affected by the time zone selected from the list under the chart?
   We expect you to send UTС timestamp. The browser will show it in the user's time zone in the table. 
   It may not coincide with the time zone on the chart, this is the user's choice and this is normal. 
   But if you send executions, then whatever time zone is selected on the chart, they will be displayed correctly, on the corresponding candle.

🔥 How can we map extra parameters required for order Placement in the order Custom fields. ex: for order_placement we need productType to place an order whereas in the place_order API the productType isnt supported so how can we map that in /config endpoint
   This can be done via orderDialogCustomFields object at the account level or at the instrument level, with the latter taking precedence.

Positions
.........

🎾 How does TradingView receive information about the events of the broker's trading platrorm?
   We expect that during the trade sasstion, all closed positions also will be sent to the `/positions`_.
   
   The same applies to executed orders. If we get an order with ``filled`` status in the `/orders`_, then we show the
   user a message.

Balances
........

Executions
..........

Orders History
..............

🔥 What is the difference between Filled, Cancelled and Rejected in Orders tab and in History tab. Are these only available for a single login session in the Orders tab? Or should they always be the same as History? Wouldn't this be duplication of data in such case?
   The orders statuses can be divided into two groups in our API:
   * Transitional ("placing", "inactive", "working")
   * Final ("rejected", "filled", "canceled")
   The status of an order can only change from transitional to final, but not vice versa.
   Requests:
   * In response to the /orders request, we expect ALL orders of the current trading session and orders with transitional statuses from previous trading sessions.
   * In response to the /ordersHistory request, we expect ALL orders with final statuses from previous trading sessions.
   Tab Display:
   * The Orders tab displays all orders that come in response to the /orders request.
   * The History tab displays all orders that come in response to the /ordersHistory request and orders from /orders that have the final status. So, orders with final statuses from /orders are simultaneously displayed on both the Orders and the History tabs.

Get Leverage
............

Set Leverage
............

Preview Leverage
................

Trading
-------

Place Order
...........

Modify Order
............

Cancel Order
............

Preview Order
.............

Modify Position
...............

Close Position
..............

Market Data
-----------

Quotes
......

🎾 Is the `/quotes`_ method required? Or do you have your own sources of quotes for securites?
   This method is optional, but highly desirable. It is needed to display your quotes directly in the
   :ref:`Order Ticket<section-uielements-orderticket>`. This will reduce the chance of order execution at prices other
   than what the user sees.

🎾 Are requests for quotes coming from the client or from the server?
   Requests to the `/quotes`_ going from the client, requests to the `/streaming`_ going from the server. The broker
   should to stream of quotes to the `/streaming`_ for the server and simultaneously send them separately to each client
   in the response to requests to the `/quotes`_.

🔥 How we can provide values specific to the position side (buy or sell)?
   for example for EURUSD it is 100000 * 0.00001 or 1.0
   this is in the currency of the symbol though
   then we take this and multiply it with the selected quantity
   that is the pipValue
   and then if we want it in the account currency, we need to know if it is a buy or sell position

   So, you can provide any of these as pipValue and you can provide values specific to the position side in /quotes

Depth
.....

🔥 How your depth panel works? I have just set some static prices there but I will update it with real ones soon. How would I translate our logic into the /depth endpoint. And what will be the outcome in the UI panel?
   Each price corresponds to the number (volume) of open buy and sell orders. This presentation of information corresponds to how the DOM usually works.

Data Permissions
----------------

Groups
......

🎾 What if a user may have a different set of instruments for different accounts, because there is no such parameter as account id in the `/permissions`?
   Different sets of instruments for different accounts can be implemented via `/instruments`_. The permission mechanism
   serves somewhat differently, for example, to restrict access to paid data.

🎾 Should we implement `/permissions`_ if we return the same set of instruments for all users?
   The `/permissions`_ endpoint specifies which groupsare available for the certain user. It is only required if you use
   groups of symbols to restrict access to instrument's data.

Permissions
...........

🎾 We sell data subscriptions. How can we inform that real-time data is available to the user?
   A broker should implement the `/permissions`_ endpoint. Otherwise we will show :term:`BATS` data for these exchanges
   if the user didn't buy a subscription from us.
   
   When user logins into integration, we requests to the `/permissions`_ for determing a list of the subscriptions.
   For users without real-time data subscriptions, we will show free BATS or delayed market data.

Data Integration
----------------

🔥 The Data Integration API just used to record broker's data to TradingView database. Tradingview do not show the data to chart?
   The Data Integration API must have 3 endpoints - symbol_info, history and streaming.
   symbol_info - is a set of rules for each instrument/symbol
   history - contains information about past transactions - we need 1-minute resolution bars. We request historical data once to be placed in our database.
   streaming - contains information about transactions in real-time - we need quotes and trades .  We use streaming data continuously.
   All data that we receive is shown on the TradingView chart.

Symbol Info
............

🎾 If the broker satisfied with TradingView instruments, can we not send anything to `/symbol_info`_ and not implement `/streaming`_ and `/history`_?
   That's right, in this case the data integration is irrelevant.

🎾 How to set session time for data integration?
   Use ``timezone`` and ``session-regular`` parameters in the `/symbol_info`_, but only for instruments which trading data
   we will receive from you. For those instruments which we already have, sessions are configured.

🔥 what is the process of adding a new symbol to the API? I have some new symbols but they don't show in the chart. Do you call /symbol_info regularly or do you need to do it manually?
   we request symbol_info every hour and automatically update if everything is ok. But if we find some critical changes or invalid values, manual verification will be required.

🔥 In the search I would like to have only Activtrades symbols. Also there are categories that we don't support like Stock, Crypto and Economy. I would like to only have available categories
   When a user is logged into Activtrades, only the broker's symbols are filtered in the symbol search.
   But the user can turn off these filters. This symbol search behavior cannot be changed.

🎾 How often do you call the `/symbol_info`_ endpoint?
   Every hour.

🔥 from symbol info interface docs I found symbol “should contain uppercase letters, numbers, a dot or an underscore”. However our exchange symbols contain a SLASH “/” like “BTC/USDT”, is it allowed or we have to do a conversion to “BTC_USDT”?
   You can add ``ticker`` field. We will use the ticker name for requests to API, it will be used prior to symbol filed. Ticker has no strict requirements.
   ``symbol`` is what we show on the chart. so, you can have two fileds:

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

🔥 do you want us to send only outright futures contracts or calendar spreads as well?
   outright futures - is it perpetual futures without expiration date,
   calendar spreads - for example monthly expiring contrancts.

🔥 ``has-no-volume`` : does this indicate whether we can report trading volume on the symbol?
   If you can provide trading volume,  just set has-no-volume:false

🔥 ``session-premarket`` : our market is open from 1700-1600 CT and we have a pre-open time that's at 16:50CT. should pre-open should be reported under ``session-premarket`` or included under ``session-regular``?
   It depend on how the bars are built. We build bars by session-regular.
   for exmple for session ``1700-1600`` we build all resolutions (5min, 1h, 4h ...) from 17:00, even if we have a session-premarket.

🔥 SymbolInfoResponse : we're not sure what to put in these fields bar-source, bar-transform and bar-fillgaps . can you give us some examples and how they're used for building bars?
   If we need to build bars from trades then bar-source: trade, from bids - bar-source: bid
   * bar-transform is required to align the bars. For cases when open price is always equal to close price of the previous bar. 
   If you dont have any alignments, just omit this field.
   * bar-fillgaps generate of degenerate bars in the absence of trades (bars with zero volume and equal OHLC values). 

History
.......
🎾 Is `/history`_ requested only for those instruments for wich we supply our quotes?
   `/history`_ is requested for all instruments represented in the ``symbol`` field of `/symbol_info`_.

🎾 What requests go from the server, not from the client to the broker's server (for example, `/symbol_info`_, `/history`_, `/groups`_)?
   The server requests `/symbol_info`_ and `/groups`_ once an hour.
   `/history`_ endpoint used to populate our database with historical data its full depth once.
   Then, once a day, there will be requests for data in a shallow history to compensate for lost ticks in streaming, for
   example, in cases of disconnection.

🔥 if we must support the Countback parameter in the request. It is not marked as required in the api description
   history can be requested in two ways:
   1. without countback ``history?from=1622030000&resolution=1&symbol=EURUSD&to=1622030400`` 
   in this case we expect 1-min candles in range ``1622030000 - 1622030400``  . The client will not request historical data for more than 24 hours.
   1. with countback ``history?countback=250&from=0&resolution=1&symbol=EURUSD&to=1622030400``
   in this case we expect 250 bars to ``to=1622030400``  ignoring ``from``  parameter. The client will not request  more than 2500 candles.

🔥 I'm having some trouble with the /history request. would also like to know how big intervals do you use (from/to)
   we request 1 day between from and to per request. Requests are executed sequentially
   If we request during a period when there is no data, you must return 200, no_data field and nb: https://files.slack.com/files-pri/T0266AC0C-F01V7G3BX8W/image.png

🔥 what resolutions would you be sending in the request?
   the customer (our data-feed) will request /history once for putting full depth of history in our db. 
   We require only 1-min resolution bars. We build on charts others resolution from 1-min  - 5, 15, 60, 240 and custom like 33 or 14M.

🔥 how often do you call /history to update your db?
   once a day

🔥 how often do you send this request and how large is the expected from/to range? is this mainly for gap fill if the real time streaming connection is lost?
   We use history endpoint in two cases:
   * once before deploying the datafeed to fill our database with all historical data
   * for gap fill the real time streaming connection is lost
   In both cases we request data for 1 day  in range from/to.

🔥 are we expected to fill in gaps even if the data is unchanged? or do you handle that? eg. the high price at minute 1 is 1.23 and it doesn't change until minute 30 - do you want us to fill in 1.23 for every 1 minute interval?
   don't quite understand. If we talking about /history only, then the data should not change.

🔥 query params from and to: what is the expected timestamp precision? seconds?
   timestamp must be in seconds

🔥 for /history we're planning to support 1 minute intervals only, so we will set ``supported-resolutions`` to [1], and you all can aggregate daily/weekly/monthly stats using this data. please confirm if this is correct.
   in this case, you can omit the supported-resolutions  as an optional field and the default will be used. anyway, we will only use 1-min resolution bars.

🔥 for /history we're expecting you will always send 1 day from/to date range. do you also use countback in some cases?
   countback parameter should be supported

🔥 HistorySuccessResponse : if our price/volume data does not change for multiple 1 minute intervals, do you want us to copy over the data from the previous interval or leave the values as null? this is particularly relevant for daily open/close prices. there is more context in my previous thread + examples
   | let's say our session-regular times are 9am to 9pm
   | we have open price=1.23 at 9am and close price=1.24 at 9pm
   | we have no other trades in between open and close
   | now you send us a history request from 9am to 9pm with resolution=1 minute
   | should our response be:
   | a) 2 bars only at 9am and 9pm, and no other bars are sent to you because there was no trading activity
   | b) 720 bars, (1 minute interval for 12 hr time range). 9am bar has open price and 9pm bar has close price. every other bar has null values
   | c) 720 bars, and we copy open price = 1.23 on each of the 720 bars. close price is null until the last bar at 9pm

   In this case we need only two bars - option a)

🔥 HistoryNextBarResponse : this will be sent if there is no data for any of the stats within the from/to time range, is that correct? and for a 1 minute interval you want us to send the nb field to the previous available minute where data was present?
   HistoryNextBarResponse  If the request was sent in a range that has no data and no data in the past than we expect no_data . 
   If the request was sent in a range that has no data, but there is data in the past we expect no_data; 
   nb: 1624366020  where 1624366020 is the timestamp of the nearest bar to from

Stream of prices
.................

🎾 How do you get prices from brokers? The price can change more than ten times per second for each of the instruments. The usual GET request is not enough here.
   Endpoint `/streaming`_ is a permanent connection through which we accept changes in quotes for all instruments.

🔥 For stream of prices response, I found Symbol id is required, Can I use ticker format instead. i.e. return “BTC/USDT” instead of “BTCUSDT”
    yes, you can

🔥 StreamingDailyBarResponse: can this be inferred from our 1 minute history intervals + live feed? our understanding is we don't need to send these.
   Correctly, you do not need to sent it. If there is has-daily: false  in the symbol_info  we will skip the daily updates.

🔥 streaming: historyEquality --- is it expected that the query to /history should instead match the built bar and only consider trades within the time interval, even for open and close prices?
   we expect information about closed trades in the range from/to for the historical bar.

   ``history?from=1626051480&resolution=1&symbol=LTECU21&to=1626051539``

   1 bar should return with:

   * open price --- the first trade between 1626051480 and 1626051539
   * close price --- the last trade between 1626051480 and 1626051539
   * high --- the highest price between 1626051480 and 1626051539
   * low --- the lowest price between 1626051480 and 1626051539
   * volume --- sum of trades sizes between 1626051480 and 1626051539