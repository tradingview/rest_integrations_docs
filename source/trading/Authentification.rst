.. contents::
   :depth: 5

Authentication
--------------
| After passing the authentication, regardless of the method of obtaining the access token, all requests to the broker's
  REST server will be signed using the ``"Authorization: Bearer ACCESS_TOKEN"`` header.

Password Bearer
...............
| In this type of authorization, the user enters the login and password on the TradingView website.
| The broker's server receives the entered user credentials in a POST request to the ``/authorize`` endpoint. Fields
  expected in response:

* ``access_token`` - directly the value of access token, which will be used to sign requests to the broker's REST server
* ``expiration`` - an optional parameter that defines the expiration time of the token in the form of a unix timestamp.
  In the current implementation, with this authentication method, the token will not be updated, even if the expiration
  field is received in the response and this moment of time approaches. This is due to TradingView's security policy,
  which prohibits the storage of any user credentials from third-party resources on the TradingView side.

| By default, placeholders in the authorization pop-up window have the values ``login`` and ``password``. However, at
  the request of the broker, they can be replaced. In this case, new placeholders must be provided in English.

OAuth2Bearer
............
| TradingView's security policy does not allow the same OAuth secrets for all of the six supported
  :ref:`connections<environments-label>` between the TradingView client and the broker's server. Therefore, all
  ``client_id`` values (and ``client_secret`` values in case of using the *OAuth2 Code flow* authorization option) must
  be unique. On the TradingView side, all OAuth secrets are kept in a special high-security secret vault. Security audits
  are performed regularly.

.. important:: Since the procedure for refreshing the token occurs asynchronously and takes some time, it is possible
  that there will be a period of time after the broker's server issues a new access token, during which it will receive
  requests with the old access token, since the new access token is not yet managed to reach the client. Therefore,
  the broker's server should not invalidate the old access token immediately after issuing a new one and accept requests
  with the old access token for some time, at least until the requests come with the new access token.

OAuth2 Implicit flow
''''''''''''''''''''
| This type of authorization is implemented in accordance with the `RFC 6749 <https://datatracker.ietf.org/doc/html/rfc6749#section-4.2>`_.
  The procedure for OAuth2 Implicit flow is as follows.

Authorization
"""""""""""""
#. The user selects a broker in the Trading panel on the Chart page on the TradingView website.
#. The user is shown a login popup where the user clicks the ``Continue`` button
#. A new browser tab is opened by the Authorization URL of the broker, in the GET parameters of the request are transmitted:

    * ``response_type`` - the value will always be ``token``
    * ``client_id`` - unique identifier of the client
    * ``redirect_uri`` - Redirection Endpoint. For security reasons, it is better to configure the value of this
      parameter on your server and, when receiving an authorization request, check this parameter for compliance with
      the one in the configuration
    * ``scope`` - an optional parameter, the value of which is pre-registered on the TradingView side
    * ``state`` - a string value used to maintain state between the request and the callback. Shouldn't be changed on
      the broker's server and should return to the callback unchanged.
    * ``prompt`` - the parameter takes the value of ``login`` when requesting authorization and value of ``none`` when
      requesting to refresh the token
    * ``lang`` - a parameter on demand, transfers the locale of the TradingView site, which the user uses at the time of
      authorization from the list ``ar``, ``br``, ``cs``, ``de``, ``el``, ``en``, ``es``, ``fa``, ``fr``, ``he``, ``hu``,
      ``id``, ``in``, ``it``, ``ja``, ``kr``, ``ms``, ``nl``, ``pl``, ``ro``, ``ru``, ``sv``, ``th``, ``tr``, ``uk``,
      ``vi``, ``zh``.

#. The broker's server gives a page with an authorization form and prompts the user to enter their credentials.
#. The broker's server authenticates and authorizes the user after submitting the form and, if successful, redirects
   the request to ``redirect_uri`` with parameters that are passed as a fragment

    * ``access_token`` - directly the value of access token, which will be used to sign requests to the broker's REST
      server
    * ``state`` - the unchanged value of the state field from the original authorization request
    * ``expires_in`` - an optional parameter that defines the token lifetime in seconds. If this parameter is omitted,
      the token will not be updated. But it must be borne in mind that this can harm the user's safety.

.. important:: The browser tab on which the authorization process is underway will in any case be closed after 120 seconds
  from the moment it was opened, even if the access token has not been received. Therefore, you should not require any action
  from the user on this tab, except for entering credentials. If, for example, it is required to give the user the opportunity
  to sign-up, then this should be done in another tab, opened using an external link from the authorization tab.

Refresh Token
"""""""""""""

| When the access token expires approaching, TradingView automatically launches the access token refresh procedure, which
  follows the following scenario.

