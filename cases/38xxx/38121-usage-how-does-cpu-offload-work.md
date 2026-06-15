# vllm-project/vllm#38121: [Usage]: how does cpu offload work?

| 字段 | 值 |
| --- | --- |
| Issue | [#38121](https://github.com/vllm-project/vllm/issues/38121) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how does cpu offload work?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm im trying to load a 7b model on 16gb vram. i set cpu offload to 20gb, but i can still see the gpu exploding, does this mean only after the gpu is exhausted, the cpu is used? can we choose between how much to put in cpu and gpu? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pu? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: how does cpu offload work? usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm im trying to load a 7b model on 16gb vram. i set cpu offload to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _env.py` ``` ### How would you like to use vllm im trying to load a 7b model on 16gb vram. i set cpu offload to 20gb, but i can still see the gpu exploding, does this mean only after the gpu is exhausted, the cpu is use...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
