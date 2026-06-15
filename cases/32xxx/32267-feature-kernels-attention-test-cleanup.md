# vllm-project/vllm#32267: [Feature]: Kernels Attention Test cleanup

| 字段 | 值 |
| --- | --- |
| Issue | [#32267](https://github.com/vllm-project/vllm/issues/32267) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Kernels Attention Test cleanup

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Kernels Attention Test should test purely the attention kernels themselves, not higher-level functionality in the `Attention` objects, etc. Right now, tests like `test_num_heads_not_divisble_by_num_kv_heads` and `test_mha_attn.py` don't follow this rule, which means that we must include `vllm/model_executor/layers/attention` as a source dependency in CI for proper coverage, when this shouldn't really be necessary if we're purely testing kernels. Resolving this will make CI more efficient. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: that we must include `vllm/model_executor/layers/attention` as a source dependency in CI for proper coverage, when this shouldn't really be necessary if we're purely testing kernels. Resolving this will make CI more eff...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _attn.py` don't follow this rule, which means that we must include `vllm/model_executor/layers/attention` as a source dependency in CI for proper coverage, when this shouldn't really be necessary if we're purely testing...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Kernels Attention Test cleanup feature request ### 🚀 The feature, motivation and pitch Kernels Attention Test should test purely the attention kernels themselves, not higher-level functionality in the `Attent...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: Kernels Attention Test cleanup feature request ### 🚀 The feature, motivation and pitch Kernels Attention Test should test purely the attention kernels themselves, not higher-level functionality in the `Attent...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
