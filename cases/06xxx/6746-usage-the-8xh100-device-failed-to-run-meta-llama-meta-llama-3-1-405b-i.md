# vllm-project/vllm#6746: [Usage]: The 8xH100 device failed to run meta-llama/Meta-Llama-3.1-405B-Instruct-FP8.

| 字段 | 值 |
| --- | --- |
| Issue | [#6746](https://github.com/vllm-project/vllm/issues/6746) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: The 8xH100 device failed to run meta-llama/Meta-Llama-3.1-405B-Instruct-FP8.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-1053-nvidia-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version: 550.90.07 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.6 /usr/lib/x86_64-...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Mitigation; Sp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ve...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: The 8xH100 device failed to run meta-llama/Meta-Llama-3.1-405B-Instruct-FP8. usage ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.1+...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: The 8xH100 device failed to run meta-llama/Meta-Llama-3.1-405B-Instruct-FP8. usage ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch versio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: The 8xH100 device failed to run meta-llama/Meta-Llama-3.1-405B-Instruct-FP8. usage ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch versio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
