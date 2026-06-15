# vllm-project/vllm#35828: [Bug]: Qwen3-Next accuracy regression on AMD

| 字段 | 值 |
| --- | --- |
| Issue | [#35828](https://github.com/vllm-project/vllm/issues/35828) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next accuracy regression on AMD

### Issue 正文摘录

### Your current environment Tested with Mi300x ### 🐛 Describe the bug GSM8k is ~50% on AMD now. Should be ~85% ``` CUDA_VISIBLE_DEVICES=2 VLLM_ROCM_USE_AITER=1 VLLM_ROCM_USE_AITER_MHA=1 VLLM_ROCM_USE_AITER_LINEAR=0 VLLM_ROCM_USE_AITER_RMSNORM=0 VLLM_GPU_MEMORY_UTILIZATION=0.95 lm_eval --model vllm --model_args pretrained=$HOME/hf_models/Qwen/Qwen3-Next-80B-A3B-Instruct,max_model_len=8096 --tasks gsm8k --batch_size auto |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.4920|± |0.0138| | | |strict-match | 5|exact_match|↑ |0.2532|± |0.0120| ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Qwen3-Next accuracy regression on AMD bug;rocm ### Your current environment Tested with Mi300x ### 🐛 Describe the bug GSM8k is ~50% on AMD now. Should be ~85% ``` CUDA_VISIBLE_DEVICES=2 VLLM_ROCM_USE_AITER=1 VLLM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Qwen3-Next accuracy regression on AMD bug;rocm ### Your current environment Tested with Mi300x ### 🐛 Describe the bug GSM8k is ~50% on AMD now. Should be ~85% ``` CUDA_VISIBLE_DEVICES=2 VLLM_ROCM_USE_AITER=1 VLLM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Next accuracy regression on AMD bug;rocm ### Your current environment Tested with Mi300x ### 🐛 Describe the bug GSM8k is ~50% on AMD now. Should be ~85% ``` CUDA_VISIBLE_DEVICES=2 VLLM_ROCM_USE_AITER=1 VLLM...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ~50% on AMD now. Should be ~85% ``` CUDA_VISIBLE_DEVICES=2 VLLM_ROCM_USE_AITER=1 VLLM_ROCM_USE_AITER_MHA=1 VLLM_ROCM_USE_AITER_LINEAR=0 VLLM_ROCM_USE_AITER_RMSNORM=0 VLLM_GPU_MEMORY_UTILIZATION=0.95 lm_eval --model vllm...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Qwen3-Next accuracy regression on AMD bug;rocm ### Your current environment Tested with Mi300x ### 🐛 Describe the bug GSM8k is ~50% on AMD now. Should be ~85% ``` CUDA_VISIBLE_DEVICES=2 VLLM_ROCM_USE_AITER=1 VLLM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
