import cv2
import numpy as np
import matplotlib.pyplot as plt

# 設定：比較したい blockSize のリスト
block_sizes = [5, 11, 21]
numDisparities = 16 * 6

results = []

for b_size in block_sizes:
    # --- BM アルゴリズム ---
    # BMはグレースケールのみ。numDisparitiesは16の倍数、blockSizeは奇数である必要があります
    stereo_bm = cv2.StereoBM_create(numDisparities=numDisparities, blockSize=b_size)
    disp_bm = stereo_bm.compute(imgL_gray, imgR_gray).astype(np.float32) / 16.0
    results.append((f"BM (size={b_size})", disp_bm))

    # --- SGBM アルゴリズム ---
    stereo_sgbm = cv2.StereoSGBM_create(
        minDisparity=0,
        numDisparities=numDisparities,
        blockSize=b_size,
        P1=8 * b_size**2,
        P2=32 * b_size**2,
        uniquenessRatio=10,
        speckleWindowSize=100,
        speckleRange=31
    )
    disp_sgbm = stereo_sgbm.compute(imgL_gray, imgR_gray).astype(np.float32) / 16.0
    results.append((f"SGBM (size={b_size})", disp_sgbm))

# 2行3列で表示
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()

for i, (title, disp) in enumerate(results):
    # 見やすくするために jet カラーマップを適用（正規化）
    disp_vis = cv2.normalize(disp, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    axes[i].imshow(disp_vis, cmap='jet')
    axes[i].set_title(title)
    axes[i].axis('off')

plt.tight_layout()
plt.savefig('comparison_grid.png') # 1つの画像として保存
plt.show()
