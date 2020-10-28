#!/usr/bin/env python
# author: yurz
#

def mod_since(date_since, file_path):
    import os
    from datetime import datetime
    from time import mktime

    try:
        time_since = mktime(datetime.strptime(date_since, '%d/%m/%Y').timetuple())
        file_mod_time = os.path.getmtime(file_path)
    except:
        return True

    if file_mod_time >= time_since:
        return True
    else:
        return False


def time_stamp():
    import datetime
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def main(keywords=None, search_dir=None, date_since=None):
    ##
    ### enter arguments below if ran as a standalone script ###
    keywords = '''12345,678910,blah-blah'''
    search_dir = "//tuna/data/.../process/"
    date_since = "01/11/2012"
    ### end of arguments ###
    ##

    import os
    from sys import stdout

    results = "search_results" + "_" + time_stamp() + ".txt"
    keyword_list = keywords.split(",")
    results_file = open(results, "w")

    file_num = 0
    line_num = 0
    find_num = 0

    print
    "Searching"

    for root, dirs, files in os.walk(search_dir):
        for file in files:
            print
            ".",
            fullpath = os.path.join(root, file)
            if mod_since(date_since, fullpath) and file.endswith(".log"):
                file_num += 1
                with open(fullpath, "r") as search_file:
                    for line in search_file:
                        line_num += 1
                        for keyword in keyword_list:
                            if keyword in line:
                                find_num += 1
                                results_file.write(keyword + "\t" + fullpath + "::\t" + line)
    results_file.close()

    print
    "\n\n", str(line_num), "lines in", str(file_num), "files searched"
    print
    str(find_num), "results recorded in", results


if __name__ == '__main__':
    import time

    start_time = time.time()
    main()
    print
    "Job ran for", time.time() - start_time, "seconds"