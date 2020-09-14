import sys
import zlib

data_stream = open(sys.argv[1], "rb") #bytes型で読み込み
decomp_obj = zlib.decompressobj(16+zlib.MAX_WBITS) #ヘッダサイズをgzipヘッダ用に調整
decompressed = b'' #復号結果

while True:
    buf = data_stream.read(64) # ストリームの一部をbufに格納,
                               # 後にパケットペイロードに置き換え
    if not buf:
        decompressed += decomp_obj.flush()
        break
    while True:
        if not buf:
            break
        decompressed += decomp_obj.decompress(buf)
        buf = decomp_obj.unconsumed_tail

print(decompressed.decode()) #文字列に変換して出力
        
