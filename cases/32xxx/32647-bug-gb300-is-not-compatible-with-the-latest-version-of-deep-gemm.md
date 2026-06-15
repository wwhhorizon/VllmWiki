# vllm-project/vllm#32647: [Bug]: GB300 is not compatible with the latest version of deep_gemm.

| 字段 | 值 |
| --- | --- |
| Issue | [#32647](https://github.com/vllm-project/vllm/issues/32647) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GB300 is not compatible with the latest version of deep_gemm.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After installing deep_gemm using `tools/install_deepgemm.sh`, vLLM does not work properly. I noticed that [https://github.com/vllm-project/vllm/pull/32479](https://github.com/vllm-project/vllm/pull/32479) updated the version of deep_gemm used by vLLM. ``` vllm serve /mnt/nfs/models/deepseek-ai/DeepSeek-V3.2 -tp=4 --tokenizer-mode deepseek_v32 ``` ``` orker_TP2 pid=3972774) ERROR 01-20 06:34:02 [multiproc_executor.py:839] File " .252", line 1133, in forward (Worker_TP2 pid=3972774) ERROR 01-20 06:34:02 [multiproc_executor.py:839] submod_1 = self.submod_1(getitem, s72, l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_modules_k_cache_kv_cache_0_, getitem_1, getitem_2, getitem_3, l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_topk_indices_buffer); getitem = l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_modules_k_cache_kv_cache_0_ = getitem_1 = getitem_2 = getitem_3 = submod_1 = None (Worker_TP2 pid=3972774) ERROR 01-20 06:34:02 [multiproc_executor.py:839] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: GB300 is not compatible with the latest version of deep_gemm. bug ### Your current environment ### 🐛 Describe the bug After installing deep_gemm using `tools/install_deepgemm.sh`, vLLM does not work properly. I n...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 6:34:02 [multiproc_executor.py:839] return self.worker.execute_model(scheduler_output) (Worker_TP2 pid=3972774) ERROR 01-20 06:34:02 [multiproc_executor.py:839] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP2 pi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: GB300 is not compatible with the latest version of deep_gemm. bug ### Your current environment ### 🐛 Describe the bug After installing deep_gemm using `tools/install_deepgemm.sh`, vLLM does not work properly. I n...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: elf_attn_modules_mla_attn_modules_indexer_modules_k_cache_kv_cache_0_, q_fp8, k_1, weights_1, 128, 'ue8m0', 2048, 128, 163840, 6553600, l_self_modules_layers_modules_0_modules_self_attn_modules_mla_attn_modules_indexer_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: iproc_executor.py:839] File "/home/vllm/chauncey/vllm/vllm/compilation/cuda_graph.py", line 222, in __call__ (Worker_TP2 pid=3972774) ERROR 01-20 06:34:02 [multiproc_executor.py:839] return self.runnable(*args, **kwargs...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
