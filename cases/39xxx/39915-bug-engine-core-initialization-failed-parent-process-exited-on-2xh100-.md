# vllm-project/vllm#39915: [Bug]: Engine core initialization failed (Parent process exited) on 2xH100 with Llama-3.3-70B-FP8 (TP/PP=2)

| 字段 | 值 |
| --- | --- |
| Issue | [#39915](https://github.com/vllm-project/vllm/issues/39915) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine core initialization failed (Parent process exited) on 2xH100 with Llama-3.3-70B-FP8 (TP/PP=2)

### Issue 正文摘录

### Your current environment ## **Description** When attempting to run `nvidia/Llama-3.3-70B-Instruct-FP8` on a Google Cloud instance with **2x NVIDIA H100 GPUs**, the engine fails during initialization. The crash occurs immediately after NCCL is initialized, with the error: > `INFO [v1/executor/multiproc_executor.py:707] Parent process exited, terminating worker` This has been reproduced on **vLLM v0.14.0** and **v0.19.0**. The crash occurs regardless of whether Tensor Parallelism (`tensor_parallel_size=2`) or Pipeline Parallelism (`pipeline_parallel_size=2`) is configured. --- ## **Environment** ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Engine core initialization failed (Parent process exited) on 2xH100 with Llama-3.3-70B-FP8 (TP/PP=2) bug ### Your current environment ## **Description** When attempting to run `nvidia/Llama-3.3-70B-Instruct-FP8`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] numpy==2.3.5 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: itialization failed (Parent process exited) on 2xH100 with Llama-3.3-70B-FP8 (TP/PP=2) bug ### Your current environment ## **Description** When attempting to run `nvidia/Llama-3.3-70B-Instruct-FP8` on a Google Cloud ins...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Engine core initialization failed (Parent process exited) on 2xH100 with Llama-3.3-70B-FP8 (TP/PP=2) bug ### Your current environment ## **Description** When attempting to run `nvidia/Llama-3.3-70B-Instruct-FP8` on a Go...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
