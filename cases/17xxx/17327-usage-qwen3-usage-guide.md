# vllm-project/vllm#17327: [Usage] Qwen3 Usage Guide

| 字段 | 值 |
| --- | --- |
| Issue | [#17327](https://github.com/vllm-project/vllm/issues/17327) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 96; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage] Qwen3 Usage Guide

### Issue 正文摘录

vLLM v0.8.4 and higher natively supports all Qwen3 and Qwen3MoE models. Example command: * `vllm serve Qwen/... --enable-reasoning --reasoning-parser deepseek_r1` * All models should work with the command as above. You can test the reasoning parser with the following example script: https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_with_reasoning_streaming.py * Some MoE models might not be divisible by TP 8. Either lower your TP size or use `--enable-expert-parallel`. * If you are seeing the following error when running fp8 dense models, you are running on vLLM v0.8.4. Please upgrade to v0.8.5. ``` File ".../vllm/model_executor/parameter.py", line 149, in load_qkv_weight param_data = param_data.narrow(self.output_dim, shard_offset, IndexError: start out of range (expected to be in range of [-18, 18], but got 2048) ``` * If you are seeing the following error when running MoE models with fp8, you are running with too much tensor parallelize degree that the weights are not divisible. Consider `--tensor-parallel-size 4` or `--tensor-parallel-size 8 --enable-expert-parallel`. ``` File ".../vllm/vllm/model_executor/layers/quantization/fp8.py",...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: expert-parallel`. * If you are seeing the following error when running fp8 dense models, you are running on vLLM v0.8.4. Please upgrade to v0.8.5. ``` File ".../vllm/model_executor/parameter.py", line 149, in load_qkv_w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage] Qwen3 Usage Guide usage;stale vLLM v0.8.4 and higher natively supports all Qwen3 and Qwen3MoE models. Example command: * `vllm serve Qwen/... --enable-reasoning --reasoning-parser deepseek_r1` * All models shoul...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: usage;stale vLLM v0.8.4 and higher natively supports all Qwen3 and Qwen3MoE models. Example command: * `vllm serve Qwen/... --enable-reasoning --reasoning-parser deepseek_r1` * All models should work with the command as...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: of gate's and up's weight = 192 is not divisible by weight quantization block_n = 128. ```
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage] Qwen3 Usage Guide usage;stale vLLM v0.8.4 and higher natively supports all Qwen3 and Qwen3MoE models. Example command: * `vllm serve Qwen/... --enable-reasoning --reasoning-parser deepseek_r1` * All models shoul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
