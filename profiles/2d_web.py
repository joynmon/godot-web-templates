# Build profile for small 2D web games (Godot 4.5+).
# Used with: scons platform=web profile=profiles/2d_web.py
# Turn a line to "yes"/remove it if a game needs that feature back.

# Big switches
disable_3d = "yes"
disable_physics_3d = "yes"
disable_navigation_3d = "yes"
disable_navigation_2d = "yes"
disable_xr = "yes"
deprecated = "no"   # removes old APIs (e.g. Image.create -> use Image.create_empty); scripts using them fail ONLY in the web build

# Simple text server (no ICU). Fine for Latin/Vietnamese text without complex shaping.
module_text_server_adv_enabled = "no"
module_text_server_fb_enabled = "yes"

# Modules a 2D web game does not need
module_basis_universal_enabled = "no"
module_camera_enabled = "no"
module_csg_enabled = "no"
module_dds_enabled = "no"
module_enet_enabled = "no"
module_fbx_enabled = "no"
module_gltf_enabled = "no"
module_godot_physics_3d_enabled = "no"
module_gridmap_enabled = "no"
module_hdr_enabled = "no"
module_jolt_physics_enabled = "no"
module_jsonrpc_enabled = "no"
module_ktx_enabled = "no"
module_lightmapper_rd_enabled = "no"
module_meshoptimizer_enabled = "no"
module_mobile_vr_enabled = "no"
module_multiplayer_enabled = "no"
module_navigation_2d_enabled = "no"
module_navigation_3d_enabled = "no"
module_openxr_enabled = "no"
module_raycast_enabled = "no"
module_tga_enabled = "no"
module_theora_enabled = "no"
module_tinyexr_enabled = "no"
module_upnp_enabled = "no"
module_vhacd_enabled = "no"
module_webrtc_enabled = "no"
module_websocket_enabled = "no"
module_webxr_enabled = "no"
module_xatlas_unwrap_enabled = "no"

# Kept on purpose: gdscript, freetype, svg, webp, jpg, bmp, ogg, vorbis,
# regex, zip, noise, interactive_music, msdfgen, mbedtls, godot_physics_2d.
