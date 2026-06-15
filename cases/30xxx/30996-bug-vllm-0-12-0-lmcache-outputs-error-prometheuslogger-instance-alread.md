# vllm-project/vllm#30996: [Bug]: vLLM 0.12.0 + LMCache outputs ERROR: PrometheusLogger instance already created with different metadata.

| 字段 | 值 |
| --- | --- |
| Issue | [#30996](https://github.com/vllm-project/vllm/issues/30996) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.12.0 + LMCache outputs ERROR: PrometheusLogger instance already created with different metadata.

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : version 4.2.0 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Nov 6 2025, 13:44:16) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.14.0-35-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.41 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA RTX 6000 Ada Generation Nvidia driver version : 570.133.07 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Architecture: x86_64 CPU op-mode(s)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : version 4.2.0 Libc version : glibc-2.39 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.9.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] mypy==1.18.2 [pip3] mypy-boto3-s3==1.42.10 [pip3] mypy_extensions==1.1.0 [pip3] numpy==1.26.4 [pip3] nvidia-cublas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: DA runtime version : 12.9.41 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA RTX 6000 Ada Generation Nvidia driver version : 570.133.07 cuDNN version : Could not collect HIP runtime version : N...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: : PrometheusLogger instance already created with different metadata. bug;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
