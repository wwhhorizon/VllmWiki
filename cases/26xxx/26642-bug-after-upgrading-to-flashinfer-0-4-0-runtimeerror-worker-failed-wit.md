# vllm-project/vllm#26642: [Bug]: After upgrading to Flashinfer 0.4.0: RuntimeError: Worker failed with error 'Could not find nvcc'

| 字段 | 值 |
| --- | --- |
| Issue | [#26642](https://github.com/vllm-project/vllm/issues/26642) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: After upgrading to Flashinfer 0.4.0: RuntimeError: Worker failed with error 'Could not find nvcc'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After installing flashinfer-python v.0.4.0, when trying to serve any model, I get the error: ``` ERROR: (Worker_TP1 pid=3534) ERROR 10-11 22:28:17 [multiproc_executor.py:694] RuntimeError: Could not find nvcc ``` If I reinstall the old version with 'uv pip install flashinfer-python==0.3.0', the the error goes away. My path includes /usr/local/cuda/bin and typing 'nvcc --version' shows it works, returning: ``` nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2025 NVIDIA Corporation Built on Fri_Feb_21_20:23:50_PST_2025 Cuda compilation tools, release 12.8, V12.8.93 Build cuda_12.8.r12.8/compiler.35583870_0 ``` Anybody has experienced this problem? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nvcc' bug ### Your current environment ### 🐛 Describe the bug After installing flashinfer-python v.0.4.0, when trying to serve any model, I get the error: ``` ERROR: (Worker_TP1 pid=3534) ERROR 10-11 22:28:17 [multiproc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: After upgrading to Flashinfer 0.4.0: RuntimeError: Worker failed with error 'Could not find nvcc' bug ### Your current environment ### 🐛 Describe the bug After installing flashinfer-python v.0.4.0, when trying to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: fer-python==0.3.0', the the error goes away. My path includes /usr/local/cuda/bin and typing 'nvcc --version' shows it works, returning: ``` nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2025 NVIDIA Corporati...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ug After installing flashinfer-python v.0.4.0, when trying to serve any model, I get the error: ``` ERROR: (Worker_TP1 pid=3534) ERROR 10-11 22:28:17 [multiproc_executor.py:694] RuntimeError: Could not find nvcc ``` If...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
