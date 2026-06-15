# vllm-project/vllm#37073: [Feature]:

| 字段 | 值 |
| --- | --- |
| Issue | [#37073](https://github.com/vllm-project/vllm/issues/37073) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello, Recent research on reasoning metrics such as Deep-Thinking Ratio (DTR) and related work (e.g. https://arxiv.org/abs/2602.13517 and https://arxiv.org/abs/2603.10165) shows that intermediate transformer activations contain useful signals about reasoning quality during generation. These signals can be used for: • reasoning metrics (e.g. DTR) • candidate pruning in multi-sample reasoning • inference-time compute allocation • router calibration • model interpretability Currently most optimized inference frameworks only return the final logits or tokens, which makes it impossible to compute these metrics. It would be very helpful if the framework supported an optional debugging/research mode that exposes intermediate layer outputs during generation. For example: generate( prompt, return_hidden_states=True, layers=[4,8,12,16] ) or generate( prompt, return_layer_logits=True ) This mode could be: • disabled by default • restricted to batch size = 1 • limited to selected layers • marked as a research/debug feature Providing this capability would enable experimentation with reasoning metrics without requiring users to reimplement the entire infe...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ture request ### 🚀 The feature, motivation and pitch Hello, Recent research on reasoning metrics such as Deep-Thinking Ratio (DTR) and related work (e.g. https://arxiv.org/abs/2602.13517 and https://arxiv.org/abs/2603.1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ple reasoning • inference-time compute allocation • router calibration • model interpretability Currently most optimized inference frameworks only return the final logits or tokens, which makes it impossible to compute...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: pruning in multi-sample reasoning • inference-time compute allocation • router calibration • model interpretability Currently most optimized inference frameworks only return the final logits or tokens, which makes it im...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: feature request ### 🚀 The feature, motivation and pitch Hello, Recent research on reasoning metrics such as Deep-Thinking Ratio (DTR) and related work (e.g. https://arxiv.org/abs/2602.13517 and https://arxiv....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
