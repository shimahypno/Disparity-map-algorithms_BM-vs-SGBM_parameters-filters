import numpy as np

# 穴埋めアルゴリズムの定義
def fill_holes_local(disp, window=3, max_iter=5):
    disp_filled = disp.copy()
    h, w = disp.shape
    r = window // 2

    for _ in range(max_iter):
        # 無効な値（通常、視差が計算できなかった場所は0以下になります）を特定
        nan_mask = (disp_filled <= 0) 
        
        # 穴がなくなれば終了
        if not nan_mask.any(): 
            break

        ys, xs = np.where(nan_mask)
        for y, x in zip(ys, xs):
            # 周辺画素の範囲を決定
            y0, y1 = max(0, y - r), min(h, y + r + 1)
            x0, x1 = max(0, x - r), min(w, x + r + 1)
            
            # 周辺のパッチを取得
            patch = disp_filled[y0:y1, x0:x1]
            # 有効な（0より大きい）値のみを抽出
            valid = patch[patch > 0] 
            
            if valid.size > 0:
                # 有効な値の中央値（Median）で穴を埋める
                disp_filled[y, x] = np.median(valid)
                
    return disp_filled

# フィルタ適用
# 前のステップで計算した 'disparity' を入力します
disp_refined = fill_holes_local(disparity, window=3, max_iter=5)

# 結果の表示（確認用）
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.subplot(121); plt.imshow(disparity, cmap='jet'); plt.title('Before (Original Disparity)')
plt.subplot(122); plt.imshow(disp_refined, cmap='jet'); plt.title('After (Hole Filled)')
plt.show()
