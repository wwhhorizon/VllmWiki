# vllm-project/vllm#32782: [Bug]: KV cache 0.14 regression vs 0.11 and 0.13 

| 字段 | 值 |
| --- | --- |
| Issue | [#32782](https://github.com/vllm-project/vllm/issues/32782) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KV cache 0.14 regression vs 0.11 and 0.13 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I updated to vllm 0.14, I get a regression regarding this command (works with 0.11 and 0.13 but fails with 0.14) I was able to start vllm with max-len 100000; now its fails under 30000. I can't tell if this i a bug or an expected behavior from 0.14. ```bash -c 'source /home/anthony/vllm/bin/activate; PYTHONHASHSEED=0 OMP_NUM_THREADS=1 PYTORCH_ALLOC_CONF="expandable_segments:True" VLLM_USE_MEMORY_EFFICIENT_KERNELS=1 VLLM_PP_LAYER_PARTITION="26,11,7,4" TORCH_CUDA_ARCH_LIST="8.6" CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=3,1,2,5 vllm serve cyankiwi/Qwen3-Coder-30B-A3B-Instruct-AWQ-4bit --max-model-len 40000 --port 8080 --dtype half --pipeline-parallel-size 4 --tensor-parallel-size 1 --gpu-memory-utilization=0.96 --max_num_batched_tokens 512 --max_num_seqs 4' (APIServer pid=15841) INFO 01-21 14:16:50 [api_server.py:1272] vLLM API server version 0.14.0 (APIServer pid=15841) INFO 01-21 14:16:50 [utils.py:263] non-default args: {'model_tag': 'cyankiwi/Qwen3-Coder-30B-A3B-Instruct-AWQ-4bit', 'port': 8080, 'model': 'cyankiwi/Qwen3-Coder-30B-A3B-Instruct-AWQ-4bit', 'dtype': 'half', 'max_model_len': 40000, 'pipeline_parallel_size':...

## 现有链接修复摘要

#33698 [Core][BugFix] Fix PP KV cache sharding memory validation

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: EADS=1 PYTORCH_ALLOC_CONF="expandable_segments:True" VLLM_USE_MEMORY_EFFICIENT_KERNELS=1 VLLM_PP_LAYER_PARTITION="26,11,7,4" TORCH_CUDA_ARCH_LIST="8.6" CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=3,1,2,5 vllm serv...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: wen3-Coder-30B-A3B-Instruct-AWQ-4bit --max-model-len 40000 --port 8080 --dtype half --pipeline-parallel-size 4 --tensor-parallel-size 1 --gpu-memory-utilization=0.96 --max_num_batched_tokens 512 --max_num_seqs 4' (APISe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=3,1,2,5 vllm serve cyankiwi/Qwen3-Coder-30B-A3B-Instruct-AWQ-4bit --max-model-len 40000 --port 8080 --dtype half --pipeline-parallel-size 4 --tensor-parallel-size 1 --gpu-mem...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: KV cache 0.14 regression vs 0.11 and 0.13 bug ### Your current environment ### 🐛 Describe the bug I updated to vllm 0.14, I get a regression regarding this command (works with 0.11 and 0.13 but fails with 0.14) I...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33698](https://github.com/vllm-project/vllm/pull/33698) | closes_keyword | 0.95 | [Core][BugFix] Fix PP KV cache sharding memory validation | Fixes #32105. Refs #32782. Regression introduced by #29431 (commit 8ee90c8). This PR fixes incorrect KV cache sharding memory validation under Pipeline Parallelism, which could ca |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
