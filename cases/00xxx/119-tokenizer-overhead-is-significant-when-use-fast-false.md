# vllm-project/vllm#119: Tokenizer overhead is significant when use_fast=False

| 字段 | 值 |
| --- | --- |
| Issue | [#119](https://github.com/vllm-project/vllm/issues/119) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Tokenizer overhead is significant when use_fast=False

### Issue 正文摘录

After #114 , the server decodes the running sequences every step. This leads to significant overhead, especially when the slow tokenizer is used (e.g., LLaMA). ``` # opt-13b inference latency (bs 8, input 32, output 128) Avg latency: 3.57 seconds Tokenizer (fast): 0.14 seconds # llama-13b inference latency (bs 8, input 32, output 128) Avg latency: 5.28 seconds Tokenizer (slow): 1.97 seconds ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he running sequences every step. This leads to significant overhead, especially when the slow tokenizer is used (e.g., LLaMA). ``` # opt-13b inference latency (bs 8, input 32, output 128) Avg latency: 3.57 seconds Token...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Tokenizer overhead is significant when use_fast=False performance After #114 , the server decodes the running sequences every step. This leads to significant overhead, especially when the slow tokenizer is used (e.g., L...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: significant overhead, especially when the slow tokenizer is used (e.g., LLaMA). ``` # opt-13b inference latency (bs 8, input 32, output 128) Avg latency: 3.57 seconds Tokenizer (fast): 0.14 seconds # llama-13b inference...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: d is significant when use_fast=False performance After #114 , the server decodes the running sequences every step. This leads to significant overhead, especially when the slow tokenizer is used (e.g., LLaMA). ``` # opt-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: when the slow tokenizer is used (e.g., LLaMA). ``` # opt-13b inference latency (bs 8, input 32, output 128) Avg latency: 3.57 seconds Tokenizer (fast): 0.14 seconds # llama-13b inference latency (bs 8, input 32, output...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
