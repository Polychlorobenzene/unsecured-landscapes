# UNSECURED LANDSCAPES

Unsecured Landscapes is an exercise of juxtaposing moving images from nature places that are being surveillance by IP Cameras. The footage is taken by a bot every 12 hours from cameras found at insecam. This project was initiated during the Automating Video Class at ITP, NYU.

![description](static/imgs/one.png)

## How it works

Two cronjob task runs every 8 and 12 hours executing the `record.py` and `cut.py` python scripts. The first one uses `ipvideos.py` to call a curated list of IP addresses of unsecured cameras found at insecam.org. This script records a 5 seconds video in 30 fps of every IP given. The second script `cut.py`, grab all the footage taken by the first script and cut and resize all the videos to have the same size and aspect ratio. After that cuts all the videos in half, saving the left and right parts separately. Lastly, the same script makes a composition with all the footage that has been cut in the right side.

## Try it

[UNSECURED LANDSCAPES](http://unsecured-landscapes.matamala.info/)


## License

MIT
