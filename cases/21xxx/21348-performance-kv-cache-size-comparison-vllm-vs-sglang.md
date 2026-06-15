# vllm-project/vllm#21348: [Performance]: KV Cache Size Comparison vLLM vs SGLang

| 字段 | 值 |
| --- | --- |
| Issue | [#21348](https://github.com/vllm-project/vllm/issues/21348) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: KV Cache Size Comparison vLLM vs SGLang

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Hi team! I was running some experiments and launched `Qwen3-235B-A22B-FP8` on both vLLM and SGLang on 4xH100 GPUs. On vLLM is see these logs about KV Cache: ``` Available KV cache memory: 8.11 GiB GPU KV cache size: 178,880 tokens ``` For SGLang is saw this: ``` KV Cache is allocated. #tokens: 367404, K size: 8.23 GB, V size: 8.23 GB ``` Seems like the KV Cache memory is almost **2x** for SGLang compared to vLLM. Does anybody know why? Commands used to launch vLLM: ``` CUDA_VISIBLE_DEVICES=0,1,2,3 \ vllm serve /path/to/Qwen3-235B-A22B-FP8 \ --tensor-parallel-size 4 \ --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"}' ``` Commands used to launch SGLang: ``` python3 -m sglang.launch_server --model /path/to/Qwen3-235B-A22B-FP8 --tp 4 --trust-remote-code --host 0.0.0.0 --port 8000 --mem-fraction-static 0.93 ``` ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom ri...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: eriments and launched `Qwen3-235B-A22B-FP8` on both vLLM and SGLang on 4xH100 GPUs. On vLLM is see these logs about KV Cache: ``` Available KV cache memory: 8.11 GiB GPU KV cache size: 178,880 tokens ``` For SGLang is s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rmance regression Hi team! I was running some experiments and launched `Qwen3-235B-A22B-FP8` on both vLLM and SGLang on 4xH100 GPUs. On vLLM is see these logs about KV Cache: ``` Available KV cache memory: 8.11 GiB GPU...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression Hi team! I was running some experiments and launched `Qwen3-235B-A22B-FP8` on both vLLM and SGLang on 4xH100 GPUs. On vLLM is see these l...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: n Hi team! I was running some experiments and launched `Qwen3-235B-A22B-FP8` on both vLLM and SGLang on 4xH100 GPUs. On vLLM is see these logs about KV Cache: ``` Available KV cache memory: 8.11 GiB GPU KV cache size: 1...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Performance]: KV Cache Size Comparison vLLM vs SGLang performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Hi team! I was running some experiments and launched `Qwen3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
