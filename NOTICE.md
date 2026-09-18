# NOTICE — third-party components in Duskhold

Duskhold itself is proprietary; see [LICENSE](LICENSE). The components listed here are **not**
owned by Kaan Ipek and stay under their own licences, which the proprietary licence explicitly
carves out.

Every row was verified against a file in this working tree on **2026-09-05**, and the "Licence text
in this tree" column is the file that was read. Anything that could not be verified from a file is
in [§7 Unverified](#7-unverified--check-before-shipping) — no licence in this document is assumed
from a project's reputation. The rows added on **2026-09-17** (three older Quaternius packs, the
AI-generated art and audio, the Play Games plugin) say where their evidence came from, and everything
with no licence file in this tree is also listed in §7.

Attribution obligations, in one line: **CC0 requires none**, **the SIL OFL requires that its licence
text ships with the fonts** (see §3), **Apache-2.0 requires the licence and notices to travel with
the code** (see §4), **MIT requires the copyright line to travel with the code** (see §4).

Two screens carry that inside the app, and they do different jobs. The **credits** screen
(`Assets/Duskhold/Scripts/UI/CreditsScreen.cs`, text transcribed from `CREDITS.md` into
`Assets/Duskhold/Resources/Credits.txt` at forge time) is the provenance a player and App Review can
read: which free packs, which AI tools (ChatGPT image generation, Stable Audio 3), and what is
Duskhold's own. Until 2026-09-17 it said every art, audio and font asset was CC0 or OFL, which was
false (§1b, §2b), and it named other developers' games; `DuskholdMenuForge.WriteCreditsAsset` now
refuses to forge a `CREDITS.md` that names another game or makes a claim about how the art was produced. The **licences** screen behind it
(`DuskholdMenuForge.BuildLicencesSheet`, text baked from `Assets/Duskhold/Legal/*.txt` at forge
time) prints the OFL, MIT and Apache-2.0 texts in full, and that one **is** compliance: it is the
only copy of those licences that reaches a player's device.

---

## 1. 3D models and animations — CC0 1.0 packs, plus the Kül Sürüsü bodies

`Assets/Duskhold/Art/CREDITS.txt` is the short version of this section kept beside the models, and it
also records which licences are *banned* from the project (anything non-commercial, share-alike,
Asset-Store-account-bound or Mixamo-derived) because Duskhold is ad-supported.

**Re-checked 2026-09-17** against what ships (a model counts as shipped when a prefab, scene, asset or
animator controller under `Assets/Duskhold` references its GUID) and against the pack zips in
`AssetStaging/` by SHA-1:
- The **KayKit Medieval Builder Pack** is in the tree but **0 of its 30 files is referenced**, so it does
  not ship and the in-game credits no longer name it. `DuskholdPrefabForge` still configures its imports.
