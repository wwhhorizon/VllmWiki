# vllm-project/vllm#8902: [Feature]: Guided Decoding Schema Cache Store

| 字段 | 值 |
| --- | --- |
| Issue | [#8902](https://github.com/vllm-project/vllm/issues/8902) |
| 状态 | closed |
| 标签 | feature request;structured-output;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Guided Decoding Schema Cache Store

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # Problem I am currently working with structured outputs and experimented a little with VLLM + Outlines. Since our JSON Schemas can get quite complex the generation of the FSM can take around 2 Minutes per Schema. It would be great to have a feature where you can provide a Schema-Store to save your generated schemas over time in a local file and reload them when you restart your deployment. Ideally this would be implemented as flag in the vllm serve arguments: https://docs.vllm.ai/en/latest/models/engine_args.html # Current Implementation I assume that this is currently not supported and the code to not recompute the schema is handled with the @cache() decorator here: ![Screenshot 2024-09-27 134948](https://github.com/user-attachments/assets/4d6480a8-5a79-40ab-8b5c-6023b0551233) ### Alternatives Alternative solution would probably be to create custom python code to handle this for my use-case and use the VLLM python functions for generation instead of the "VLLM serve" command. However not sure how you could handle this with the API Deployment. ### Additional context PS: Happy to contribute to this feature if this is something that can be use...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nes. Since our JSON Schemas can get quite complex the generation of the FSM can take around 2 Minutes per Schema. It would be great to have a feature where you can provide a Schema-Store to save your generated schemas o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Guided Decoding Schema Cache Store feature request;structured-output;stale ### 🚀 The feature, motivation and pitch # Problem I am currently working with structured outputs and experimented a little with VLLM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ted as flag in the vllm serve arguments: https://docs.vllm.ai/en/latest/models/engine_args.html # Current Implementation I assume that this is currently not supported and the code to not recompute the schema is handled...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: lemented as flag in the vllm serve arguments: https://docs.vllm.ai/en/latest/models/engine_args.html # Current Implementation I assume that this is currently not supported and the code to not recompute the schema is han...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
