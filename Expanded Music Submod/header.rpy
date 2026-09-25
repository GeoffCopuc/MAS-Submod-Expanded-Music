init -990 python in mas_submod_utils:
    Submod(
        author="Geoff Copuc",
        name="Expanded Music",
        description="Inserts more music from the original game and DDLC+ into the music menu and allows Monika to choose music herself.",
        version="0.5.0",
        settings_pane="expandedmusic_settings_main"
    )

init -989 python in gsm_utils:
    import store

    #Register the updater if needed
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Expanded Music",
            user_name="GeoffCopuc",
            repository_name="MAS-Submod-Expanded-Music",
            update_dir=""
        )



default persistent._ms_enabled_songs = [
    "playwithme_var6",
    "sayo_nara"
]

default persistent._ms_rand_whitelist = list()

screen expandedmusic_settings_main():
    $ tooltip = renpy.get_screen("submods", "screens").scope["tooltip"]
    
    vbox:
        style_prefix "check"
        box_wrap False
        xfill True
        xmaximum 1000
        
        hbox:
            textbutton _("{b}Additional Music{/b}"):
                selected False
                action Show("expandedmusic_settings_additional")
                hovered SetField(tooltip, "value", "Configure the songs this submod adds to the music menu")
                unhovered SetField(tooltip, "value", tooltip.default)
            
            textbutton _("{b}Random Music Whitelist{/b}"):
                selected False
                action Show("expandedmusic_settings_random")
                hovered SetField(tooltip, "value", "Configure the songs Monika can choose from when asking her to play music")
                unhovered SetField(tooltip, "value", tooltip.default)

screen expandedmusic_settings_additional():
    modal True
    zorder 200
    style_prefix "confirm"
    add mas_getTimeFile("gui/overlay/confirm.png")
    
    frame:
        vbox:
            spacing 10

            hbox:
                style_prefix "generic_fancy_check"
                spacing 5
                
                textbutton _("Play With Me (Variant 6)"):
                    action [
                        ToggleSetMembership(persistent._ms_enabled_songs, "playwithme_var6"),
                        Function(store.songs.initMusicChoices, store.mas_egg_manager.sayori_enabled())
                    ]
                
                if not store.mas_egg_manager.sayori_enabled():
                    textbutton _("Sayo-Nara"):
                        action [
                            ToggleSetMembership(persistent._ms_enabled_songs, "sayo_nara"),
                            Function(store.songs.initMusicChoices, store.mas_egg_manager.sayori_enabled())
                        ]
            
            vbox:
                text _("Bonus tracks:")
                hbox:
                    style_prefix "generic_fancy_check"
                    spacing 5
                    
                    textbutton _("Poems Are Forever"):
                        action [
                            ToggleSetMembership(persistent._ms_enabled_songs, "poems_forever"),
                            Function(store.songs.initMusicChoices, store.mas_egg_manager.sayori_enabled())
                        ]
                    
                    textbutton _("Doki Doki"):
                        action [
                            ToggleSetMembership(persistent._ms_enabled_songs, "doki_doki"),
                            Function(store.songs.initMusicChoices, store.mas_egg_manager.sayori_enabled())
                        ]
            
            vbox:
                text _("Doki Doki Literature Club Plus!:")
                hbox:
                    style_prefix "generic_fancy_check"
                    spacing 5
                    
                    textbutton _("OST"):
                        action [
                            ToggleSetMembership(persistent._ms_enabled_songs, "ddlc_plus"),
                            Function(store.songs.initMusicChoices, store.mas_egg_manager.sayori_enabled())
                        ]
                    
                    textbutton _("Dear Sunshine"):
                        action [
                            ToggleSetMembership(persistent._ms_enabled_songs, "dear_sunshine"),
                            Function(store.songs.initMusicChoices, store.mas_egg_manager.sayori_enabled())
                        ]
                    
                    textbutton _("Candy Hearts"):
                        action [
                            ToggleSetMembership(persistent._ms_enabled_songs, "candy_hearts"),
                            Function(store.songs.initMusicChoices, store.mas_egg_manager.sayori_enabled())
                        ]
            
            textbutton _("Back"):
                selected False
                action Hide("expandedmusic_settings_additional")
