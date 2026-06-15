# vllm-project/vllm#21475: [RFC]: vLLM vs HuggingFace numerical parity report

| 字段 | 值 |
| --- | --- |
| Issue | [#21475](https://github.com/vllm-project/vllm/issues/21475) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: vLLM vs HuggingFace numerical parity report

### Issue 正文摘录

### Motivation. There have been various [reports](https://x.com/finbarrtimbers/status/1941184677047566548) of numerical discrepancy between vLLM and RL trainers or HuggingFace. We ran numerical benchmark on four open weights models, both dense and MoE, and would like to share some findings. Feedback is welcomed! ### Models tested - Qwen/Qwen3-0.6B - meta-llama/Llama-3.1-8B - google/gemma-3-1b-it - microsoft/Phi-tiny-MoE-instruct ### Results and next steps - Logprobs discrepancy can be found in all 4 models, with max relative error ranging 24%~170% - Relative error for raw logits is small (1~2%) for the 3 dense models, indicating discrepancy arising from (or widen by) logprobs calculation process - Raw logits error is 13% for the Phi MoE model We need to dig deeper into logprobs calculation, which looks simple. Another theory is the small 1~2% logits error is widened by `logsoftmax` - this needs a mathematical verification and/or a ablation study. Note: we use `transformers` eager mode (https://github.com/huggingface/transformers/issues/39565) as the baseline. To reproduce the report, checkout #21286 and run `DISABLE_KERNEL_MAPPING=1 python tools/numerics/benchmark_logprobs.py --gp...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [RFC]: vLLM vs HuggingFace numerical parity report RFC;stale ### Motivation. There have been various [reports](https://x.com/finbarrtimbers/status/1941184677047566548) of numerical discrepancy between vLLM and RL traine...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: [RFC]: vLLM vs HuggingFace numerical parity report RFC;stale ### Motivation. There have been various [reports](https://x.com/finbarrtimbers/status/1941184677047566548) of numerical discrepancy between vLLM and RL traine...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: h max relative error ranging 24%~170% - Relative error for raw logits is small (1~2%) for the 3 dense models, indicating discrepancy arising from (or widen by) logprobs calculation process - Raw logits error is 13% for...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: . We ran numerical benchmark on four open weights models, both dense and MoE, and would like to share some findings. Feedback is welcomed! ### Models tested - Qwen/Qwen3-0.6B - meta-llama/Llama-3.1-8B - google/gemma-3-1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: iscrepancy between vLLM and RL trainers or HuggingFace. We ran numerical benchmark on four open weights models, both dense and MoE, and would like to share some findings. Feedback is welcomed! ### Models tested - Qwen/Q...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
