import libvirt

SASL_USER = "sasl"
SASL_PASS = "112444aa"

def request_cred(credentials, user_data):
  for credential in credentials:
    if credential[0] == libvirt.VIR_CRED_AUTHNAME:
      credential[4] = SASL_USER
    elif credential[0] == libvirt.VIR_CRED_PASSPHRASE:
      credential[4] = SASL_PASS
  return 0

auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_PASSPHRASE], request_cred, None]
conn = libvirt.openAuth('qemu+tls://kvm.autovm.net/system', auth, 0)
