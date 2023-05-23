.. links
.. _`/authorize`: https://www.tradingview.com/rest-api-spec/#operation/authorize
.. _`Auth0 service`: https://auth0.com/docs/authorization/flows/call-your-api-using-the-authorization-code-flow
.. _`Redirection Endpoint`: https://tools.ietf.org/html/rfc6749#section-3.1.2

Authentication
--------------

.. contents:: :local:
   :depth: 2

After passing the authentication, regardless of the method of obtaining the access token, all requests to the 
broker's REST server will use the ``Authorization: Bearer ACCESS_TOKEN`` header.

.. important:: 
  The authentication page must only contain objects relevant to logging and signing-up processes.
  Placing irrelevant links, promos, etc., is not allowed as it goes against the TradingView guidelines and affects the overall user experience.

.. _password-bearer-flow:

Password Bearer
...............
In this type of authorization, the user enters the login and password on the TradingView website.
The broker's server receives the entered user credentials in a POST request to the `/authorize`_ endpoint.

Fields expected in response:

* ``access_token`` --- access token, which will be added to the Authorization Header for requests to the broker's REST
  server.
* ``expiration`` --- token expiration time in Unix Timestamp format, an optional parameter.

In the current implementation, the token will not be refreshed, even if the ``expiration`` field is received in the 
response and that point in time is approaching. For better security, please use 
:ref:`OAuth2 Code flow<oauth2-code-flow>`.

By default, placeholders in the authorization pop-up window have the values ``login`` and ``password``.
If you wish to change these values, provide your version in English.

.. _oauth2-flow:

OAuth2Bearer
............
TradingView's security policy does not allow the same OAuth secrets for all of the six supported
:ref:`connections<trading-environments>` between the TradingView client and the broker's server. Therefore, all
``client_id`` values (and ``client_secret`` values in case of using the :ref:`OAuth2 Code flow<oauth2-code-flow>`
authorization option) must be unique. On the TradingView side, all OAuth secrets are kept in a special high-security 
secret vault. Security audits are performed regularly.

.. important:: :ref:`OAuth2 Implicit flow<oauth2-implicit-flow>` and :ref:`OAuth2 Code flow<oauth2-code-flow>` support
  token refreshing. The token is refreshed asynchronously and takes some time. Therefore, the broker's server must
  accept requests with the old access token until requests come with the new token. After that, the old token can be
  invalidated.

.. _oauth2-implicit-flow:

OAuth2 Implicit flow
''''''''''''''''''''
This type of authorization is implemented following :rfc:`6749#section-4.2`. Let's consider
:ref:`authorization<oauth2-implicit-flow-authorization>` and :ref:`refresh token<oauth2-implicit-flow-refresh-token>`
procedures.

.. important:: The :ref:`OAuth2 Implicit flow<oauth2-implicit-flow>` will be deprecated in the future. Please consider
  using the :ref:`OAuth2 Code flow<oauth2-code-flow>`.

.. _oauth2-implicit-flow-authorization:

Authorization
"""""""""""""
1. A user opens the *Chart* page on the TradingView website, then selects a broker in the *Trading Panel*.
2. A login popup appears. The user clicks the *Continue* button on this popup.
3. A new browser tab opens at the broker's *Authorization URL*.
4. The following query parameters are sent in the GET request:

   * ``response_type`` --- the value will always be ``token``.
   * ``client_id`` --- unique identifier of the client.
   * ``redirect_uri`` --- `Redirection Endpoint`_. For security reasons, it is better to configure the value of 
     this parameter on your server and, when receiving an authorization request, check this parameter for 
     compliance with the one in the configuration.
   * ``scope`` --- an optional parameter, the value of which is pre-registered on the TradingView side.
   * ``state`` --- a string value used to maintain the state between the request and the callback. Should not be
     modified on the broker's server and should return to the callback unchanged.
   * ``prompt`` --- the parameter takes the ``login`` value when requesting authorization and the ``none`` value when
     requesting to refresh the token.
   * ``lang`` --- a parameter on demand, transfers the locale of the TradingView platform, which a trader uses at 
     the time of authorization from the list ``ar``, ``br``, ``cs``, ``de``, ``el``, ``en``, ``es``, ``fa``, 
     ``fr``, ``he``, ``hu``, ``id``, ``in``, ``it``, ``ja``, ``kr``, ``ms``, ``nl``, ``pl``, ``ro``, ``ru``, 
     ``sv``, ``th``, ``tr``, ``uk``, ``vi``, ``zh``.

5. The broker's server gives a page with an authorization form and prompts the user to enter their credentials.
6. The broker's server authenticates and authorizes the user after submitting the form and if successful redirects
   the request to ``redirect_uri`` with following parameters that are passed as a fragment:

   * ``access_token`` --- the value of access token which will be used to sign requests to the broker's REST server.
   * ``state`` --- the value of the ``state`` field from the original authorization request. Should return unchanged.
   * ``expires_in`` --- an optional parameter that defines the token\'s lifetime in seconds. If this parameter is
     omitted, the token will not be refreshed. Note, that this can harm the user\'s safety.

