
historyNoDataWithNb
-------------------

In this test we check that ``no_data`` comes with an ``nb`` value. 
For this test we need to find the gaps and make sure that they have ``nb``. 

To do this, requesting a large piece of minute historical data. ``from = "the beginning of the session"``, 
``to = "from + 500 minutes"``, making request, looking for missing bars in the response. 

For example, in response it\'s ``time = x`` for one bar, the next one has ``x + 120``, so the bar between them is 
missing. 

Then requesting the missing bar separately and checking that the response should contain ``s="no_data"`` and correct 
``nb``. 

If ``"has-intraday" = false`` is specified for the symbol in the symbol info, then the test for this symbol will be 
skipped.