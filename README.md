# BatchedFFmpeg

Process multiple videos with one line of ffmpeg command.

![ezgif-1-b9b482fb9e6f](https://user-images.githubusercontent.com/35001605/145683660-2bd91e58-988a-4c1a-9955-533aa5cecba4.gif)

## Requirements

- ffmpeg

## Install

```
pip install batchedffmpeg
```

## Usage

```
batchedffmpeg [options] [[infile options] -i infile]… {[outfile options] outfile}…
```

Usage is the same with original ffmpeg besides `infile`. 

`infile` can be a video file or **folder(=directory) the video files are saved**. If you type a folder, program will search all video files in a folder including subfolders and then those files will be processed under the same command.
