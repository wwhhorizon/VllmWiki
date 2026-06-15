# vllm-project/vllm#27471: [Bug]: NVFP4A16 spurious warning that GPU doesn't support Fp4

| 字段 | 值 |
| --- | --- |
| Issue | [#27471](https://github.com/vllm-project/vllm/issues/27471) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | kernel;quantization |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NVFP4A16 spurious warning that GPU doesn't support Fp4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When loading a NVFP4A16 quantized model we get a spurious warning ``` (Worker_TP0 pid=201) WARNING 10-24 09:50:14 [marlin_utils_fp4.py:137] Your GPU does not have native support for FP4 computation but FP4 quantization is being used. Weight-only FP4 compression will be used leveraging the Marlin kernel. This may degrade performance for compute-heavy workloads. ``` This is using 2x RTX Pro 6000, which do support Fp4. That warning is coming from https://github.com/vllm-project/vllm/blob/3567816932e674abce3f44ceb0aff03f73b5aaff/vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py#L136-L142 I believe that warning was supposed to be removed when the emulation path for NVFP4A16 was removed in https://github.com/vllm-project/vllm/pull/18000. If so I can submit a simple PR to remove that part. Otherwise does it mean there is a new marlin kernel planned that avoids software-dequantizing of NVFP4? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lot...

## 现有链接修复摘要

#31346 [Bugfix] Remove spurious NVFP4 'GPU does not support FP4' warning

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: NVFP4A16 spurious warning that GPU doesn't support Fp4 bug;stale ### Your current environment ### 🐛 Describe the bug When loading a NVFP4A16 quantized model we get a spurious warning ``` (Worker_TP0 pid=201) WARN...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y degrade performance for compute-heavy workloads. ``` This is using 2x RTX Pro 6000, which do support Fp4. That warning is coming from https://github.com/vllm-project/vllm/blob/3567816932e674abce3f44ceb0aff03f73b5aaff/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: formance frontend_api;model_support;quantization kernel;quantization env_dependency #31346 [Bugfix] Remove spurious NVFP4 'GPU does not support FP4' warning Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nvironment ### 🐛 Describe the bug When loading a NVFP4A16 quantized model we get a spurious warning ``` (Worker_TP0 pid=201) WARNING 10-24 09:50:14 [marlin_utils_fp4.py:137] Your GPU does not have native support for FP4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: NVFP4A16 spurious warning that GPU doesn't support Fp4 bug;stale ### Your current environment ### 🐛 Describe the bug When loading a NVFP4A16 quantized model we get a spurious warning ``` (Worker_TP0 pid=201) WARN...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31346](https://github.com/vllm-project/vllm/pull/31346) | closes_keyword | 0.95 | [Bugfix] Remove spurious NVFP4 'GPU does not support FP4' warning | Fixes #27471 🤖 Generated with [Claude Code](https://claude.com/claude-code) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
