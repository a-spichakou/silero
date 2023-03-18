from base64 import b64encode

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

import os
import torch


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
local_file = 'model.pt'

#if not os.path.isfile(local_file):
#    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
#                                   local_file)  

device = torch.device('cpu')
torch.set_num_threads(1)

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)


@app.route("/spec")
def spec():
    return jsonify(swagger(app))


@app.route("/synthesize/", methods=["POST"])
@cross_origin()
def synthesize():
    request_json = request.get_json()

    text = request_json["text"]
    speaker = request_json["voice"]

    audio_paths = model.save_wav(text=text,
                             speaker=speaker,
                             sample_rate=48000)

    with open(audio_paths, mode="rb") as wavefile:
        audio_bytes = wavefile.read()

    result = b64encode(audio_bytes).decode("utf-8")
    os.remove(audio_paths)

    return {
        "response_code": 200,
         "response": [
        {
          "name": speaker,
          "response_audio": result
        }
    ]
   }


if __name__ == "__main__":
    app.run()