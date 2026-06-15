# vllm-project/vllm#16227: [Feature]: Llama4 Pretrained Model support

| 字段 | 值 |
| --- | --- |
| Issue | [#16227](https://github.com/vllm-project/vllm/issues/16227) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Llama4 Pretrained Model support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently the Llama4 Instuct Model have been supported in rencent release while the pretrained model is pending. Please support this model. As far as I'm concerned, Pretrained model is really closed to the instruct one while there are some diffs: 1. Pretrained model's in bf16 which needs more memory and it can't loaded with 8H100. 2. No pp support, which means all the parameter must be divided by tp size while the head size of pretrained one is **40** causing a lot of problem. for example, hidden_size_mlp must be divided by tp( usually not divided by 20, 40 likes factor) 3. If only text model is needed to do text generation, can we add a params to only load text parts parametes when inference? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rained model's in bf16 which needs more memory and it can't loaded with 8H100. 2. No pp support, which means all the parameter must be divided by tp size while the head size of pretrained one is **40** causing a lot of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Llama4 Pretrained Model support feature request ### 🚀 The feature, motivation and pitch Currently the Llama4 Instuct Model have been supported in rencent release while the pretrained model is pending. Please...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: o the instruct one while there are some diffs: 1. Pretrained model's in bf16 which needs more memory and it can't loaded with 8H100. 2. No pp support, which means all the parameter must be divided by tp size while the h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Llama4 Pretrained Model support feature request ### 🚀 The feature, motivation and pitch Currently the Llama4 Instuct Model have been supported in rencent release while the pretrained model is pending. Please...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
