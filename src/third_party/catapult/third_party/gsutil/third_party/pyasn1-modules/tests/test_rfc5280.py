#
# This file is part of pyasn1-modules software.
#
# Copyright (c) 2005-2017, Ilya Etingof <etingof@gmail.com>
# License: http://pyasn1.sf.net/license.html
#
import sys

from pyasn1.codec.der import decoder as der_decoder
from pyasn1.codec.der import encoder as der_encoder

from pyasn1_modules import pem
from pyasn1_modules import rfc5280

try:
    import unittest2 as unittest

except ImportError:
    import unittest


class CertificateTestCase(unittest.TestCase):
    pem_text = """\
MIIC5zCCAlACAQEwDQYJKoZIhvcNAQEFBQAwgbsxJDAiBgNVBAcTG1ZhbGlDZXJ0
IFZhbGlkYXRpb24gTmV0d29yazEXMBUGA1UEChMOVmFsaUNlcnQsIEluYy4xNTAz
BgNVBAsTLFZhbGlDZXJ0IENsYXNzIDMgUG9saWN5IFZhbGlkYXRpb24gQXV0aG9y
aXR5MSEwHwYDVQQDExhodHRwOi8vd3d3LnZhbGljZXJ0LmNvbS8xIDAeBgkqhkiG
9w0BCQEWEWluZm9AdmFsaWNlcnQuY29tMB4XDTk5MDYyNjAwMjIzM1oXDTE5MDYy
NjAwMjIzM1owgbsxJDAiBgNVBAcTG1ZhbGlDZXJ0IFZhbGlkYXRpb24gTmV0d29y
azEXMBUGA1UEChMOVmFsaUNlcnQsIEluYy4xNTAzBgNVBAsTLFZhbGlDZXJ0IENs
YXNzIDMgUG9saWN5IFZhbGlkYXRpb24gQXV0aG9yaXR5MSEwHwYDVQQDExhodHRw
Oi8vd3d3LnZhbGljZXJ0LmNvbS8xIDAeBgkqhkiG9w0BCQEWEWluZm9AdmFsaWNl
cnQuY29tMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDjmFGWHOjVsQaBalfD
cnWTq8+epvzzFlLWLU2fNUSoLgRNB0mKOCn1dzfnt6td3zZxFJmP3MKS8edgkpfs
2Ejcv8ECIMYkpChMMFp2bbFc893enhBxoYjHW5tBbcqwuI4V7q0zK89HBFx1cQqY
JJgpp0lZpd34t0NiYfPT4tBVPwIDAQABMA0GCSqGSIb3DQEBBQUAA4GBAFa7AliE
Zwgs3x/be0kz9dNnnfS0ChCzycUs4pJqcXgn8nCDQtM+z6lU9PHYkhaM0QTLS6vJ
n0WuPIqpsHEzXcjFV9+vqDWzf4mH6eglkrh/hXqu1rweN1gqZ8mRzyqBPu3GOd/A
PhmcGcwTTYJBtYze4D1gCCAPRX5ron+jjBXu
"""

    def setUp(self):
        self.asn1Spec = rfc5280.Certificate()

    def testDerCodec(self):

        substrate = pem.readBase64fromText(self.pem_text)

        asn1Object, rest = der_decoder.decode(substrate, asn1Spec=self.asn1Spec)

        assert not rest
        assert asn1Object.prettyPrint()
        assert der_encoder.encode(asn1Object) == substrate


class CertificateListTestCase(unittest.TestCase):
    pem_text = """\
MIIBVjCBwAIBATANBgkqhkiG9w0BAQUFADB+MQswCQYDVQQGEwJBVTETMBEGA1UE
CBMKU29tZS1TdGF0ZTEhMB8GA1UEChMYSW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRk
MRUwEwYDVQQDEwxzbm1wbGFicy5jb20xIDAeBgkqhkiG9w0BCQEWEWluZm9Ac25t
cGxhYnMuY29tFw0xMjA0MTExMzQwNTlaFw0xMjA1MTExMzQwNTlaoA4wDDAKBgNV
HRQEAwIBATANBgkqhkiG9w0BAQUFAAOBgQC1D/wwnrcY/uFBHGc6SyoYss2kn+nY
RTwzXmmldbNTCQ03x5vkWGGIaRJdN8QeCzbEi7gpgxgpxAx6Y5WkxkMQ1UPjNM5n
DGVDOtR0dskFrrbHuNpWqWrDaBN0/ryZiWKjr9JRbrpkHgVY29I1gLooQ6IHuKHY
vjnIhxTFoCb5vA==
"""

    def setUp(self):
        self.asn1Spec = rfc5280.CertificateList()

    def testDerCodec(self):

        substrate = pem.readBase64fromText(self.pem_text)

        asn1Object, rest = der_decoder.decode(substrate, asn1Spec=self.asn1Spec)

        assert not rest
        assert asn1Object.prettyPrint()
        assert der_encoder.encode(asn1Object) == substrate


suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)
