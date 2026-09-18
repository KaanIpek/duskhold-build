# Security policy

## Reporting a vulnerability

Email **rld.ranger07@gmail.com** with `DUSKHOLD SECURITY` in the subject line.

Please include:

- what the issue is, and what an attacker gets out of it;
- how to reproduce it — the platform (iOS or Android), the app version and build number from the
  in-game **Settings** screen, and the steps;
- anything you had to install, patch or intercept to make it work.

You will get an acknowledgement, and a fix will be shipped in a store update if the report holds up.
This is a one-person project: expect a human reply rather than a ticket number, and expect the fix to
travel at the speed of app review.

Please give a reasonable amount of time for a fix before disclosing publicly, and please do not test
against other players' accounts, other people's devices, or the live backend in a way that degrades
service. Do not access, modify or delete data belonging to anyone but yourself.

There is no bug bounty.

## What is in scope

- The shipped Duskhold apps for iOS and Android (bundle id `com.rldgames.duskhold`).
- The account, friends and save systems built on Unity Gaming Services — in particular anything that
  lets one player read, alter or delete another player's data.
- The published policy pages under <https://kaanipek.github.io/duskhold/>.

Out of scope: findings that require a jailbroken or rooted device and affect only that device;
missing hardening that has no demonstrated impact; reports about third-party SDKs that should go to
their vendors (Google Mobile Ads, Unity Gaming Services); and cheating in single-player, which is a
design question rather than a vulnerability.

## Repository and artefact status

The Duskhold **source repository is private**. Its contents — code, assets, data and tooling — are
proprietary and are covered by [LICENSE](LICENSE); the third-party components listed in
[NOTICE.md](NOTICE.md) keep their own licences.

A separate **public** repository exists only to run the iOS build pipeline on GitHub's free macOS
runners. It contains a workflow and no game code. The build payload it consumes is **encrypted**
before it is pushed, and is decrypted only inside the runner from a repository secret. An encrypted
payload is still proprietary material under §8 of the licence: possessing one grants no right to
decrypt it.

No credential, signing key, keystore or API token is committed to any Duskhold repository. The
Android upload keystore and its passwords live outside the tree, and the build refuses to produce a
store bundle if the keystore path resolves inside the project directory
(`Assets/Editor/DuskholdBuild.cs`, `ConfigureKeystore`). If you ever find key material in a Duskhold
repository, in a build artefact, or in a CI log, that is a valid security report — send it to the
address above rather than opening an issue.
