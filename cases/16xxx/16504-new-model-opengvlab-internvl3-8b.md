# vllm-project/vllm#16504: [New Model]: OpenGVLab/InternVL3-8B

| 字段 | 值 |
| --- | --- |
| Issue | [#16504](https://github.com/vllm-project/vllm/issues/16504) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: OpenGVLab/InternVL3-8B

### Issue 正文摘录

### The model to consider. Hi the new internvl3 series have just dropped and was hopping to get vllm support for this ### The closest model vllm already supports. internvl2.5 should be close ### What's your difficulty of supporting the model you want? based on the code example for quickstart on huggingface, i dont think it will be a big probelm as most of the code is reused as per internvl2.5 on huggingface ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: OpenGVLab/InternVL3-8B ### The model to consider. Hi the new internvl3 series have just dropped and was hopping to get vllm support for this ### The closest model vllm already supports. internvl2.5 should b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ace ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
