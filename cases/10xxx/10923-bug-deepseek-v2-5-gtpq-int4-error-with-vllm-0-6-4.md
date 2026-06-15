# vllm-project/vllm#10923: [Bug]: deepseek v2.5 gtpq(int4) error with vllm-0.6.4

| 字段 | 值 |
| --- | --- |
| Issue | [#10923](https://github.com/vllm-project/vllm/issues/10923) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;moe;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deepseek v2.5 gtpq(int4) error with vllm-0.6.4

### Issue 正文摘录

### Your current environment Warning: Your installation of OpenCV appears to be broken: module 'cv2.dnn' has no attribute 'DictValue'.Please follow the instructions at https://github.com/opencv/opencv-python/issues/884 to correct your environment. The import of cv2 has been skipped. Collecting environment information... PyTorch version: 2.6.0.dev20241203+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.4 Libc version: glibc-2.35 Python version: 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.4.0-144-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.6.77 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 GPU 2: NVIDIA A40 GPU 3: NVIDIA A40 GPU 4: NVIDIA A40 GPU 5: NVIDIA A40 GPU 6: NVIDIA A40 GPU 7: NVIDIA A40 Nvidia driver version: 550.54.14 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.5.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.5.0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: or with vllm-0.6.4 bug;stale ### Your current environment Warning: Your installation of OpenCV appears to be broken: module 'cv2.dnn' has no attribute 'DictValue'.Please follow the instructions at https://github.com/ope...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: mation... PyTorch version: 2.6.0.dev20241203+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nvironment. The import of cv2 has been skipped. Collecting environment information... PyTorch version: 2.6.0.dev20241203+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: U...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: deepseek v2.5 gtpq(int4) error with vllm-0.6.4 bug;stale ### Your current environment Warning: Your installation of OpenCV appears to be broken: module 'cv2.dnn' has no attribute 'DictValue'.Please follow the ins...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nformation... PyTorch version: 2.6.0.dev20241203+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
