
historyOutsideBarsInclusion
---------------------------

Checking the inclusion of the last bars in the response and the number of bars. 

``to = "current to minutes - 30 minutes - 1 second"``, ``from = "to - 50 minutes + 1 second"``, requesting minute 
historical data. Expecting to get ``50`` bars (if there are no gaps). 

If less than ``50`` bars were received, then there was a gap and writing a warning in the log, if more than ``50`` 
bars were received --- getting an error. 

If there were ``50`` bars, then checking if the time of the first and the last bars is correct. 

* Expecting, that the number of minutes in the time of the first bar is equal to the number of minutes in from 
  parameter.
* Expecting, that the number of minutes in the time of the last bar is equal to the number of minutes in the from 
  parameter. 

If ``"has-intraday"=false`` is specified for the symbol in the symbol info, then the test for this symbol will be 
skipped.