# Disparity Mapping for Stereo Vision

This folder contains the implementation and optimization results of the Disparity Mapping stage, developed as part of the PBL Stereo Vision project.

## Overview

The goal of this module is to generate a high-precision disparity map from rectified stereo image pairs. This map serves as the critical input for subsequent 3D point cloud reconstruction.

## Contents
- **code/**: Implementation of disparity algorithms and post-processing filters.
- **results/**: Visualizations of algorithm comparisons, parameter sweeps, and the final refined map.

## Key Technical Features

### 1. Algorithm Selection: BM vs. SGBM
I compared the standard **Block Matching (BM)** and **Semi-Global Block Matching (SGBM)** algorithms. While BM is computationally faster, SGBM provides significantly better results with sharper edges and lower noise, making it the preferred choice for high-quality 3D modeling.

### 2. Parameter Optimization (Block Size)
The `blockSize` parameter was optimized through a comprehensive parameter sweep. 
- **Small Block Size (e.g., 5)**: High detail but susceptible to salt-and-pepper noise.
- **Large Block Size (e.g., 21)**: Smooth results but blurred object boundaries.
- **Optimal Selection**: A `blockSize` of **11** was selected as the "Sweet Spot" for the Tsukuba dataset to balance precision and stability.

### 3. Post-processing: Hole Filling
To handle occlusions and pixels where disparity could not be calculated, I implemented a **Local Hole-Filling filter**. By using a local median interpolation method, the "holes" (invalid pixels) are seamlessly filled, resulting in a dense disparity map.

## Results
- The comparison grid shows the distinct advantage of SGBM over BM.
- The included GIF demonstrates the dynamic impact of parameter tuning.
- The final output is a refined, dense disparity map ready for 3D reconstruction.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib
- imageio (for GIF generation)