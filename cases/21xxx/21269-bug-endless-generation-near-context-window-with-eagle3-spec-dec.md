# vllm-project/vllm#21269: [Bug]: Endless Generation near Context Window with Eagle3/Spec Dec

| 字段 | 值 |
| --- | --- |
| Issue | [#21269](https://github.com/vllm-project/vllm/issues/21269) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Endless Generation near Context Window with Eagle3/Spec Dec

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We recently tried to enable the recently merged eagle3, and all seemed well at a first glance. However, occasionally if you chat at lengths near the max context window of the draft model, the model loses coherence and generates until the output limit hits. This does not occur if spec dec is disabled. We think that this behavior has been persistent for months (previously it used to outright crash the vLLM engine, but patch in April made max_new_tokens effective in avoiding this). cc @zixi-qi @morgendave **vLLM Config:** **vLLM Logs (We hit our max_new_tokens limit):** **Strange output:** We used to have infinite generations very occasionally with scout itself as well, but this was fixed with presence penalty set to something higher than 0.0. I'm aware that draft models do not respect any filter except for temperature; if this gets fixed by that eventual change then that works too. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sionally if you chat at lengths near the max context window of the draft model, the model loses coherence and generates until the output limit hits. This does not occur if spec dec is disabled. We think that this behavi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Endless Generation near Context Window with Eagle3/Spec Dec bug;stale ### Your current environment ### 🐛 Describe the bug We recently tried to enable the recently merged eagle3, and all seemed well at a first gla...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: oo. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
