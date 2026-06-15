# vllm-project/vllm#1935: 2080ti 22G *2, In WSL2, benchmarks test, orca-2-13B-AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#1935](https://github.com/vllm-project/vllm/issues/1935) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 2080ti 22G *2, In WSL2, benchmarks test, orca-2-13B-AWQ

### Issue 正文摘录

(llm) root@DESKTOP-1CSPSTT:~/vllm-main/benchmarks# python benchmark_serving.py --tokenizer /mnt/e/Code/text-generation-webui/models/orca-2-13B-AWQ --dataset ShareGPT_V3_unfiltered_cleaned_split.json --num-prompts 800 --request-rate 8 Namespace(backend='vllm', host='localhost', port=8000, dataset='ShareGPT_V3_unfiltered_cleaned_split.json', tokenizer='/mnt/e/Code/text-generation-webui/models/orca-2-13B-AWQ', best_of=1, use_beam_search=False, num_prompts=800, request_rate=8.0, seed=0, trust_remote_code=False) Token indices sequence length is longer than the specified maximum sequence length for this model (5924 > 4096). Running this sequence through the model will result in indexing errors 2 gpu(no nvlink): Total time: 670.81 s Throughput: 1.19 requests/s Average latency: 281.92 s Average latency per token: 1.03 s Average latency per output token: 5.69 s gpu 0(pcie16 *3.0 * 16): Total time: 777.56 s Throughput: 1.03 requests/s Average latency: 334.56 s Average latency per token: 1.33 s Average latency per output token: 7.89 s gpu 1(pcie16 *3.0 * 4): Total time: 774.99 s Throughput: 1.03 requests/s Average latency: 334.06 s Average latency per token: 1.32 s Average latency per output...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: 2080ti 22G *2, In WSL2, benchmarks test, orca-2-13B-AWQ (llm) root@DESKTOP-1CSPSTT:~/vllm-main/benchmarks# python benchmark_serving.py --tokenizer /mnt/e/Code/text-generation-webui/models/orca-2-13B-AWQ --dataset ShareG...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t_remote_code=False) Token indices sequence length is longer than the specified maximum sequence length for this model (5924 > 4096). Running this sequence through the model will result in indexing errors 2 gpu(no nvlin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: filtered_cleaned_split.json --num-prompts 800 --request-rate 8 Namespace(backend='vllm', host='localhost', port=8000, dataset='ShareGPT_V3_unfiltered_cleaned_split.json', tokenizer='/mnt/e/Code/text-generation-webui/mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Code/text-generation-webui/models/orca-2-13B-AWQ', best_of=1, use_beam_search=False, num_prompts=800, request_rate=8.0, seed=0, trust_remote_code=False) Token indices sequence length is longer than the specified maximum...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: xt-generation-webui/models/orca-2-13B-AWQ', best_of=1, use_beam_search=False, num_prompts=800, request_rate=8.0, seed=0, trust_remote_code=False) Token indices sequence length is longer than the specified maximum sequen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
