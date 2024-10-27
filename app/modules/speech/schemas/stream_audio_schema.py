from marshmallow import Schema, fields

class StreamAudioSchema(Schema):
    text = fields.Str(required=True, validate=lambda x: len(x) <= 1000)
    language = fields.Str(required=False, missing='pt')