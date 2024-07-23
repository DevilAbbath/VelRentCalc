def rentcalcv1(csubs, quser, texpenses):
    return (csubs * quser) - texpenses


def rentcalcv2(csubs, qsuser, qpuser, texpenses):
    pcalc = (csubs * qpuser) * 0.5
    scalc = csubs * qsuser

    return (pcalc + scalc) - texpenses

def mathreason(actualprofits, previousprofits):

    reason = actualprofits / previousprofits
    return round(reason, 2)