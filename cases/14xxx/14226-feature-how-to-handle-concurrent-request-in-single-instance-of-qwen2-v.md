# vllm-project/vllm#14226: [Feature]: How to handle concurrent request in single instance of Qwen2-VL model.

| 字段 | 值 |
| --- | --- |
| Issue | [#14226](https://github.com/vllm-project/vllm/issues/14226) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 43; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: How to handle concurrent request in single instance of Qwen2-VL model.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am using the Qwen2-VL-7B model on vLLM with a single machine that has a 24GB GPU. The model itself takes approximately 18GB to load, leaving 6GB available. During inference, a single request consumes around 2GB of GPU memory. When two users send requests simultaneously: - The first user receives a response in 8 seconds. - The second user receives a response in 15 seconds. Given that 6GB of GPU memory is available, is there a way to efficiently handle concurrent requests on a single instance? Why does the second request take longer, and how can this be optimized?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: How to handle concurrent request in single instance of Qwen2-VL model. feature request ### 🚀 The feature, motivation and pitch I am using the Qwen2-VL-7B model on vLLM with a single machine that has a 24GB GP...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nds. Given that 6GB of GPU memory is available, is there a way to efficiently handle concurrent requests on a single instance? Why does the second request take longer, and how can this be optimized?
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 6GB available. During inference, a single request consumes around 2GB of GPU memory. When two users send requests simultaneously: - The first user receives a response in 8 seconds. - The second user receives a response...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: How to handle concurrent request in single instance of Qwen2-VL model. feature request ### 🚀 The feature, motivation and pitch I am using the Qwen2-VL-7B model on vLLM with a single machine that has a 24GB GP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
