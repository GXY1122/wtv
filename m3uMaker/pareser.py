# -*- coding:utf-8 -*-
import codecs
import os
from m3u_parser import M3uParser

content = ''
output = './output/checked.m3u'
m3u_playlist = M3uParser()


def get_file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.m3u':
                L.append(os.path.join(root, file))
    return L


def check(file_path):
    global content
    m3u_playlist.parse_m3u(file_path)
    m3u_playlist.remove_by_extension("mp4")
    m3u_playlist.filter_by("status", "GOOD")
    print("check (%s), online size is [%d]" % (file_path, len(m3u_playlist.get_list())))


if __name__ == '__main__':
    if os.path.exists(output):
        os.remove(output)
        content = '#EXTM3U\n'
    files = get_file_name('./input')
    for file in files:
        check(file)
    for item in m3u_playlist.get_list():
        content += "#EXTINF:-1," + item['name'] + '\n' + item['url'] + '\n'
    f = codecs.open(output, 'a', 'utf-8')
    f.write(content)
    f.close()
