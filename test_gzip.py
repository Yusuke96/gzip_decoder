import gzip

with gzip.open("/home/yusuke/work/gzip/tmp.gz","rt") as f:
    plane = f.read()

print(plane)
