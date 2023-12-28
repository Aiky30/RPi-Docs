## Preparing an image

1. Download the OS of choice.

2. Check the file against the checksum:

```shell
sha256sum Downloads/2023-12-05-raspios-bookworm-arm64-full.img
```

4. Plug the SD card into a USB card reader attached to an Ubuntu machine. 

5. If it's a .xz file, you will need to extract it

```shell
unxz ~/Downloads/2023-12-05-raspios-bookworm-arm64-full.img.xz
```

## Installing the image

1. Find the drive

```shell
fdisk -l
```

2. Replace `sdb` with your drive from the point above
```shell
sudo dd if=~/Downloads/2023-12-05-raspios-bookworm-arm64-full.img of=/dev/sdb status=progress bs=4M
```
