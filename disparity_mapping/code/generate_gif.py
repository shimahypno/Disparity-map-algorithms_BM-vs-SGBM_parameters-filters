import os

# 保存用フォルダの作成
os.makedirs('video_frames', exist_ok=True)

# 3から31まで2刻み（奇数のみ）でループ
for b_size in range(3, 33, 2):
    stereo = cv2.StereoSGBM_create(
        numDisparities=numDisparities,
        blockSize=b_size,
        P1=8 * b_size**2,
        P2=32 * b_size**2
    )
    disp = stereo.compute(imgL_gray, imgR_gray).astype(np.float32) / 16.0
    
    # 保存用に色付け
    disp_color = cv2.applyColorMap(
        cv2.normalize(disp, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8), 
        cv2.COLORMAP_JET
    )
    
    # ファイル名にパラメータを含めて保存
    filename = f'video_frames/sgbm_bsize_{b_size:02d}.png'
    cv2.imwrite(filename, disp_color)
    print(f'Saved: {filename}')


Saved: video_frames/sgbm_bsize_03.png
Saved: video_frames/sgbm_bsize_05.png
Saved: video_frames/sgbm_bsize_07.png
Saved: video_frames/sgbm_bsize_09.png
Saved: video_frames/sgbm_bsize_11.png
Saved: video_frames/sgbm_bsize_13.png
Saved: video_frames/sgbm_bsize_15.png
Saved: video_frames/sgbm_bsize_17.png
Saved: video_frames/sgbm_bsize_19.png
Saved: video_frames/sgbm_bsize_21.png
Saved: video_frames/sgbm_bsize_23.png
Saved: video_frames/sgbm_bsize_25.png
Saved: video_frames/sgbm_bsize_27.png
Saved: video_frames/sgbm_bsize_29.png
Saved: video_frames/sgbm_bsize_31.png




import imageio
import os
import re

def create_gif(folder_path, output_name, duration=0.5):
    images = []
    # ファイル名から数字を抽出して正しくソートする
    filenames = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')],
                       key=lambda x: int(re.findall(r'\d+', x)[0]))

    for filename in filenames:
        file_path = os.path.join(folder_path, filename)
        images.append(imageio.imread(file_path))
        print(f"Adding: {filename}")

    # GIFとして保存 (durationは各フレームの表示秒数)
    imageio.mimsave(output_name, images, duration=duration)
    print(f"Successfully saved: {output_name}")

# 実行
create_gif('video_frames', 'sgbm_parameter_sweep.gif', duration=0.3)


/tmp/ipython-input-851318381.py:13: DeprecationWarning: Starting with ImageIO v3 the behavior of this function will switch to that of iio.v3.imread. To keep the current behavior (and make this warning disappear) use `import imageio.v2 as imageio` or call `imageio.v2.imread` directly.
  images.append(imageio.imread(file_path))
Adding: sgbm_bsize_03.png
Adding: sgbm_bsize_05.png
Adding: sgbm_bsize_07.png
Adding: sgbm_bsize_09.png
Adding: sgbm_bsize_11.png
Adding: sgbm_bsize_13.png
Adding: sgbm_bsize_15.png
Adding: sgbm_bsize_17.png
Adding: sgbm_bsize_19.png
Adding: sgbm_bsize_21.png
Adding: sgbm_bsize_23.png
Adding: sgbm_bsize_25.png
Adding: sgbm_bsize_27.png
Adding: sgbm_bsize_29.png
Adding: sgbm_bsize_31.png
Successfully saved: sgbm_parameter_sweep.gif


