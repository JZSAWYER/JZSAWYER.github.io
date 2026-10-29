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

Activation reviewed repository documentation and scripts only. Dependencies were
not installed, the site was not built or previewed, and no site content or hosting
settings were changed.
