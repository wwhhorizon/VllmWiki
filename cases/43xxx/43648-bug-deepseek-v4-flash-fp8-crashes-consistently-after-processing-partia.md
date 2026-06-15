# vllm-project/vllm#43648: [Bug]: DeepSeek-V4-Flash-FP8 crashes consistently after processing partial benchmark requests with data parallel and expert parallel (vLLM v0.20.1, H200)

| 字段 | 值 |
| --- | --- |
| Issue | [#43648](https://github.com/vllm-project/vllm/issues/43648) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | fp8;moe;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V4-Flash-FP8 crashes consistently after processing partial benchmark requests with data parallel and expert parallel (vLLM v0.20.1, H200)

### Issue 正文摘录

### Your current environment GPU model: NVIDIA H200 vLLM version: v0.20.1 ### 🐛 Describe the bug When running performance benchmarks on DeepSeek-V4-Flash-FP8 using vLLM v0.20.1 with expert parallel and data parallel on H200, the vLLM server crashes consistently after processing some of the benchmark requests. The crash is 100% reproducible. ### Model used Model: `DeepSeek-V4-Flash-FP8` https://huggingface.co/sgl-project/DeepSeek-V4-Flash-FP8 FP8 quantization enabled via config.json modification: Added `"expert_dtype": "fp8"` to config.json to support FP8 execution. ### Reproduction steps 1. Prepare the model checkpoint with custom config.json as described above. 2. Start vLLM server with the following command: ```bash vllm serve ./DeepSeek-V4-Flash-FP8 \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --data-parallel-size 4 \ --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE", "custom_ops":["all"]}' \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice \ --reasoning-parser deepseek_v4 \ --port 9000 3、Run benchmark requests (using vLLM's benchmark_serving.py or similar benchmarking tool). 4、S...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: .1, H200) bug ### Your current environment GPU model: NVIDIA H200 vLLM version: v0.20.1 ### 🐛 Describe the bug When running performance benchmarks on DeepSeek-V4-Flash-FP8 using vLLM v0.20.1 with expert parallel and dat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: DeepSeek-V4-Flash-FP8 crashes consistently after processing partial benchmark requests with data parallel and expert parallel (vLLM v0.20.1, H200) bug ### Your current environment GPU model: NVIDIA H200 vLLM vers...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: pert parallel (vLLM v0.20.1, H200) bug ### Your current environment GPU model: NVIDIA H200 vLLM version: v0.20.1 ### 🐛 Describe the bug When running performance benchmarks on DeepSeek-V4-Flash-FP8 using vLLM v0.20.1 wit...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ```bash vllm serve ./DeepSeek-V4-Flash-FP8 \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --data-parallel-size 4 \ --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWIS...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: Seek-V4-Flash-FP8 \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --data-parallel-size 4 \ --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE", "custom_ops":["all"]}...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /local/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0xdc253 (0x7f8c266b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #5: <unkn… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | 0x94ac3 (0x7f8c571a2ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #6: <unknown function> + 0x1268d0 (0x7f8c572348d0 in /usr/lib/x86_64-linux-gnu/libc.so.6) bench crash res: ==… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
