def get_risk(type):
    if type == "unsafe":
        return "high"
    elif type == "dark":
        return "medium"
    else:
        return "low"