* TradingView opens a hidden iframe using the Broker's Authorization URL, all the same parameters are sent in the
  GET request parameters as during authorization, with the exception of the ``prompt`` parameter, which takes the value
  of ``none`` and thereby informs the broker's server that the background refresh of the access token is taking place
* The broker's server, having received a request with the ``prompt: none`` parameter, instead of displaying a page with
  an authorization form, immediately redirects the request for a Redirect URL with a new access token.

| To identify the user when updating the token, it is possible to leave the ``httpOnly`` cookie on the authorization page
  when the initial authentication passes.

.. warning:: There is a problem that if the user has disabled third-party cookies in his browser, then this cookie will
   not be sent to the broker's server in a request to refresh the token. Within the option of *OAuth2 Implicit flow*,
   this problem is not solved in any way. Therefore, it is preferable to use the *OAuth2 Code flow* option, which does not
   have this problem when refreshing the token.

OAuth2 Code flow
''''''''''''''''
| This type of authorization is implemented in accordance with the `RFC 6749 <https://datatracker.ietf.org/doc/html/rfc6749#section-4.1>`_.
| Unlike OAuth2 Implicit flow, OAuth2 Code flow does not have a problem with user identification when refreshing
  an access token, so a refresh token can be used for this and there is no need for cookies. In addition, the procedure
  for obtaining the access token directly and updating it is performed between the TradingView servers and the broker,
  so the OAuth2 Code flow option is much more secure than the OAuth2 Implicit flow.
| The procedure for OAuth2 Code flow is as follows.

Authorization
"""""""""""""
#. The user selects a broker in the Trading panel on the Chart page on the TradingView website.
#. The user is shown a login popup where the user clicks the ``Continue`` button
#. A new browser tab is opened by the Authorization URL of the broker, in the GET parameters of the request are transmitted:

    * ``response_type`` - the value will always be ``token``
    * ``client_id`` - unique identifier of the client
    * ``redirect_uri`` - Redirection Endpoint. For security reasons, it is better to configure the value of this
      parameter on your server and, when receiving an authorization request, check this parameter for compliance with
      the one in the configuration
    * ``scope`` - an optional parameter, the value of which is pre-registered on the TradingView side
    * ``state`` - a string value used to maintain state between the request and the callback. Shouldn't be changed on
      the broker's server and should return to the callback unchanged.
    * ``prompt`` - the parameter takes the value of ``login`` when requesting authorization and value of ``none`` when
      requesting to refresh the token
    * ``lang`` - a parameter on demand, transfers the locale of the TradingView site, which the user uses at the time of
      authorization from the list ``ar``, ``br``, ``cs``, ``de``, ``el``, ``en``, ``es``, ``fa``, ``fr``, ``he``, ``hu``,
      ``id``, ``in``, ``it``, ``ja``, ``kr``, ``ms``, ``nl``, ``pl``, ``ro``, ``ru``, ``sv``, ``th``, ``tr``, ``uk``,
      ``vi``, ``zh``.

#. The broker's server gives a page with an authorization form and prompts the user to enter their credentials.
#. The broker's server authenticates and authorizes the user after submitting the form and, if successful, redirects
   the request to redirect_uri with GET parameters:

    * ``code`` - an authorization code with a short expiration time, which will subsequently be exchanged for an access token
    * ``state`` - the unchanged value of the state field from the original Authorization request

#. The TradingView Server sends a POST request for the access token to the token endpoint of the broker's server with
   the following parameters in the ``application/x-www-form-urlencoded`` format.

    * ``grant_type`` - the value is always equal to ``authorization_code``
    * ``code`` - authorization code obtained from response to Authorization request
    * ``client_id`` - unique identifier of the client
    * ``client_secret`` - a unique client secret. This parameter has been added for compatibility with the
      `Auth0 service <https://auth0.com/docs/authorization/flows/call-your-api-using-the-authorization-code-flow>`_,
      where it is required
    * ``redirect_uri`` - the same Redirect URI as in the Authorization Request

#. The broker's server sends a response to a request for an access token with a body with the following fields:

    * ``token_type`` - value must be ``bearer``
    * ``access_token`` - access token that will be used in REST requests to the broker's server
    * ``expires_in`` - token lifetime in seconds
    * ``refresh_token`` - a token that is exchanged for a new access token before the expiration of the current access token

Refresh Token
"""""""""""""
| When the expiration time of the current access token approaches, the TradingView server automatically starts the procedure
  for refreshing the access token. To do this, a request is sent to the broker's server for the token endpoint with
  the following parameters:

    * ``grant_type`` - the value will always be ``refresh_token``
    * ``refresh_token`` - a refresh token received in the same request as the current access token
    * ``client_secret`` - the value of the client secret provided by the broker.

| The response is expected to be exactly the same as for the request to obtain an access token during the initial
  authorization.
