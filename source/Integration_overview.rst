.. links
.. _`autotest service`: https://cu-jenkins.xtools.tv
.. _`beta-rest.tradingview.com`: https://beta-rest.tradingview.com/
.. _`Trading`: https://www.tradingview.com/rest-api-spec/#tag/Trading

.. _`/accounts`: https://www.tradingview.com/rest-api-spec/#operation/getAccounts
.. _`/authorize`: https://www.tradingview.com/rest-api-spec/#operation/authorize
.. _`/balances`: https://www.tradingview.com/rest-api-spec/#operation/getBalances
.. _`/config`: https://www.tradingview.com/rest-api-spec/#operation/getConfiguration
.. _`/depth`: https://www.tradingview.com/rest-api-spec/#operation/getDepth
.. _`/executions`: https://www.tradingview.com/rest-api-spec/#operation/getExecutions
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory
.. _`/instruments`: https://www.tradingview.com/rest-api-spec/#operation/getInstruments
.. _`/mapping`: https://www.tradingview.com/rest-api-spec/#operation/getMapping
.. _`/orders`: https://www.tradingview.com/rest-api-spec/#operation/getOrders
.. _`/ordersHistory`: https://www.tradingview.com/rest-api-spec/#operation/getOrdersHistory
.. _`/positions`: https://www.tradingview.com/rest-api-spec/#operation/getPositions
.. _`/permissions`: https://www.tradingview.com/rest-api-spec/#operation/getPermissions
.. _`/quotes`: https://www.tradingview.com/rest-api-spec/#operation/getQuotes
.. _`/state`: https://www.tradingview.com/rest-api-spec/#operation/getState
.. _`/streaming`: https://www.tradingview.com/rest-api-spec/#operation/streaming
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo
.. _`PasswordBearer`: https://www.tradingview.com/rest-api-spec/#section/Authentication/PasswordBearer
.. _`ServerOAuth2Bearer`: https://www.tradingview.com/rest-api-spec/#section/Authentication/ServerOAuth2Bearer

Integration overview
********************

.. .. contents:: :local:
..   :depth: 0

Integration architecture
------------------------

What are the parts of the integration
.....................................
The broker's integration consists of two independent parts: data integration based on a server-to-server 
architecture and trading integration based on a client-server architecture.

Why data integration is needed
..............................
The TradingView website can only receive data from the TradingView server. Indicators are counted on this server, as 
well as server alerts, etc. Data integration is required in order for the market data to be first received by the 
TradingView server, and then transferred to the client side. For CFDs, FOREX and CRYPTO the data needs to be connected 
in any case, as it is not linked to the particular exchange and is always different.

In what cases it is possible not to integrate data
..................................................
Market data can come to the TradingView server from another source, for example, directly from the exchange. There is no
need for market data integration in this case, and the broker needs to implement `/mapping`_ endpoint to solve 
:ref:`the symbol names matching<mapping-symbols-label>` issue between the TradingView and broker symbols.

Mandatory Endpoints by broker/exchange type
...........................................

+-------------------+---------+-------------+--------------------+----------------+
| Broker type       | FX/CFD  | Crypto Spot | Crypto Derivatives | Stocks/Futures |
+-------------------+         |             |                    |                |
| Endpoints         |         |             |                    |                |
+===================+=========+=============+====================+================+
| `/accounts`_      | Yes     | Yes         | Yes                | Yes            |
+-------------------+---------+-------------+--------------------+----------------+
| `/balances`_      | ???       | Yes         | ???                  | ???              |
+-------------------+---------+-------------+--------------------+----------------+
| `/config`_        | Yes     | Yes         | Yes                | Yes            |
+-------------------+---------+-------------+--------------------+----------------+
| `/depth`_         | ???       | Yes         | Yes                | Yes            |
+-------------------+---------+-------------+--------------------+----------------+
| `/executions`_    | Yes     | Yes         | Yes                | Yes            |
+-------------------+---------+-------------+--------------------+----------------+
| `/history`_       | Yes     | Yes         | Yes                | ???              |
+-------------------+---------+-------------+--------------------+----------------+
| `/instruments`_   | Yes     | Yes         | Yes                | Yes            |
+-------------------+---------+-------------+--------------------+----------------+
| `/mapping`_       | ???       | ???           | ???                  | Yes            |
+-------------------+---------+-------------+--------------------+----------------+
| `/orders`_        | Yes     | Yes         | Yes                | Yes            |
+-------------------+---------+-------------+--------------------+----------------+
| `/ordersHistory`_ | Yes     | Yes         | Yes                | Yes            |
+-------------------+---------+-------------+--------------------+----------------+
| `/positions`_     | Yes     | ???           | Yes                | Yes            |
+-------------------+---------+-------------+--------------------+----------------+
| `/quotes`_        | Yes     | Yes         | Yes                | Yes            |
+-------------------+---------+-------------+--------------------+----------------+
| `/state`_         | Yes     | Yes         | Yes                | Yes            |
+-------------------+---------+-------------+--------------------+----------------+
| `/streaming`_     | Yes     | Yes         | Yes                | ???              |
+-------------------+---------+-------------+--------------------+----------------+
| `/symbol_info`_   | Yes     | Yes         | Yes                | ???              |
+-------------------+---------+-------------+--------------------+----------------+

