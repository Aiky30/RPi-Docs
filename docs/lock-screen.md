# Add lock screen feature

Open the config to add the menu item
```
sudo geany /etc/xdg/lxpanel/LXDE-pi/panels/panel
```

Add the following to the plugin type=menu
```
    item {
      name=Lock...
      image=gnome-lockscreen
      action=/usr/bin/dm-tool lock
    }
```