# vllm-project/vllm#4066: Does vllm support both CUDA 11.3 version and PyTorch 1.12?

| 字段 | 值 |
| --- | --- |
| Issue | [#4066](https://github.com/vllm-project/vllm/issues/4066) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;moe;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Does vllm support both CUDA 11.3 version and PyTorch 1.12?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ``` python3 collect_env.py Collecting environment information... PyTorch version: 1.12.1+cu113 Is debug build: False CUDA used to build PyTorch: 11.3 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.27 Python version: 3.10.14 (main, Apr 14 2024, 08:51:48) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.90.1.el7.x86_64-x86_64-with-glibc2.27 Is CUDA available: True CUDA runtime version: 11.3.109 CUDA_MODULE_LOADING set to: GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 525.105.17 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.2.0 /usr/local/cuda-11.3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: Does vllm support both CUDA 11.3 version and PyTorch 1.12? installation ### Your current environment ```text The output of `python collect_env.py` ``` ``` python3 collect_env.py Collecting environment information... PyT...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: Does vllm support both CUDA 11.3 version and PyTorch 1.12? installation ### Your current environment ```text The output of `python collect_env.py` ``` ``` python3 collect_env.py Collecting environment information... PyT...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: rc/pybind.cpp.o [3/14] Building CUDA object CMakeFiles/_C.dir/csrc/quantization/marlin/marlin_cuda_kernel.cu.o FAILED: CMakeFiles/_C.dir/csrc/quantization/marlin/marlin_cuda_kernel.cu.o /usr/local/cuda/bin/nvcc -forward...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: vironment information... PyTorch version: 1.12.1+cu113 Is debug build: False CUDA used to build PyTorch: 11.3 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: collect_env.py` ``` ``` python3 collect_env.py Collecting environment information... PyTorch version: 1.12.1+cu113 Is debug build: False CUDA used to build PyTorch: 11.3 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
