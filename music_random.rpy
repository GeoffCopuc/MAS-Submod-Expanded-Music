screen expandedmusic_settings_random():
    modal True
    zorder 200
    style_prefix "confirm"
    add mas_getTimeFile("gui/overlay/confirm.png")
    
    frame:
        vbox:
            xmaximum 1100
            ymaximum 600
            xfill True
            yfill True
            
            viewport:
                id "viewport"
                scrollbars "vertical"
                xalign 0.5
                ymaximum 550
                mousewheel True
                
                vbox:
                    spacing 5
                    
                    for song in store.songs.music_choices:
                        hbox:
                            style_prefix "generic_fancy_check"
                            
                            textbutton _(song[0]):
                                action ToggleSetMembership(persistent._ms_rand_whitelist, song)
            
            hbox:
                xalign 1.0
                ypos 20
                spacing 5
                
                textbutton _("Enable all"):
                    xalign 1.0
                    selected False
                    action [
                        SetField(persistent, "_ms_rand_whitelist", store.songs.music_choices),
                        Function(store.songs.initMusicChoices, store.mas_egg_manager.sayori_enabled())
                    ]
                
                textbutton _("Disable all"):
                    selected False
                    action SetField(persistent, "_ms_rand_whitelist", list())
            
            hbox:
                yanchor 1.0
                ypos 20
                
                textbutton _("Back"):
                    selected False
                    action Hide("expandedmusic_settings_random")



init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_expandedmusic_choose_song",
            category=["music"],
            prompt="Can you choose the music?",
            pool=True,
            unlocked=True,
            rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST},
            aff_range=(mas_aff.HAPPY, None)
        ),
        restartBlacklist=True
    )

label mas_expandedmusic_choose_song:
    m 7hub "Sure [player]!"
    
    if not persistent._ms_rand_whitelist or len(persistent._ms_rand_whitelist) == 0:
        $ song_choice = renpy.random.choice(store.songs.music_choices)
    else:
        $ song_choice = renpy.random.choice(persistent._ms_rand_whitelist)
    
    m 6dta ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    
    python:
        renpy.notify ("Now playing:\n[song_choice[0]]")
        mas_play_song(song_choice[1], set_per=True)
    
        music_quips = [
            _("There we go."),
            _("How about this one?"),
            _("This one!"),
            _("I like this song~")
        ]
        music_quip = renpy.random.choice(music_quips)
    
    m 3eub "[music_quip]"
    return
