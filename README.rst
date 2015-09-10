twilio-thinq-python
===================

To use (with caution), simply do::

    >>> from twilio_with_thinq import TwilioWrapper
    >>> wrapper = TwilioWrapper(customer_number, twilio_account_sid, twilio_auth_token, twilio_phone_number)
    >>> print "Call sid: " + str(wrapper.call())