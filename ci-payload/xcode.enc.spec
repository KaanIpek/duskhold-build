format=duskhold-ci-payload/1
cipher=aes-256-cbc
kdf=pbkdf2
salt=yes
md5_target=ciphertext
decrypt=openssl enc -d -aes-256-cbc -pbkdf2 -pass env:PAYLOAD_KEY
built=2026-09-18T04:02:31Z
cfbundleversion=35
