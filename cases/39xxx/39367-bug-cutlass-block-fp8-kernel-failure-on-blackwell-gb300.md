# vllm-project/vllm#39367: [Bug]: CUTLASS block FP8 kernel failure on Blackwell GB300

| 字段 | 值 |
| --- | --- |
| Issue | [#39367](https://github.com/vllm-project/vllm/issues/39367) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;triton |
| 症状 |  |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUTLASS block FP8 kernel failure on Blackwell GB300

### Issue 正文摘录

### Your current environment Initially followed the instructions in https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#nvidia-cuda. For the patch below the vLLM was built from source. Both are 0.19.0 ### 🐛 Describe the bug `cutlass_scaled_mm_supports_block_fp8()` incorrectly reports support for Blackwell (cc=10.3, `to_int()` = 103 ≥ 100), but the kernel raises `RuntimeError: Error Internal` at runtime during the profile/dummy run. The patch forces the Triton fallback for all Blackwell devices, which works correctly. However it has a perf penalty. ``` diff --git a/vllm/model_executor/layers/quantization/utils/w8a8_utils.py b/vllm/model_executor/layers/quantization/utils/w8a8_utils.py --- a/vllm/model_executor/layers/quantization/utils/w8a8_utils.py +++ b/vllm/model_executor/layers/quantization/utils/w8a8_utils.py @@ -23,6 +23,11 @@ def cutlass_block_fp8_supported() -> bool: capability_tuple = current_platform.get_device_capability() capability = -1 if capability_tuple is None else capability_tuple.to_int() + # CUTLASS block FP8 kernels fail at runtime on Blackwell (B300, cc >= 100). + # Fall back to Triton instead. + if capability >= 100: + return False + return ops.c...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: CUTLASS block FP8 kernel failure on Blackwell GB300 bug ### Your current environment Initially followed the instructions in https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#nvidia-cuda. For the pa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUTLASS block FP8 kernel failure on Blackwell GB300 bug ### Your current environment Initially followed the instructions in https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#nvidia-cuda. For the pa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: CUTLASS block FP8 kernel failure on Blackwell GB300 bug ### Your current environment Initially followed the instructions in https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#nvidia-cuda. For the pa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: CUTLASS block FP8 kernel failure on Blackwell GB300 bug ### Your current environment Initially followed the instructions in https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#nvidia-cuda. For the pa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: h works correctly. However it has a perf penalty. ``` diff --git a/vllm/model_executor/layers/quantization/utils/w8a8_utils.py b/vllm/model_executor/layers/quantization/utils/w8a8_utils.py --- a/vllm/model_executor/laye...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
