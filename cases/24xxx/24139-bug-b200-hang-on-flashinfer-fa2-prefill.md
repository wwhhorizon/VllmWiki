# vllm-project/vllm#24139: [Bug]: B200 hang on flashinfer fa2 prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#24139](https://github.com/vllm-project/vllm/issues/24139) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: B200 hang on flashinfer fa2 prefill

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Currently vLLM is randomly hanging for me on B200s. Here is the function trace I'm seeing on nightly builds, though this happens on `v0.10.1.1` as well. ``` 2025-09-02 21:59:48.617724 Return from _expand_5d in /.venv/lib/python3.12/site-packages/flashinfer/utils.py:69 to _unpack_paged_kv_cache in /.venv/lib/python3.12/site-packages/flashinfer/utils.py:140 2025-09-02 21:59:48.617737 Return from _unpack_paged_kv_cache in /.venv/lib/python3.12/site-packages/flashinfer/utils.py:142 to run in /.venv/lib/python3.12/site-packages/flashinfer/prefill.py:1999 2025-09-02 21:59:48.617746 Call to _check_cached_qkv_data_type in /.venv/lib/python3.12/site-packages/flashinfer/utils.py:218 from run in /.venv/lib/python3.12/site-packages/flashinfer/prefill.py:2000 2025-09-02 21:59:48.617754 Return from _check_cached_qkv_data_type in /.venv/lib/python3.12/site-packages/flashinfer/utils.py:225 to run in /.venv/lib/python3.12/site-packages/flashinfer/prefill.py:2000 2025-09-02 21:59:48.617794 Call to _get_cache_alibi_slopes_buf in /.venv/lib/python3.12/site-packages/flashinfer/utils.py:189 from run in /.venv/lib/python3.12/site-packages/flashinfer/pr...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: B200 hang on flashinfer fa2 prefill bug;stale ### Your current environment ### 🐛 Describe the bug Currently vLLM is randomly hanging for me on B200s. Here is the function trace I'm seeing on nightly builds, thoug...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: anging for me on B200s. Here is the function trace I'm seeing on nightly builds, though this happens on `v0.10.1.1` as well. ``` 2025-09-02 21:59:48.617724 Return from _expand_5d in /.venv/lib/python3.12/site-packages/f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: B200 hang on flashinfer fa2 prefill bug;stale ### Your current environment ### 🐛 Describe the bug Currently vLLM is randomly hanging for me on B200s. Here is the function trace I'm seeing on nightly builds, thoug...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: B200 hang on flashinfer fa2 prefill bug;stale ### Your current environment ### 🐛 Describe the bug Currently vLLM is randomly hanging for me on B200s. Here is the function trace I'm seeing on nightly builds, thoug...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: es it past this prefill call. Server was started with `vllm serve openai/gpt-oss-120b --uvicorn-log-level warning`. I'm having a hard time triggering this with a simple script sending requests, but I have a script using...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
