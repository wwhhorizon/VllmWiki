# vllm-project/vllm#1027: Support YaRN models (RoFormer implementation in rotary_embedding kernel)

| 字段 | 值 |
| --- | --- |
| Issue | [#1027](https://github.com/vllm-project/vllm/issues/1027) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support YaRN models (RoFormer implementation in rotary_embedding kernel)

### Issue 正文摘录

Feature request Nous Research and EleutherAI have recently released the YaRN model, which comes in two versions with context sizes of 64k and 128k. This model utilizes RoFormer-style embeddings, distinguishing it from GPT-NeoX and GPT-J. It is built upon the foundation of the LLaMa 2 model, making it largely compatible with some minor adjustments required for optimal support. Motivation The YaRN model's longer context length (up to 128k) is highly valuable for tasks involving extensive context, compared to the limited 4096 context length of the llama2 base model. Other YaRN paper: [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/pdf/2309.00071.pdf) YaRN Code: [YaRN Github](https://github.com/jquesnelle/yarn)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: and EleutherAI have recently released the YaRN model, which comes in two versions with context sizes of 64k and 128k. This model utilizes RoFormer-style embeddings, distinguishing it from GPT-NeoX and GPT-J. It is built...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Support YaRN models (RoFormer implementation in rotary_embedding kernel) Feature request Nous Research and EleutherAI have recently released the YaRN model, which comes in two versions with context sizes of 64k and 128k...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rmer implementation in rotary_embedding kernel) Feature request Nous Research and EleutherAI have recently released the YaRN model, which comes in two versions with context sizes of 64k and 128k. This model utilizes RoF...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: YaRN models (RoFormer implementation in rotary_embedding kernel) Feature request Nous Research and EleutherAI have recently released the YaRN model, which comes in two versions with context sizes of 64k and 128k. This m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
