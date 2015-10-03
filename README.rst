twilio-thinq-python, Twilio Wrapper Python Library For thinQ LCR integration
=========================================================================

**Note that you will need a valid LCR Account with thinQ before using the libraries. For more information please contact your thinQ Sales representative at `http://www.thinq.com/library/ <http://www.thinq.com/library/>`_**
----------------------------------------------------------------------------------------------------------------

To use (with caution), simply do::

    >>> from twilio_with_thinq import TwilioWrapper
    >>> wrapper = TwilioWrapper(customer_number, twilio_account_sid, twilio_auth_token, twilio_phone_number)
    >>> print "Call sid: " + str(wrapper.call())