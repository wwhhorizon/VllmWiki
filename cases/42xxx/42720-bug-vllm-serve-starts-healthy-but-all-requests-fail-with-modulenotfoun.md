# vllm-project/vllm#42720: [Bug]: vllm serve starts healthy but all requests fail with ModuleNotFoundError when using --prefix-caching-hash-algo xxhash or xxhash_cbor without xxhash installed

| 字段 | 值 |
| --- | --- |
| Issue | [#42720](https://github.com/vllm-project/vllm/issues/42720) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve starts healthy but all requests fail with ModuleNotFoundError when using --prefix-caching-hash-algo xxhash or xxhash_cbor without xxhash installed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving with `--prefix-caching-hash-algo xxhash` or `--prefix-caching-hash-algo xxhash_cbor` and the `xxhash` package is not installed, vLLM starts up successfully and reports healthy, but every inference request fails at runtime with a `ModuleNotFoundError`. The missing dependency is never checked at startup or config validation time, so the server appears ready but is completely non-functional. This is more severe than a startup crash: users see a healthy server, `/v1/models` returns 200, and there is no indication anything is wrong until the first request arrives and returns HTTP 500. ## Steps to Reproduce **Step 1: ensure `xxhash` is not installed** ```bash pip uninstall xxhash -y ``` **Case 1: `--prefix-caching-hash-algo xxhash`** ```bash vllm serve \ --host 127.0.0.1 \ --port 20818 \ --prefix-caching-hash-algo xxhash ``` **Case 2: `--prefix-caching-hash-algo xxhash_cbor`** ```bash vllm serve \ --host 127.0.0.1 \ --port 20819 \ --prefix-caching-hash-algo xxhash_cbor ``` Both commands start successfully and log `Application startup complete`. Then send an inference request: ```bash curl -s http://127.0.0.1: /v1/chat/comp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: en using --prefix-caching-hash-algo xxhash or xxhash_cbor without xxhash installed bug ### Your current environment ### 🐛 Describe the bug When serving with `--prefix-caching-hash-algo xxhash` or `--prefix-caching-hash-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: te. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: `, or 2. `xxhash` is included as a required dependency in vLLM's package metadata so it is always available when either option is used. In either case, a server that cannot process any requests must not be allowed to re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: uleNotFoundError`. The missing dependency is never checked at startup or config validation time, so the server appears ready but is completely non-functional. This is more severe than a startup crash: users see a health...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm serve starts healthy but all requests fail with ModuleNotFoundError when using --prefix-caching-hash-algo xxhash or xxhash_cbor without xxhash installed bug ### Your current environment ### 🐛 Describe the bu...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
