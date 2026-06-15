# vllm-project/vllm#27815: [Bug]: torch.compile startup time logging not correct

| 字段 | 值 |
| --- | --- |
| Issue | [#27815](https://github.com/vllm-project/vllm/issues/27815) |
| 状态 | open |
| 标签 | bug;torch.compile;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: torch.compile startup time logging not correct

### Issue 正文摘录

### Your current environment n/a ### 🐛 Describe the bug @mgoin mentioned on slack: Looking at some of the slow tests in CI, I’ve found that there seems to be a large discrepancy with how much time torch.compile says it takes versus how long it actually takes I’ve attached a section from this test for quantization/test_torchao.py::test_qwenvl_int8wo_model_loading_with_params https://buildkite.com/organizations/vllm/pipelines/ci/builds/35163/jobs/0199eb2d-ccf5-462f-9c44-834b47fbac0f/log#203-4688 If we zoom in, it say compiling the dynamic graph takes 41s and in total takes 47s, but in the time between those two logs, it is clear that 8 minutes have passed! ``` [2025-10-16T06:08:44Z] (EngineCore_DP0 pid=23579) INFO 10-15 23:08:44 [backends.py:247] Cache the graph for dynamic shape for later use [2025-10-16T06:09:23Z] (EngineCore_DP0 pid=23579) INFO 10-15 23:09:23 [backends.py:274] Compiling a graph for dynamic shape takes 41.40 s [2025-10-16T06:17:21Z] (EngineCore_DP0 pid=23579) INFO 10-15 23:17:21 [monitor.py:33] torch.compile takes 47.72 s in total ``` Do we have any ideas why this might be happening? ### Before submitting a new issue... - [x] Make sure you already searched for rel...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: torch.compile startup time logging not correct bug;torch.compile;stale ### Your current environment n/a ### 🐛 Describe the bug @mgoin mentioned on slack: Looking at some of the slow tests in CI, I’ve found that t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: attached a section from this test for quantization/test_torchao.py::test_qwenvl_int8wo_model_loading_with_params https://buildkite.com/organizations/vllm/pipelines/ci/builds/35163/jobs/0199eb2d-ccf5-462f-9c44-834b47fbac...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ` [2025-10-16T06:08:44Z] (EngineCore_DP0 pid=23579) INFO 10-15 23:08:44 [backends.py:247] Cache the graph for dynamic shape for later use [2025-10-16T06:09:23Z] (EngineCore_DP0 pid=23579) INFO 10-15 23:09:23 [backends.p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s how long it actually takes I’ve attached a section from this test for quantization/test_torchao.py::test_qwenvl_int8wo_model_loading_with_params https://buildkite.com/organizations/vllm/pipelines/ci/builds/35163/jobs/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
