import glob, os, shutil

cnt = 0

for path in glob.iglob('/data/AnotherMissOh/AnotherMissOh_images/dramaqa_frames/**/*.jpg', recursive=True):
    # /data/AnotherMissOh/AnotherMissOh_images/dramaqa_frames/AnotherMissOh01/001/0078/IMAGE_0000004295.jpg
    episode = path.split('/')[5][-2:]
    scene   = path.split('/')[6]
    shot    = path.split('/')[7]
    filename = os.path.basename(path)
    shutil.copy(path, '/data/AnotherMissOh/images_all/' + '{}_{}_{}_{}'.format(episode, scene,shot, filename[6:]))
    
    if cnt % 1000 == 0:
        print(cnt, ':', path)
    cnt += 1
