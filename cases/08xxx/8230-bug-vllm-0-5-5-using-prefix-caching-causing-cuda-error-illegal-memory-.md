# vllm-project/vllm#8230: [Bug]: vLLM 0.5.5 using prefix caching causing CUDA error: illegal memory access

| 字段 | 值 |
| --- | --- |
| Issue | [#8230](https://github.com/vllm-project/vllm/issues/8230) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.5.5 using prefix caching causing CUDA error: illegal memory access

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug --enable-prefix-caching causing CUDA error: illegal memory access. According to the trackback, this bug seems to be caused by FlashAttention. I notice that [PR 7018](https://github.com/vllm-project/vllm/pull/7018) and [PR 7142](https://github.com/vllm-project/vllm/pull/7142) seem to have fixed the problem, but vLLM 0.5.5 still have this bug. Exception in worker VllmWorkerProcess while processing method start_worker_execution_loop: CUDA error: an illegal memory access was encountered Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. , Traceback (most recent call last): File "/usr/local/lib/python3.11/site-packages/vllm/executor/multiproc_worker_utils.py", line 223, in _run_worker_process output = executor(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/site-packages/vllm/worker/worker_base.py", line 69, in start_worker_execution_loop output = self.execute_model(execute_model_req=None) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: er_execution_loop: CUDA error: an illegal memory access was encountered Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. , Traceback (most recent call last): File "/usr/local/lib/python3.11/site-packa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: emory access. According to the trackback, this bug seems to be caused by FlashAttention. I notice that [PR 7018](https://github.com/vllm-project/vllm/pull/7018) and [PR 7142](https://github.com/vllm-project/vllm/pull/71...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ine 157, in forward attn_output = self.attn(q, k, v, kv_cache, attn_metadata) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .py", line 69, in start_worker_execution_loop output = self.execute_model(execute_model_req=None) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/site-packages/vllm/worker/worker_base.py", lin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 0.5.5 using prefix caching causing CUDA error: illegal memory access bug;stale ### Your current environment ### 🐛 Describe the bug --enable-prefix-caching causing CUDA error: illegal memory access. According to the trac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
