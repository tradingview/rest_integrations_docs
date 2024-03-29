.. links
.. _`Jenkins`: https://cu-jenkins.xtools.tv
.. _`autotest service`: https://cu-jenkins.xtools.tv
.. _`TradingView REST API`: https://www.tradingview.com/rest-api-spec/
.. _`Data_integrations section`: https://cu-jenkins.xtools.tv/job/Data_integration/
.. _`Trading section`: https://cu-jenkins.xtools.tv/job/Trading/
.. _`/authorize`: https://www.tradingview.com/rest-api-spec/#operation/authorize

Trading integration tests
=========================

.. contents:: :local:
  :depth: 1

Test stages
-----------
In general, trading integration testing is independent of the :doc:`data integration <../data/index>` (exceptions are 
:ref:`described separately<trading-mapping-how-to-match-symbols>`) and happens in several stages.

While preparing for implementation, the broker provides a list of features available to its platform users. Based on 
that list, we compile a set of test cases and pass them to the broker. These test cases help to make sure that the 
integration with the TradingView user interface works correctly.

We provide a special `autotest service`_ for the `TradingView REST API`_. Please be aware that your API implementation 
needs to pass these tests successfully in order to be added to the :ref:`TradingView sandbox<hat-is-the-sandbox>`.

You can request access to the service if only even one part of the endpoints (either data or trading) is implemented. 
Below is a guide on how to use this service.

Test structure
--------------

We provide `Jenkins`_ for the automated testing of the trading and data integration endpoints implementation.

Use `Data_Integrations section`_ to test data integration, and `Trading section`_ for trading integration.

.. image:: ../../images/TradingTests_TestStructure_JenkinsSections.png
   :scale: 100 %
   :alt: Sections list
   :align: center

Each section contains a project with the broker's name on it.

.. image:: ../../images/TradingTests_TestStructure_JenkinsPlans.png
   :scale: 100 %
   :alt: Plans list
   :align: center

There are three options for authorization into the broker's API server. 

* You can implement an `/authorize`_ endpoint specifically for testing and use a login-password pair.
* Use a permanent hardwired token.
* Leave ``ACCESS_TOKEN`` field empty, and enter it manually.

Select the desired option and then provide us with the credentials and API server address in order to use the 
`autotest service`_.

Launching the tests
-------------------

.. image:: ../../images/TradingTests_Launching_JenkinsBuildWithParametersA.png
   :scale: 80 %
   :alt: Plans list
   :align: center

* Go to your build plan (Jenkins → Trading → Broker_name) to run the test.
* Open the **Build with Parameters** section.
* Change the build parameters if necessary.
* Click the **Build** button.

.. image:: ../../images/TradingTests_Launching_JenkinsBuildWithParametersB.png
   :scale: 40 %
   :alt: Plans list
   :align: center

The following parameters are used for the build:

* ``REST_API_URL`` --- your `TradingView REST API`_ implementation address;
* ``LOGIN``, ``PASSWORD`` --- data for ``REST_API_URL`` access with the login/password authorization;
* ``ACCESS_TOKEN`` --- token (in case token authorization is used);
* ``SSHOST`` --- Symbol Search host.

The fields contain default data (pre-sent by the broker). The value of sensitive ``PASSWORD`` or ``ACCESS_TOKEN`` 
parameters can be masked. The values can be changed if required.

Results analysis
----------------

Go to the **Allure Report** section to view the test results. It is available in the panel on the left side and in the 
**Build History** below.

.. image:: ../../images/TradingTests_Results_AllureReport.png
   :scale: 80 %
   :alt: Plans list
   :align: center

The **Categories** section shows information about failed tests. So, in the **Suites** section you can find the 
results of the failed and passed tests. 

In addition to the error message itself, pay attention to the following fields:

* **Request** --- API request body;
* **Response** --- response received;
* **Error** --- the results of comparison of the response received vs. expected response.

.. image:: ../../images/TradingTests_Results_AllureErrors.png
   :scale: 80 %
   :alt: Plans list
   :align: center