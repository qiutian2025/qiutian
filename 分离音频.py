# 需提前安装依赖库：
# pip install moviepy spleeter ffmpeg-python

import os
from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path, audio_output="audio.wav"):
    """从视频中提取音频"""
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_output)
    return audio_output

def separate_vocals(audio_path, output_dir="output"):
    """使用 Spleeter 分离人声"""
    from spleeter.separator import Separator
    
    # 使用预训练模型（默认2轨：人声/伴奏）
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(audio_path, output_dir)
    
    # 生成文件路径：output_dir/audio/vocals.wav
    base_name = os.path.basename(audio_path).split('.')[0]
    return os.path.join(output_dir, base_name, "vocals.wav")

# 使用示例
if __name__ == "__main__":
    video_path = "C:\\Users\\Administrator\\Desktop\\那是我的祖国.mp4"  # 输入视频路径
    
    # 步骤1：提取音频
    audio_file = extract_audio_from_video(video_path)
    
    # 步骤2：分离人声
    vocals_path = separate_vocals(audio_file)
    
    print(f"人声已保存至：{vocals_path}")