# vllm-project/vllm#5607: [Bug]: Concurrent requests messing up GREEDY responses

| 字段 | 值 |
| --- | --- |
| Issue | [#5607](https://github.com/vllm-project/vllm/issues/5607) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Concurrent requests messing up GREEDY responses

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... /opt/vllm/lib64/python3.11/site-packages/transformers/utils/hub.py:124: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and will be removed in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.4 (Plow) (x86_64) GCC version: (GCC) 11.4.1 20231218 (Red Hat 11.4.1-3) Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.34 Python version: 3.11.7 (main, Jan 22 2024, 00:00:00) [GCC 11.4.1 20231218 (Red Hat 11.4.1-3)] (64-bit runtime) Python platform: Linux-4.18.0-372.46.1.el8_6.x86_64-x86_64-with-glibc2.34 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.104.12 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits ph...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: d in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.4 (Plow)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ead. warnings.warn( PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.4 (Plow) (x86_64) GCC version: (GCC) 11.4.1 20231218...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ```text The output of `python collect_env.py` Collecting environment information... /opt/vllm/lib64/python3.11/site-packages/transformers/utils/hub.py:124: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and wil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Concurrent requests messing up GREEDY responses bug ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... /opt/vllm/lib64/python3.11/site-packages/transf...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.41.2 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu12==2.18.1.0.4.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
