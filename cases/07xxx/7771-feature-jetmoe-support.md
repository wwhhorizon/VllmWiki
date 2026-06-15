# vllm-project/vllm#7771: [Feature]: `JetMoE` support

| 字段 | 值 |
| --- | --- |
| Issue | [#7771](https://github.com/vllm-project/vllm/issues/7771) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: `JetMoE` support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, I'm doing research for various MoE model architectures. And I found out that `JetMoE` architecture is promising for following reasons: 1. Inference efficiency: With only 2.2B active parameters and low training budgets, it surpasses the performance of llama2 model of similar sizes. 2. Potential of jetmoe: Only a single experiment was conducted in the JetMoE paper so that performance upper bound of this architectured models would be greater. 3. Unique architecture: Mixture-of-Attentions (MoA) is supported in this model. 4. Huggingface integrated: HF already supports this architecture! references: - https://github.com/myshell-ai/JetMoE/tree/main - https://huggingface.co/docs/transformers/model_doc/jetmoe ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: he feature, motivation and pitch Hi, I'm doing research for various MoE model architectures. And I found out that `JetMoE` architecture is promising for following reasons: 1. Inference efficiency: With only 2.2B active...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: `JetMoE` support feature request;stale ### 🚀 The feature, motivation and pitch Hi, I'm doing research for various MoE model architectures. And I found out that `JetMoE` architecture is promising for following...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: etMoE` architecture is promising for following reasons: 1. Inference efficiency: With only 2.2B active parameters and low training budgets, it surpasses the performance of llama2 model of similar sizes. 2. Potential of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: request;stale ### 🚀 The feature, motivation and pitch Hi, I'm doing research for various MoE model architectures. And I found out that `JetMoE` architecture is promising for following reasons: 1. Inference efficiency: W...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: `JetMoE` support feature request;stale ### 🚀 The feature, motivation and pitch Hi, I'm doing research for various MoE model architectures. And I found out that `JetMoE` architecture is promising for following...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
