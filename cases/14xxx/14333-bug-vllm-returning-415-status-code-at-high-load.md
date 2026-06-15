# vllm-project/vllm#14333: [Bug]: vLLM returning 415 status code at high load

| 字段 | 值 |
| --- | --- |
| Issue | [#14333](https://github.com/vllm-project/vllm/issues/14333) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cache;fp8;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM returning 415 status code at high load

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are running `neuralmagic/Llama-3.3-70B-Instruct-quantized.w8a8` on `2 x H100 80 GB` vLLM openai image tag: `v0.7.3` Docker Args ``` --host 0.0.0.0 --port 8000 --disable-log-requests --download-dir /data/ --tokenizer-mode auto --model neuralmagic/Llama-3.3-70B-Instruct-quantized.w8a8 --tokenizer neuralmagic/Llama-3.3-70B-Instruct-quantized.w8a8 --trust-remote-code --dtype auto --tensor-parallel-size 2 --gpu-memory-utilization 0.99 --served-model-name llm --max-model-len 20000 --enforce-eager --kv-cache-dtype fp8 --max-num-seqs 16 ``` When running a load test (input = 16000 tokens, output = 256 tokens), as load increases at some point vLLM starts returning 415 for most of the requests ``` INFO 03-05 22:52:30 metrics.py:455] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 174.9 tokens/s, Running: 6 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 16.9%, CPU KV cache usage: 0.0%. INFO 03-05 22:52:35 metrics.py:455] Avg prompt throughput: 7901.7 tokens/s, Avg generation throughput: 9.2 tokens/s, Running: 9 reqs, Swapped: 0 reqs, Pending: 7 reqs, GPU KV cache usage: 25.2%, CPU KV cache usage: 0.0%. INFO 03...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ct-quantized.w8a8` on `2 x H100 80 GB` vLLM openai image tag: `v0.7.3` Docker Args ``` --host 0.0.0.0 --port 8000 --disable-log-requests --download-dir /data/ --tokenizer-mode auto --model neuralmagic/Llama-3.3-70B-Inst...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: # 🐛 Describe the bug We are running `neuralmagic/Llama-3.3-70B-Instruct-quantized.w8a8` on `2 x H100 80 GB` vLLM openai image tag: `v0.7.3` Docker Args ``` --host 0.0.0.0 --port 8000 --disable-log-requests --download-di...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: are running `neuralmagic/Llama-3.3-70B-Instruct-quantized.w8a8` on `2 x H100 80 GB` vLLM openai image tag: `v0.7.3` Docker Args ``` --host 0.0.0.0 --port 8000 --disable-log-requests --download-dir /data/ --tokenizer-mod...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ion 0.99 --served-model-name llm --max-model-len 20000 --enforce-eager --kv-cache-dtype fp8 --max-num-seqs 16 ``` When running a load test (input = 16000 tokens, output = 256 tokens), as load increases at some point vLL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rent environment ### 🐛 Describe the bug We are running `neuralmagic/Llama-3.3-70B-Instruct-quantized.w8a8` on `2 x H100 80 GB` vLLM openai image tag: `v0.7.3` Docker Args ``` --host 0.0.0.0 --port 8000 --disable-log-req...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
