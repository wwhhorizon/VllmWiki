# vllm-project/vllm#20783: [Bug]: Performance Anomaly: compressed-tensors shows no speedup over BF16 on H100s on vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#20783](https://github.com/vllm-project/vllm/issues/20783) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Performance Anomaly: compressed-tensors shows no speedup over BF16 on H100s on vLLM

### Issue 正文摘录

### Your current environment sudo docker run --gpus all --shm-size=240g -d \ --name vllm-benchmark --workdir /app -v "$(pwd)":/app \ --entrypoint "" vllm/vllm-openai:v0.9.2 bash /app/auto_tune_latency.sh If it helps... Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.0.3 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.0-1026-gcp-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: over BF16 on H100s on vLLM bug;stale ### Your current environment sudo docker run --gpus all --shm-size=240g -d \ --name vllm-benchmark --workdir /app -v "$(pwd)":/app \ --entrypoint "" vllm/vllm-openai:v0.9.2 bash /app...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: maly: compressed-tensors shows no speedup over BF16 on H100s on vLLM bug;stale ### Your current environment sudo docker run --gpus all --shm-size=240g -d \ --name vllm-benchmark --workdir /app -v "$(pwd)":/app \ --entry...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.2.6.post1+cu128torch2.7 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.3.14 [pip3] nvidia-cuda-cupti-cu12==12.8.57 [pip3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Performance Anomaly: compressed-tensors shows no speedup over BF16 on H100s on vLLM bug;stale ### Your current environment sudo docker run --gpus all --shm-size=240g -d \ --name vllm-benchmark --workdir /app -v "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ]: Performance Anomaly: compressed-tensors shows no speedup over BF16 on H100s on vLLM bug;stale ### Your current environment sudo docker run --gpus all --shm-size=240g -d \ --name vllm-benchmark --workdir /app -v "$(pw...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
