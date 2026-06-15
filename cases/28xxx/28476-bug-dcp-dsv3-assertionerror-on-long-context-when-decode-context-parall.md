# vllm-project/vllm#28476: [Bug]: [DCP] [DSV3] AssertionError on long context when --decode-context-parallel-size is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#28476](https://github.com/vllm-project/vllm/issues/28476) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [DCP] [DSV3] AssertionError on long context when --decode-context-parallel-size is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - Minimal reproducer: The model server is launched with full DCP and a single near-context-limit input (over 120k) is processed. (almost 100% reproducible on my machine) - vLLM version: v0.11.1rc7.dev20+g9973e6e04 - Hardware: H100 x 8 x 2 nodes (over IB networking) - Model checkpoint: deepseek-ai/DeepSeek-V3 - Attention Backend: FlashMLA - Launch command: `VLLM_MOE_DEEP_GEMM=0 vllm serve /mnt/models --served-model-name deepseek-ai/DeepSeek-V3 -tp 16 -dcp 16 --enable-expert-parallel --all2all-backend deepep_low_latency --distributed-executor-backend ray --async-scheduling --max-model-len 128K --max-num-batched-tokens 16K --max-num-seqs 32` # Error traceback ``` [1;36m(APIServer pid=1554) [0;0m INFO: 172.16.33.39:51958 - "GET /metrics HTTP/1.1" 200 OK [1;36m(APIServer pid=1554) [0;0m INFO: 172.16.33.39:51958 - "GET /metrics HTTP/1.1" 200 OK [1;36m(APIServer pid=1554) [0;0m INFO: 172.16.93.20:37418 - "GET /health HTTP/1.1" 200 OK [1;36m(APIServer pid=1554) [0;0m INFO 11-11 23:20:12 [logger.py:37] Request cmpl-2f596feab8044210b24f979c15ed186d-0 details: prompt: '안녕?', prompt_token_ids: [0, 31404, 11939, 246, 33], prompt_embeds shape:...

## 现有链接修复摘要

#41229 [Bugfix][MLA][DCP] Round chunked-prefill workspace and max_context_chunk to satisfy DCP divisibility asserts

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: [DCP] [DSV3] AssertionError on long context when --decode-context-parallel-size is enabled bug ### Your current environment ### 🐛 Describe the bug - Minimal reproducer: The model server is launched with full DCP...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e near-context-limit input (over 120k) is processed. (almost 100% reproducible on my machine) - vLLM version: v0.11.1rc7.dev20+g9973e6e04 - Hardware: H100 x 8 x 2 nodes (over IB networking) - Model checkpoint: deepseek-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=16, pipeline_parallel_size=1, data_parallel_si...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: -V3 -tp 16 -dcp 16 --enable-expert-parallel --all2all-backend deepep_low_latency --distributed-executor-backend ray --async-scheduling --max-model-len 128K --max-num-batched-tokens 16K --max-num-seqs 32` # Error traceba...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: r IB networking) - Model checkpoint: deepseek-ai/DeepSeek-V3 - Attention Backend: FlashMLA - Launch command: `VLLM_MOE_DEEP_GEMM=0 vllm serve /mnt/models --served-model-name deepseek-ai/DeepSeek-V3 -tp 16 -dcp 16 --enab...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41229](https://github.com/vllm-project/vllm/pull/41229) | mentioned | 0.6 | [Bugfix][MLA][DCP] Round chunked-prefill workspace and max_context_chunk to satisfy DCP divisibility asserts | fix-cached prefix + many concurrent short tails (same crash family as #28476; #28526 only fixed the adjacent `reorg_kvcache` shape assert). Concretely: with `chunked_prefill_works… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
