def compare(phoenix_to_slc,phoenix_to_tampa):
    if phoenix_to_slc>phoenix_to_tampa:
        print("slc is far from phoenix compared to tampa")
    elif phoenix_to_slc<phoenix_to_tampa:
        print("tampa,florida is far from phoenix compared to slc")
    else:
        print("both location are same")


compare(phoenix_to_slc=1750,phoenix_to_tampa=576)