.. important:: The authorization process takes place on a separate tab. It will close in **120 seconds** after opening, 
  even if no access token has been received. You should not require the user to do anything on this tab other than 
  enter credentials. For example, you want to give a user the ability to sign up. Place a link that opens a new sign up
  tab in the authorization tab.

.. _oauth2-implicit-flow-refresh-token:

Token refreshing
""""""""""""""""
When the access token expires, TradingView triggers a token renew. It happens in the following scenario:

* TradingView opens a hidden iframe at the Broker's *Authorization URL*. The GET request has the same query parameters
  as during authorization except the prompt parameter, which is set to ``none`` to tell the broker's server to refresh
  the access token in the background.
* After receiving a request with the ``prompt: none`` parameter, the broker's server redirects the request to the 
  *Redirect URL* with a new access token. The page with the authorization form does not show to the user.

It is possible to set the ``httpOnly`` cookie on the authorization page when the token is renewed after passing the 
initial authentication. It will allow you to identify the user in the future.

.. warning:: If third-party cookies are disabled in the user's browser, you will not be able to identity that user
  with the ``httpOnly`` cookie. It is preferable to use the :ref:`OAuth2 Code flow<oauth2-code-flow>`, which does not
  have this issue when updating the token.

.. _oauth2-code-flow:

OAuth2 Code flow
''''''''''''''''

This type of authorization is implemented following :rfc:`6749#section-4.1` and is more secure than the 
:ref:`OAuth2 Implicit flow<oauth2-implicit-flow>`. There is no difficulty with user identification during token 
refreshing. The procedures for :ref:`obtaining<oauth2-code-flow-authorization>` an access token and its 
:ref:`renewal<oauth2-implicit-code-refresh-token>` are performed between the TradingView servers and the broker's 
server, and avoid storing the token on the client side.

.. _oauth2-code-flow-authorization:

Authorization
"""""""""""""
1. A user opens the *Chart* page on the TradingView website, then selects a broker in the *Trading Panel*.
2. A login popup appears. The user clicks the *Continue* button on this popup.
3. A new browser tab opens at the broker's *Authorization URL*.
4. The following query parameters are sent in the GET request:

   * ``response_type`` --- the value will always be ``code``.
   * ``client_id`` --- a unique identifier of the client.
   * ``redirect_uri`` --- `Redirection Endpoint`_. For security reasons, when receiving an authorization request, check
     this parameter for compliance with the one in the configuration.
   * ``scope`` --- an optional parameter, the value of which is pre-registered on the TradingView side, if it is
     provided by the broker.
   * ``state`` --- a string value used to maintain the state between the request and the callback. Shouldn't be
     modified on the broker's server and should return to the callback unchanged.
   * ``lang`` --- a parameter on demand, transfers the locale of the TradingView platform, which a trader uses at the
     time of authorization from the list ``ar``, ``br``, ``cs``, ``de``, ``el``, ``en``, ``es``, ``fa``, ``fr``,
     ``he``, ``hu``, ``id``, ``in``, ``it``, ``ja``, ``kr``, ``ms``, ``nl``, ``pl``, ``ro``, ``ru``, ``sv``, ``th``,
     ``tr``, ``uk``, ``vi``, ``zh``.

5. The broker's server gives a page with an authorization form and prompts the user to enter their credentials.
6. The broker's server authenticates and authorizes the user after submitting the form.
7. If successful, the broker's server redirects the request to ``redirect_uri`` with GET parameters:

   * ``code`` --- an authorization code with a short expiration time, which will subsequently be exchanged for an
     access token.
   * ``state`` --- the value of the ``state`` field from the original authorization request. Should return unchanged.

8. The TradingView server sends a POST request for an access token in the ``application/x-www-form-urlencoded`` 
   format to the token endpoint of the broker's server with the following parameters:

   * ``grant_type`` --- the value always equal to ``authorization_code``.
   * ``code`` --- authorization code obtained from a response to authorization request.
   * ``client_id`` --- a :ref:`unique identifier <faq-unique-client-secrets>` of the client.
   * ``client_secret`` --- a unique client secret. This parameter has been added for compatibility with the 
     `Auth0 service`_, where it is required.
   * ``redirect_uri`` --- the same *Redirect URI* as in the authorization request.

9. The broker's server sends a response to a request for an access token with the following fields in its body:

   * ``token_type`` --- the value must be ``bearer``.
   * ``access_token`` --- access token\'s that will be used in REST requests to the broker's server.
   * ``expires_in`` --- token lifetime in seconds.
   * ``refresh_token`` --- a token that is exchanged for a new access token before the expiration of the current 
     access token.

.. _oauth2-implicit-code-refresh-token:

Token refreshing
""""""""""""""""

When the *access token* expiration is approaching, TradingView automatically starts the token renewal procedure.
A request for a token endpoint is sent to the broker's server with the following parameters:

* ``grant_type`` --- the value will always be ``refresh_token``.
* ``refresh_token`` --- a refresh token received in the same request as the current access token.
* ``client_secret`` --- the value of the :ref:`unique client secret <faq-unique-client-secrets>` provided by the 
  broker.

The response is expected to be the same as for the request to obtain an access token during the initial
authorization.
