from pyotp.otp import OTP
import urllib


class HOTP(OTP):
    def at(self, count):
        """
        Generates the OTP for the given count
        @param [Integer] count counter
        @returns [Integer] OTP
        """
        return self.generate_otp(count)
    
    def verify(self, otp, counter):
        """
        Verifies the OTP passed in against the current time OTP
        @param [String/Integer] otp the OTP to check against
        @param [Integer] counter the counter of the OTP
        """
        return otp == self.at(counter)
    
    def provisioning_uri(self, name, initial_count=0):
        """
        Returns the provisioning URI for the OTP
        This can then be encoded in a QR Code and used
        to provision the Google Authenticator app
        @param [String] name of the account
        @param [Integer] initial_count starting counter value, defaults to 0
        @return [String] provisioning uri
        """
        return 'otpauth://hotp/%(name)s?secret=%(secret)s&counter=%(initial_count)s' % {
            'name': urllib.quote(name, safe='@'),
            'secret': self.secret,
            'initial_count': initial_count,
        }
