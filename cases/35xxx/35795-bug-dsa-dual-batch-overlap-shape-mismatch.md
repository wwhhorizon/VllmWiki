# vllm-project/vllm#35795: [Bug]: DSA + Dual batch overlap shape mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#35795](https://github.com/vllm-project/vllm/issues/35795) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DSA + Dual batch overlap shape mismatch

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug If `--enable-dbo` is enabled and the model is using the sparse indexer for DSA - such as GLM5 model, this results in an error as follows (shortened for clarity): ``` 811741-(EngineCore_DP3 pid=1559457) ERROR 03-02 20:31:32 [core.py:1008] File " .8", line 5, in forward 811742-(EngineCore_DP3 pid=1559457) ERROR 03-02 20:31:32 [core.py:1008] sparse_attn_indexer = torch.ops.vllm.sparse_attn_indexer(x_3, 'model.layers.0.self_attn.indexer.k_cache', l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_modules_indexer_op_modules_k_cache_kv_cache_0_, q_fp8, k_1, weights_1, 128, 'ue8m0', 2048, 128, 32768, 1310720, l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_modules_indexer_op_topk_indices_buffer); x_3 = l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_modules_indexer_op_modules_k_cache_kv_cache_0_ = q_fp8 = k_1 = weights_1 = l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_modules_indexer_op_topk_indices_buffer = sparse_attn_indexer = None 811743-(EngineCore_DP3 pid=1559457) ERROR 03-02 20:31:32 [core.py:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: DSA + Dual batch overlap shape mismatch bug ### Your current environment ### 🐛 Describe the bug If `--enable-dbo` is enabled and the model is using the sparse indexer for DSA - such as GLM5 model, this results in...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: _0_modules_self_attn_modules_mla_attn_modules_indexer_modules_indexer_op_topk_indices_buffer); x_3 = l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_modules_indexer_op_modules_k_cache_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 559457) ERROR 03-02 20:31:32 [core.py:1008] topk_indices_buffer[:num_decode_tokens, : topk_indices.shape[-1]] = ( 811749-(EngineCore_DP3 pid=1559457) ERROR 03-02 20:31:32 [core.py:1008] ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 559457) ERROR 03-02 20:31:32 [core.py:1008] File "/home/matej/dev/vllm-benchmarking/.venv/lib/python3.12/site-packages/torch/_ops.py", line 1255, in __call__ 811745-(EngineCore_DP3 pid=1559457) ERROR 03-02 20:31:32 [cor...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
