# vllm-project/vllm#40682: [Bug]:  Prefix caching causes AssertionError for pooling models (embedding models) with empty kv_cache_groups

| 字段 | 值 |
| --- | --- |
| Issue | [#40682](https://github.com/vllm-project/vllm/issues/40682) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  Prefix caching causes AssertionError for pooling models (embedding models) with empty kv_cache_groups

### Issue 正文摘录

### Your current environment python3 -m vllm.entrypoints.openai.api_server --model bge-m3 \ --trust-remote-code \ --served-model-name embed \ --enable-prefix-caching \ --gpu-memory-utilization 0.9 \ --max-model-len 8192 \ --convert embed \ --dtype=bfloat16 \ --enforce-eager \ --max_num_seqs $BATCH_SIZE ```text Your output of `python collect_env.py` here ``` When launching a pooling model (such as BGE-M3 embedding model) with --enable-prefix-caching flag enabled, the following error occurs: AssertionError: HybridKVCacheCoordinator requires at least two attention groups. ### 🐛 Describe the bug Complete Stack Trace File "/path/to/vllm/v1/core/kv_cache_coordinator.py", line 434, in verify_and_split_kv_cache_groups assert len(attention_groups) > 1, ( "HybridKVCacheCoordinator requires at least two attention groups." ) AssertionError: HybridKVCacheCoordinator requires at least two attention groups. Reproduction Steps 1. Start vLLM API server with a pooling model and prefix caching enabled: python3 -m vllm.entrypoints.openai.api_server \ --model bge-m3 \ --enable-prefix-caching \ --trust-remote-code 2. Observe the pooling model's KVCacheConfig: KVCacheConfig(num_blocks=1, kv_cache_tensor...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: embed \ --dtype=bfloat16 \ --enforce-eager \ --max_num_seqs $BATCH_
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Prefix caching causes AssertionError for pooling models (embedding models) with empty kv_cache_groups bug ### Your current environment python3 -m vllm.entrypoints.openai.api_server --model bge-m3 \ --trust-remote...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ere ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ode 2. Observe the pooling model's KVCacheConfig: KVCacheConfig(num_blocks=1, kv_cache_tensors=[], kv_cache_groups=[]) 3. Error is raised Root Cause The coordinator selection logic in get_kv_cache_coordinator() function...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
