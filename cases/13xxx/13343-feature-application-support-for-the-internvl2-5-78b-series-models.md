# vllm-project/vllm#13343: [Feature]: Application support for the InternVL2.5-78B series models.

| 字段 | 值 |
| --- | --- |
| Issue | [#13343](https://github.com/vllm-project/vllm/issues/13343) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Application support for the InternVL2.5-78B series models.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch OpenGVLab/InternVL2_5-78B OpenGVLab/InternVL2_5-78B-MPO OpenGVLab/InternVL2_5-78B-AWQ OpenGVLab/InternVL2_5-78B-MPO-AWQ https://huggingface.co/OpenGVLab/InternVL2_5-78B https://huggingface.co/OpenGVLab/InternVL2_5-78B-MPO https://huggingface.co/OpenGVLab/InternVL2_5-78B-AWQ https://huggingface.co/stmacdonell/InternVL2_5-78B-MPO-AWQ ### Alternatives OpenGVLab/InternVL2_5-78B OpenGVLab/InternVL2_5-78B-MPO OpenGVLab/InternVL2_5-78B-AWQ OpenGVLab/InternVL2_5-78B-MPO-AWQ https://huggingface.co/OpenGVLab/InternVL2_5-78B https://huggingface.co/OpenGVLab/InternVL2_5-78B-MPO https://huggingface.co/OpenGVLab/InternVL2_5-78B-AWQ https://huggingface.co/stmacdonell/InternVL2_5-78B-MPO-AWQ ### Additional context OpenGVLab/InternVL2_5-78B OpenGVLab/InternVL2_5-78B-MPO OpenGVLab/InternVL2_5-78B-AWQ OpenGVLab/InternVL2_5-78B-MPO-AWQ https://huggingface.co/OpenGVLab/InternVL2_5-78B https://huggingface.co/OpenGVLab/InternVL2_5-78B-MPO https://huggingface.co/OpenGVLab/InternVL2_5-78B-AWQ https://huggingface.co/stmacdonell/InternVL2_5-78B-MPO-AWQ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Application support for the InternVL2.5-78B series models. feature request ### 🚀 The feature, motivation and pitch OpenGVLab/InternVL2_5-78B OpenGVLab/InternVL2_5-78B-MPO OpenGVLab/InternVL2_5-78B-AWQ OpenGVL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: AWQ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ure]: Application support for the InternVL2.5-78B series models. feature request ### 🚀 The feature, motivation and pitch OpenGVLab/InternVL2_5-78B OpenGVLab/InternVL2_5-78B-MPO OpenGVLab/InternVL2_5-78B-AWQ OpenGVLab/In...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
