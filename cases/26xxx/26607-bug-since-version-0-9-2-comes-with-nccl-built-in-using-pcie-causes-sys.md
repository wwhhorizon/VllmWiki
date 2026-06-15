# vllm-project/vllm#26607: [Bug]: Since version 0.9.2 comes with nccl built-in, using PCIE causes sys errors. How to disable nccl in vllm for versions after 0.9.2?

| 字段 | 值 |
| --- | --- |
| Issue | [#26607](https://github.com/vllm-project/vllm/issues/26607) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Since version 0.9.2 comes with nccl built-in, using PCIE causes sys errors. How to disable nccl in vllm for versions after 0.9.2?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug sh 06_startVllmAPI.sh INFO 09-30 10:30:16 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=1599676) INFO 09-30 10:30:17 [api_server.py:1896] vLLM API server version 0.10.2 (APIServer pid=1599676) INFO 09-30 10:30:17 [utils.py:328] non-default args: {'port': 6006, 'model': './autodl-tmp/modelscope/models/GeoGPT/Qwen2.5-72B-GeoGPT', 'tokenizer': './autodl-tmp/modelscope/models/GeoGPT/Qwen2.5-72B-GeoGPT', 'trust_remote_code': True, 'dtype': 'bfloat16', 'served_model_name': ['Qwen2.5-72B-GeoGPT'], 'tensor_parallel_size': 8, 'gpu_memory_utilization': 0.5} (APIServer pid=1599676) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=1599676) INFO 09-30 10:30:24 [__init__.py:742] Resolved architecture: Qwen2ForCausalLM (APIServer pid=1599676) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=1599676) INFO 09-30 10:30:24 [__init__.py:1815] Using max model len 131072 (APIServer pid=1599676) INFO 09-30 10:30:24 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 09-30 10:30:29 [__init__.py:216] Automaticall...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: es sys errors. How to disable nccl in vllm for versions after 0.9.2? bug;stale ### Your current environment ### 🐛 Describe the bug sh 06_startVllmAPI.sh INFO 09-30 10:30:16 [__init__.py:216] Automatically detected platf...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Since version 0.9.2 comes with nccl built-in, using PCIE causes sys errors. How to disable nccl in vllm for versions after 0.9.2? bug;stale ### Your current environment ### 🐛 Describe the bug sh 06_startVllmAPI.s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: odelscope/models/GeoGPT/Qwen2.5-72B-GeoGPT', 'trust_remote_code': True, 'dtype': 'bfloat16', 'served_model_name': ['Qwen2.5-72B-GeoGPT'], 'tensor_parallel_size': 8, 'gpu_memory_utilization': 0.5} (APIServer pid=1599676)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 76) INFO 09-30 10:30:17 [utils.py:328] non-default args: {'port': 6006, 'model': './autodl-tmp/modelscope/models/GeoGPT/Qwen2.5-72B-GeoGPT', 'tokenizer': './autodl-tmp/modelscope/models/GeoGPT/Qwen2.5-72B-GeoGPT', 'trus...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /vllm00/lib/python3.12/site-packages/torch/lib/libtorch_cpu.so) frame #4: c10d::tcpstore::check(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | vllm00/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xdbbf4 (0x7b4740cdbbf4 in /home/aigeohub/.conda/envs/vllm00/bin/../lib/libstdc++.so… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | in /home/aigeohub/.conda/envs/vllm00/bin/../lib/libstdc++.so.6) frame #7: <unknown function> + 0x9caa4 (0x7b47bb89caa4 in /lib/x86_64-linux-gnu/libc.so.6) frame #8: <unknown funct… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
