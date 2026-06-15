# vllm-project/vllm#25689: [Feature]: Enabling performance optimizations by default

| 字段 | 值 |
| --- | --- |
| Issue | [#25689](https://github.com/vllm-project/vllm/issues/25689) |
| 状态 | open |
| 标签 | feature request;torch.compile;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enabling performance optimizations by default

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In vLLM, achieving the best performance often requires many additional CLI/config flags. We should instead enable the best behavior by default where we can. For example, look at the [Blackwell recipe for LLaMa 3](https://github.com/vllm-project/recipes/blob/main/Llama/Llama3.3_Blackwell.yaml): ``` kv-cache-dtype: fp8 compilation-config: '{"pass_config":{"enable_fi_allreduce_fusion":true,"enable_attn_fusion":true,"enable_noop":true},"custom_ops":["+quant_fp8","+rms_norm"],"cudagraph_mode":"FULL_DECODE_ONLY","splitting_ops":[]}' ``` Resolving most of these requires feature work, and some of these are only going to be available when using `torch>=2.9`. Instead of waiting for the release, we should enable relevant features now (conditional on the torch version), or as soon as they are merged. The work is tracked in [milestone](https://github.com/vllm-project/vllm/milestone/14); this just tracks changing the defaults. Features only dependent on additional work: - [x] `CUDAGraphMode`: this should already be possible, when `splitting_ops=[]`, `FULL_AND_PIECEWISE` should convert to `FULL` which should downgrade to `FULL_DECODE_ONLY` (needs verificat...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Enabling performance optimizations by default feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch In vLLM, achieving the best performance often requires many additional CLI/config flag...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: re]: Enabling performance optimizations by default feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch In vLLM, achieving the best performance often requires many additional CLI/config flags. We...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: m-project/recipes/blob/main/Llama/Llama3.3_Blackwell.yaml): ``` kv-cache-dtype: fp8 compilation-config: '{"pass_config":{"enable_fi_allreduce_fusion":true,"enable_attn_fusion":true,"enable_noop":true},"custom_ops":["+qu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ble the best behavior by default where we can. For example, look at the [Blackwell recipe for LLaMa 3](https://github.com/vllm-project/recipes/blob/main/Llama/Llama3.3_Blackwell.yaml): ``` kv-cache-dtype: fp8 compilatio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vLLM, achieving the best performance often requires many additional CLI/config flags. We should instead enable the best behavior by default where we can. For example, look at the [Blackwell recipe for LLaMa 3](https://g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
