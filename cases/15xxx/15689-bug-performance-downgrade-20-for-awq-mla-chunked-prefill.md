# vllm-project/vllm#15689: [Bug]: Performance downgrade 20% for AWQ + MLA + chunked-prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#15689](https://github.com/vllm-project/vllm/issues/15689) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Performance downgrade 20% for AWQ + MLA + chunked-prefill

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug L20x2, PP=2, TP=8, AWQ, MLA+Chunked-Prefill The performance downgrade is due to https://github.com/vllm-project/vllm/pull/15492 for MLA + chunked-prefill (tested on AWQ + PP2 + TP8), where the decode TPS decreased from 390 TPS to 290 TPS. To avoid affecting the generation of the Triton kernel, I think we should handle this processing outside the `merge_attn_states_kernel` kernel. Otherwise, dynamically checking each value for infinity within the kernel might impact the execution efficiency of the generated Triton kernel. - launch ```bash python3 -m vllm.entrypoints.openai.api_server \ --model=/workspace/DeepSeek-R1-awq \ --dtype=auto \ --tokenizer-mode=auto \ --trust-remote-code \ --max-model-len 32768 \ --max-num-batched-tokens 2048 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --gpu-memory-utilization 0.90 \ --max-num-seqs 128 \ --no-enable-prefix-caching \ --enable-chunked-prefill=True \ --disable-custom-all-reduce \ --max-log-len 0 --port 6666 ``` - before https://github.com/vllm-project/vllm/pull/15492, all is well. ```bash INFO 03-28 13:16:42 [metrics.py:481] Avg prompt throughput: 0.0 tokens/s, Avg generation t...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Performance downgrade 20% for AWQ + MLA + chunked-prefill bug ### Your current environment ### 🐛 Describe the bug L20x2, PP=2, TP=8, AWQ, MLA+Chunked-Prefill The performance downgrade is due to https://github.com...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: tps://github.com/vllm-project/vllm/pull/15492 for MLA + chunked-prefill (tested on AWQ + PP2 + TP8), where the decode TPS decreased from 390 TPS to 290 TPS. To avoid affecting the generation of the Triton kernel, I thin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: reased from 390 TPS to 290 TPS. To avoid affecting the generation of the Triton kernel, I think we should handle this processing outside the `merge_attn_states_kernel` kernel. Otherwise, dynamically checking each value...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: each value for infinity within the kernel might impact the execution efficiency of the generated Triton kernel. - launch ```bash python3 -m vllm.entrypoints.openai.api_server \ --model=/workspace/DeepSeek-R1-awq \ --dty...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: enai.api_server \ --model=/workspace/DeepSeek-R1-awq \ --dtype=auto \ --tokenizer-mode=auto \ --trust-remote-code \ --max-model-len 32768 \ --max-num-batched-tokens 2048 \ --tensor-parallel-size 8 \ --pipeline-parallel-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
