.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory

historyNoDataChanges
--------------------

* ``from = "current - 30 minutes"``, ``to = "current"``, making request. 
* Then no requests for 2 minutes, after that, making request again with the same from, but updating to. 
* Then verifying that the result of the second query includes the results of the first query, that is, the bars from 
  the first query are at the beginning of the second. 
* If ``has-intraday=false`` is specified for the symbol in the symbol info, then the test for this symbol will be 
  skipped.