- The nine early creature bodies at `Art/Creatures/*.fbx` are byte-identical to three older Quaternius
  packs that `Art/Creatures/Quaternius_License.txt` does not record: Frog, Rat, Snake_angry, Spider and
  Wasp to `AssetStaging/Quaternius/animated-easy-enemies.zip` (the site's **Easy Enemy Pack**); Bat,
  Dragon and Slime to `lowpoly-animated-monsters.zip` (**Animated Monster Pack**); Horse to
  `lowpoly-animated-animals.zip` (**Farm Animal Pack**, whose zip holds Cow, Horse, Llama, Pig, Pug,
  Sheep and Zebra). The Horse is therefore **not** from Ultimate Animated Animals, as this file and
  `Quaternius_License.txt` used to say. None of the three zips carries a licence file; the pack pages
  `quaternius.com/packs/easyenemy.html`, `/animatedmonster.html` and `/farmanimal.html` read
  "License: CC0" when fetched on 2026-09-17.

| Component | Version | Licence | Licence text in this tree | Used for |
|---|---|---|---|---|
| KayKit — Medieval Hexagon Pack, Kay Lousberg | 1.0 (2024-04-26) | CC0 1.0 | `Assets/Duskhold/Art/Hex/KayKit_Hexagon_License.txt` | The art spine: hex terrain, all building models in five faction palettes, walls, gates, tower bases, scaffolding, rubble, trees, rocks, props, flags |
| KayKit — Character Pack: Adventurers | 2.0 (2025-10-22) | CC0 1.0 | `Assets/Duskhold/Art/Characters/Adventurers/KayKit_Adventurers_License.txt` | The five human champions and every hand-slot weapon and shield |
| KayKit — Character Pack: Skeletons | 1.1 (2025-10-22) | CC0 1.0 | `Assets/Duskhold/Art/Characters/Skeletons/KayKit_Skeletons_License.txt` | The night horde bodies re-kitted into the enemy roles, plus the champion The Bonecaller |
| KayKit — Character Animations | 1.1 (2025-12-10) | CC0 1.0 | `Assets/Duskhold/Art/Characters/Animations/KayKit_Animations_License.txt` | 132 clips on the shared `Rig_Medium` skeleton: locomotion, melee, ranged, casting, hits, deaths, awaken/resurrect |
| KayKit — Medieval Builder Pack | 1.0 (2021-07-30) | CC0 1.0 | `Assets/Duskhold/Art/Buildings/Builder/KayKit_Builder_License.txt` | **Nothing that ships** (0 of 30 files referenced, 2026-09-17); imported, never placed |
| Kenney — Pirate Kit | 2.1 (2026-02-17) | CC0 1.0 | `Assets/Duskhold/Art/Ships/Kenney-License.txt` | Ships and coastal props |
| Quaternius — Ultimate Monsters | downloaded 2026-09-04 and 2026-09-05 | CC0 1.0 (pack page and in-pack `LICENSE.txt`); the site-wide page showed Quaternius Asset License v1.0 the same day | `Assets/Duskhold/Art/Creatures/Quaternius_License.txt` (both texts reproduced verbatim, with the download URLs and the date) | 29 creature bodies under `Art/Creatures/UltimateMonsters/` (17 on 2026-09-04, 12 more on 2026-09-05 from the same pack folder) |
| **Kül Sürüsü enemy pack** (13 bodies, Ash Raider to Ash Golem) | delivered 2026-09-07, 2026-09-08 and 2026-09-09 | **Not CC0.** Its licence file declares it proprietary to Duskhold, like the code | `Assets/Duskhold/Art/Creatures/KulSurusu/KulSurusu_License.txt` | Thirteen enemy bodies under `Art/Creatures/KulSurusu/`, colour in COLOR_0 with no textures. The shipped Tomb Guard differs from its source in one spot — the cross on its shield was replaced with a plain pale — which the pack licence records. **Who or what made them is not recorded** (the licence file says "made for Duskhold" but names no maker, and every source file carried the same stray 80-triangle Icosphere); the in-game credits therefore say only that they are in none of the packs and are covered by Duskhold's licence. Listed here so the folder is not read as sitting under the Quaternius licence one level up |
| Quaternius — Cute Animated Monsters | downloaded 2026-09-04 | CC0 1.0 | same file | Crab and Tree under `Art/Creatures/CuteMonsters/` |
| Quaternius — Ultimate Animated Animals | downloaded 2026-09-04 | CC0 1.0 | same file | Bull, Fox, Stag, Wolf |
| Quaternius — Easy Enemy Pack | zip in `AssetStaging/Quaternius/animated-easy-enemies.zip`, download date not recorded | CC0 1.0 per the pack page (read 2026-09-17) | **none in the tree or the zip** — see §7 | Frog, Rat, Snake_angry, Spider, Wasp under `Art/Creatures/` |
| Quaternius — Animated Monster Pack | zip in `AssetStaging/Quaternius/lowpoly-animated-monsters.zip`, download date not recorded | CC0 1.0 per the pack page (read 2026-09-17) | **none in the tree or the zip** — see §7 | Bat, Dragon, Slime under `Art/Creatures/` |
| Quaternius — Farm Animal Pack | zip in `AssetStaging/Quaternius/lowpoly-animated-animals.zip`, download date not recorded | CC0 1.0 per the pack page (read 2026-09-17) | **none in the tree or the zip** — see §7 | The champions' Horse mount (`Art/Creatures/Horse.fbx`) |

### 1b. 2D art generated with AI image tools

Not third-party licensed content and not CC0: these files are output of **OpenAI's ChatGPT image
generation**, cut out and cleaned up by the project's scripts. Recorded in `Tools/slice_lib.py`
("Grid slicer for the ChatGPT art pipeline"), `Tools/photoreal_grids.py` (which item, boon, research
and plot image sits in which cell of which ChatGPT sheet), the commit messages of 2a6290d ("New
GPT-generated TRANSPARENT icon set": the menu glyphs, chests, coin, gem, seal) and 4c5463f ("All 25
ability icons regenerated as GPT-transparent stylized art"), and `Growth/PLAY_LAUNCH.md` (the Play
Console AI-asset declaration: "The painted art came out of a ChatGPT image pipeline", icon included).

| Folder | What | Basis |
|---|---|---|
| `Assets/Duskhold/UI/Art/Items`, `Boons`, `Research`, `Plots` | item, boon and research icons, plot marks | `Tools/photoreal_grids.py` |
| `Assets/Duskhold/UI/Art/Abilities`, `Glyphs` | ability icons, menu symbols, chests and currency marks | commits 4c5463f, 2a6290d |
| `Assets/Duskhold/UI/Art/Relics`, `Portraits`, `Fair`, the banners, `victory_dawn.png`, `defeat_fall.png`, `app_icon.png` | relic pictures, champion portraits, Fair pictures, menu banners, result art, the app icon | commits e1a370b and 13d0f1d (the same art rounds; they do not name the tool) and `Growth/PLAY_LAUNCH.md` |

**Not** AI output, although it sits in the same folder: `UI/Art/Store/` holds Apple's own Sign in with
Apple button art and Google's Play Games badge (provenance in `UI/Art/Store/README.txt`). The icons
under `UI/Icons/` are renders of the CC0 models above made by `DuskholdIconForge`, plus a few drawn by
`DuskholdSpriteForge`.

**Standing restriction on the Quaternius models.** The newer Quaternius Asset License forbids
redistributing the raw models *as assets*. Shipping them inside the game binary is expressly
permitted; publishing the `.fbx` files as a downloadable pack from any repository is not. Because
Duskhold's source repository is going private and only encrypted build payloads reach a public
repository, this is satisfied by construction — but do not "helpfully" publish `Assets/Duskhold/Art`
anywhere.

---

## 2. Audio — Kenney CC0 1.0 packs, plus Stable Audio output (§2b)

| Component | Licence | Licence text in this tree | Used for |
|---|---|---|---|
| Kenney — Impact Sounds | CC0 1.0 | `Assets/Duskhold/Audio/SFX/Kenney_ImpactSounds_License.txt` | Melee and armoured hits, arrow and bolt impacts, siege booms, unit deaths, building destruction, footsteps |
| Kenney — RPG Audio | CC0 1.0 | `Assets/Duskhold/Audio/SFX/Kenney_RPGAudio_License.txt` | Bow releases, cloth and leather foley, coin handling |
| Kenney — Interface Sounds | CC0 1.0 | `Assets/Duskhold/Audio/SFX/Kenney_InterfaceSounds_License.txt` | Clicks, confirmations, refusals, build placement |
| Kenney — Music Jingles | CC0 1.0 | `Assets/Duskhold/Audio/Music/Kenney_MusicJingles_License.txt` | Dawn, dusk, night, level-up, victory and defeat stingers (`jingles_*.ogg`) |

### 2b. Music and spell sounds — generated with Stable Audio 3, one open obligation

`day.wav`, `dusk.wav`, `night.wav`, `boss.wav`, `menu.wav`, `victory.wav` (`Audio/Music/`) and the twelve
`cast_*.wav` spell sounds (`Audio/SFX/Casts/`) were generated on the author's own machine with **Stable
Audio 3** (Stability AI, open weights). Nothing was uploaded. Measured 2026-09-17: all 6 score files are
byte-identical to `D:\cowork\StableAudio\out\duskhold\`, and all 12 cast files to
`D:\cowork\StableAudio\out\duskhold_casts\` (written by `generate_duskhold_casts.py`, outside this repo).
Under the Stability AI Community License the author owns the outputs, and generated audio is not a
"Derivative Work" of the model — but **commercial use requires a free registration at
<https://stability.ai/community-license>, and that registration has not been submitted.**

What the licence says (moved here from `CREDITS.md` on 2026-09-17, because the in-game credits are
player text, not a licence analysis; verified against the agreement text, not from memory):

- **It applies to individuals.** The agreement binds "any individual person or entity"; Stability's own
  licence page describes it as covering "researchers, developers, small businesses, and creators with less
  than $1M in annual revenue". **No company is required.**
- **You own the audio.** *"As between You and Stability AI, You own any outputs generated from the Models"*,
  and the definition of Derivative Work explicitly *"do[es] not include the output of any Model."*
- **Registration is required for commercial use, and it is free.**
  *"If You are using or distributing the Stability AI Materials for a Commercial Purpose, You must register
  with Stability AI at stability.ai/community-license."* It is a form, not a purchase.
- **Above $1M** the Community License terminates and an Enterprise licence is needed
  (<https://stability.ai/enterprise>).
- The attribution chain (ship a copy of the agreement, keep a Notice file, display "Powered by Stability AI")
  is written against distributing *the model or a Derivative Work*, which a generated audio file is not.
  The wording is ambiguous enough that crediting Stability in the game's credits costs nothing and removes
  the question, so the in-game credits name Stable Audio 3 and carry "Powered by Stability AI".

- Provenance: `Assets/Duskhold/Audio/Music/Duskhold_Score_Attribution.txt`.
- Prompts, seeds and render settings of the score: `Assets/Duskhold/Audio/Music/Duskhold_Score_Prompts.json`.
- **Action, and it gates selling the game rather than developing it:** submit the free registration
  before the App Store listing goes on sale. It is a form, not a purchase.

*Not legal advice — a reading of the licence text with the relevant clauses quoted so they can be checked.*

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
| **Google Play Games plugin for Unity** (`Assets/GooglePlayGames/com.google.play.games`), © Google Inc. | 2.2.1 (`Editor/GooglePlayGamesPlugin_v2.2.1.txt`) | **Apache License 2.0**, read 2026-09-17 from the header of the plugin's own sources (e.g. `Runtime/Scripts/GameInfo.cs`); the folder carries **no `LICENSE` file** | **none in this tree**, and the plugin is not named on the in-app LICENCES sheet — see §7. The Apache-2.0 body itself is already on that sheet | Sign in with Play Games on Android (`Scripts/Platform/PlayGamesSignIn.cs`, under `DUSKHOLD_PLAYGAMES`). `Runtime/Google.Play.Games.asmdef` lists Android and Editor only, so `Google.Play.Games.dll` is in the Android player and **not** in the iOS one |
| `com.google.android.gms:play-services-games-v2` / `:play-services-nearby` | 22.0.0 / 18.5.0 (`GooglePlayGamesPluginDependencies.xml`) | Google Play Services terms | none — fetched by Gradle at build time | The Play Games runtime behind the plugin above, Android only |

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
not found". Put the package back for editor work only AFTER a release build.

The manual `grep -c 'MCPForUnity'` this section used to prescribe is now enforced, twice. Since
2026-09-17 an iOS or Android build refuses to start while the package is in `Packages/manifest.json` or
`packages-lock.json` and reads its own export back for `MCPForUnity`, the QA harness and test assemblies
(`StoreDevToolsGate` in `Assets/Editor/DuskholdBuild.cs`, report `Logs/store_devtools_gate.txt`;
`StoreDevToolsGate.VerifyExisting` re-reads an export already on disk). And `Tools/push_ios_payload.sh`
refuses to push unless that report is newer than every file in `Builds/iOS`, says
`OUTPUT VERDICT iOS: PASS`, and the account gate
(`py -3 D:\cowork\RLDGames-Ops\tools\apple_gate\gate.py --app duskhold --build Builds/iOS`) exits 0.

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
| Quaternius Easy Enemy Pack, Animated Monster Pack, Farm Animal Pack (nine bodies under `Art/Creatures/`, §1) | No licence file in the tree or in the three zips, no download date, and `Art/Creatures/Quaternius_License.txt` does not record them (it also places the Horse under Ultimate Animated Animals, which the SHA-1 match contradicts). | All three pack pages read "License: CC0" on 2026-09-17, the licence Quaternius gives its other packs in this tree. **Do**: add these three packs, their page URLs and that date to `Quaternius_License.txt` and `Art/CREDITS.txt`, and correct the Horse line there (both files are hand-written, not forged). |
| Kül Sürüsü maker (§1) | No maker is recorded for the thirteen bodies. | An owner decision (`Store/apple_43_claims_audit.md` §11.1). No Apple-facing or in-game text says who made them until it is recorded. |
| Google Play Games plugin for Unity 2.2.1 (§4) | It ships in the Android player, but no `LICENSE` file is in `Assets/GooglePlayGames/`, and the in-app LICENCES sheet (`Assets/Duskhold/Legal/NOTICES.txt`, "CODE LIBRARIES COMPILED INTO THIS APP") does not name it. Apache-2.0 asks for the notice to travel with the distribution. | Every source file in the plugin carries the Apache-2.0 header © Google Inc., and the Apache-2.0 body is already on the sheet. **Do**: copy the upstream `LICENSE` into `Assets/Duskhold/Legal/` and add one line naming the plugin to `NOTICES.txt`, then re-forge (`BuildLicencesSheet`). Hand-written file; not this round's lane. |
| `Assets/Duskhold/Legal/NOTICES.txt` MUSIC paragraph | It says only "The six score beds were generated locally with Stable Audio 3". The twelve `cast_*.wav` spell sounds (§2b) came from the same model and are now named on the credits screen, so the two in-app screens disagree. | **Do**: add the twelve cast sounds to that paragraph and re-forge. Hand-written file; not this round's lane. |

---

## 8. Duskhold's own work

The C# code, every ScriptableObject and balance table, the three custom shaders
(`Duskhold/HealthBar`, `Duskhold/Marker`, `Duskhold/VertexLit`), the hex-grid maths, the map layouts
and the script that draws them (`Tools/draw_maps.py`: "a painter, not a generator"), the research
tree, the map thumbnails rendered from level data, the icons rendered from the CC0 models (§1b), the
Turkish and English game text, the design documents and the build/QA harnesses belong to this project
and are covered by [LICENSE](LICENSE), not by anything in this file. 61 of the repository's 64
commits (counted 2026-09-17) carry a `Co-Authored-By` trailer naming an AI coding assistant. The
AI-generated 2D art (§1b) and audio (§2b) are listed with their tools, not here.

No asset, line of code or line of text from any other developer's game is used here. This file does
not name other games: `Tools/ci_repo_bootstrap.sh` copies it into the PUBLIC build repository
(KaanIpek/duskhold-build), so a paragraph that once listed the games whose mechanics informed Duskhold
was public while it said it was private. The design references live in `docs/DUSKHOLD_DESIGN.md`,
which is never published.

---

*This is a factual inventory, not legal advice. Where a licence is quoted, the quoted file in this
tree is the source and is the thing to read.*
