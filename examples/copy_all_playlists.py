#!/usr/bin/env python3
import logging
from spotify2tidal import Spotify2Tidal

import config

if __name__ == "__main__":
    """Copy all user playlists from Spotify to Tidal.

    This does not include special playlists like 'Discover Weekly'.

    In order to work, a Spotify client has to be registered and the
    corresponding ID, secret and redirection URI have to be set in the
    configuration file 'config.py'.
    """
    # Enable logging to see what is going on
    logging.getLogger("spotify2tidal").addHandler(logging.FileHandler("copy_playlists.log"))
    logging.getLogger("spotify2tidal").setLevel(logging.DEBUG)

    st = Spotify2Tidal(
        config.spotify_username,
        config.spotify_client_id,
        config.spotify_client_secret,
        config.spotify_client_redirect_uri,
    )

    st.copy_elected_spotify_playlists()
