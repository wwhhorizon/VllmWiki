# vllm-project/vllm#9080: [Bug]: Lack of reproducibility across multiple runs of prefix cache benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#9080](https://github.com/vllm-project/vllm/issues/9080) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Lack of reproducibility across multiple runs of prefix cache benchmark

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Lack of random seed for reproducibility in prefix cache benchmark. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Lack of reproducibility across multiple runs of prefix cache benchmark bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Lack of random seed for reproducibility in prefix...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Lack of reproducibility across multiple runs of prefix cache benchmark bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Lack of random seed for reproducibility in prefix...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rk. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Lack of reproducibility across multiple runs of prefix cache benchmark bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Lack of random seed for reproducibility in prefix...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: runs of prefix cache benchmark bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Lack of random seed for reproducibility in prefix cache benchmark. ### Before submitting a new i...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
