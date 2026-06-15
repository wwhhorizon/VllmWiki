# vllm-project/vllm#33142: [Feature]: Tequila/Sherry/BitNet and Ternary support

| 字段 | 值 |
| --- | --- |
| Issue | [#33142](https://github.com/vllm-project/vllm/issues/33142) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Tequila/Sherry/BitNet and Ternary support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch There are a lot of models like BitNet v2 that are experimental, and Falcon-Edge sort of broke away into a new QAT norm https://huggingface.co/tiiuae/Falcon-E-3B-Base https://falcon-lm.github.io/blog/falcon-edge/ And also there are PTQ potential for a lot of the existing models, but they lack support in mainstream tooling https://github.com/Tencent/AngelSlim/tree/tequila/TernaryQuant https://github.com/Tencent/AngelSlim/tree/sherry/Sherry ### Alternatives Nobody has made an alternative yet other than Microsoft's defacto option https://github.com/microsoft/BitNet https://github.com/microsoft/unilm and for those on MLX hardware there are even less options https://github.com/exo-explore/mlx-bitnet ### Additional context https://github.com/vllm-project/vllm/issues/18213 https://github.com/vllm-project/vllm/issues/17279 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: uest;unstale ### 🚀 The feature, motivation and pitch There are a lot of models like BitNet v2 that are experimental, and Falcon-Edge sort of broke away into a new QAT norm https://huggingface.co/tiiuae/Falcon-E-3B-Base...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Tequila/Sherry/BitNet and Ternary support feature request;unstale ### 🚀 The feature, motivation and pitch There are a lot of models like BitNet v2 that are experimental, and Falcon-Edge sort of broke away int...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nstream tooling https://github.com/Tencent/AngelSlim/tree/tequila/TernaryQuant https://github.com/Tencent/AngelSlim/tree/sherry/Sherry ### Alternatives Nobody has made an alternative yet other than Microsoft's defacto o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 279 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
