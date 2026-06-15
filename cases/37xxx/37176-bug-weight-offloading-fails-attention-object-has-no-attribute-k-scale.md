# vllm-project/vllm#37176: [Bug]: weight offloading fails: 'Attention' object has no attribute 'k_scale'

| 字段 | 值 |
| --- | --- |
| Issue | [#37176](https://github.com/vllm-project/vllm/issues/37176) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;moe;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: weight offloading fails: 'Attention' object has no attribute 'k_scale'

### Issue 正文摘录

### Your current environment 8x RTX PRO 6000, vLLM 0.17.1 ### 🐛 Describe the bug I tried to start vLLM with weight offloading v2 for GLM-4.7 on 8x RTX PRO 6000. ``` vllm serve "zai-org/GLM-4.7-FP8" \ --served-model-name "zai-org/GLM-4.7-FP8" \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --cpu-offload-gb 500 \ --offload-group-size 2 \ --offload-num-in-group 1 \ --offload-prefetch-step 1 \ ``` GLM-4.7-FP8 runs fine on that hardware without model weight offloading. With the above command, the startup fails with **AttributeError: 'Attention' object has no attribute 'k_scale'. Did you mean: '_k_scale'?** ``` WorkerProc failed to start. Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 771, in worker_main worker = WorkerProc(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 597, in __init__ self.worker.load_model() File "/usr/local/lib/python3.12/dist-packages/vllm/v1/work...

## 现有链接修复摘要

#37178 Bugfix for offloading+prefetch for GLM-4.7-FP8 | #37194 fix: handle missing parameters gracefully in weight offloading | #37211 fix: Add missing k_scale attribute to Attention for weight offloading

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: weight offloading fails: 'Attention' object has no attribute 'k_scale' bug ### Your current environment 8x RTX PRO 6000, vLLM 0.17.1 ### 🐛 Describe the bug I tried to start vLLM with weight offloading v2 for GLM-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/v1/ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ' object has no attribute 'k_scale' bug ### Your current environment 8x RTX PRO 6000, vLLM 0.17.1 ### 🐛 Describe the bug I tried to start vLLM with weight offloading v2 for GLM-4.7 on 8x RTX PRO 6000. ``` vllm serve "za...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: model-name "zai-org/GLM-4.7-FP8" \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --cpu-offload-gb 500 \ --offload-group-size 2 \ --offload-num-in-group 1 \ --offload-prefetch-step 1 \ ``` GLM-4.7-FP8 runs fine o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ion;sampling_logits;speculative_decoding attention;cuda;fp8;moe;sampling;triton build_error;crash;nan_inf dtype;env_dependency #37178 Bugfix for offloading+prefetch for GLM-4.7-FP8 | #37194 fix: handle missing parameter...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37178](https://github.com/vllm-project/vllm/pull/37178) | closes_keyword | 0.95 | Bugfix for offloading+prefetch for GLM-4.7-FP8 | fixes a bug when using offload+prefetch feature with GLM-4.7-FP8 on RTX PRO 6000 hardware, see #37176 . ## Test Plan ``` vllm serve "zai-org/GLM-4.7-FP8" \ --served-model-name "z |
| [#37194](https://github.com/vllm-project/vllm/pull/37194) | closes_keyword | 0.95 | fix: handle missing parameters gracefully in weight offloading | fix addresses issue #37176 where weight offloading fails with 'AttributeError: Attention object has no attribute k_scale'. The root cause is that during model weight loading, cert |
| [#37211](https://github.com/vllm-project/vllm/pull/37211) | closes_keyword | 0.95 | fix: Add missing k_scale attribute to Attention for weight offloading | Fixes #37176 The `BaseKVCacheMethod.create_weights()` creates `k_scale`, `v_scale`, `q_scale`, and `prob_scale` as nn.Parameter objects for weight loading. However, `process_weigh |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
