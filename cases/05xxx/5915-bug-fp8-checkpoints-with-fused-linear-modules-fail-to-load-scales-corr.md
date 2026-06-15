# vllm-project/vllm#5915: [Bug]: FP8 checkpoints with fused linear modules fail to load scales correctly

| 字段 | 值 |
| --- | --- |
| Issue | [#5915](https://github.com/vllm-project/vllm/issues/5915) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: FP8 checkpoints with fused linear modules fail to load scales correctly

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Description: When loading FP8 quantized models with merged linear modules (e.g., Phi-3 with merged qkv_proj and up_gate_proj), the scales for each shard are not handled correctly. This occurs because the vLLM FP8 config assumes separate scales for each shard, but merged layers have a single scale. Steps to Reproduce: 1. Attempt to load an FP8 quantized Phi-3 model (e.g., https://huggingface.co/nm-testing/Phi-3-mini-128k-instruct-FP8) 2. Observe error due to shape mismatch: ``` param_data.shape=torch.Size([2]) loaded_weight.shape=torch.Size([]) param_data.shape=torch.Size([3]) loaded_weight.shape=torch.Size([]) ``` Expected Behavior: Scales should be correctly loaded for merged linear modules in FP8 checkpoints. Proposed Fix: Modify `process_weights_after_loading` in MergedColumnParallelLinear and QKVParallelLinear to repeat the merged scale during weight loading. Temporary Workaround: Apply the following patch in `vllm/model_executor/layers/linear.py`: ```python - assert param_data.shape == loaded_weight.shape - param_data.copy_(loaded_weight) + temp = loaded_weight.repeat(param_d...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FP8 checkpoints with fused linear modules fail to load scales correctly bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Description: When loading FP8 quan...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: py` ``` ### 🐛 Describe the bug Description: When loading FP8 quantized models with merged linear modules (e.g., Phi-3 with merged qkv_proj and up_gate_proj), the scales for each shard are not handled correctly. This occ...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: scales for each shard, but merged layers have a single scale. Steps to Reproduce: 1. Attempt to load an FP8 quantized Phi-3 model (e.g., https://huggingface.co/nm-testing/Phi-3-mini-128k-instruct-FP8) 2. Observe error d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nm-testing/Phi-3-mini-128k-instruct-FP8) 2. Observe error due to shape mismatch: ``` param_data.shape=torch.Size([2]) loaded_weight.shape=torch.Size([]) param_data.shape=torch.Size([3]) loaded_weight.shape=torch.Size([]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: pt to load an FP8 quantized Phi-3 model (e.g., https://huggingface.co/nm-testing/Phi-3-mini-128k-instruct-FP8) 2. Observe error due to shape mismatch: ``` param_data.shape=torch.Size([2]) loaded_weight.shape=torch.Size(...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
