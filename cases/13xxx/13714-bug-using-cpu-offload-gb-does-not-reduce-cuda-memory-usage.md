# vllm-project/vllm#13714: [Bug]: Using `cpu-offload-gb` does not reduce CUDA memory usage

| 字段 | 值 |
| --- | --- |
| Issue | [#13714](https://github.com/vllm-project/vllm/issues/13714) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using `cpu-offload-gb` does not reduce CUDA memory usage

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm experimenting with the `cpu-offload-gb` in an attempt to reduce CUDA memory usage by vLLM. However, I don't see any change when running vLLM with this setting vs without this setting. Am I missing something? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Using `cpu-offload-gb` does not reduce CUDA memory usage bug;stale ### Your current environment ### 🐛 Describe the bug I'm experimenting with the `cpu-offload-gb` in an attempt to reduce CUDA memory usage by vLLM...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Using `cpu-offload-gb` does not reduce CUDA memory usage bug;stale ### Your current environment ### 🐛 Describe the bug I'm experimenting with the `cpu-offload-gb` in an attempt to reduce CUDA memory usage by vLLM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
