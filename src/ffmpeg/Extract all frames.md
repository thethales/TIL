# FFMPEG

## FFMPEG extract all frames of a video

```
ffmpeg -i "C:\video.mp4"  -r 24/1 C:\folder\img%03d.jpg
```
Being,  
- 24/1 => The frame rate per second
- -i   => The input file
- %03d => The file name of the output frames concatenated to an ordinal sequential number formatted using 3 digits