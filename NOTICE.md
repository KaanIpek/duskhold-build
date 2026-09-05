# NOTICE — third-party components in Duskhold

Duskhold itself is proprietary; see [LICENSE](LICENSE). The components listed here are **not**
owned by Kaan Ipek and stay under their own licences, which the proprietary licence explicitly
carves out.

Every row was verified against a file in this working tree on **2026-09-05**, and the "Licence text
in this tree" column is the file that was read. Anything that could not be verified from a file is
in [§7 Unverified](#7-unverified--check-before-shipping) and nowhere else — no licence in this
document is assumed from a project's reputation.

Attribution obligations, in one line: **CC0 requires none**, **the SIL OFL requires that its licence
text ships with the fonts** (see §3), **Apache-2.0 requires the licence and notices to travel with
the code** (see §4), **MIT requires the copyright line to travel with the code** (see §4).

Two screens carry that inside the app, and they do different jobs. The **credits** screen
(`Assets/Duskhold/Scripts/UI/CreditsScreen.cs`, text transcribed from `CREDITS.md` into
`Assets/Duskhold/Resources/Credits.txt` at forge time) names the art, audio and font authors; every
one of those packs is CC0 or OFL, so that screen is goodwill. The **licences** screen behind it
(`DuskholdMenuForge.BuildLicencesSheet`, text baked from `Assets/Duskhold/Legal/*.txt` at forge
time) prints the OFL, MIT and Apache-2.0 texts in full, and that one **is** compliance: it is the
only copy of those licences that reaches a player's device.

---

## 1. 3D models and animations — all CC0 1.0

`Assets/Duskhold/Art/CREDITS.txt` is the short version of this section kept beside the models, and it
also records which licences are *banned* from the project (anything non-commercial, share-alike,
Asset-Store-account-bound or Mixamo-derived) because Duskhold is ad-supported.

| Component | Version | Licence | Licence text in this tree | Used for |
|---|---|---|---|---|
| KayKit — Medieval Hexagon Pack, Kay Lousberg | 1.0 (2024-04-26) | CC0 1.0 | `Assets/Duskhold/Art/Hex/KayKit_Hexagon_License.txt` | The art spine: hex terrain, all building models in five faction palettes, walls, gates, tower bases, scaffolding, rubble, trees, rocks, props, flags |
| KayKit — Character Pack: Adventurers | 2.0 (2025-10-22) | CC0 1.0 | `Assets/Duskhold/Art/Characters/Adventurers/KayKit_Adventurers_License.txt` | The five human champions and every hand-slot weapon and shield |
| KayKit — Character Pack: Skeletons | 1.1 (2025-10-22) | CC0 1.0 | `Assets/Duskhold/Art/Characters/Skeletons/KayKit_Skeletons_License.txt` | The night horde bodies re-kitted into the enemy roles, plus the champion The Bonecaller |
| KayKit — Character Animations | 1.1 (2025-12-10) | CC0 1.0 | `Assets/Duskhold/Art/Characters/Animations/KayKit_Animations_License.txt` | 132 clips on the shared `Rig_Medium` skeleton: locomotion, melee, ranged, casting, hits, deaths, awaken/resurrect |
| KayKit — Medieval Builder Pack | 1.0 (2021-07-30) | CC0 1.0 | `Assets/Duskhold/Art/Buildings/Builder/KayKit_Builder_License.txt` | Extra building silhouettes (watchtower, archery range, lumber mill, farm plot) |
| Kenney — Pirate Kit | 2.1 (2026-02-17) | CC0 1.0 | `Assets/Duskhold/Art/Ships/Kenney-License.txt` | Ships and coastal props |
| Quaternius — Ultimate Monsters | downloaded 2026-09-04 and 2026-09-05 | CC0 1.0 (pack page and in-pack `LICENSE.txt`); the site-wide page showed Quaternius Asset License v1.0 the same day | `Assets/Duskhold/Art/Creatures/Quaternius_License.txt` (both texts reproduced verbatim, with the download URLs and the date) | 29 creature bodies under `Art/Creatures/UltimateMonsters/` (17 on 2026-09-04, 12 more on 2026-09-05 from the same pack folder) |
| Quaternius — Cute Animated Monsters | downloaded 2026-09-04 | CC0 1.0 | same file | Crab and Tree under `Art/Creatures/CuteMonsters/` |
| Quaternius — Ultimate Animated Animals | downloaded 2026-09-04 | CC0 1.0 | same file | Bull, Fox, Stag, Wolf, and the champion's Horse mount |

**Standing restriction on the Quaternius models.** The newer Quaternius Asset License forbids
redistributing the raw models *as assets*. Shipping them inside the game binary is expressly
permitted; publishing the `.fbx` files as a downloadable pack from any repository is not. Because
Duskhold's source repository is going private and only encrypted build payloads reach a public
repository, this is satisfied by construction — but do not "helpfully" publish `Assets/Duskhold/Art`
anywhere.

---

## 2. Audio — all CC0 1.0

| Component | Licence | Licence text in this tree | Used for |
|---|---|---|---|
| Kenney — Impact Sounds | CC0 1.0 | `Assets/Duskhold/Audio/SFX/Kenney_ImpactSounds_License.txt` | Melee and armoured hits, arrow and bolt impacts, siege booms, unit deaths, building destruction, footsteps |
| Kenney — RPG Audio | CC0 1.0 | `Assets/Duskhold/Audio/SFX/Kenney_RPGAudio_License.txt` | Bow releases, cloth and leather foley, coin handling |
| Kenney — Interface Sounds | CC0 1.0 | `Assets/Duskhold/Audio/SFX/Kenney_InterfaceSounds_License.txt` | Clicks, confirmations, refusals, build placement |
| Kenney — Music Jingles | CC0 1.0 | `Assets/Duskhold/Audio/Music/Kenney_MusicJingles_License.txt` | Dawn, dusk, night, level-up, victory and defeat stingers (`jingles_*.ogg`) |

### 2b. The original score — generated locally, one open obligation

`day.wav`, `dusk.wav`, `night.wav`, `boss.wav`, `menu.wav`, `victory.wav` were generated on the
author's own machine with **Stable Audio 3** (Stability AI, open weights). Nothing was uploaded.
Under the Stability AI Community License the author owns the outputs, and generated audio is not a
"Derivative Work" of the model — but **commercial use requires a free registration at
<https://stability.ai/community-license>, and that registration has not been submitted.**

- Provenance and the quoted licence clauses: `Assets/Duskhold/Audio/Music/Duskhold_Score_Attribution.txt`
  and the "Music" section of `CREDITS.md`.
- Prompts, seeds and render settings: `Assets/Duskhold/Audio/Music/Duskhold_Score_Prompts.json`.
- **Action, and it gates selling the game rather than developing it:** submit the free registration
  before the App Store listing goes on sale. It is a form, not a purchase.

---

## 3. Fonts — SIL Open Font License 1.1

The OFL is the one licence in this project with a live redistribution condition: the licence text
must be distributed with the fonts, the fonts must not be sold on their own, and a modified version
must not reuse the reserved name.

**The fonts are redistributed as Font Software, not merely as atlases.** `Cinzel_TMP.asset:61` and
`Barlow_TMP.asset:128` are `m_AtlasPopulationMode: 1` (Dynamic) with a live `m_SourceFontFile`
reference and `m_GlyphTable: []` — nothing is pre-baked, so Unity serialises the `.ttf` binaries
themselves into the player data. The shipped `Builds/iOS/Data/sharedassets0.assets` for build 28
carries the font name tables (`Barlow-SemiBold`, `Cinzel-Variable`) to prove it. Build 28 carried
**no OFL text anywhere** — every `.assets`, `.resource` and `global-metadata.dat` file in it was
searched for "SIL OPEN FONT LICENSE" and returned nothing.

That is fixed for build 29 and later by the in-app **licences** screen, which bakes
`Assets/Duskhold/Legal/Fonts_OFL-1.1.txt` — the three copyright notices plus the OFL text in full —
into the menu scene at forge time. Switching the two TMP assets to a static atlas instead was
considered and is **wrong for this tree**: the baked glyph tables are empty
(`m_GlyphTable: []`, `m_CharacterTable: []`, `m_ClearDynamicDataOnBuild: 1`), so a static asset here
would ship a font with no glyphs and every line of text in the game would vanish.

No font is modified (TMP atlases are generated *from* them, which the OFL permits), no font is sold
on its own, and neither Cinzel nor Barlow declares a Reserved Font Name. Liberation Sans does
declare one ("Liberation"), and its TMP asset is a static atlas carrying no font binary, so no
reserved-name question arises there either.

| Font | Author | Licence | Licence text in this tree | Shipped inside the app? | Used for |
|---|---|---|---|---|---|
| Cinzel (variable) | Natanael Gama / NDISCOVER | SIL OFL 1.1 | `Assets/Duskhold/UI/Fonts/Cinzel_OFL.txt`, and `Assets/Duskhold/Legal/Fonts_OFL-1.1.txt` | yes — licences screen | Display face: phase banner, panel titles, champion name |
| Barlow Regular + SemiBold | Jeremy Tribby | SIL OFL 1.1 | `Assets/Duskhold/UI/Fonts/Barlow_OFL.txt`, and `Assets/Duskhold/Legal/Fonts_OFL-1.1.txt` | yes — licences screen | Body face: all HUD and menu text |
| Liberation Sans | Red Hat / Google (digitised data) | SIL OFL 1.1 | `Assets/TextMesh Pro/Fonts/LiberationSans - OFL.txt`, and `Assets/Duskhold/Legal/Fonts_OFL-1.1.txt` | yes — licences screen | TextMesh Pro's default fallback face, shipped with the TMP essentials |

---

## 4. Plugins and SDKs compiled into the game

| Component | Version | Licence | Licence text in this tree | Used for |
|---|---|---|---|---|
| Google Mobile Ads — Unity plugin | 11.3.0 (`Assets/GoogleMobileAds/GoogleMobileAds_version-11.3.0_manifest.txt`) | Apache License 2.0 | `Assets/GoogleMobileAds/LICENSE` | Rewarded ads and the UMP consent flow (`Scripts/Meta/DuskholdAds.cs`) |
| External Dependency Manager for Unity (EDM4U) | 1.2.188 (`Assets/ExternalDependencyManager/Editor/1.2.188`) | Apache License 2.0 | `Assets/ExternalDependencyManager/Editor/LICENSE` | Resolves the Gradle and CocoaPods dependencies of the ads plugin at build time |
| Sign in with Apple Unity Plugin (`com.lupidan.apple-signin-unity`) | 1.5.0 (`Packages/manifest.json`) | MIT License, © 2019 Daniel Lupiañez Casares | `Assets/Duskhold/Legal/AppleSignIn_MIT.txt` (copied verbatim from `Library/PackageCache/com.lupidan.apple-signin-unity@c7f424ea2c97/LICENSE.md`, which `.gitignore` excludes) | The native Sign in with Apple sheet behind the UGS account link |
| Google Mobile Ads iOS SDK | `~> 13.6` (`Builds/iOS/Podfile`) | Closed-source binary under Google's own SDK terms (<https://developers.google.com/admob/terms>) | none — fetched by CocoaPods at build time on the macOS runner | The ads runtime on iOS |
| Google User Messaging Platform (iOS) | 3.1.0 (`Builds/iOS/Podfile`) | Closed-source binary under Google's own terms | none — fetched by CocoaPods | GDPR/consent form on iOS |
| `com.google.android.gms:play-services-ads` | 25.4.0 (`Assets/GoogleMobileAds/Editor/GoogleMobileAdsDependencies.xml`) | Android Software Development Kit License / Google Play Services terms | none — fetched by Gradle at build time | The ads runtime on Android |
| `com.google.android.ump:user-messaging-platform` | 4.0.0 (`Assets/GoogleMobileAds/Editor/GoogleUmpDependencies.xml`) | Google Play Services terms | none — fetched by Gradle | Consent form on Android |
| `androidx.constraintlayout` / `androidx.lifecycle-process` / `androidx.fragment` | 2.1.4 / 2.6.2 / 1.7.1 (same XML) | Apache-2.0 upstream (AndroidX); **no licence file exists in this tree** — see §7 | none | Transitive dependencies of the ads SDK |
| `googlemobileads-unity.aar`, `GoogleMobileAdsPlugin.androidlib`, `unity-plugin-library.xcframework` | ship with plugin 11.3.0 | Apache-2.0, as part of the Unity plugin above | `Assets/GoogleMobileAds/LICENSE` | Prebuilt native glue for the ads plugin |
| **websocket-sharp**, © 2010–2021 sta.blockhead | vendored inside `com.unity.services.wire` | **MIT License** | `Assets/Duskhold/Legal/UnityServicesWire_ThirdParty.txt` (copied verbatim from `Library/PackageCache/com.unity.services.wire@d50817c0adab/Third Party Notices.md`) | The websocket transport under Unity Gaming Services. **It really ships**: `websocket-sharp.dll` is listed in `Builds/iOS/Data/ScriptingAssemblies.json` for build 28 |
| **unity-websocket-webgl**, © 2018 Jiri Hybek | vendored inside `com.unity.services.wire`, modified by Unity | **Apache License 2.0** | same file, which also lists Unity's five modifications; the licence body is `Assets/Duskhold/Legal/Apache-2.0.txt` | Same transport; `unity-websocket-sharp.dll` in the shipped assembly list |

MIT and Apache-2.0 both require their notice to travel with the distribution, and the usual way a
mobile game satisfies that is an in-app open-source notices screen. **Duskhold now has one**:
Settings > CREDITS > LICENCES, forged from `Assets/Duskhold/Legal/` by
`DuskholdMenuForge.BuildLicencesSheet`. It carries `NOTICES.txt` (who, what licence, whose
copyright), the OFL, the MIT text with both copyright lines, and Apache-2.0 in full — 19.4k
characters, split one label per document because a single TextMesh Pro label stops drawing past
about 16,000 characters.

**Nothing in this section is verified against a shipped binary yet.** It describes the tree as of
2026-09-05; build 28 does not have the screen, and the first build that does is build 29. Re-check
by grepping the rebuilt `Builds/iOS/Data/sharedassets0.assets` for `SIL OPEN FONT LICENSE` and
`Permission is hereby granted` — build 28 returned zero hits for both.

---

## 5. Unity engine and packages

Unity Engine **6000.4.8f1** (URP). Use of the engine is governed by the author's own Unity licence
agreement; it grants nothing to a reader of this repository. Every package below was read from
`Packages/manifest.json` and its licence from `Library/PackageCache/<package>/LICENSE.md`.
`Library/` is `.gitignore`d, so those paths resolve only on a machine that has resolved the
packages — they are cited as evidence of what was read, not as files a reader of this repository
can open. The three licences that carry a redistribution obligation (§3, §4) are copied into
`Assets/Duskhold/Legal/` for exactly that reason.

| Package | Version | Licence (from the package's own LICENSE.md) |
|---|---|---|
| `com.unity.render-pipelines.universal` (+ `.core`, `.universal-config`, `com.unity.shadergraph`) | 17.4.0 | Unity Companion License |
| `com.unity.burst` | 1.8.29 | Unity Companion License (source) / Unity Package Distribution License |
| `com.unity.collections`, `com.unity.mathematics`, `com.unity.ai.navigation`, `com.unity.inputsystem`, `com.unity.ugui` | 6.4.0 / 1.3.3 / 2.0.12 / 1.19.0 / 2.0.0 | Unity Companion License |
| `com.unity.netcode.gameobjects` | 2.5.1 | Unity Companion License |
| `com.unity.nuget.newtonsoft-json` | transitive | Unity Companion License (Unity's redistribution of Json.NET) |
| `com.unity.nuget.mono-cecil` | transitive | Unity Companion License |
| `com.unity.ext.nunit` | transitive | Unity Package Distribution License |
| `com.unity.purchasing` | 4.15.1 | Unity IAP Service terms of service (an "Operate Service") |
| `com.unity.services.core`, `.authentication`, `.cloudsave`, `.friends`, `.relay`, `.qos`, `.wire` | 3.4.x–3.7.0 | Unity Terms of Service (<https://unity.com/legal>) |
| `com.unity.test-framework` (+ `.performance`) | 1.6.0 | Unity Companion License — editor/test only, never in a player build |
| Unity engine modules (`com.unity.modules.*`) | 1.0.0 | Part of the engine, under the Unity licence agreement |

---

## 6. Editor-only tooling — must never reach a player build

| Component | Version | Licence | Used for |
|---|---|---|---|
| MCP for Unity (`com.coplaydev.unity-mcp`) | 10.1.2, from `https://github.com/CoplayDev/unity-mcp.git#v10.1.2` | **Unverified — no LICENSE file exists in the package at all** | The editor automation bridge (`Assets/Editor/DuskholdMcpBridgeBoot.cs`). Development convenience only |

**REMOVED from `Packages/manifest.json` and `Packages/packages-lock.json` on 2026-09-05.** It has to
be, and an earlier draft of this section said the opposite on the strength of a check that looked in
the wrong place.

The package declares an Editor assembly (`MCPForUnity.Editor`, `includePlatforms: [Editor]`) **and** a
Runtime assembly (`MCPForUnity.Runtime`) whose asmdef sets `"includePlatforms": []` — every platform —
so it is registered as a player assembly. It **did** reach build 28:
`Builds/iOS/Data/ScriptingAssemblies.json` (150 entries, from the build whose `Info.plist` reads
`CFBundleVersion 28`) lists `MCPForUnity.Runtime.dll` at index 80, between `AppleAuth.dll` (78) and
`unity-websocket-sharp.dll` (82). `Builds/iOS/Il2CppOutputProject/Source/il2cppOutput/` contains no
MCP `.cpp` file, which is true and is what the earlier check saw — but IL2CPP emitting no code for a
fully stripped assembly does not un-register it, and the registry is what the runtime reads.

So build 28 shipped a compiled assembly from a package with **no `LICENSE` file of any kind**, **no
`license` field in its `package.json`** (only a `licensesUrl` pointing at GitHub) and **no copyright
line in its `README.md`**.

`DuskholdMcpBridgeBoot` reaches the bridge by reflection and never references the assembly, so
`Assembly-CSharp-Editor` still compiles with the package gone; the bridge simply reports "bridge type
not found". Put the package back for editor work only AFTER a release build, and re-verify before
each payload push:

```
grep -c 'MCPForUnity' Builds/iOS/Data/ScriptingAssemblies.json   # must be 0
```

---

## 7. Unverified — check before shipping

Nothing below is claimed to be licensed a particular way. Each is a real gap.

| Component | What is missing | Why it is probably fine, and what to do |
|---|---|---|
| MCP for Unity 10.1.2 | The package in `Library/PackageCache` has **no `LICENSE` file at all**, and its `package.json` has **no `license` field**. The upstream repository is widely described as MIT, but that could not be verified from anything in this tree. | **Done**: removed from `Packages/manifest.json` and `packages-lock.json` on 2026-09-05, because it *did* reach build 28 (§6). To use it again, put the dependency back for editor work only, after the release build, and check `ScriptingAssemblies.json` before the next payload push. |
| ~~No in-app open-source notices screen~~ | — | **Done 2026-09-05**: Settings > CREDITS > LICENCES prints the OFL, both MIT notices and Apache-2.0 in full, from `Assets/Duskhold/Legal/`. Not yet verified against a binary — the first build that carries it is build 29. |
| AndroidX libraries (constraintlayout, lifecycle-process, fragment) | Fetched by Gradle at build time; no licence file lands in this tree. | AndroidX is Apache-2.0 upstream, and Apache-2.0 attribution for transitively linked Android libraries is conventionally satisfied by an in-app open-source-notices screen. Duskhold now has one, and `Assets/Duskhold/Legal/NOTICES.txt` names AndroidX in it with the Apache-2.0 body beside it. **Do**: record the exact resolved artefact versions here after the first store AAB. |
| Google Mobile Ads native SDKs (iOS pods, Android `play-services-ads`) | Closed-source binaries fetched at build time; there is no licence file to point at. | Their terms are accepted through the AdMob account, not through a file. No action beyond keeping the AdMob account in good standing. |
| Stability AI Community License registration | Not submitted. | Free, and required before the game is monetised. See §2b. |

---

## 8. Original work — no third party involved

Every line of C#, every ScriptableObject and balance table, the three custom shaders
(`Duskhold/HealthBar`, `Duskhold/Marker`, `Duskhold/VertexLit`), the hex-grid maths, the map
generator, the research tree, the generated UI chrome and icons, the map thumbnails, the Turkish and
English game text, the design documents and the build/QA harnesses were written for this project and
are covered by [LICENSE](LICENSE), not by anything in this file.

Mechanics are informed by Thronefall, Nightfall: Kingdom Frontier TD, Kingdom Rush, They Are Billions
and Bad North. No asset, line of code or line of text from any of those games is used here.

---

*This is a factual inventory, not legal advice. Where a licence is quoted, the quoted file in this
tree is the source and is the thing to read.*
