# vllm-project/vllm#28152: [Feature]: Factor out `zero_expert_num` from `FusedMoE`

| 字段 | 值 |
| --- | --- |
| Issue | [#28152](https://github.com/vllm-project/vllm/issues/28152) |
| 状态 | closed |
| 标签 | help wanted;feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Factor out `zero_expert_num` from `FusedMoE`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We have many special cases in `FusedMoE` for `zero_expert_num` This parameter is used exclusively for `LongCatFlash`. We should factor this out of `FusedMoe` and put the complexity into the model file. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: Factor out `zero_expert_num` from `FusedMoE` help wanted;feature request ### 🚀 The feature, motivation and pitch We have many special cases in `FusedMoE` for `zero_expert_num` This parameter is used exclusive...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: feature request ### 🚀 The feature, motivation and pitch We have many special cases in `FusedMoE` for `zero_expert_num` This parameter is used exclusively for `LongCatFlash`. We should factor this out of `FusedMoe` and p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: We should factor this out of `FusedMoe` and put the complexity into the model file. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already se...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ature]: Factor out `zero_expert_num` from `FusedMoE` help wanted;feature request ### 🚀 The feature, motivation and pitch We have many special cases in `FusedMoE` for `zero_expert_num` This parameter is used exclusively...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
