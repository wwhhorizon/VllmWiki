# vllm-project/vllm#18834: [Bug][Regression]: Dimension out of range when using MooncakeStoreConnector

| 字段 | 值 |
| --- | --- |
| Issue | [#18834](https://github.com/vllm-project/vllm/issues/18834) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Regression]: Dimension out of range when using MooncakeStoreConnector

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using disaggregated prefill with the mooncake store connector, the decoding instance crashes with an `IndexError: Dimension out of range` from the `reshape_and_cache_flash` kernel. The bug is not triggered when using normal non-disaggregated serving with the same model. It seems that it is the vLLM Mooncake integration not conforming to the new expected shape of the KV cache. The bug appears to be a regression, triggered by the following change: (#16605) ``` commit 9e96f56efb5b44a12d9d516276daa5538700a211 2025-04-26 Shu Wang Allocate kv_cache with stride order (#16605) 9e96f56efb csrc/cache_kernels.cu (Shu Wang 2025-04-26 00:03:31 -0500 439) int64_t page_stride = key_cache.stride(1); 9e96f56efb csrc/cache_kernels.cu (Shu Wang 2025-04-26 00:03:31 -0500 440) int64_t head_stride = key_cache.stride(2); ``` Error message: ``` ERROR 05-28 10:18:40 [engine.py:164] IndexError('Dimension out of range (expected to be in range of [-2, 1], but got 2)')^M ERROR 05-28 10:18:40 [engine.py:164] Traceback (most recent call last):^M ERROR 05-28 10:18:40 [engine.py:164] File "/opt/vllm/vllm/engine/multiprocessing/engine.py", line 162, in start...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: egression]: Dimension out of range when using MooncakeStoreConnector bug;stale ### Your current environment ### 🐛 Describe the bug When using disaggregated prefill with the mooncake store connector, the decoding instanc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cache;cuda;kernel;operator;sampling...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 2) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 4a12d9d516276daa5538700a211 2025-04-26 Shu Wang Allocate kv_cache with stride order (#16605) 9e96f56efb csrc/cache_kernels.cu (Shu Wang 2025-04-26 00:03:31 -0500 439) int64_t page_stride = key_cache.stride(1);
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug][Regression]: Dimension out of range when using MooncakeStoreConnector bug;stale ### Your current environment ### 🐛 Describe the bug When using disaggregated prefill with the mooncake store connector, the decoding...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
