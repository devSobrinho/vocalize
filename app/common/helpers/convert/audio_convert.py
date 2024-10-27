from pydub import AudioSegment
from werkzeug.datastructures import FileStorage

class AudioConvert:

  def mp3_to_wav(self, audio: FileStorage, wav_path: str) -> str:
    print(f"Converting mp3 to {wav_path}")
    audio.export(wav_path, format="wav")
    return wav_path

  def mpeg_to_wav(self, audio: FileStorage, wav_path: str) -> str:
    print(f"Converting mpeg to {wav_path}")
    audio.export(wav_path, format="wav")
    return wav_path


