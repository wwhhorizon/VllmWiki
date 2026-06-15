# vllm-project/vllm#37758: [Bug]: FLASHINFER_CUTLASS and FLASHINFER_TRTLLM do not work for Qwen3.5 Bf16 DP/EP

| 字段 | 值 |
| --- | --- |
| Issue | [#37758](https://github.com/vllm-project/vllm/issues/37758) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: FLASHINFER_CUTLASS and FLASHINFER_TRTLLM do not work for Qwen3.5 Bf16 DP/EP

### Issue 正文摘录

### Your current environment b200, main ### 🐛 Describe the bug both of these fail ``` VLLM_USE_FLASHINFER_MOE_FP16=1 VLLM_FLASHINFER_MOE_BACKEND=latency chg run --gpus 2 -- pytest -s -v evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-qwen35-blackwell.txt VLLM_USE_FLASHINFER_MOE_FP16=1 VLLM_FLASHINFER_MOE_BACKEND=throughput chg run --gpus 2 -- pytest -s -v evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-qwen35-blackwell.txt ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: LLM do not work for Qwen3.5 Bf16 DP/EP bug ### Your current environment b200, main ### 🐛 Describe the bug both of these fail ``` VLLM_USE_FLASHINFER_MOE_FP16=1 VLLM_FLASHINFER_MOE_BACKEND=latency chg run --gpus 2 -- pyt...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ese fail ``` VLLM_USE_FLASHINFER_MOE_FP16=1 VLLM_FLASHINFER_MOE_BACKEND=latency chg run --gpus 2 -- pytest -s -v evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-qwen35-blackwell.txt VLLM_USE_FLAS...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: FLASHINFER_CUTLASS and FLASHINFER_TRTLLM do not work for Qwen3.5 Bf16 DP/EP bug ### Your current environment b200, main ### 🐛 Describe the bug both of these fail ``` VLLM_USE_FLASHINFER_MOE_FP16=1 VLLM_FLASHINFER...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: FLASHINFER_CUTLASS and FLASHINFER_TRTLLM do not work for Qwen3.5 Bf16 DP/EP bug ### Your current environment b200, main ### 🐛 Describe the bug both of these fail ``` VLLM_USE_FLASHINFER_MOE_FP16=1 VLLM_FLASHINFER...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: FLASHINFER_CUTLASS and FLASHINFER_TRTLLM do not work for Qwen3.5 Bf16 DP/EP bug ### Your current environment b200, main ### 🐛 Describe the bug both of these fail ``` VLLM_USE_FLASHINFER_MOE_FP16=1 VLLM_FLASHINFER...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
