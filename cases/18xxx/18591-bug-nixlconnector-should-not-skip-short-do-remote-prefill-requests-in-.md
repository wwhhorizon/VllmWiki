# vllm-project/vllm#18591: [Bug]: NixlConnector should not skip short do_remote_prefill requests in connector metadata

| 字段 | 值 |
| --- | --- |
| Issue | [#18591](https://github.com/vllm-project/vllm/issues/18591) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NixlConnector should not skip short do_remote_prefill requests in connector metadata

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `pytest -v -x v1/kv_connector/unit/test_nixl_connector.py::test_prompt_less_than_block_size` was failed (#18490). https://github.com/vllm-project/vllm/pull/18429 wanted to fix it by skipping adding this request into the connector's metadata. But the failure reason is the unit test has not been updated to due the changes in NixlConnectorSheduler. The short (promot < block_size) `do_remote_prefill` request should be copied into the connector's metadata with an empty `local_block_ids`, so that NixlConnectorWorker can skip (async) reading remote kv blocks, but still be able to [send notificaiton to the prefill worker to release its remote kv blocks](https://github.com/vllm-project/vllm/blob/9c1baa5bc6caedabeac1a6da57ec79b41e13056d/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py#L733-L735). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error;na...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: NixlConnector should not skip short do_remote_prefill requests in connector metadata bug ### Your current environment ### 🐛 Describe the bug `pytest -v -x v1/kv_connector/unit/test_nixl_connector.py::test_prompt_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 5). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: lConnector should not skip short do_remote_prefill requests in connector metadata bug ### Your current environment ### 🐛 Describe the bug `pytest -v -x v1/kv_connector/unit/test_nixl_connector.py::test_prompt_less_than_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
