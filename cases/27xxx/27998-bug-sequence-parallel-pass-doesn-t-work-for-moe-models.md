# vllm-project/vllm#27998: [Bug]: Sequence Parallel Pass doesn't work for MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#27998](https://github.com/vllm-project/vllm/issues/27998) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Sequence Parallel Pass doesn't work for MoE models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Sequence Parallel does not appear to be working on MoE models such as `Qwen/Qwen3-30B-A3B-Instruct-2507`. Steps for reproduction: 1. start server with ``` VLLM_DISABLE_COMPILE_CACHE=1 vllm serve Qwen/Qwen3-30B-A3B-Instruct-2507 --tensor-parallel-size 2 --gpu-memory-utilization=0.9 --no-enable-prefix-caching --compilation-config '{"pass_config": { "enable_sequence_parallelism": true} , "level": 3, "use_inductor_graph_partition": false, "splitting_ops":[], "cudagraph_mode": "FULL"}' ``` 2. Then send a request. Sometimes this crashes on engine startup and sometimes it crashes after sending a request or simply outputs incorrect text. Based on the fx-graph dumps, it appears that there exists a pattern which can be replaced for the gemm following attention and that the patterns are indeed being matched and replaced: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Sequence Parallel Pass doesn't work for MoE models bug;torch.compile ### Your current environment ### 🐛 Describe the bug Sequence Parallel does not appear to be working on MoE models such as `Qwen/Qwen3-30B-A3B-I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: hing --compilation-config '{"pass_config": { "enable_sequence_parallelism": true} , "level": 3, "use_inductor_graph_partition": false, "splitting_ops":[], "cudagraph_mode": "FULL"}' ``` 2. Then send a request. Sometimes...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Sequence Parallel Pass doesn't work for MoE models bug;torch.compile ### Your current environment ### 🐛 Describe the bug Sequence Parallel does not appear to be working on MoE models such as `Qwen/Qwen3-30B-A3B-I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: false, "splitting_ops":[], "cudagraph_mode": "FULL"}' ``` 2. Then send a request. Sometimes this crashes on engine startup and sometimes it crashes after sending a request or simply outputs incorrect text. Based on the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ry;speculative_decoding attention;cuda;gemm;kernel;moe;operator;sampling;triton build_error;crash;mismatch;nan_inf dtype;env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure K...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 53 (0x15554ccb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #4: <unknown function> + 0x94ac3 (0x15555523cac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #5: <unknown f… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /venv2/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xdc253 (0x15554ccb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unkn… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | 53 (0x15554ccb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown function> + 0x94ac3 (0x15555523cac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #8: <unknown f… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
