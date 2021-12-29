streamingTransferEncodingHeader
-------------------------------

``Transfer-Encoding`` header test, the expected set value is ``chunked``. However, it mainly depends on the protocol 
version supported by the service under test, if it\'s HTTP/2.0, then the test is skipped with the corresponding 
message in the log, since HTTP/2.0 doesn\'t support this header.