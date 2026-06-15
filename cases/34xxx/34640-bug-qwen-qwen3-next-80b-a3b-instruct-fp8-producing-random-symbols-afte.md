# vllm-project/vllm#34640: [Bug]: Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 producing random symbols after 3bb4e4311

| 字段 | 值 |
| --- | --- |
| Issue | [#34640](https://github.com/vllm-project/vllm/issues/34640) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 producing random symbols after 3bb4e4311

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/commit/3bb4e4311c6da31257e6c8e5b1027ef516e025c8 introduces some changes makes the output of Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 as random symbols. Before this commit everything is fine. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 producing random symbols after 3bb4e4311 bug ### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/commit/3bb4e4311c6da31257e6c8e5b1027ef516...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 producing random symbols after 3bb4e4311 bug ### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/commit/3bb4e4311c6da31257e6c8e5b1027ef516...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 producing random symbols after 3bb4e4311 bug ### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/commit/3bb4e4311c6da31257e6c8e5b1027ef516...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tization;sampling_logits;speculative_decoding cuda;fp8;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
