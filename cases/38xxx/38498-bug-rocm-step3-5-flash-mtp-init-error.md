# vllm-project/vllm#38498: [Bug][ROCm]: Step3.5 Flash MTP init error

| 字段 | 值 |
| --- | --- |
| Issue | [#38498](https://github.com/vllm-project/vllm/issues/38498) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm]: Step3.5 Flash MTP init error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve Step-3.5-Flash-FP8 \ --served-model-name step3p5-flash \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --max-num-seqs 512 \ --disable-cascade-attn \ --reasoning-parser step3p5 \ --enable-auto-tool-choice \ --tool-call-parser step3p5 \ --trust-remote-code \ --async-scheduling \ --no-enable-prefix-caching \ --compilation-config '{"cudagraph_mode": "PIECEWISE"}' \ --attention-config.backend ROCM_AITER_UNIFIED_ATTN \ --speculative_config '{"method": "step3p5_mtp", "num_speculative_tokens": 1}' \ --quantization fp8 ``` then got the error ``` (Worker pid=96931) (Worker_TP1_EP1 pid=96931) ERROR 03-30 03:13:32 [multiproc_executor.py:880] WorkerProc hit an exception. (Worker pid=96931) (Worker_TP1_EP1 pid=96931) ERROR 03-30 03:13:32 [multiproc_executor.py:880] Traceback (most recent call last): (Worker pid=96931) (Worker_TP1_EP1 pid=96931) ERROR 03-30 03:13:32 [multiproc_executor.py:880] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 875, in worker_busy_loop (Worker pid=96931) (Worker_TP1_EP1 pid=96931) ERROR 03-30 03:13:32 [multiproc_executor.py:880] output = func(*args,...

## 现有链接修复摘要

#39110 [Core] Disable HMA for eagle/MTP with sliding window models | #39376 [Core] Disable HMA for eagle/MTP with sliding window models

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: IECEWISE"}' \ --attention-config.backend ROCM_AITER_UNIFIED_ATTN \ --speculative_config '{"method": "step3p5_mtp", "num_speculative_tokens": 1}' \ --quantization fp8 ``` then got the error ``` (Worker pid=96931) (Worker...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: pilation-config '{"cudagraph_mode": "PIECEWISE"}' \ --attention-config.backend ROCM_AITER_UNIFIED_ATTN \ --speculative_config '{"method": "step3p5_mtp", "num_speculative_tokens": 1}' \ --quantization fp8 ``` then got th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: executor.py:880] File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker pid=96931) (Worker_TP1_EP1 pid=96931) ERROR 03-30 03:13:32 [multiproc_executor.py:880] return func(...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nt environment ### 🐛 Describe the bug ``` vllm serve Step-3.5-Flash-FP8 \ --served-model-name step3p5-flash \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --max-num-seqs 512 \ --disable-cascade-attn \ --reasoni...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug][ROCm]: Step3.5 Flash MTP init error bug;rocm ### Your current environment ### 🐛 Describe the bug ``` vllm serve Step-3.5-Flash-FP8 \ --served-model-name step3p5-flash \ --tensor-parallel-size 8 \ --enable-expe

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39110](https://github.com/vllm-project/vllm/pull/39110) | closes_keyword | 0.95 | [Core] Disable HMA for eagle/MTP with sliding window models | Fixes #38498 Signed-off-by: Bortlesboat <bortlesboat@users.noreply.github.com> |
| [#39376](https://github.com/vllm-project/vllm/pull/39376) | closes_keyword | 0.95 | [Core] Disable HMA for eagle/MTP with sliding window models | Fixes #38498 **Duplicate check:** No existing open PR addresses this. Previous PRs and issues discuss the symptom but no fix was merged. **Tests:** Verified the guard logic match |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
