# vllm-project/vllm#17524: [Bug]: Batch Order Affects the Results even Set Seed in Batch Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#17524](https://github.com/vllm-project/vllm/issues/17524) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Batch Order Affects the Results even Set Seed in Batch Inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Even though I set the seed everything, the batch order may affect the final production results. In my reproduction code below, the preds1 != preds2 == preds3. Is this the expected behavior? And how can I ensure all results are reproducible in batch inference (I use batch inference to speed up, as I have many cases to call). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: this the expected behavior? And how can I ensure all results are reproducible in batch inference (I use batch inference to speed up, as I have many cases to call). ### Before submitting a new issue... - [x] Make sure yo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency;shape Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s3. Is this the expected behavior? And how can I ensure all results are reproducible in batch inference (I use batch inference to speed up, as I have many cases to call). ### Before submitting a new issue... - [x] Make...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
