# vllm-project/vllm#40111: [CI Failure]: Plugin Tests (2 GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#40111](https://github.com/vllm-project/vllm/issues/40111) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Plugin Tests (2 GPUs)

### Issue 正文摘录

### Name of failing test ``` plugins_tests/test_terratorch_io_processor_plugins.py:test_prithvi_mae_plugin_online[ibm-nasa-geospatial/Prithvi-EO-2.0-300M-BurnScars-https://huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2.0-300M-BurnScars/resolve/main/examples/subsetted_512x512_HLS.S30.T10SEH.2018190.v1.4_merged.tif-prithvi_to_tiff-c07f4f602da73552] _ ``` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [Plugin Tests (2 GPUs)](https://buildkite.com/vllm/ci/builds/61575/steps/canvas?sid=019d94e1-7b95-4954-b2b9-1c8c001033c0) fails with ``` [2026-04-17T04:39:06Z] ret = requests.post( [2026-04-17T04:39:06Z] server.url_for("pooling"), [2026-04-17T04:39:06Z] json=request_payload_url, [2026-04-17T04:39:06Z] ) [2026-04-17T04:39:06Z] [2026-04-17T04:39:06Z] response = ret.json() [2026-04-17T04:39:06Z] [2026-04-17T04:39:06Z] # verify the request response is in the correct format [2026-04-17T04:39:06Z] > assert (parsed_response := IOProcessorResponse(**response)) [2026-04-17T04:39:06Z] E pydantic_core._pydantic_core.ValidationError: 1 validation error for IOProcessorResponse [2026-0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Plugin Tests (2 GPUs) ci-failure ### Name of failing test ``` plugins_tests/test_terratorch_io_processor_plugins.py:test_prithvi_mae_plugin_online[ibm-nasa-geospatial/Prithvi-EO-2.0-300M-BurnScars-https://h
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _plugin_online[ibm-nasa-geospatial/Prithvi-EO-2.0-300M-BurnScars-https://huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2.0-300M-BurnScars/resolve/main/examples/subsetted_512x512_HLS.S30.T10SEH.2018190.v1.4_merged.tif-pr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 7f4f602da73552] _ ``` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [Plugin Tests (2 GPUs)](https://bu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -b2b9-1c8c001033c0) fails with ``` [2026-04-17T04:39:06Z] ret = requests.post( [2026-04-17T04:39:06Z] server.url_for("pooling"), [2026-04-17T04:39:06Z] json=request_payload_url, [2026-04-17T04:39:06Z] ) [2026-04-17T04:3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Plugin Tests (2 GPUs) ci-failure ### Name of failing test ``` plugins_tests/test_terratorch_io_processor_plugins.py:test_prithvi_mae_plugin_online[ibm-nasa-geospatial/Prithvi-EO-2.0-300M-BurnScars-https://...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
