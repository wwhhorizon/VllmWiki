# vllm-project/vllm#42924: [Bug]: ExampleConnector.start_load_kv hardcodes .cuda() breaking CPU-only deployments

| 字段 | 值 |
| --- | --- |
| Issue | [#42924](https://github.com/vllm-project/vllm/issues/42924) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ExampleConnector.start_load_kv hardcodes .cuda() breaking CPU-only deployments

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py` line 191, `start_load_kv` hardcodes `.cuda()` when loading the saved KV cache: ```python kv_cache = safetensors.torch.load_file(filename)["kv_cache"].cuda() ``` This crashes on CPU-only builds with: AssertionError: Torch not compiled with CUDA enabled The save path (line 256) correctly uses .cpu(), but the load path assumes GPU. *Reproduction* Run prefill + decode disaggregated serving with VLLM_TARGET_DEVICE=cpu and kv_connector: ExampleConnector. The decode worker crashes when attempting to load the KV cache saved by the prefill worker. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#42926 [Bugfix] Use platform-agnostic device in example_connector load | #43007 fix: load example connector kv on target device

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: This crashes on CPU-only builds with: AssertionError: Torch not compiled with CUDA enabled
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Reproduction* Run prefill + decode disaggregated serving with VLLM_TARGET_DEVICE=cpu and kv_co
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: ExampleConnector.start_load_kv hardcodes .cuda() breaking CPU-only deployments bug ### Your current environment ### 🐛 Describe the bug In `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py` line 1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: upport;sampling_logits;speculative_decoding cache;cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency #42926 [Bugfix] Use platform-agnostic device in example_connector load | #43007 fix: load example...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: `start_load_kv` hardcodes `.cuda()` when loading the saved KV cache:

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42926](https://github.com/vllm-project/vllm/pull/42926) | closes_keyword | 0.95 | [Bugfix] Use platform-agnostic device in example_connector load | Fix #42924 In `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py` line 191, `start_load_kv` hardcodes `.cuda()` when loading the saved KV cache: |
| [#43007](https://github.com/vllm-project/vllm/pull/43007) | closes_keyword | 0.95 | fix: load example connector kv on target device | Fixes #42924 ## To verify - `python -m ruff check vllm\distributed\kv_transfer\kv_connector\v1\example_connector.py tests\v1\kv_connector\unit\test_example_connector.py` - `python |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
