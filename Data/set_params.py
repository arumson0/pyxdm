def set_params(functional, file_type, triples):
    if file_type.lower() == 'qe':
        if triples:
            params = {
            "b86bpbe": {"a1":0.57814950, "a2":1.67847807/0.529177, "zdamp":89260.32818953},
            "pbe":     {"a1":0.24433986, "a2":3.02044267/0.529177, "zdamp":150899.43966183},
            "revpbe":  {"a1":0.41333285, "a2":1.68631544/0.529177, "zdamp":29159.62835771},
            }
        else:
            params = {
            "b86bpbe": {"a1":0.651200, "a2":2.765236/0.529177, "zdamp":91449.08237214},
            "pbe":     {"a1":0.327500, "a2":5.229439/0.529177, "zdamp":153389.95959690},
            "revpbe":  {"a1":0.449951, "a2":1.575732/0.529177, "zdamp":30160.04701768},
            }
    elif file_type.lower() == 'aims':
        if triples:
            params = {
            "b86bpbe_lightdenser": {"a1":0.70672254, "a2":1.50693259/0.529177, "zdamp":114637.74034629},
            "pbe_lightdenser":     {"a1":0.34223376, "a2":2.90495924/0.529177, "zdamp":198245.79588527},
            "revpbe_lightdenser":  {"a1":0.98046708, "a2":0.18099533/0.529177, "zdamp":38712.36546260},
            "b86bpbe_tight":       {"a1":0.90401707, "a2":0.75222329/0.529177, "zdamp":93799.43257484},
            "pbe_tight":           {"a1":0.51026744, "a2":2.25168618/0.529177, "zdamp":159796.67525956},
            "revpbe_tight":        {"a1":0.93044021, "a2":0.16595377/0.529177, "zdamp":31749.65131209},
            }
        else:
            params = {
                "b86bpbe_lightdenser": {"a1":0.68811169, "a2":1.57894970/0.529177, "zdamp":116996.37456697},
                "pbe_lightdenser":     {"a1":0.32750033, "a2":2.96273826/0.529177, "zdamp":200770.40192761},
                "revpbe_lightdenser":  {"a1":0.92553653, "a2":0.36491034/0.529177, "zdamp":39880.10993795},
                "b86bpbe_tight":       {"a1":0.90036997, "a2":0.78080918/0.529177, "zdamp":96089.42234843},
                "pbe_tight":           {"a1":0.51240107, "a2":2.25880715/0.529177, "zdamp":162372.65733623},
                "revpbe_tight":        {"a1":0.89915582, "a2":0.28492491/0.529177, "zdamp":32842.28307901},
        }
    
    if functional not in params:
        raise ValueError(f"WARNING: {functional} has not been parameterized for XDM. Sorry.")
    a1 = params[functional]["a1"]
    a2 = params[functional]["a2"]
    zdamp = params[functional]["zdamp"]

    return a1, a2, zdamp
