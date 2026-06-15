# vllm-project/vllm#31624: [Bug]: ModelOpt Llama-4 Checkpoints Take 5+ minutes to load

| 字段 | 值 |
| --- | --- |
| Issue | [#31624](https://github.com/vllm-project/vllm/issues/31624) |
| 状态 | open |
| 标签 | bug;help wanted;good first issue;feature request |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ModelOpt Llama-4 Checkpoints Take 5+ minutes to load

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In working on some MoE refactors, I discovered that L4 for ModelOpt takes 5+minutes to load weights even from CPU page cache. - https://huggingface.co/nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 The root cause is basically this hack logic to load the state dict that ModelOpt uses - https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/llama4.py#L439-L523 [modelopt is the fused case] What happens is that the CPU tensor (loaded weight) that we are going to load into the GPU tensor (param) becomes non-contiguous due to this logic. As a result, when we eventually call `_copy()` from CPU->GPU we are calling this on a non-contiguous cpu tensor which takes 3-4s per weight. To hack around this for local R&D, I simply immediately move the loaded_weight to the GPU. This makes the gather happen on the GPU which accelerates things a lot. This isn't reasonable as an actual solution though We should investigate where the logic in the weight loader can avoid creating non-contiguous CPU tensors ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for r...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: ModelOpt Llama-4 Checkpoints Take 5+ minutes to load bug;help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch In working on some MoE refactors, I discovered that L4 for ModelOpt ta...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: e cache. - https://huggingface.co/nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 The root cause is basically this hack logic to load the state dict that ModelOpt uses - https://github.com/vllm-project/vllm/blob/main/vllm/mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: eight) that we are going to load into the GPU tensor (param) becomes non-contiguous due to this logic. As a result, when we eventually call `_copy()` from CPU->GPU we are calling this on a non-contiguous cpu tensor whic...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ture request ### 🚀 The feature, motivation and pitch In working on some MoE refactors, I discovered that L4 for ModelOpt takes 5+minutes to load weights even from CPU page cache. - https://huggingface.co/nvidia/Llama-4-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
