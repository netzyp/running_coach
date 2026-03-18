import json


def data_context(runs, question):
    prompt = f"""You are a running coach, take into account all of my strava runs {json.dumps(runs)}, now take into account the following question and answer it: {question}"""
    return prompt

