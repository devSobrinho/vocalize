from app.modules.speech.schemas.stream_audio_schema import StreamAudioSchema
from gtts import gTTS
from io import BytesIO

class SpeechService:
    def _limit_text(self, text: str, limit: int = 1000) -> str:
        return text[:limit]

    def _limit_words_generator(self, text: str, chunk_size: int = 100) -> list:
        phrases = []
        words = text.split()
        for i in range(0, len(words), chunk_size):
            phrases.append(' '.join(words[i:i + chunk_size]))
        return phrases
    
    def _generate_audio_buffer(self, phrases: list, language: str = 'pt') -> str:
        for phrase in phrases:
            tts = gTTS(text=phrase, lang=language)
            audio_buffer = BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
        return audio_buffer

    def stream_audio(self, data: StreamAudioSchema) -> str:
        text = self._limit_text(data['text'])
        phrases = self._limit_words_generator(text)
        audio_buffer = self._generate_audio_buffer(phrases, data['language'])
        return audio_buffer
    


