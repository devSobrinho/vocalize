from flask import Blueprint, Response, jsonify, request
from app.modules.speech.speech_service import SpeechService
from app.modules.speech.schemas.stream_audio_schema import StreamAudioSchema
from marshmallow import ValidationError

speech_bd = Blueprint('speech', __name__)
speech_service = SpeechService()
stream_audio_schema = StreamAudioSchema()

@speech_bd.route('/stream_audio', methods=['POST'])
def stream_audio():
  try:
    data = stream_audio_schema.load(request.json)
  except ValidationError as err:
    return jsonify(err.messages), 400
  result = speech_service.stream_audio(data) 
  return Response(result, mimetype="audio/wav")
