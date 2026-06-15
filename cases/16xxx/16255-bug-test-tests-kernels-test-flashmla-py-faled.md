# vllm-project/vllm#16255: [Bug]: Test tests/kernels/test_flashmla.py faled

| 字段 | 值 |
| --- | --- |
| Issue | [#16255](https://github.com/vllm-project/vllm/issues/16255) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Test tests/kernels/test_flashmla.py faled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` pytest tests/kernels/test_flashmla.py -v ``` It shows error: ``` E TypeError: do_bench() got an unexpected keyword argument 'fast_flush' ``` I found that this parameter has been removed in triton: https://github.com/triton-lang/triton/pull/4485 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 485 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: gument 'fast_flush' ``` I found that this parameter has been removed in triton: https://github.com/triton-lang/triton/pull/4485 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
