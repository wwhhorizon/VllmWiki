# vllm-project/vllm#20468: [Feature]: Support EPLB for More MoE Models, e.g. Qwen 3, Llama 4

| 字段 | 值 |
| --- | --- |
| Issue | [#20468](https://github.com/vllm-project/vllm/issues/20468) |
| 状态 | closed |
| 标签 | good first issue;feature request;stale |
| 评论 | 32; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support EPLB for More MoE Models, e.g. Qwen 3, Llama 4

### Issue 正文摘录

### 🚀 The feature, motivation and pitch 🎉 **#18343 introduces dynamic Expert Parallelism Load Balancing (EPLB)** for DeepSeek-V2/V3/R1 models. As MoE (Mixture-of-Experts) models become more common, we’d love help extending EPLB support to other MoE models—such as Qwen3, Llama 4, and more. This is a great **first good issue** for anyone interested in model internals or systems work. #18343 was built with generality in mind, so extending it to other models or quantization methods should be relatively straightforward. --- ### ✅ How to add support for a new model Implement the `MixtureOfExperts` protocol. Specifically, you’ll need to: - Expose relevant MoE configuration flags. - Provide access to expert weights for EPLB to rearrange. - Forward EPLB-related arguments into the `FusedMoE` layer. 📌 **Note on weight loading:** For models with **redundant experts**, you’ll need to carefully adjust the weight loading logic. `FusedMoE` returns an `expert_params_mapping` that reflects expert duplication, but you may need to modify the model class to ensure correct loading behavior. 🔎 Example: See how it’s done in [`deepseek_v2.py`](https://github.com/vllm-project/vllm/pull/18343/files#diff-420...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Support EPLB for More MoE Models, e.g. Qwen 3, Llama 4 good first issue;feature request;stale ### 🚀 The feature, motivation and pitch 🎉 **#18343 introduces dynamic Expert Parallelism Load Balancing (EPLB)** f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: EPLB for More MoE Models, e.g. Qwen 3, Llama 4 good first issue;feature request;stale ### 🚀 The feature, motivation and pitch 🎉 **#18343 introduces dynamic Expert Parallelism Load Balancing (EPLB)** for DeepSeek-V2/V3/R...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 43 was built with generality in mind, so extending it to other models or quantization methods should be relatively straightforward. --- ### ✅ How to add support for a new model Implement the `MixtureOfExperts` protocol....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ure, motivation and pitch 🎉 **#18343 introduces dynamic Expert Parallelism Load Balancing (EPLB)** for DeepSeek-V2/V3/R1 models. As MoE (Mixture-of-Experts) models become more common, we’d love help extending EPLB suppo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: Support EPLB for More MoE Models, e.g. Qwen 3, Llama 4 good first issue;feature request;stale ### 🚀 The feature, motivation and pitch 🎉 **#18343 introduces dynamic Expert Parallelism Load Balancing (EPLB)** f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
