# vllm-project/vllm#33813: [Bug]: llm.score() fails on batched multimodal input for qwen3-vl-reranker

| 字段 | 值 |
| --- | --- |
| Issue | [#33813](https://github.com/vllm-project/vllm/issues/33813) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;multimodal_vlm |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: llm.score() fails on batched multimodal input for qwen3-vl-reranker

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using qwen3-vl-reranker with llm.score(), the function claims to support batch inference (1 -> N or N -> N), but passing batched multimodal inputs causes a runtime error. Single-pair scoring works correctly. However, when I pass a list of multimodal inputs as a batch, llm.score() crashes with: ValueError: Missing 'type' field in multimodal part. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: llm.score() fails on batched multimodal input for qwen3-vl-reranker bug ### Your current environment ### 🐛 Describe the bug When using qwen3-vl-reranker with llm.score(), the function claims to support batch infe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ns. development frontend_api;model_support;multimodal_vlm cuda crash env_dependency;shape Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development frontend_api;model_support;multimodal_vlm cuda crash env_dependency;shape...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
