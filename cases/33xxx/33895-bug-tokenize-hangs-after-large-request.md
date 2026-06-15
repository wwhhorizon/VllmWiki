# vllm-project/vllm#33895: [Bug]: /tokenize hangs after large request

| 字段 | 值 |
| --- | --- |
| Issue | [#33895](https://github.com/vllm-project/vllm/issues/33895) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: /tokenize hangs after large request

### Issue 正文摘录

### Your current environment n/a ### 🐛 Describe the bug running vllm using `vllm/vllm-openai:v0.15.0` + `QuantTrio/Qwen3-235B-A22B-Instruct-2507-AWQ` after calling large number of `/tokenize` requests, this endpoint will become unresponsive -> will hang forever I can reproduce this on both v0.14.0 and v0.15.0 -> issue did not exists on v0.11.0 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ests, this endpoint will become unresponsive -> will hang forever I can reproduce this on both v0.14.0 and v0.15.0 -> issue did not exists on v0.11.0 ### Before submitting a new issue... - [x] Make sure you already sear...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ### 🐛 Describe the bug running vllm using `vllm/vllm-openai:v0.15.0` + `QuantTrio/Qwen3-235B-A22B-Instruct-2507-AWQ` after calling large number of `/tokenize` requests, this endpoint will become unresponsive -> will han...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 1.0 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ribe the bug running vllm using `vllm/vllm-openai:v0.15.0` + `QuantTrio/Qwen3-235B-A22B-Instruct-2507-AWQ` after calling large number of `/tokenize` requests, this endpoint will become unresponsive -> will hang forever...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: /tokenize hangs after large request bug ### Your current environment n/a ### 🐛 Describe the bug running vllm using `vllm/vllm-openai:v0.15.0` + `QuantTrio/Qwen3-235B-A22B-Instruct-2507-AWQ` after calling large nu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
