# TVModule third-party distribution notices

This package redistributes unmodified Windows x64 binaries. It does not relicense
third-party components or include user credentials. The Unity integration is
maintained separately in NeuroMita-Unity.

## VLC 3.0.21

Copyright VideoLAN, VLC authors and the individual dependency authors.
The supplied binaries and plugins match the official VLC 3.0.21 Windows x64
distribution. VLC is distributed under GPL-2.0-or-later; the libVLC library uses
LGPL-2.1-or-later. Individual plugins and dependencies retain their own licenses.
Do not describe the entire VLC plugin bundle as LGPL-only.

Preserved upstream notices: LICENSES/VLC-COPYING.txt, VLC-COPYING.LIB.txt,
VLC-AUTHORS.txt, VLC-THANKS.txt and VLC-README.txt.

Official binary distribution:
https://download.videolan.org/pub/videolan/vlc/3.0.21/win64/

Corresponding VLC source, including build instructions, contribution dependency
recipes and patches: https://download.videolan.org/pub/videolan/vlc/3.0.21/vlc-3.0.21.tar.xz
The same source archive is attached to this module release. Additional upstream
dependency sources referenced by those recipes are mirrored at
https://download.videolan.org/pub/contrib/ .

## yt-dlp 2026.08.19

Copyright yt-dlp contributors and bundled dependency authors.
yt-dlp source uses the Unlicense. The standalone Windows executable contains
additional dependencies with their own license conditions; preserve the full
upstream THIRD_PARTY_LICENSES file, not just the Unlicense.

License: LICENSES/yt-dlp-LICENSE.txt.
Bundled dependencies: LICENSES/yt-dlp-THIRD_PARTY_LICENSES.txt.
Exact source and release: https://github.com/yt-dlp/yt-dlp/releases/tag/2026.08.19

## User data

config.json, exported browser cookies and account credentials are not release
assets. Each user configures access locally. Installing these tools does not
guarantee that YouTube will accept a request or browser session.
