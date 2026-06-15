# vllm-project/vllm#18466: [Bug][Failing Test] distributed tests (4 GPUS) - v1/test_async_llm_dp.py::test_load

| 字段 | 值 |
| --- | --- |
| Issue | [#18466](https://github.com/vllm-project/vllm/issues/18466) |
| 状态 | closed |
| 标签 | bug;ci-failure |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;kernel;moe;quantization;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug][Failing Test] distributed tests (4 GPUS) - v1/test_async_llm_dp.py::test_load

### Issue 正文摘录

### Your current environment Still failing on main as of commit 0c15c2e486 ### 🐛 Describe the bug Failing tests: https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests?branch=main&period=2days&query=test_async_llm_dp&commit=Search ``` FAILED v1/test_async_llm_dp.py::test_load[RequestOutputKind.DELTA] - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause. FAILED v1/test_async_llm_dp.py::test_load[RequestOutputKind.FINAL_ONLY] - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #18543 [Bugfix] Use random hidden states in dummy sampler run

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: est] distributed tests (4 GPUS) - v1/test_async_llm_dp.py::test_load bug;ci-failure ### Your current environment Still failing on main as of commit 0c15c2e486 ### 🐛 Describe the bug Failing tests: https://buildkite.com/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tes/ci-1/tests?branch=main&period=2days&query=test_async_llm_dp&commit=Search ``` FAILED v1/test_async_llm_dp.py::test_load[RequestOutputKind.DELTA] - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: on_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory cache;cuda;kernel;moe;quantization;sampling build_error;crash;mismatch dtype;env_dependency #4 Use F...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: orrectness attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory cache;cuda;kernel;moe;quantization;sampling build_error;crash;mismatch dtype;env_d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: sync_llm_dp&commit=Search ``` FAILED v1/test_async_llm_dp.py::test_load[RequestOutputKind.DELTA] - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | xdc253 (0x7f57129b3253 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #4: <unknown function> + 0x94ac3 (0x7f58141a2ac3 in /lib/x86_64-linux-gnu/libc.so.6) frame #5: clone + 0x44 (… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x7f572269ee8d in /usr/local/lib/python3.12/dist-pack… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdc253 (0x7f57129b3253 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unknown… |
| [#18543](https://github.com/vllm-project/vllm/pull/18543) | closes_keyword | 0.95 | [Bugfix] Use random hidden states in dummy sampler run | FIX #18466 FIX #18498 FIX #18525 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
