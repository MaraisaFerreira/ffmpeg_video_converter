import os
import fnmatch

ffmpeg_path = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'  # codec de video
crf = '-crf 23'  # qualidade - 15 a 28
preset = '-preset ultrafast'
codec_audio = '-c:a aac'  # codec de audio
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:30'  # tp de conversão ou nd '' p/ converter o vídeo inteiro

source_path = r'C:\Users\m\Videos'
to_path = r'C:\Users\m\Videos'

for root, folders, files in os.walk(source_path):
    for file in files:
        if not fnmatch.fnmatch(file, '*.mp4'):  # procura videos mkv
            continue

        full_path = os.path.join(root, file)
        file_name, _ = os.path.splitext(full_path)
        subs_path = file_name + '.srt'

        if os.path.isfile(subs_path):  # verif se existe legendas p/ cd video
            input_subs = f'-i "{subs_path}"'
            map_subs = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_subs = ''
            map_subs = ''

        file_name, file_extension = os.path.splitext(file)

        new_file_name = file_name + '_NOVO' + '.mp4'  # converte p/.mp4
        file_path = os.path.join(root, new_file_name)

        run = f'{ffmpeg_path} -i "{full_path}" {input_subs} ' \
              f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
              f'{debug} {map_subs} "{file_path}"'

        os.system(run)  # exec o script
