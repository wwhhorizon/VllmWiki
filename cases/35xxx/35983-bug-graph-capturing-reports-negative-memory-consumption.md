# vllm-project/vllm#35983: [Bug]: Graph Capturing reports negative memory consumption

| 字段 | 值 |
| --- | --- |
| Issue | [#35983](https://github.com/vllm-project/vllm/issues/35983) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Graph Capturing reports negative memory consumption

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The approach used to track how much memory is consumed by CudaGraphs seems to be broken as it reports negative values `(EngineCore_DP0 pid=3771514) INFO 03-04 08:50:51 [gpu_model_runner.py:5365] Graph capturing finished in 5 secs, took -0.35 GiB` command to reproduce `vllm serve meta-llama/Llama-3.1-8B-Instruct` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;opera...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cribe the bug The approach used to track how much memory is consumed by CudaGraphs seems to be broken as it reports negative values `(EngineCore_DP0 pid=3771514) INFO 03-04 08:50:51 [gpu_model_runner.py:5365] Graph capt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s negative values `(EngineCore_DP0 pid=3771514) INFO 03-04 08:50:51 [gpu_model_runner.py:5365] Graph capturing finished in 5 secs, took -0.35 GiB` command to reproduce `vllm serve meta-llama/Llama-3.1-8B-Instruct` ### B...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Graph Capturing reports negative memory consumption bug;stale ### Your current environment ### 🐛 Describe the bug The approach used to track how much memory is consumed by CudaGraphs seems to be broken as it repo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
