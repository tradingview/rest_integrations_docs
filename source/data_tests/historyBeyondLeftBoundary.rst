.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory

historyBeyondLeftBoundary
-------------------------
.. Data boundary test

* This test runs only if ``--left`` (data boundary) parameter is set. 
* This test checks if the API returns ``no_data`` response beyond left boundary. 
* In the test setting value ``to="left - 10 minutes"``, making a request and expecting to get ``s="no_data"`` without 
  ``nb`` field. 
* If ``"has-intraday"=false`` is specified for the symbol in the symbol info, then the test for this symbol will be 
  skipped.

Request error
  Error on sending HTTP request to `/history`_ endpoint.

Data is available
  There is data beyond data boundary.

Next Bar is present
  There is ``nb`` field with non-zero timestamp in ``no_data`` response.