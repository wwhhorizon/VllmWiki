# vllm-project/vllm#30919: [Bug]: GPT-OSS-120B NotImplementedError: FlashInfer backend currently does not support attention sinks

| 字段 | 值 |
| --- | --- |
| Issue | [#30919](https://github.com/vllm-project/vllm/issues/30919) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPT-OSS-120B NotImplementedError: FlashInfer backend currently does not support attention sinks

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Use B200 machine but vLLM currently has functional issue. Error log please see below. This functional issue is caused by https://github.com/vllm-project/vllm/pull/30842. Repro command export VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8087 --model openai/gpt-oss-120b --tokenizer openai/gpt-oss-120b --dtype auto --kv-cache-dtype fp8 --tensor-parallel-size 8 --pipeline-parallel-size 1 --data-parallel-size 1 --swap-space 16 --max-num-seqs 1024 --trust-remote-code --max-model-len 2058 --gpu-memory-utilization 0.9 --max-num-batched-tokens 8192 --no-enable-prefix-caching --async-scheduling --stream-interval 20 --compilation_config.pass_config.fuse_allreduce_rms true --compilation_config.pass_config.eliminate_noops true --compilation_config.max_cudagraph_capture_size 2048 error message: (Worker_TP0 pid=829034) INFO 12-17 18:48:07 [backends.py:278] Compiling a graph for compile range (183, 8192) takes 3.09 s (Worker_TP0 pid=829034) INFO 12-17 18:48:08 [gpu_worker.py:375] Available KV cache memory: 140.97 GiB (EngineCore_DP0 pid=828900) INFO 12-17 18:48:08 [kv_cache_utils.py:12...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: m-project/vllm/pull/30842. Repro command export VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8087 --model openai/gpt-oss-120b --tokenizer openai/gpt-oss-120b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: s bug;stale ### Your current environment ### 🐛 Describe the bug Use B200 machine but vLLM currently has functional issue. Error log please see below. This functional issue is caused by https://github.com/vllm-project/vl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: GPT-OSS-120B NotImplementedError: FlashInfer backend currently does not support attention sinks bug;stale ### Your current environment ### 🐛 Describe the bug Use B200 machine but vLLM currently has functional iss...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GPT-OSS-120B NotImplementedError: FlashInfer backend currently does not support attention sinks bug;stale ### Your current environment ### 🐛 Describe the bug Use B200 machine but vLLM currently has functional iss...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: pid=829034) INFO 12-17 18:48:07 [backends.py:278] Compiling a graph for compile range (183, 8192) takes 3.09 s (Worker_TP0 pid=829034) INFO 12-17 18:48:08 [gpu_worker.py:375] Available KV cache memory: 140.97 GiB (Engin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
