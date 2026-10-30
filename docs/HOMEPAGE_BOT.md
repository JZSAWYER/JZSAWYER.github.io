# Homepage bot

Homepage bot maintains the owner's existing personal academic homepage in
[JZSAWYER/JZSAWYER.github.io](https://github.com/JZSAWYER/JZSAWYER.github.io).
Each concrete owner request defines the authorized work. Preserve the
AcadHomepage/Jekyll stack and existing design conventions.

## Working rules

- Follow the owner's current instructions and repository `AGENTS.md` when present.
- Use the registered workspace and permanent branch; keep code and documentation
  together. Preserve existing owner changes and unrelated artifacts.
- Requested work may cover profile and publication content, navigation, layout,
  mobile responsiveness, accessibility, and link or build verification.
- Use GitHub for repository hosting. Create a pull request only when explicitly
  requested; deployment and hosting or domain changes need owner authorization.
- Keep repository documentation public-safe. Do not include credentials, private
  conversations, account identifiers, or unpublished personal documents.
- Leave generated `.intern_workspace` records to the relay. Other bots' tasks and
  private materials are outside this role.

## Source map

- `_config.yml`: site settings and author profile.
- `_pages/about.md`: homepage assembly and redirects; `_pages/includes/` contains
  introduction, news, publications, honors, and other sections.
- `_data/navigation.yml`: navigation links and section anchors.
- `_layouts/` and `_includes/`: templates and shared components.
- `assets/` and `_sass/`: scripts and styles; `images/` and `files/`: site assets.
- `_site/`: existing generated output; make source edits in the files above.

## Build and preview

Read [README.md](../README.md), the [local preview instructions](README-zh.md),
[Gemfile](../Gemfile), and [run_server.sh](../run_server.sh) before site edits.
Dependencies use Ruby/Bundler and the `github-pages` gem with `Gemfile.lock`.

For authorized site work with dependencies available, run `bash run_server.sh`
and preview at `http://127.0.0.1:4000`. The script sets a local Bundler path,
supports `JEKYLL_DEST` for build output, and selects Jekyll live reload or Hawkins
based on compatibility. Restart the server after changing `_config.yml`.
For a build check, use `bundle exec jekyll build --destination` with a temporary
output directory to preserve the tracked `_site/` files.

Verify links and anchors for content changes; check desktop, mobile, keyboard
navigation, and relevant accessibility behavior for layout changes. Report checks
performed and any unresolved limits. Hosting configuration must be inspected when
deployment is requested; template documentation does not establish live settings.

## Review before publication

Keep review HTML under `docs/preview/`, which is excluded by `_config.yml`.
The current review artifact is `docs/preview/homepage-preview.html`, delivered as
standalone HTML for the owner to open directly. Keep the generated HTML local;
version its lossless archive instead. The versioned
[homepage-preview.zip](preview/homepage-preview.zip) contains its exact bytes;
extract `homepage-preview.html` and open it in a browser. This lossless archive
keeps the embedded assets and review styling intact and passes the existing
Git size and privacy guards. It does not publish or deploy the website.
Generate it from a fresh Jekyll build outside the checkout, embedding local
styles, scripts, images, and fonts. Use the versioned
[preview packager](preview/package_preview.py) with a build directory and output
HTML path. Normalize section links for opening the file directly and omit
unrelated analytics. The approved publication version now uses FlagCounter Mini
with the existing counter ID. The preview embeds a genuine pageviews snapshot
for offline viewing and refreshes it after a live image loads. It omits the
country table and map while keeping the provider's required link to its
statistical information. That linked provider page can still show geographic
data. The previous full counter and Busuanzi drafts are not selected for
publication.

The [Mini-counter preview](preview/homepage-counter-alternative.zip) documents
the same approved display. No supported per-entry exclusion was verified in the
public [FAQ](https://s03.flagcounter.com/faq.html), code generator, or Pro feature
list. Do not treat `flags_0` on the full counter as a geographic filter; it hides
the number of collected flags, not individual rows. The Mini endpoint is the
documented aggregate-only display.
The original site templates and styles remain the source for publication.

The current content draft uses **third-year Ph.D. student**, includes seven LLM
publications, and retains the existing public CV download. Research wording uses
**agentic RL** alongside LLM post-training. The VLKEB news entry keeps its
acceptance announcement and omits the collaboration and resource sentence.
Internships precede
publications. The papers are grouped into **Post-training** (four, including
agent harnesses and reasoning evaluation) and **Knowledge Editing** (three).
AI for Science interests, papers, and associated news are omitted from the
homepage. The introduction includes the requested Chinese names alongside
Bin Dong, Wentao Zhang, Jiang Bian, and Lei Song; the page remains in English. The supplied CV draft is a private
reference and is not a repository asset. XYZ AI Lab and MSRA dates
follow that draft, including their overlap; no relationship between the two
appointments is inferred. CRIPAC lists the documented October 2023 start only,
because the previous end date preceded the start. The end date remains unknown.

Publication author order and venue labels follow the linked papers and publisher
records. In particular, VLKEB includes Tao Yu and MorphoBench is in Findings of
ACL 2026. Equal contribution marks follow the published records and the owner's CV draft.

The preview build uses Jekyll 3.9.3 and the site dependencies pinned in
`Gemfile.lock`. Its isolated build bundle contains the configured plugins and
GFM parser; installation of the complete `github-pages` dependency bundle has
not been validated in this environment. No repository dependency versions were
changed. `tzinfo-data` was removed from the Jekyll plugin list after reproducing
a load failure: it was not declared in the Gemfile and is timezone data rather
than a site plugin. The configured timezone remains `Asia/Shanghai`.

The visual refinement keeps the profile sidebar and publication thumbnails.
It draws on the clear typography, spacing, and restrained accents of the
[reference homepage](https://haolpku.github.io/), using an independent deeper
teal palette, soft borders, and aligned news dates. Typography uses locally
bundled **Source Sans 3**, regular body text, semibold headings, normal letter
spacing, and larger publication text. Upright and italic variable WOFF2 files
come from the [pinned Adobe release](https://github.com/adobe-fonts/source-sans/tree/87b37a2daaed80fcb8e8ccb0085c4d72ddade12e).
The original copyright and [OFL license](../assets/fonts/source-sans-3/LICENSE.md)
are bundled with the fonts and preserved in the stylesheet embedded in the
standalone preview. Homepage styles are scoped in [`_sass/_homepage.scss`](../_sass/_homepage.scss).
[`assets/js/homepage.js`](../assets/js/homepage.js) progressively adds topic
filters, native abstract disclosures, active navigation, and a return-to-top
link. With JavaScript disabled, all seven papers and complete abstracts remain
available. Keyboard focus and reduced-motion preferences are supported.

Navigation uses clean heading targets while retaining the previous dash-prefixed
fragments and the Experiences alias. Wrapping Markdown sections changes
Kramdown's automatic heading slugs, so both current and legacy targets are
checked in rendered HTML. Section links open in the current tab.

The Jekyll build and standalone HTML checks pass for seven publication cards,
four/three topic groups, eight news entries, all seven navigation links, the
requested professor names, removed content, and local assets. The standalone
approved Mini preview embeds the pageviews image, fonts, and styles. It uses no
external map script.
The typography and interaction revision passed all 40 browser checks in headless Chromium 102 at widths 320, 390, 768,
and 1440 pixels. Those checks verify loaded
Source Sans 3 regular/semibold faces, embedded font sources, and the requested
wording corrections. Other checks cover filters, native disclosures, menu keyboard behavior,
skip-link focus, sticky-header clearance, active navigation, image loading,
reduced motion, no-JavaScript content, and horizontal overflow. The theme
scrolling handler is disabled on the homepage so native focus and scroll
margins work. The test host lacks CJK and emoji fonts; screenshot review uses
temporary fallback fonts without adding CJK or emoji font assets to the site.
The approved Mini source passes a fresh Jekyll build. Its packaged preview
passed 17 focused browser checks online and offline at widths 320, 390, and
1440: correct counter ID, pageviews-only endpoint, loaded live/snapshot image,
retained provider link, no map, no overflow, and no JavaScript errors.
Desktop/mobile screenshots were reviewed.

## Publication handoff

Publication of the approved Mini-counter version is owner-authorized. The public
GitHub Actions history confirms Pages builds from `main`; the latest successful
run uses commit `51d871249005c7e0061f7a802d64a66958df208a`. The live site still
shows the older homepage. A guarded dry-run push to `main` was rejected by the
installed workspace Git guard, which permits only the registered bot branch.
The restriction was rechecked after the latest publication request and remains
in place. This is a publishing-path restriction, not a reported site build
failure. No guard or protection was changed or bypassed.

[homepage-publication.zip](preview/homepage-publication.zip) contains a binary
patch against that `main` commit and application instructions. It includes only
the reviewed site sources, font licenses, and used new publication figures.
It excludes management records, preview artifacts, private attachments, and
unused draft figures. Applying the patch to the base index was checked without
changing the working branch. An operator with an approved publishing path must
apply/commit/push the patch and verify the Pages build and live site. Actual
publication remains unfinished; restoring files or uploading this bot branch
is not evidence of deployment.

## Operator publication without ZIP files

The owner can publish from their own server terminal with GitHub SSH write
access and a configured Git commit identity. These commands create a fresh
checkout, require the reviewed `main` base, and restore only the approved site
paths from a pinned public commit. They do not merge the bot branch or copy
management records. They leave the bot workspace and its guard unchanged.
The pinned source commit and restore command were checked against the reviewed
publication patch: the resulting bytes match exactly, and the whitespace check
passes. No new site build is needed for this documentation-only addition.

```bash
(
  set -eu
  publish_dir="$(mktemp -d /tmp/homepage-publish.XXXXXX)"
  git clone --branch main git@github.com:JZSAWYER/JZSAWYER.github.io.git "$publish_dir"
  cd "$publish_dir"

  base=51d871249005c7e0061f7a802d64a66958df208a
  approved=f3889b19aef9d833ecf874b55342336af6ba3ede
  if [ "$(git rev-parse HEAD)" != "$base" ]; then
    echo "main has changed. Stop and send homepage bot this output."
    exit 1
  fi

  git restore --source="$approved" --staged --worktree -- \
    _config.yml _data _includes _layouts _pages _sass assets \
    images/ai4ai.png images/harnesses.png images/morphobench.png \
    images/rc-grpo.png images/scan.png
  git -c core.whitespace=cr-at-eol diff --cached --check
  git commit -m "Update academic homepage and visitor statistics"
  git push origin main
)
```

The push must succeed before checking the repository's
[Pages deployment](https://github.com/JZSAWYER/JZSAWYER.github.io/actions) and
[live homepage](https://jzsawyer.github.io/). An authentication, commit-identity,
or branch-protection error requires the owner to return the terminal output;
do not change or bypass repository protections.

## Publication figure sources

New thumbnails reproduce the original figures at reduced size; scientific
content is not redrawn. Each publication card links to its source paper.

| Asset | Original source |
| --- | --- |
| `images/rc-grpo.png` | Figure 1, [RC-GRPO](https://arxiv.org/abs/2602.03025), page 2 |
| `images/ai4ai.png` | AI4AI loop illustration, [XYZ AI Lab technical blog](https://xyz-lab.ai/blogs/ai4ai-at-scale/) |
| `images/harnesses.png` | Figure 1, [More Programs or More Rolls?](https://arxiv.org/abs/2609.35873), page 3 |
| `images/morphobench.png` | Figure 1, [MorphoBench](https://aclanthology.org/2026.findings-acl.1171.pdf), page 2 |
| `images/scan.png` | Figure 1, [SCAN](https://arxiv.org/abs/2603.15226), page 3 |
