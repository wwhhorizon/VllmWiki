# vllm-project/vllm#4121: [Misc] [CI]: AMD test flaky on main CI

| 字段 | 值 |
| --- | --- |
| Issue | [#4121](https://github.com/vllm-project/vllm/issues/4121) |
| 状态 | closed |
| 标签 | rocm;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc] [CI]: AMD test flaky on main CI

### Issue 正文摘录

### Anything you want to discuss about vllm. Most recent `main` failure: https://buildkite.com/vllm/ci/builds/4903#018ee887-5a56-431e-9d7c-5a903b095046 Failed yesterday on `main` as well: https://buildkite.com/vllm/ci/builds/4858#018ee579-1bc4-4691-9327-2756e81185e1 ``` torch.cuda.OutOfMemoryError: HIP out of memory. Tried to allocate 4.70 GiB. GPU 0 has a total capacty of 63.98 GiB of which 3.06 GiB is free. Of the allocated memory 51.96 GiB is allocated by PyTorch, and 29.10 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_HIP_ALLOC_CONF ``` ``` Traceback (most recent call last): File "/opt/conda/envs/py_3.9/lib/python3.9/runpy.py", line 197, in _run_module_as_main return _run_code(code, main_globals, None, File "/opt/conda/envs/py_3.9/lib/python3.9/runpy.py", line 87, in _run_code exec(code, run_globals) File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/vllm-0.4.0.post1+rocm603-py3.9-linux-x86_64.egg/vllm/entrypoints/api_server.py", line 106, in engine = AsyncLLMEngine.from_engine_args( File "/opt/conda/envs/py_3.9/lib/python3.9...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Misc] [CI]: AMD test flaky on main CI rocm;stale ### Anything you want to discuss about vllm. Most recent `main` failure: https://buildkite.com/vllm/ci/builds/4903#018ee887-5a56-431e-9d7c-5a903b095046 Failed yesterday...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Misc] [CI]: AMD test flaky on main CI rocm;stale ### Anything you want to discuss about vllm. Most recent `main` failure: https://buildkite.com/vllm/ci/builds/4903#018ee887-5a56-431e-9d7c-5a903b095046 Failed yesterday...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: gg/vllm/engine/llm_engine.py", line 226, in _initialize_kv_caches self.model_executor.initialize_cache(num_gpu_blocks, num_cpu_blocks) File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/vllm-0.4.0.post1+rocm603-py...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc] [CI]: AMD test flaky on main CI rocm;stale ### Anything you want to discuss about vllm. Most recent `main` failure: https://buildkite.com/vllm/ci/builds/4903#018ee887-5a56-431e-9d7c-5a903b095046 Failed yesterday...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: NF ``` performance ci_build;hardware_porting;scheduler_memory cuda crash;oom env_dependency Anything you want to discuss about vllm.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
