format=duskhold-ci-payload/1
cipher=aes-256-cbc
kdf=pbkdf2
salt=yes
md5_target=ciphertext
decrypt=openssl enc -d -aes-256-cbc -pbkdf2 -pass env:PAYLOAD_KEY
built=2026-11-02T10:13:59Z
cfbundleversion=46
