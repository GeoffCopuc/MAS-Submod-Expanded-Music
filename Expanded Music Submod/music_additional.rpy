init 1 python in songs:
    import os
    import mutagen.mp3 as muta3
    import mutagen.oggopus as mutaopus
    import mutagen.oggvorbis as mutaogg
    import store
    
    
    # Renamed (slightly)
    JUST_MONIKA = "Just Monika."
    SAYO_NARA_SENS = "Sayo-Nara"
    
    
    # DDLC bgm
    OHAYOU_SAYORI = "Ohayou Sayori!"
    LOVE_AND_LIT = "Dreams of Love and Literature"
    PLAY_WITH_ME = "Play with Me"
    POEM_PANIC = "Poem Panic!"
    DAIJOUBU = "Daijoubu!"
    
    # Okay, Everyone!
    OKAY_EV = "Okay, Everyone!"
    OKAY_EV_NAT = "Okay, Everyone! (Natsuki)"
    OKAY_EV_SAY = "Okay, Everyone! (Sayori)"
    OKAY_EV_YUR = "Okay, Everyone! (Yuri)"
    
    # DDLC Theme
    DDLC_THEME = "Doki Doki Theme"
    
    # Bonus Tracks
    POEMS_FOREVER = "Poems Are Forever"
    DOKI_DOKI = "Doki Doki"
    
    # DDLC Plus
    MY_SONG_YOUR_NOTE = "My Song, Your Note"
    PEACHY_PIE = "Peachy Pie"
    STRAWBERRY_PEPPERMINT = "Strawberry Peppermint"
    LAVENDER_MIST = "Lavender Mist"
    JUST_A_LITTLE_BIT = "Just A Little Bit"
    LETS_TEAMWORK = "Let's Teamwork!"
    DUSK = "Dusk"
    PIECE_BY_PIECE = "Piece By Piece"
    HUG_ENERGY = "Hug Energy"
    FRIEND_AND_LIT = "Stories of Friendship and Literature"
    DEAR_SUNSHINE = "Dear Sunshine"
    CANDY_HEARTS = "Candy Hearts"
    
    
    # DDLC bgm
    FP_OHAYOU_SAYORI = "<loop 4.499>bgm/2.ogg"
    FP_LOVE_AND_LIT = "<loop 19.451>bgm/4.ogg"
    FP_PLAY_WITH_ME = "<loop 10.893>bgm/6.ogg"
    FP_POEM_PANIC = "<loop 2.291>bgm/7.ogg"
    FP_DAIJOUBU = "<loop 9.938>bgm/8.ogg"
    
    # Okay, Everyone!
    FP_OKAY_EV = "<loop 4.444>bgm/5.ogg"
    FP_OKAY_EV_NAT = "<loop 4.444>bgm/5_natsuki.ogg"
    FP_OKAY_EV_SAY = "<loop 4.444>bgm/5_sayori.ogg"
    FP_OKAY_EV_YUR = "<loop 4.444>bgm/5_yuri.ogg"
    
    # DDLC Theme
    FP_DDLC_THEME = "<loop 22.073>bgm/1.ogg"
    
    # Bonus Tracks
    FP_POEMS_FOREVER = "Submods/Expanded Music Submod/bgm/poems_are_forever.ogg"
    FP_DOKI_DOKI = "Submods/Expanded Music Submod/bgm/doki_doki.ogg"
    
    # DDLC Plus
    FP_MY_SONG_YOUR_NOTE = "Submods/Expanded Music Submod/bgm/my_song_your_note.ogg"
    FP_PEACHY_PIE = "Submods/Expanded Music Submod/bgm/peachy_pie.ogg"
    FP_STRAWBERRY_PEPPERMINT = "Submods/Expanded Music Submod/bgm/strawberry_peppermint.ogg"
    FP_LAVENDER_MIST = "Submods/Expanded Music Submod/bgm/lavender_mist.ogg"
    FP_JUST_A_LITTLE_BIT = "Submods/Expanded Music Submod/bgm/just_a_little_bit.ogg"
    FP_LETS_TEAMWORK = "Submods/Expanded Music Submod/bgm/lets_teamwork.ogg"
    FP_DUSK = "Submods/Expanded Music Submod/bgm/dusk.ogg"
    FP_PIECE_BY_PIECE = "Submods/Expanded Music Submod/bgm/piece_by_piece.ogg"
    FP_HUG_ENERGY = "Submods/Expanded Music Submod/bgm/hug_energy.ogg"
    FP_FRIEND_AND_LIT = "Submods/Expanded Music Submod/bgm/stories_of_friendship_and_literature.ogg"
    FP_DEAR_SUNSHINE = "Submods/Expanded Music Submod/bgm/dear_sunshine.ogg"
    FP_CANDY_HEARTS = "Submods/Expanded Music Submod/bgm/candy_hearts.ogg"
    
    def initMusicChoices(sayori=False):
        global music_choices
        global music_pages
        music_choices = list()
        
        if not sayori:            
            # Just Monika.
            music_choices.append((JUST_MONIKA, FP_JUST_MONIKA))
            
            # Your Reality
            music_choices.append((YOURE_REAL, FP_YOURE_REAL))
            music_choices.append((PIANO_COVER, FP_PIANO_COVER))
            music_choices.append((YR_EUROBEAT, FP_YR_EUROBEAT))
            
            # DDLC bgm
            music_choices.append((OHAYOU_SAYORI, FP_OHAYOU_SAYORI))
            music_choices.append((LOVE_AND_LIT, FP_LOVE_AND_LIT))
            music_choices.append((PLAY_WITH_ME, FP_PLAY_WITH_ME))
            music_choices.append((POEM_PANIC, FP_POEM_PANIC))
            music_choices.append((DAIJOUBU, FP_DAIJOUBU))
            music_choices.append((MY_FEELS, FP_MY_FEELS))
            music_choices.append((MY_CONF, FP_MY_CONF))
            music_choices.append((STILL_LOVE, FP_STILL_LOVE))
            
            # Okay, Everyone!
            music_choices.append((OKAY_EV, FP_OKAY_EV))
            music_choices.append((OKAY_EV_MON, FP_OKAY_EV_MON))
            music_choices.append((OKAY_EV_NAT, FP_OKAY_EV_NAT))
            music_choices.append((OKAY_EV_SAY, FP_OKAY_EV_SAY))
            music_choices.append((OKAY_EV_YUR, FP_OKAY_EV_YUR))
            
            # DDLC Theme
            music_choices.append((DDLC_THEME, FP_DDLC_THEME))
            music_choices.append((DDLC_MT_80, FP_DDLC_MT_80))
            
            # Bonus Tracks
            if "poems_forever" in store.persistent._ms_enabled_songs:
                music_choices.append((POEMS_FOREVER, FP_POEMS_FOREVER))
            if "doki_doki" in store.persistent._ms_enabled_songs:
                music_choices.append((DOKI_DOKI, FP_DOKI_DOKI))
                
            # DDLC Plus
            if "ddlc_plus" in store.persistent._ms_enabled_songs:
                music_choices.append((MY_SONG_YOUR_NOTE, FP_MY_SONG_YOUR_NOTE))
                music_choices.append((PEACHY_PIE, FP_PEACHY_PIE))
                music_choices.append((STRAWBERRY_PEPPERMINT, FP_STRAWBERRY_PEPPERMINT))
                music_choices.append((LAVENDER_MIST, FP_LAVENDER_MIST))
                music_choices.append((JUST_A_LITTLE_BIT, FP_JUST_A_LITTLE_BIT))
                music_choices.append((LETS_TEAMWORK, FP_LETS_TEAMWORK))
                music_choices.append((DUSK, FP_DUSK))
                music_choices.append((PIECE_BY_PIECE, FP_PIECE_BY_PIECE))
                music_choices.append((HUG_ENERGY, FP_HUG_ENERGY))
                music_choices.append((FRIEND_AND_LIT, FP_FRIEND_AND_LIT))
            
            # DDLC Plus Bonus Tracks
            if "dear_sunshine" in store.persistent._ms_enabled_songs:
                music_choices.append((DEAR_SUNSHINE, FP_DEAR_SUNSHINE))
            if "candy_hearts" in store.persistent._ms_enabled_songs:
                music_choices.append((CANDY_HEARTS, FP_CANDY_HEARTS))
            
            # Misc
            if "playwithme_var6" in store.persistent._ms_enabled_songs:
                music_choices.append((PLAYWITHME_VAR6, FP_PLAYWITHME_VAR6))
            if "sayo_nara" in store.persistent._ms_enabled_songs:
                music_choices.append((SAYO_NARA_SENS, FP_SAYO_NARA))
        
        else:
            music_choices.append((SAYO_NARA, FP_SAYO_NARA))
        
        _m1_zz_music_selector__scanCustomBGM(music_choices)
        
        # checks whitelist and removes songs that no longer exist
        if store.persistent._ms_rand_whitelist:
            for song in store.persistent._ms_rand_whitelist:
                if song not in store.songs.music_choices:
                    store.persistent._ms_rand_whitelist.remove(song)
        
        music_pages = _m1_zz_music_selector__paginate(music_choices)
    
