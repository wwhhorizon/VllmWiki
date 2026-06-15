# vllm-project/vllm#20261: [Bug]: Prefix caching ignores visual input, causing incorrect multimodal outputs under concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#20261](https://github.com/vllm-project/vllm/issues/20261) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;scheduler_memory;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefix caching ignores visual input, causing incorrect multimodal outputs under concurrency

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving the qwen2.5-vl multimodal model using vllm serve, I noticed that enabling --enable-prefix-caching leads to incorrect outputs (e.g., repeated, truncated, or garbled tokens) under high concurrency or heavy asynchronous usage. The Prefix cache hit rate is around 40%. All the requests use identical text prompts but slightly different images (The images are mazes with different structures). Disabling prefix caching (--no-enable-prefix-caching) resolves the issue. I wonder if the cache key only considers text prompts and does not take image content or image-derived embeddings into account? Or although the images are different mazes, the embedding may be quite similar, leading to the incorrect cache matching? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#36622 [Bugfix] Fix off-by-one in multimodal prefix cache hash boundary check

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Prefix caching ignores visual input, causing incorrect multimodal outputs under concurrency bug;unstale ### Your current environment ### 🐛 Describe the bug When serving the qwen2.5-vl multimodal model using vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: sual input, causing incorrect multimodal outputs under concurrency bug;unstale ### Your current environment ### 🐛 Describe the bug When serving the qwen2.5-vl multimodal model using vllm serve, I noticed that enabling -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;scheduler_memory;speculative_decoding cuda;operator;trito...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ng? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: d tokens) under high concurrency or heavy asynchronous usage. The Prefix cache hit rate is around 40%. All the requests use identical text prompts but slightly different images (The images are mazes with different struc...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36622](https://github.com/vllm-project/vllm/pull/36622) | closes_keyword | 0.95 | [Bugfix] Fix off-by-one in multimodal prefix cache hash boundary check | Closes #20261 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