Features of the implementation of some endpoints
................................................
Processed once at login: `/config`_, `/accounts`_, `/instruments`_, `/ordersHistory`_, `/permissions`_.

The rest of the requests are sent either on a regular basis or are the result of user actions. In the first case, their
frequency is set using :ref:`trading-configuring-pulling-intervals` in the `/config`_. In the second case, it happens in
the `Trading`_ section.

In some cases, the listed endpoints may not be implemented.

* `/mapping`_ --- not necessary if you work exclusively on your own symbols.
* `/executions`_ --- can be disabled through the config, but in this case, transactions will not be displayed on the 
  "Chart".
* `/positions`_ --- can be disabled through the config, not used for Crypto Spot trading.
* `/balances`_ --- can be disabled, used for Crypto Spot only.
* `/depth`_ --- can be disabled if you are not going to support :term:`DOM` display.
* `/permissions`_, `/groups`_ --- it's set up on our side, if you are not going to restrict certain groups of users 
  access to certain data (for example, on geographically, or depending on the tariff plan), we will not activated it 
  on our side.

Trading integration issues
--------------------------

How trading integration works
.............................
The trading integration uses a client-server architecture: requests from the user's browser are sent directly to the
broker's server. The TradingView server is not involved in this data exchange. An exception is a request to the
`/permissions`_. It is sent from the TradingView server to give the user access to the data.
  
Requests from the client browser require a configured :ref:`CORS policy<cors-policy-label>` on the broker side.

.. _trading-environments:

Types of environments
.....................
There are several environment variants used in the development and support of the integration. Each environment has its
URL.

- The *production environment* with the real market data is available to the end-users. TradingView implements the 
  production environment on its side, and the brokers do it on theirs.
- The *staging environment* is for testing and does not contain real market data. TradingView implements the staging 
  environment on its side, and the brokers do it on theirs.
- The *local environment* is used on developers\' computers and does not contain real market data. Connections to the 
  broker\'s staging environment are made from the ``localhost:6285`` address.

The table lists six pairs of environments connections.

+-------------------------+--------------------+
| TradingView environment | Broker environment |
+=========================+====================+
| production              | production         |
+-------------------------+--------------------+
| staging                 | production         |
+-------------------------+--------------------+
| localhost               | production         |
+-------------------------+--------------------+
| production              | staging            |
+-------------------------+--------------------+
| staging                 | staging            |
+-------------------------+--------------------+
| localhost               | staging            |
+-------------------------+--------------------+

A TradingView website in a sandbox or production can only be connected to one broker environment at a time. You can
switch between environments through the browser console. Instructions can be provided after configuration by the
TradingView team is completed.

.. _what-is-the-sandbox:

What is the Sandbox
...................
The sandbox is a fully functional copy of the TradingView website located at `beta-rest.tradingview.com`_. Access to the
resource is provided by adding an IP address to the whitelist on the TradingView side.

When broker's integration can be placed in the Sandbox
......................................................
There are two conditions to place a broker integration to the sandbox:

* passing conformational (authorization & trading conformance) tests at the `autotest service`_,
* availability of market data required for the integration to work on the TradingView staging server

If the broker does not integrate market data but uses data obtained by TradingView from another source,
it is necessary to implement the `/mapping`_ endpoint.

.. _localization-support:

Localization support
....................
Usually, the integration of a specific broker is aimed at an audience using their own national language.
However, English language support is required for all requests coming from the main locale of the 
TradingView application.

The user's locale can be determined through the ``locale`` query parameter, which is present in every request coming 
from the client to the broker's server.

.. _cors-policy-label:

CORS policy
...........
Test servers and website versions in different languages are located on ``*.tradingview.com`` subdomains. For example, 
the German version of the site is located at ``de.tradingview.com``. TradingView can send a request from any of these 
addresses.

Therefore, you must include an ``Access-Control-Allow-Origin`` response header with the specific subdomain that sent 
the request in each endpoint for each response code.

In addition, in the broker staging environment it is necessary to allow requests from the ``localhost:6285``.
This address is used on developers\' computers.

