# vllm-project/vllm#10163: [Usage]: Poor Successful requests with Llama 3.1 405-FP8 in 8xH100 SXM5

| 字段 | 值 |
| --- | --- |
| Issue | [#10163](https://github.com/vllm-project/vllm/issues/10163) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Poor Successful requests with Llama 3.1 405-FP8 in 8xH100 SXM5

### Issue 正文摘录

### Your current environment ``` # python collect_env.py WARNING 11-08 16:53:16 cuda.py:23] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead, and make sure to uninstall `pynvml`. When both of them are installed, `pynvml` will take precedence and cause errors. See https://pypi.org/project/pynvml for more information. Warning: Your installation of OpenCV appears to be broken: module 'cv2.dnn' has no attribute 'DictValue'.Please follow the instructions at https://github.com/opencv/opencv-python/issues/884 to correct your environment. The import of cv2 has been skipped. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.27.6 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.8.0-47-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: 16:53:16 cuda.py:23] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead, and make sure to uninstall `pynvml`. When both of them are installed, `pynvml` will take precedence and cause erro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: Poor Successful requests with Llama 3.1 405-FP8 in 8xH100 SXM5 usage;stale ### Your current environment ``` # python collect_env.py WARNING 11-08 16:53:16 cuda.py:23] You are using a deprecated `pynvml` package...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: ul requests even with low QPS = 0.2 and no error in logs. ``` # python3 benchmark_serving.py --backend vllm --model meta-llama/Llama-3.1-405B-FP8 --dataset-name sharegpt --dataset-path="ShareGPT_V3_unfiltered_cleaned_sp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Poor Successful requests with Llama 3.1 405-FP8 in 8xH100 SXM5 usage;stale ### Your current environment ``` # python collect_env.py WARNING 11-08 16:53:16 cuda.py:23] You are using a deprecated `pynvml` package...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: Poor Successful requests with Llama 3.1 405-FP8 in 8xH100 SXM5 usage;stale ### Your current environment ``` # python collect_env.py WARNING 11-08 16:53:16 cuda.py:23] You are using a deprecated `pynvml` package...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
