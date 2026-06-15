# vllm-project/vllm#13030: [Usage]: ARM architecture usage

| 字段 | 值 |
| --- | --- |
| Issue | [#13030](https://github.com/vllm-project/vllm/issues/13030) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: ARM architecture usage

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run VLLM on a server with an aarch64 architecture, equipped with NVIDIA's graphics card, and hope to use the GPU to run VLLM. Do you know if this is supported? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: ARM architecture usage usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run VLLM on a server with an aarch64 architecture, equipp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
