# vllm-project/vllm#35944: [Bug]: jetson agx thor报错

| 字段 | 值 |
| --- | --- |
| Issue | [#35944](https://github.com/vllm-project/vllm/issues/35944) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | shape_align |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: jetson agx thor报错

### Issue 正文摘录

### Your current environment (vllm35) nvidia@localhost:/data/lqy/vllm/qwne3.5$ vllm serve \ > "/data/lqy/qwen3.5/Qwen3.5-9B" \ > --async-scheduling \ > --port 8000 \ > --host 0.0.0.0 \ > --trust-remote-code \ > --swap-space 16 \ > --max-model-len 32768 \ > --tensor-parallel-size 1 \ > --max-num-seqs 256 \ > --gpu-memory-utilization 0.7 \ > --enable-prefix-caching DEBUG 03-04 10:16:27 [plugins/__init__.py:36] No plugins for group vllm.platform_plugins found. DEBUG 03-04 10:16:27 [platforms/__init__.py:36] Checking if TPU platform is available. DEBUG 03-04 10:16:27 [platforms/__init__.py:55] TPU platform is not available because: No module named 'libtpu' DEBUG 03-04 10:16:27 [platforms/__init__.py:61] Checking if CUDA platform is available. DEBUG 03-04 10:16:29 [platforms/__init__.py:84] Confirmed CUDA platform is available. DEBUG 03-04 10:16:29 [platforms/__init__.py:112] Checking if ROCm platform is available. DEBUG 03-04 10:16:29 [platforms/__init__.py:126] ROCm platform is not available because: No module named 'amdsmi' DEBUG 03-04 10:16:29 [platforms/__init__.py:133] Checking if XPU platform is available. DEBUG 03-04 10:16:29 [platforms/__init__.py:155] Checking if CPU platform...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: 35) nvidia@localhost:/data/lqy/vllm/qwne3.5$ vllm serve \ > "/data/lqy/qwen3.5/Qwen3.5-9B" \ > --async-scheduling \ > --port 8000 \ > --host 0.0.0.0 \ > --trust-remote-code \ > --swap-space 16 \ > --max-model-len 32768...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: y:220] Automatically detected platform cuda. DEBUG 03-04 10:16:31 [utils/flashinfer.py:45] flashinfer-cubin package was not found DEBUG 03-04 10:16:32 [utils/import_utils.py:74] Loading module triton_kernels from /data/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: y:45] flashinfer-cubin package was not found DEBUG 03-04 10:16:32 [utils/import_utils.py:74] Loading module triton_kernels from /data/lqy/vllm/qwne3.5/vllm/third_party/triton_kernels/__init__.py. DEBUG 03-04 10:16:33 [e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: 03-04 10:16:33 [config/model.py:1618] Generative models support chunked prefill. (APIServer pid=3978607) DEBUG 03-04 10:16:33 [config/model.py:1661] Hybrid models do not support prefix caching since the feature is still...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
