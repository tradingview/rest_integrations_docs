.. links
.. _`/authorize`: https://www.tradingview.com/rest-api-spec/#operation/authorize
.. _`ServerOAuth2Bearer`: https://www.tradingview.com/rest-api-spec/#section/Authentication/ServerOAuth2Bearer

Authentication
--------------

For the `/authorize`_ endpoint, you should use either :ref:`PasswordBearer <password-bearer-flow>` or 
`ServerOAuth2Bearer`_. But, if your integration imply brokerage data stream and your data is public, you might not have
to implement the authorization endpoint. 

You should have two separate sets of credentials for your production server. So, for OAuth2, these are different client 
id, client secret and private key. Each request to `/authorize`_ must return a unique token with a limited lifetime. 
Several clients must be able to log in with one set of credentials.

If `/authorize`_ exists, all requests without a token or with an expired token should return code ``401``.