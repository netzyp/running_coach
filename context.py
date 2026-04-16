import json

training_plan="""| Week | Dates | Mon | Tue | Wed | Thu | Fri | Sat | Sun | ~Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NOW | Mar 9–15 | REST | — | — | — | REST | REST | 15km Easy. Stay relaxed, 6:00–6:30/km. | ~15km |
| Week 1 | Mar 16–22 | REST | 12km Tempo. 2km warmup. 8km at 5:50–6:00/km continuous. 2km cooldown. Learn to hold race pace comfortably. | 10km Hills. 2km warmup. 8x 60–90sec hard uphill, run back down easy. 2km cooldown. | 10km Easy 6:00–6:30/km. | REST | 6km Easy optional. | 25km. First 20km at 6:00–6:15/km, last 5km push to 5:45/km. Practice banking time on flat sections. | ~63km |
| Week 2 | Mar 23–29 | REST | 14km Tempo. 2km warmup. 10km at 5:50–6:00/km. 2km cooldown. | 10km Hills. 2km warmup. 10x 60–90sec hard uphill, run back down easy. 2km cooldown. | 10km Easy 6:00–6:30/km. | REST | 6km Easy optional. | 28km. Run the whole thing including hills. Target 6:00–6:15/km on flats, controlled effort on hills — slow down but don't walk. | ~68km |
| Week 3 | Mar 30–Apr 5 | REST | 14km Intervals. 2km warmup. 7x 1km at 4:45–5:00/km. 90sec walk recovery. 2km cooldown. | 12km Hills. 2km warmup. 8x 2min hard uphill, run back down easy. 2km cooldown. | 10km Easy 6:00–6:30/km. | REST | 8km Easy optional. | 32km. Simulate race structure — first 20km at 6:00–6:15/km to bank time, then push through the last 12km on tired legs at 6:15–6:30/km. | ~76km |
| Week 4 | Apr 6–12 | REST | 16km Tempo. 2km warmup. 12km at 5:50–6:00/km continuous. 2km cooldown. | 12km Hills. 2km warmup. 8x 2–3min hard uphill, run back down easy. 2km cooldown. | 10km Easy 6:00–6:30/km. | REST | REST | 36km. Full race rehearsal. First 25km at 6:00–6:15/km. Km 25–30 simulate the big climb (find a long hill, run it hard). Last 6km push to 5:50/km simulating a race finish. | ~74km |
| Week 5 DELOAD | Apr 13–19 | REST | 10km Easy 6:00–6:30/km. No effort. | 8km Easy 6:15/km. Flat route. | 8km Easy 6:15/km. | REST | REST | 20km Easy 6:15–6:30/km. Full recovery week — don't chase pace. | ~46km |
| Week 6 | Apr 20–26 | REST | 14km Intervals. 2km warmup. 8x 1km at 4:45–5:00/km. 90sec walk recovery. 2km cooldown. | 12km Tempo on a hilly route. 2km warmup. 8km at 5:50/km — run every hill, back off effort not pace. 2km cooldown. | 10km Easy 6:00–6:30/km. | REST | REST | 38km. Race rehearsal — wear your race kit, eat race-day breakfast, run at race time. First 30km at 6:00–6:15/km then simulate the km 33–38 climb by finding the hilliest 5km on your route and attacking it. | ~74km |
| Week 7 PEAK | Apr 27–May 3 | REST | 12km Tempo on hilly route. 2km warmup. 8km at 5:50/km running every hill. 2km cooldown. | 10km Easy 6:00–6:30/km. Protect legs. | 10km Easy 6:00–6:30/km. | REST | REST | 42km. Your biggest run. Treat it exactly like race day. First 33km at 6:00–6:15/km banking time, then push through a big hill section from km 33–38, then hold on for the last 4km. If you can do this you can do 60km. | ~74km |
| Week 8 TAPER | May 4–10 | REST | 10km Easy 6:00/km. Feeling fresh is the only goal. | 8km Easy 6:15/km. | 8km Easy 6:15/km. | REST | REST | 20km Easy 6:15/km. Last long run. Controlled and comfortable. | ~46km |
| Week 9 TAPER | May 11–17 | REST | 6km Easy 6:15/km. Short and relaxed. | REST | 4km Easy then 4x 20sec strides. Wake legs up, don't tire them. | REST | REST | 5km Shakeout. No pace target. Just move. | ~15km |
| RACE DAY | Sun 17 May | REST | — | — | — | REST | REST | 60KM 🏁 Km 0–33 at 6:00–6:15/km to bank time. Attack km 33–38 climb, run every metre. Hold on to Apollo Bay. | — |"""

def data_context(runs, question):
    prompt = f"""
    You are a running coach. 

    Training plan: 
    {training_plan} 

    Recent runs:
    {json.dumps(runs, indent=2)}

    Question: 
    {question}
    """
    return prompt

