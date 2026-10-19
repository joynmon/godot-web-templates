# Godot web templates

Slim Godot web export templates for 2D games, built by GitHub Actions from the
official Godot source. 3D, XR, navigation and other unused modules are turned
off so the engine file (`.wasm`) stays small enough for web portals such as
YouTube Playables (30 MiB per file).

## Build

1. Open the **Actions** tab, pick **Build web export templates**, click **Run workflow**.
2. Keep `godot_version` equal to your editor version (for example `4.6.2-stable`).
3. When it finishes, the zip is in **Releases** under the tag `<version>-<profile>`.

## Use in Godot

Project > Export > Web preset > Custom Template > Release: pick
`web_nothreads_release.zip`. Keep **Thread Support** off (these are no-threads builds).

## Profiles

`profiles/2d_web.py` lists what is turned off. Copy it to make a new profile, or
pass extra flags in the `extra_flags` input to switch a module back on
(for example `module_websocket_enabled=yes`).

## License

The engine is Godot Engine, MIT license, (c) Godot Engine contributors and
Juan Linietsky, Ariel Manzur. See https://godotengine.org/license.
The workflow and profile files in this repo are free to reuse.
