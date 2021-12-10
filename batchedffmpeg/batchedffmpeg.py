import os
import sys
import pathlib

def read_files(path, exts):
    exts = tuple(exts)
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if not file.lower().endswith(exts):
                continue     
            files.append(os.path.join(r, file))
    return files

def main():
    argv = sys.argv[1:]
    assert "-i" in argv, "usage: batchedffmpeg * -i {folder or file} *"
    
    idx_input_option = [i for i, arg in enumerate(argv) if arg == "-i"]
    assert len(idx_input_option) == 1, "usage: "
    idx_input_option = idx_input_option[0]
    
    assert len(argv) - 1 != idx_input_option, "usage: batchedffmpeg * -i {folder or file} *"
    idx_input_file = idx_input_option + 1
    input_path = argv[idx_input_file]
    
    if os.path.isfile(input_path):
        os.system("ffmpeg " + ' '.join(argv))
    elif os.path.isdir(input_path):
        video_exts = ['webm', 'mkv', 'flv', 'vob', 'ogv', 'ogg', 'rrc', 
                'gifv', 'mng', 'mov', 'avi', 'qt', 'wmv', 'yuv', 
                'rm', 'asf', 'amv', 'mp4', 'm4p', 'm4v', 'mpg',
                'mp2', 'mpeg', 'mpe', 'mpv', 'm4v', 'svi', '3gp',
                '3g2', 'mxf', 'roq', 'nsv', 'flv', 'f4v', 'f4p',
                'f4a', 'f4b']
        
        video_files = read_files(input_path, video_exts)
        
        idx_output_file = [i for i, arg in enumerate(argv[idx_input_option + 2:]) if "." in arg]
        assert len(idx_output_file) != 0, "At least one output file must be specified"
        idx_output_file = idx_input_option + 2 + idx_output_file[0]

        output_file = argv[idx_output_file]
        for video_file in video_files:
            
            input_name = pathlib.Path(video_file).stem
            
            # change input
            argv[idx_input_file] = video_file
            
            # change output
            argv[idx_output_file] = input_name + "_" + output_file
            
            os.system("ffmpeg " + ' '.join(argv))
    else:
        raise FileNotFoundError(input_path, " is unvalid as an input.")
     
if __name__ == "__main__":
    main()