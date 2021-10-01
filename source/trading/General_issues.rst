.. contents::
   :depth: 5

General issues
--------------

.. _environments-label:

Different environments
......................
| During the development and further support of integration on the broker's server, a staging environment can be used.
  That is, a broker can have two environments - production and staging. Each of them has its own URL.
| The TradingView website can also be launched in production (available to users), staging (used by testers) or on
  the local computer of the TradingView developer (localhost). Thus, there are 6 options for connecting the
  TV application and the broker's server:

* TV production - Broker production
* TV staging - Broker production
* TV localhost - Broker production
* TV production - Broker staging
* TV staging - Broker staging
* TV localhost - Broker staging

| The TradingView website in staging or production can only be connected to one broker environment at a time. Switching
  between broker environments is carried out through the browser console. Switching instructions can be obtained after
  the appropriate configuration by the TradingView team.

.. _cors-policy-label:

Configuring CORS policy on the broker side
..........................................
| Since requests to the broker originate from the browser, the broker needs to include the ``Access-Control-Allow-Origin``
  header in the response at each endpoint for each response code, indicating the specific subdomain that sent the request.
  TradingView can send a request from any ``*.tradingview.com`` subdomain. This is due to the fact that subdomains contain
  test servers, as well as local versions of the site, for example ``de.tradingview.com`` for the German version of the site.
  Also, on the broker\'s staging environment, it is necessary to allow requests from ``localhost:6285``, which is used
  on the TradingView developers\' computers.

Localization support
....................
| Although the integration of a specific broker may be targeted primarily at an audience using their own national
  language, it must support English in at least all requests coming from the main locale of the TradingView application.
  All requests coming from the client to the broker's server have the ``locale`` parameter, so it is always possible to
  identify the locale that the user is using.

.. _mapping-symbols-label:

Mapping symbols
...............

What is mapping
'''''''''''''''
| We call symbol mapping the mapping between the names of the broker's instruments and TradingView.

When is mapping necessary
'''''''''''''''''''''''''
| Mapping is necessary if the broker does not integrate its data in whole or in part on the TradingView servers, but
  uses the data already connected.


How to implement mapping
''''''''''''''''''''''''
| Mapping is set with the ``/mapping`` endpoint implementation. This endpoint must be accessible without authorization.
  In TradingView production, it is automatically requested once a day, and based on the response to the request,
  a mapping of instruments is generated on the TradingView side. In TradingView staging, the ``/mapping`` request is made
  manually if necessary.
| At the development stage, you can set a partial mapping, i.e. not for all instruments supported by the broker.

How to match symbols
''''''''''''''''''''
| To find a TradingView symbol, you can use JSON with a full list of all symbols:
  ``https://s3.amazonaws.com/tradingview-symbology/symbols.json``.
| This file is updated on daily basis. When generating a response to the ``/mapping`` request, broker must use
  the ``symbol-fullname`` field value as the TradingView symbol.
| If the broker partially uses TradingView data and partially connects his own, mapping must be done for all symbols.

Sandbox
.......

What is the Sandbox
''''''''''''''''''''
| The Sandbox is a fully functional copy of the TradingView website located at ``https://beta-rest.tradingview.com/``.

When broker's integration can be placed in the Sandbox
''''''''''''''''''''''''''''''''''''''''''''''''''''''
| The Sandbox can be accessed only from IP addresses that were previously placed in the whitelist on the TradingView side.
  The broker integration at the development stage can be placed in the sandbox only after passing the conformational
  tests at `https://www.tradingview.com/rest-api-test/ <https://www.tradingview.com/rest-api-test/>`_ and having
  the market data necessary for the integration to work, at least at the TradingView staging. In the absence of a data
  integration stage, when the broker is going to use the market data that is already available in TradingView,
  a prerequisite for placing it in the sandbox is the implementation of the
  `/mapping <https://www.tradingview.com/rest-api-spec/#operation/getMapping>`_ endpoint.
