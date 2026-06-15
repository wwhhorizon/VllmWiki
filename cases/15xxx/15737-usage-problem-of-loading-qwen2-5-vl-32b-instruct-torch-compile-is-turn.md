# vllm-project/vllm#15737: [Usage]:Problem of loading Qwen2.5-VL-32B-Instruct: torch.compile is turned on, but the model Qwen2.5-VL-32B-Instruct does not support it. 

| 字段 | 值 |
| --- | --- |
| Issue | [#15737](https://github.com/vllm-project/vllm/issues/15737) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]:Problem of loading Qwen2.5-VL-32B-Instruct: torch.compile is turned on, but the model Qwen2.5-VL-32B-Instruct does not support it. 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` (vllm_env) root@Administrator:/mnt/c/Users/dell# python collect_env.py INFO 03-29 08:52:44 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.3 (main, Feb 4 2025, 14:48:35) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A5000 GPU 1: NVIDIA RTX A5000 Nvidia driver version: 572.60 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 96 On-line CPU(s) list: 0-95 Vendo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Usage]:Problem of loading Qwen2.5-VL-32B-Instruct: torch.compile is turned on, but the model Qwen2.5-VL-32B-Instruct does not support it. usage;stale ### Your current environment ```text The output of `python collect_e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Usage]:Problem of loading Qwen2.5-VL-32B-Instruct: torch.compile is turned on, but the model Qwen2.5-VL-32B-Instruct does not support it. usage;stale ### Your current environment ```text The output of `python collect_e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: ed on, but the model Qwen2.5-VL-32B-Instruct does not support it. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` (vllm_env) root@Administrator:/mnt/c/Users/dell# python collec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: py INFO 03-29 08:52:44 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: .api_server --model Qwen2.5-VL-32B-Instruct --port 8000 --host 0.0.0.0 --dtype bfloat16 --tensor_parallel_size 2 --limit-mm-per-prompt image=5,video=5 INFO 03-29 08:49:37 [__init__.py:239] Automatically detected platfor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
