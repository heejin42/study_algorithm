def timeInWords(h, m):
    hours = [' ', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    minutes = [' ', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight' ,'twenty nine', 'half']
    if m == 0:
        return hours[h] + " o' clock"
    elif m == 30:
        return minutes[m] + " past " + hours[h]
    elif 0 < m < 30:
        if m == 15:
            return minutes[m] + " past " + hours[h]
        if m == 1:
            return minutes[m] + " minute past " + hours[h]
        return minutes[m] + " minutes past " + hours[h]
    else:
        m = 60 - m
        if m == 15:
            return minutes[m] + " to " + hours[h+1]
        if m == 1:
            return minutes[m] + " minute to " + hours[h+1]
        return minutes[m] + " minutes to " + hours[h+1]