Why use HTTPS
.............
Please avoid using HTTP instead of HTTPS.
Our website  is prohibited from accessing anything through the insecure HTTP protocol by ``Content-Security-Policy``.
HSTS disallows access to anything over the insecure HTTP protocol. Moreover, HSTS is exposed for **730 days** and
applies to all subdomains. In order for us to be able to make an HTTP request to your staging even from our staging, we
will have to:

* Turn off HSTS in production.
* Wait for two years.

Adding features after the integration release
................................................
New features need to be added to the broker's staging environment and tested in the sandbox.
The feature gets into production only after successful testing by the TradingView testing team.

Data integration issues
-----------------------

Data requirements
..................

All the data which is displayed at TradingView has to meet the following standards:

* Real-time data obtained from the `/streaming`_ endpoint must match the historical data, obtained from the `/history`_ 
  API. The allowed count of mismatched bars (candles) must not exceed 5% for frequently traded symbols, otherwise the 
  integration to TradingView is not possible.

* Historical data should look healthy. It must not contain unreasonable price gaps, 1 min and D-resolution history 
  holes, and incorrect prices.

User sees bars built from streaming ticks on the chart. The `/streaming`_ data is replaced by the data from the 
`/history`_ some time after user reloads the Chart. It is important that the data from `/streaming`_ and `/history`_ 
are the same. Data mismatch can lead to false triggering of alerts for the user, which is unacceptable. The data in the 
`/history`_ shouldn\'t change.

.. tip::

  To make sure you meet this requirement, record your streaming trades in a few minutes.

.. code-block:: json

  {
    "id":"BTCUSDT",
    "p":33405.5,
    "t":1624797120,
    "f":"t",
    "s":0.092
  },
  {
    "id":"BTCUSDT",
    "p":33417.5,
    "t":1624797179,
    "f":"t",
    "s":0.057
  }

We can build 1-minute bar from this data:

.. code-block:: json

  {
    "s":"ok",
    "t":[1624797120],
    "o":[33405.5],
    "h":[33417.5],
    "l":[33405.5],
    "c":[33417.5],
    "v":[0.149]
  }

Here are ``o`` --- price of the first deal, ``c`` --- price of the last deal, ``v`` --- sum of sizes (``s``).

Then we make a request to the `/history`_ : ``/history?symbol=BTCUSD&resolution=1&from=1624797120&to=1624797179``.
The resulting bar must match the bar built from `/streaming`_.

Endpoints requirements
......................
Data integration requires the implementation of three endpoints:

* `/symbol_info`_ --- a list of symbols and a set of rules for them; the endpoint is requested once an hour.
* `/history`_ --- full data history for each symbol gaps on 1-minute bars (candles); in some cases, the history of 
  daily bars may be required.
* `/streaming`_ --- a permanent HTTP connection, a stream of messages on completed deals; data feed should provide 
  trades and quotes. In some cases, daily bars may be required.

If your data is not public, you can add authorization via the `/authorize`_ endpoint. Two authentication options are 
supported: `PasswordBearer`_ and `ServerOAuth2Bearer`_.

Types of environments
......................

We strongly recommend using two environments in the integration process: staging and production. Each environment must 
have a separate URL.

First, the broker's staging connects to the staging of TradingView. Initial automated testing is done here, and then 
manual tests are performed after. 

.. important::
  The broker staging API should provide real data.

When the acceptance tests are successful, the broker deploys own code to the production environment. The final testing 
of the broker's production API and the deployment of the TradingView client applications are to be performed here.

All changes on the broker side go through the following steps after the deployment to the TradingView production:

* Changes are made in the broker's staging environment.
* They are then tested on the TradingView side.
* The broker transfers the changes to the production once confirmed by TradingView.

Both environments on the TradingView side are switched to the production URL once the broker's API is deployed to 
production.

.. note::
  Thus, there will be 4 client applications running on the TradingView side all the time, which will interact with the 
  broker's production API: 2 in the staging, and 2 in the production.

Each of these applications will maintain at least one persistent HTTP connection to the `/streaming`_ endpoint and make
regular requests to the `/symbol_info`_, `/history`_. The data is requested only by our API client applications running
on the servers. The end-user browser never makes requests to these endpoints.

TradingView client applications use a separate set of credentials per environment by default (if authorized).

Therefore, the broker should provide at least two independent sets of credentials to its production API: one is for 
clients in the TradingView production, one is for clients in the staging, testing and development.

If the number of simultaneous connections is limited to one connection per account, the broker needs to provide the 
required number of credentials sets:

* two for client applications in the staging,
* two for client applications in the production,
* two for development and testing.