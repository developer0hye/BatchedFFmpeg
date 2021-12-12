# BatchedFFmpeg

Process multiple videos with one line of ffmpeg command.

![ezgif-1-b9b482fb9e6f](https://user-images.githubusercontent.com/35001605/145683660-2bd91e58-988a-4c1a-9955-533aa5cecba4.gif)
![ezgif-2-4ce90071b4cd](https://user-images.githubusercontent.com/35001605/145685168-d55b420f-4481-40c5-8963-5ce1a76c6a0b.gif)

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

Usage for command is the same with original ffmpeg besides `infile`. 

`infile` can be a video file or **folder(=directory) where the video files are saved**. If `infile` is a folder, program will search all video files in a folder including subfolders and then those files will be processed under the same command.

The output file is saved differently depending on the extension of `outfile`.

### if `outfile` == video:

```
  input/
    hi.mp4
    bye.mp4
```

After running command(outfile=./output/out.avi)...

```
  output/
    hi_out.avi
    bye_out.avi
```

### elif `outfile` == img:

```
  input/
    hi.mp4
    bye.mp4
```

After running command(outfile=./output/out%4d.jpg)...

```
  output/
    hi/
      hi_out0001.jpg
      hi_out0002.jpg
      ...
    bye/
      bye_out0001.jpg
      bye_out0002.jpg
      ...
```
