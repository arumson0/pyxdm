def set_params(functional, file_type):
    if file_type.lower() == 'qe':
        params = {
        "b86bpbe": {"a1":0.651200, "a2":2.765236, "zdamp":93320.858050},
        "pbe":     {"a1":0.327500, "a2":5.229439, "zdamp":158164.71484654},
        "revpbe":  {"a1":0.563061, "a2":2.297524, "zdamp":30680.96189145},
        }
    elif file_type.lower() == 'aims':
        params = {
        "b86bpbe": {"a1":0.68811169, "a2":1.57894970/0.529177, "zdamp":116996.37456697},
        "pbe":     {"a1":0.32750033, "a2":2.96273826/0.529177, "zdamp":200770.40192761},
        "revpbe":  {"a1":0.92553653, "a2":0.36491034/0.529177, "zdamp":39880.10993795},
        }
    
    if functional not in params:
        raise ValueError(f"WARNING: {functional} has not been parameterized for XDM. Sorry.")
    a1 = params[functional]["a1"]
    a2 = params[functional]["a2"]
    zdamp = params[functional]["zdamp"]

    return a1, a2, zdamp
