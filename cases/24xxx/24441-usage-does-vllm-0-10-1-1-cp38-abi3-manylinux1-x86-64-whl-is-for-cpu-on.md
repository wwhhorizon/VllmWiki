# vllm-project/vllm#24441: [Usage]: Does ‘’vllm-0.10.1.1-cp38-abi3-manylinux1_x86_64.whl" is for cpu-only node deploy? #Xeon

| 字段 | 值 |
| --- | --- |
| Issue | [#24441](https://github.com/vllm-project/vllm/issues/24441) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does ‘’vllm-0.10.1.1-cp38-abi3-manylinux1_x86_64.whl" is for cpu-only node deploy? #Xeon

### Issue 正文摘录

### Your current environment Xeon 6548 ### How would you like to use vllm I want to run vllm for serving qwen3-0.6b model on a cpu-only node,my cpu is Xeon6548，so i wonder the release"vllm-0.10.1.1-cp38-abi3-manylinux1_x86_64.whl" is just what i need? or i must built from source code by myself? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 6548 ### How would you like to use vllm I want to run vllm for serving qwen3-0.6b model on a cpu-only node,my cpu is Xeon6548，so i wonder the release"vllm-0.10.1.1-cp38-abi3-manylinux1_x86_64.whl" is just what i need? o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lf? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
