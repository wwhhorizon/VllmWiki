# vllm-project/vllm#26093: [Installation]: non-CUDA x86 vLLM v0.10.2 wheel is CUDA dependent

| 字段 | 值 |
| --- | --- |
| Issue | [#26093](https://github.com/vllm-project/vllm/issues/26093) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: non-CUDA x86 vLLM v0.10.2 wheel is CUDA dependent

### Issue 正文摘录

### Your current environment The output of `python collect_env.py` ``` Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 (main, Sep 2 2025, 14:19:37) [Clang 20.1.4 ] (64-bit runtime) Python platform : Linux-6.14.0-1013-aws-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info =====================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: non-CUDA x86 vLLM v0.10.2 wheel is CUDA dependent installation;stale ### Your current environment The output of `python collect_env.py` ``` Collecting environment information... uv is set ================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Installation]: non-CUDA x86 vLLM v0.10.2 wheel is CUDA dependent installation;stale ### Your current environment The output of `python collect_env.py` ``` Collecting environment information... uv is set ===============...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ment The output of `python collect_env.py` ``` Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ub...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: llation]: non-CUDA x86 vLLM v0.10.2 wheel is CUDA dependent installation;stale ### Your current environment The output of `python collect_env.py` ``` Collecting environment information... uv is set =====================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .0+cpu [pip3] torchvision==0.23.0+cpu [pip3] transformers==4.56.2 [pip3] triton==3.4.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
