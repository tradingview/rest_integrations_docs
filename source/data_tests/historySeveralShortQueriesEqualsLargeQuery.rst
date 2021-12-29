
historySeveralShortQueriesEqualsLargeQuery
------------------------------------------

The purpose of this test is to verify that one large query and several small queries will give the same result, the 
same bars. 

``from = "start of session"``, ``to = "from + 200 minutes"``. Making one large query with data from and to. 

* Then making several small queries. Small queries are queries with 20-minute interval. 
* Then checking if the bars are the same. 

If ``"has-intraday"=false`` is specified for the symbol in the symbol info, then the test for this symbol will be 
skipped.