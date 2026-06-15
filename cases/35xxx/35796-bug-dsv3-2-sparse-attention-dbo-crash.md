# vllm-project/vllm#35796: [Bug][DSV3.2]: Sparse Attention + DBO Crash

| 字段 | 值 |
| --- | --- |
| Issue | [#35796](https://github.com/vllm-project/vllm/issues/35796) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][DSV3.2]: Sparse Attention + DBO Crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug If `--enable-dbo` is enabled and the model is using the sparse indexer for DSA - such as GLM5 model, this results in an error as follows (shortened for clarity): ``` 811741-(EngineCore_DP3 pid=1559457) ERROR 03-02 20:31:32 [core.py:1008] File " .8", line 5, in forward 811742-(EngineCore_DP3 pid=1559457) ERROR 03-02 20:31:32 [core.py:1008] sparse_attn_indexer = torch.ops.vllm.sparse_attn_indexer(x_3, 'model.layers.0.self_attn.indexer.k_cache', l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_modules_indexer_op_modules_k_cache_kv_cache_0_, q_fp8, k_1, weights_1, 128, 'ue8m0', 2048, 128, 32768, 1310720, l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_modules_indexer_op_topk_indices_buffer); x_3 = l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_modules_indexer_op_modules_k_cache_kv_cache_0_ = q_fp8 = k_1 = weights_1 = l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_modules_indexer_op_topk_indices_buffer = sparse_attn_indexer = None 811743-(EngineCore_DP3 pid=1559457) ERROR 03-02 20:31:32 [core.py:...

## 现有链接修复摘要

#35802 Fix: DBO + DSA shape mismatch

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug][DSV3.2]: Sparse Attention + DBO Crash bug;stale ### Your current environment ### 🐛 Describe the bug If `--enable-dbo` is enabled and the model is using the sparse indexer for DSA - such as GLM5 model, this results...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: _0_modules_self_attn_modules_mla_attn_modules_indexer_modules_indexer_op_topk_indices_buffer); x_3 = l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_modules_indexer_op_modules_k_cache_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 559457) ERROR 03-02 20:31:32 [core.py:1008] File "/home/matej/dev/vllm-benchmarking/.venv/lib/python3.12/site-packages/torch/_ops.py", line 1255, in __call__ 811745-(EngineCore_DP3 pid=1559457) ERROR 03-02 20:31:32 [cor...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35802](https://github.com/vllm-project/vllm/pull/35802) | closes_keyword | 0.95 | Fix: DBO + DSA shape mismatch | fix #35796 - when DBO is used together with sparse attention, we get a mismatch in shapes that is probably caused by `num_decode_tokens` coming from the global attention and `topk_ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
