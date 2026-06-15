# vllm-project/vllm#7479: [Bug]: aqlm test failing on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#7479](https://github.com/vllm-project/vllm/issues/7479) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: aqlm test failing on H100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The following test fails on an H100 system. It gets 7 of the 8 prompts correct. ``` pytest -s tests/models/test_aqlm.py::test_models[1-16-half-ISTA-DASLab/Llama-2-7b-AQLM-2Bit-1x16-hf] ``` I'm not sure if it is expected to work or not.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: -1x16-hf] ``` I'm not sure if it is expected to work or not. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: n H100 system. It gets 7 of the 8 prompts correct. ``` pytest -s tests/models/test_aqlm.py::test_models[1-16-half-ISTA-DASLab/Llama-2-7b-AQLM-2Bit-1x16-hf] ``` I'm not sure if it is expected to work or not. correctness...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: aqlm test failing on H100 bug;stale ### Your current environment ### 🐛 Describe the bug The following test fails on an H100 system. It gets 7 of the 8 prompts correct. ``` pytest -s tests/models/test_aqlm.py::tes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: aqlm test failing on H100 bug;stale ### Your current environment ### 🐛 Describe the bug The following test fails on an H100 system. It gets 7 of the 8 prompts correct. ``` pytest -s tests/models/test_aqlm.py::tes...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
