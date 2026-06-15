# vllm-project/vllm#33097: [Feature]: Fuse FP8 output quantization into merge_attn_states (DCP / cascade paths)

| 字段 | 值 |
| --- | --- |
| Issue | [#33097](https://github.com/vllm-project/vllm/issues/33097) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Fuse FP8 output quantization into merge_attn_states (DCP / cascade paths)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When using Decode Context Parallelism (DCP) / cascade attention, vLLM currently performs the final merge of attention states (merge_attn_states) in high precision, then runs a separate quantization kernel to convert outputs to FP8. This extra kernel launch reduces fusion/latency for DCP/cascade cases. We should add fused FP8 output quantization into merge_attn_states so it can emit FP8 directly. This is a follow up of https://github.com/vllm-project/vllm/issues/29920 Proposed change: - Extend the merge_attn_states kernel to: - Accept an o_scale (output scale) and FP8 output flag/dtype parameter. - Perform merge/weighted combination using float32 accumulation (unchanged). - Quantize the merged result in-kernel to the requested FP8 format (e4m3) and write FP8 bytes directly (instead of bf16). Add a high-level switch / API so callers can request fused FP8 output (only enabled for supported platforms/configs). - Ensure fallbacks to keep current non-fused code path if device or FA version does not support FP8-output kernels. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure yo...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Feature]: Fuse FP8 output quantization into merge_attn_states (DCP / cascade paths) feature request ### 🚀 The feature, motivation and pitch When using Decode Context Parallelism (DCP) / cascade attention, vLLM currentl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: forms the final merge of attention states (merge_attn_states) in high precision, then runs a separate quantization kernel to convert outputs to FP8. This extra kernel launch reduces fusion/latency for DCP/cascade cases....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 🚀 The feature, motivation and pitch When using Decode Context Parallelism (DCP) / cascade attention, vLLM currently performs the final merge of attention states (merge_attn_states) in high precision, then runs a separat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: unchanged). - Quantize the merged result in-kernel to the requested FP8 format (e4m3) and write FP8 bytes directly (instead of bf16). Add a high-level switch / API so callers can request fused FP8 output (only enabled f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: output quantization into merge_attn_states (DCP / cascade paths) feature request ### 🚀 The feature, motivation and pitch When using Decode Context Parallelism (DCP) / cascade attention, vLLM currently performs the final...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
