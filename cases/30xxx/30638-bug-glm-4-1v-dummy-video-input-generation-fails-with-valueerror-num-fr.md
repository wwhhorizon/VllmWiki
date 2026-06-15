# vllm-project/vllm#30638: [Bug]: GLM-4.1V dummy video input generation fails with ValueError (num_frames=1 < temporal_factor=2)

| 字段 | 值 |
| --- | --- |
| Issue | [#30638](https://github.com/vllm-project/vllm/issues/30638) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-4.1V dummy video input generation fails with ValueError (num_frames=1 < temporal_factor=2)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When initializing GLM-4.1V with vLLM (even for text-only/image-only inference), the engine core fails to start due to a **constraint mismatch in dummy video input generation**: 1. vLLM automatically generates dummy video inputs during encoder budget calculation (even when no video is provided by the user). 2. The fallback logic in `get_num_frames_with_most_features` sets `num_frames=1` (minimum value) when video token allocation is insufficient. 3. GLM-4.1V's `smart_resize` function enforces a strict constraint: `num_frames > temporal_factor=2` (not `>=`), triggering a ValueError. 4. This leads to fatal engine core initialization failure, blocking all inference for GLM-4.1V. #### Key Context - The error occurs **before any user prompts are processed** (during engine initialization). - No explicit video input is provided—this is an internal vLLM dummy input generation issue. #### Minimal reproducible example ```python3 from vllm import LLM, SamplingParams import os # Initialize GLM-4.1V (triggers dummy video input generation) llm = LLM( model="THUDM/glm-4.1v", tensor_parallel_size=2, dtype="bfloat16", enforce_eager=True, max_model...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: itialize GLM-4.1V (triggers dummy video input generation) llm = LLM( model="THUDM/glm-4.1v", tensor_parallel_size=2, dtype="bfloat16", enforce_eager=True, max_model_len=4096, disable_custom_all_reduce=True, # NPU-specif...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: llm = LLM( model="THUDM/glm-4.1v", tensor_parallel_size=2, dtype="bfloat16", enforce_eager=True, max_model_len=4096, disable_custom_all_reduce=True, # NPU-specific ) sampling_params = SamplingParams( temperature=0.0, ma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: generation fails with ValueError (num_frames=1 < temporal_factor=2) bug;stale ### Your current environment ### 🐛 Describe the bug When initializing GLM-4.1V with vLLM (even for text-only/image-only inference), the engin...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ge-only inference), the engine core fails to start due to a **constraint mismatch in dummy video input generation**: 1. vLLM automatically generates dummy video inputs during encoder budget calculation (even when no vid...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ets `num_frames=1` (minimum value) when video token allocation is insufficient. 3. GLM-4.1V's `smart_resize` function enforces a strict constraint: `num_frames > temporal_factor=2` (not `>=`), triggering a ValueError. 4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
