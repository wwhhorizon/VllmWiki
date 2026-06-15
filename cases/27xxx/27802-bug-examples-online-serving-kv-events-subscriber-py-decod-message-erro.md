# vllm-project/vllm#27802: [Bug]: examples/online_serving/kv_events_subscriber.py decod message error

| 字段 | 值 |
| --- | --- |
| Issue | [#27802](https://github.com/vllm-project/vllm/issues/27802) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache |
| 子分类 |  |
| Operator 关键词 | cache;cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: examples/online_serving/kv_events_subscriber.py decod message error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` # python vllm/examples/online_serving/kv_events_subscriber.py INFO 10-30 17:19:14 [__init__.py:216] Automatically detected platform cuda. Listening for KV cache events on topic: kv-events Error decoding message: Expected `bytes`, got `int` - at `$[1][0][1][0]` Error decoding message: Expected `bytes`, got `int` - at `$[1][0][1][0]` Error decoding message: Expected `bytes`, got `int` - at `$[1][0][1][0]` Error decoding message: Expected `bytes`, got `int` - at `$[1][0][1][0]` Error decoding message: Expected `bytes`, got `int` - at `$[1][0][1][0]` Error decoding message: Expected `bytes`, got `int` - at `$[1][0][1][0]` Error decoding message: Expected `bytes`, got `int` - at `$[1][0][1][0]` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: py INFO 10-30 17:19:14 [__init__.py:216] Automatically detected platform cuda. Listening for KV cache events on topic: kv-events Error decoding message: Expected `bytes`, got `int` - at `$[1][0][1][0]` Error decoding me...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: requently asked questions. development attention_kv_cache cache;cuda env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 4 [__init__.py:216] Automatically detected platform cuda. Listening for KV cache events on topic: kv-events Error decoding message: Expected `bytes`, got `int` - at `$[1][0][1][0]` Error decoding message: Expected `byte...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development attention_kv_cache cache;cuda env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
