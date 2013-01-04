from pyotp.otp import OTP
from pyotp.hotp import HOTP
from pyotp.totp import TOTP
import base64
import random


VERSION = '1.3.0'


def random_base32(length=16, random=random.SystemRandom(),
                  chars=base64._b32alphabet.values()):
    return ''.join(
        random.choice(chars)
        for i in xrange(length)
    )
