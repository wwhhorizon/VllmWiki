# vllm-project/vllm#37602: [Bug]: Qwen3.5-122B-A10B-FP8 EngineCore crash on concurrent image requests

| 字段 | 值 |
| --- | --- |
| Issue | [#37602](https://github.com/vllm-project/vllm/issues/37602) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel |
| 症状 | crash;mismatch;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-122B-A10B-FP8 EngineCore crash on concurrent image requests

### Issue 正文摘录

## Environment ``` vLLM version: 0.17.1 Model: Qwen/Qwen3.5-122B-A10B-FP8 PyTorch: 2.10.0+cu128 CUDA: 12.8 GPU: 4× NVIDIA H200 SXM (141 GB each) tensor_parallel_size: 4 Python: 3.10 OS: Linux (OpenShift container) ``` ## Describe the Bug `EngineCore_DP0` dies unexpectedly with **exit code 0** when concurrent multimodal (image) requests are sent to Qwen3.5-122B-A10B-FP8. **Key observation: crash is image-specific.** Text-only requests run stably under the same load. GPU KV cache usage was 14–16% at crash time, ruling out OOM. --- ### Failure 1 — Tokenizer race condition (HTTP 400, non-fatal per request) ``` RuntimeError: Already borrowed File "transformers/tokenization_utils_fast.py", line 494 self._tokenizer.enable_truncation(**target) ``` HuggingFace fast tokenizer Rust borrow checker conflict under concurrent multimodal requests. Per-request recoverable but destabilizes engine under load. Also observed before crash: ``` WARNING [context.py:276] Failed to acquire tokenizer in current thread. Retrying (1/5)... ``` --- ### Failure 2 — EngineCore hard crash (HTTP 500, fatal) ``` ERROR [core_client.py] Engine core proc EngineCore_DP0 died unexpectedly, shutting down client. ERROR [as...

## 现有链接修复摘要

#35219 [BUGFIX][Mamba][Qwen3.5] Zero freed SSM cache blocks on GPU

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: P8 EngineCore crash on concurrent image requests ## Environment ``` vLLM version: 0.17.1 Model: Qwen/Qwen3.5-122B-A10B-FP8 PyTorch: 2.10.0+cu128 CUDA: 12.8 GPU: 4× NVIDIA H200 SXM (141 GB each) tensor_parallel_size: 4 P...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen3.5-122B-A10B-FP8 EngineCore crash on concurrent image requests ## Environment ``` vLLM version: 0.17.1 Model: Qwen/Qwen3.5-122B-A10B-FP8 PyTorch: 2.10.0+cu128 CUDA: 12.8 GPU: 4× NVIDIA H200 SXM (141 GB each)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Qwen3.5-122B-A10B-FP8 EngineCore crash on concurrent image requests ## Environment ``` vLLM version: 0.17.1 Model: Qwen/Qwen3.5-122B-A10B-FP8 PyTorch: 2.10.0+cu128 CUDA: 12.8 GPU: 4× NVIDIA H200 SXM (141 GB each)...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: lthy) ``` Running: 100 reqs, Waiting: 1 req GPU KV cache usage: 14.2% MM cache hit rate: 100.0% Avg prompt throughput: 2001.2 tokens/s Avg generation throughput: 1918.4 tokens/s ``` ~19 minutes before fatal crash, a rec...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen3.5-122B-A10B-FP8 EngineCore crash on concurrent image requests ## Environment ``` vLLM version: 0.17.1 Model: Qwen/Qwen3.5-122B-A10B-FP8 PyTorch: 2.10.0+cu128 CUDA: 12.8 GPU: 4× NVIDIA H200 SXM (141 GB each)...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35219](https://github.com/vllm-project/vllm/pull/35219) | mentioned | 0.45 | [BUGFIX][Mamba][Qwen3.5] Zero freed SSM cache blocks on GPU | ssue is kernel-level, not scheduler-level. --- ## related issues - #35219 — [mamba][qwen3.5] zero freed ssm cache blocks on gpu (merged v0.17.1, different bug) - #35702 — qwen3.5-… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
