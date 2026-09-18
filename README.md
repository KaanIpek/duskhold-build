<!--
  This file is the README for the PUBLIC pipeline repository (github.com/KaanIpek/duskhold-build).
  It lives here so it is versioned with the pipeline it documents; copy it to that repository as
  README.md. Everything in it is safe to publish — check that again before editing.
-->

# duskhold-build

The build pipeline for **Duskhold**, a hex kingdom-defence game for iOS and Android by Kaan Ipek.

This repository contains a GitHub Actions workflow and nothing else. **There is no game code here.**

## What it does

Unity runs on the developer's Windows machine, where the Unity licence is active, and emits an Xcode
project. That project is encrypted, split into chunks and pushed to a payload branch of this
repository. The workflow here runs on a macOS runner — the only place `xcodebuild` exists — and
decrypts the payload, archives, signs, exports and uploads the build to TestFlight.

The split exists because Unity Personal licences can no longer be activated in CI, and because
GitHub's macOS runners are free on public repositories. Keeping the pipeline public and the source
private is what makes both true at once.

## What is in the payload

An encrypted archive (`openssl aes-256-cbc -pbkdf2`) of a generated Xcode project. The key is a
repository secret and is never written to a file, a log or a commit. The contents are proprietary:
see [LICENSE](LICENSE). Holding an encrypted payload grants no right to decrypt it.

## Secrets this workflow needs

| Secret | What it is |
|---|---|
| `PAYLOAD_KEY` | Passphrase that decrypts the build payload |
| `ASC_KEY_ID` | App Store Connect API key id |
| `ASC_ISSUER_ID` | App Store Connect issuer id |
| `ASC_KEY_P8_B64` | Base64 of the App Store Connect `.p8` key — must have the **Admin** role, because App Manager cannot create a distribution certificate |
| `APPLE_TEAM_ID` | Ten-character Apple team id |

No keystore, certificate, `.p8` or password is committed to this repository, and the workflow prints
none of them.

## Licence

The workflow, the scripts and the game they build are proprietary — all rights reserved. See
[LICENSE](LICENSE). The third-party components the game ships with keep their own CC0, SIL OFL,
Apache-2.0 and MIT licences; they are itemised in [NOTICE.md](NOTICE.md).

Security reports: **rld.ranger07@gmail.com** — see [SECURITY.md](SECURITY.md).

## Duskhold itself

Player-facing pages, including the privacy policy, the terms and the account-deletion instructions,
live at <https://kaanipek.github.io/duskhold/>.
