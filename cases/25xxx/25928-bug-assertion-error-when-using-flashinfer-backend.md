# vllm-project/vllm#25928: [Bug]: Assertion error when using FlashInfer backend

| 字段 | 值 |
| --- | --- |
| Issue | [#25928](https://github.com/vllm-project/vllm/issues/25928) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Assertion error when using FlashInfer backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash OMP_NUM_THREADS=8 VLLM_USE_AITER_UNIFIED_ATTENTION=1 VLLM_ATTENTION_BACKEND=FLASHINFER VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve --async-scheduling --gpu-memory-utilization 0.8 --enable-auto-tool-choice --tool-call-parser hermes --model=Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 ``` Then I got ``` (Worker pid=2958) INFO 09-30 13:59:50 [default_loader.py:267] Loading weights took 29.90 seconds (Worker pid=2958) INFO 09-30 13:59:51 [gpu_model_runner.py:2730] Model loading took 29.0972 GiB and 32.575064 seconds (Worker pid=2958) INFO 09-30 13:59:59 [backends.py:548] Using cache directory: /home/jasl/.cache/vllm/torch_compile_cache/b222e3a507/rank_0_0/backbone for vLLM's torch.compile (Worker pid=2958) INFO 09-30 13:59:59 [backends.py:559] Dynamo bytecode transform time: 7.64 s (Worker pid=2958) INFO 09-30 14:00:00 [backends.py:197] Cache the graph for dynamic shape for later use (Worker pid=2958) INFO 09-30 14:00:24 [backends.py:218] Compiling a graph for dynamic shape takes 24.27 s (Worker pid=2958) ERROR 09-30 14:00:26 [multiproc_executor.py:671] WorkerProc hit an exception. (Worker pid=2958) ERROR 09-30 14:00:26 [multiproc_execu...

## 现有链接修复摘要

#25933 [Bugfix]: Assertion error when using FlashInfer backend

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: Assertion error when using FlashInfer backend bug ### Your current environment ### 🐛 Describe the bug ```bash OMP_NUM_THREADS=8 VLLM_USE_AITER_UNIFIED_ATTENTION=1 VLLM_ATTENTION_BACKEND=FLASHINFER VLLM_USE_FLASHI...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 59 [backends.py:548] Using cache directory: /home/jasl/.cache/vllm/torch_compile_cache/b222e3a507/rank_0_0/backbone for vLLM's torch.compile (Worker pid=2958) INFO 09-30 13:59:59 [backends.py:559] Dynamo bytecode transf...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ED_ATTENTION=1 VLLM_ATTENTION_BACKEND=FLASHINFER VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve --async-scheduling --gpu-memory-utilization 0.8 --enable-auto-tool-choice --tool-call-parser hermes --model=Qwen/Qwen3-30B-A3B-In...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: NIFIED_ATTENTION=1 VLLM_ATTENTION_BACKEND=FLASHINFER VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve --async-scheduling --gpu-memory-utilization 0.8 --enable-auto-tool-choice --tool-call-parser hermes --model=Qwen/Qwen3-30B-A3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ry-utilization 0.8 --enable-auto-tool-choice --tool-call-parser hermes --model=Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 ``` Then I got ``` (Worker pid=2958) INFO 09-30 13:59:50 [default_loader.py:267] Loading weights took 2...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25933](https://github.com/vllm-project/vllm/pull/25933) | closes_keyword | 0.95 | [Bugfix]: Assertion error when using FlashInfer backend | Fixes #25928. ## Test Plan The following does not err any more: ```bash OMP_NUM_THREADS=8 VLLM_USE_AITER_UNIFIED_ATTENTION=1 VLLM_ATTENTION_BACKEND=FLASHINFER VLLM_USE_FLASHINFE |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
