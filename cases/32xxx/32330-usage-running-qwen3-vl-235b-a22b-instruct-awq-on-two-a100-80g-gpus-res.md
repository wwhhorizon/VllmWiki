# vllm-project/vllm#32330: [Usage]: Running Qwen3-VL-235B-A22B-Instruct-AWQ on two A100-80G GPUs results in an error

| 字段 | 值 |
| --- | --- |
| Issue | [#32330](https://github.com/vllm-project/vllm/issues/32330) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Running Qwen3-VL-235B-A22B-Instruct-AWQ on two A100-80G GPUs results in an error

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ``` python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.13.11 | packaged by Anaconda, Inc. | (main, Dec 10 2025, 21:28:48) [GCC 14.3.0] (64-bit runtime) Python platform : Linux-6.8.0-90-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA A100-SXM4-80GB GPU 1: Quadro P620 GPU 2: NVIDIA A100-SXM4-80GB Nvidia driver version : 570.124.06 cuDNN version : Probably one of the foll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: Running Qwen3-VL-235B-A22B-Instruct-AWQ on two A100-80G GPUs results in an error usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ``` python collect_env.py Collecting e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Running Qwen3-VL-235B-A22B-Instruct-AWQ on two A100-80G GPUs results in an error usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ``` python collect_env.py Collecting e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: VL-235B-A22B-Instruct-AWQ on two A100-80G GPUs results in an error usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ``` python collect_env.py Collecting environment information....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
