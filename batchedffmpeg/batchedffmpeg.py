import os
import sys
import pathlib

video_exts = ('webm', 'mkv', 'flv', 'vob', 'ogv', 'ogg', 'rrc', 
        'gifv', 'mng', 'mov', 'avi', 'qt', 'wmv', 'yuv', 
        'rm', 'asf', 'amv', 'mp4', 'm4p', 'm4v', 'mpg',
        'mp2', 'mpeg', 'mpe', 'mpv', 'm4v', 'svi', '3gp',
        '3g2', 'mxf', 'roq', 'nsv', 'flv', 'f4v', 'f4p',
        'f4a', 'f4b')

img_exts = ('png', 'jpg', 'jpeg', 'bmp')


def read_files(path, exts):
    exts = tuple(exts)
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if not file.lower().endswith(exts):
                continue     
            files.append(os.path.join(r, file))
    return files

def get_output_file_type(file):
    if file.endswith(video_exts):
        file_type = "video"
    elif file.endswith(img_exts):
        file_type = "img"
    else:
        raise TypeError(f"{file} is unvalid as an output. Valid output list: {video_exts} or {img_exts}")
    return file_type

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
        
        video_files = read_files(input_path, video_exts)
        
        idx_output_file = [i for i, arg in enumerate(argv[idx_input_option + 2:]) if "." in arg]
        assert len(idx_output_file) != 0, "At least one output file must be specified"
        idx_output_file = idx_input_option + 2 + idx_output_file[0]

        output_file = pathlib.Path(argv[idx_output_file])
        output_file_dir = output_file.parent
        output_file_fullname = output_file.name # with extension
        
        output_file_type = get_output_file_type(str(output_file_fullname))
     
        for video_file in video_files:            
            # change input
            argv[idx_input_file] = '"' + video_file + '"' # for whitespace, unicode
            
            # change output
            input_file_name = pathlib.Path(video_file).stem # without extension

            if output_file_type == "video":
                argv[idx_output_file] = os.path.join(output_file_dir, input_file_name + "_" + output_file_fullname)
            elif output_file_type == "img":
                output_file_save_folder = os.path.join(output_file_dir, input_file_name)
                os.makedirs(output_file_save_folder, exist_ok=True)
                argv[idx_output_file] = os.path.join(output_file_save_folder, input_file_name + "_" + output_file_fullname)

            argv[idx_output_file] = '"' + argv[idx_output_file] + '"' # for whitespace, unicode
            
            os.system("ffmpeg " + ' '.join(argv))
    else:
        raise FileNotFoundError(input_path, " is unvalid as an input.")
     
if __name__ == "__main__":
    main()