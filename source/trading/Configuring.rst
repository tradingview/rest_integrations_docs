.. contents::
   :depth: 5

Configuring
-----------
| There are three levels of configuration:

* broker level - applies to all subaccounts defined for the user, is carried out in the ``/config`` request
* subaccount level - extends to UI elements for a specific subaccount, is carried out in the ``/accounts`` request
* instrument level - to configure UI elements for a specific instrument, via the ``/instruments`` request

| All these requests are made once when logging into the broker integration. The configuration priority of the same
  UI elements is broker, account, instrument. Each subsequent one overrides the previous one.

Pulling intervals
.................
| Pulling intervals are configurable at the broker level only and are designed to determine the frequency of requests
  to a specific endpoint. When configuring them, it is necessary to take into account the capabilities of the
  infrastructure on the broker's side in order to avoid errors in requests for violation of rate limits, the accumulation
  of which may lead to disconnection of the broker's integration.
| Despite the fact that TradingView doesn't strictly limit the size of the pulling intervals for requests, we strongly
  don't recommend setting values for the pulling intervals exceeding the maximum recommended. When exceeded, our UI may
  become unresponsive to the user experience, which may lead to user complaints.

| Matching fields to requests:

* ``quotes`` - the ``/quotes`` and ``/depth`` requests  (max 1000ms)
* ``accountManager`` - the ``/state`` request (max 1500ms)
* ``orders`` - the ``/orders`` request (max 1500ms)
* ``positions`` - the ``/positions`` request (max 1500ms)
* ``balances`` - the ``/balances`` request (max 1500ms)

Durations
.........
| In the TradingView REST API, it is possible to configure Duration (or Time In Force) separately for each of
  the supported order types. By default, any item from the Durations list will be shown in the order ticket for Limit,
  Stop and Stop-limit orders  only. If this list should be different from the default for any of the Durations elements,
  then it is necessary to send the list for this element in the ``supportedOrderTypes`` field as an array consisting
  of the types of orders for which this Duration is available.

Account Summary Row
...................
| The ``Account Summary Row`` is a line that is always displayed after login to the integration. It contains the most
  important information about the current state of the subaccount that is currently selected by the user. By default,
  the ``Account Summary Row`` contains the ``Account Balance``, ``Equity`` and ``Profit`` fields, which display
  the values of the ``balance``, ``equity`` and ``unrealizedPL`` fields from the ``/state`` request. However,
  if necessary, the ``Account Summary Row`` allows to display other necessary broker's information. To do this, it is
  nessesary to configure the ``Account Summary Row``, and it can be configured both at the broker level - it will be
  displayed the same for all subaccounts, and at the subaccount level - it will display information for the account
  currently selected by the user, and it can be different for different subaccounts.
| For custom configuration of the Account Summary Row you need:

#. In the ``/config`` request enable the ``supportCustomAccountSummaryRow`` flag
#. Configure the ``Account Summary Row`` fields either at the broker level in the ``/config`` request in the
   ``accountSummaryRow`` object, or at the account level in the ``/accounts`` request within the ``ui`` object in
   the ``accountSummaryRow`` object. Moreover, the latter is of higher priority and will be applied if there is
   a configuration at both levels.
#. In the ``/state`` request in the ``accountSummaryRowData`` object, send values for the ``Account Summary Row`` as
   array of string values. The order and size of the sent array must match the order and size of the array specified in
   the configuration.

| If the size of the ``Account Summary Row`` display area is insufficient, for example, when using screens with a lower
  resolution or reducing its display area by increasing the display area of other items, the ``Account Summary Row``
  items are gradually hidden from the very first. Therefore, it makes sense to arrange information in order of increasing
  importance.

Account Summary Tab
...................
| The ``Account Summary Tab`` displays the information received in the ``/state`` request in a set of tables. By default,
  one table is displayed, which uses the values of the ``balance``, ``unrealizedPL`` and ``equity`` (if sent, it is optional)
  fields. But it is possible to flexibly configure the information displayed on the ``Account Summary Tab``. This can
  be done both at the broker level and will be displayed the same regardless of which account is currently selected by
  the user, and at the subaccount level, in which case its own information will be displayed for each subaccount.
  The ``accountManager`` object, which is sent at the broker level in the ``/config`` request or at the subaccount level
  in the ``/accounts`` request inside the ``ui`` object, contains an array of table objects, inside each of them
  the columns of each table are defined. Values for tables, regardless of the configuration level, are passed in the
  ``/state`` request in the ``amData`` object, which is an array of tables of arrays of rows of arrays of columns as
  string values and must be exactly the same size as the object defined in the configuration.
