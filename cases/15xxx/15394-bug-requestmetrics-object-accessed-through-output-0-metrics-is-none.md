# vllm-project/vllm#15394: [Bug]: RequestMetrics object (accessed through output[0].metrics) is None

| 字段 | 值 |
| --- | --- |
| Issue | [#15394](https://github.com/vllm-project/vllm/issues/15394) |
| 状态 | closed |
| 标签 | bug;good first issue;feature request;unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RequestMetrics object (accessed through output[0].metrics) is None

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I try to access the `RequestMetrics` object (through e.g, `output[0].metrics`), it is `None`. I can only access it when I try a Speculative Decoding configuration. Example code to reproduce it: ```python from vllm import LLM llm = LLM( model="facebook/opt-125m", ) outputs = llm.generate("Hello, world!") assert outputs[0].metrics is not None print(outputs[0].metrics) ``` Output: ``` DEBUG 03-24 12:09:29 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 03-24 12:09:29 [__init__.py:35] Checking if TPU platform is available. DEBUG 03-24 12:09:29 [__init__.py:45] TPU platform is not available because: No module named 'libtpu' DEBUG 03-24 12:09:29 [__init__.py:53] Checking if CUDA platform is available. DEBUG 03-24 12:09:29 [__init__.py:73] Confirmed CUDA platform is available. DEBUG 03-24 12:09:29 [__init__.py:101] Checking if ROCm platform is available. DEBUG 03-24 12:09:29 [__init__.py:115] ROCm platform is not available because: No module named 'amdsmi' DEBUG 03-24 12:09:29 [__init__.py:123] Checking if HPU platform is available. DEBUG 03-24 12:09:29 [__init__.py:130] HPU platform is not available becaus...

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 9: [Bug]: RequestMetrics object (accessed through output[0].metrics) is None bug;good first issue;feature request;unstale ### Your current environment ### 🐛 Describe the bug When I try to access the `RequestMetrics` object...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: oding configuration. Example code to reproduce it: ```python from vllm import LLM llm = LLM( model="facebook/opt-125m", ) outputs = llm.generate("Hello, world!") assert outputs[0].metrics is not None print(outputs[0].me...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: module named 'libtpu' DEBUG 03-24 12:09:29 [__init__.py:53] Checking if CUDA platform is available. DEBUG 03-24 12:09:29 [__init__.py:73] Confirmed CUDA platform is available. DEBUG 03-24 12:09:29 [__init__.py:101] Chec...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: n cache): DEBUG 03-24 12:09:41 [backends.py:370] /home/search/minos/vllm-benchmarks/vllm/lib/python3.12/site-packages/torch/_dynamo/polyfills/builtins.py DEBUG 03-24 12:09:41 [backends.py:370] /home/search/minos/vllm-be...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 140 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15394">#15394</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15394">#15394</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15394">#15394</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15394">#15394</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15394">#15394</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
