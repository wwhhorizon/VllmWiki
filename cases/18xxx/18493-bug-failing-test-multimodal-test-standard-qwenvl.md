# vllm-project/vllm#18493: [Bug][Failing Test]: Multimodal Test (Standard) - QwenVL

| 字段 | 值 |
| --- | --- |
| Issue | [#18493](https://github.com/vllm-project/vllm/issues/18493) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][Failing Test]: Multimodal Test (Standard) - QwenVL

### Issue 正文摘录

### Your current environment - There appears to be an issue with QwenVL - Link: https://buildkite.com/vllm/ci/builds/20415#0196f100-f857-45bf-ae5a-a9e5b90e7f62/199-9633 - Logs: ```bash [2025-05-21T05:05:21Z] FAILED models/multimodal/generation/test_qwen2_vl.py::test_qwen2_vl_image_embeddings_input[10-128-half-size_factors0-Qwen/Qwen2-VL-2B-Instruct] - vllm.worker.model_runner_base.InputProcessingError: Failed to prepare inputs for sequence group with request id: 0, Error: list index out of range -- | [2025-05-21T05:05:21Z] FAILED models/multimodal/generation/test_qwen2_vl.py::test_qwen2_vl_image_embeddings_input[10-128-half-size_factors1-Qwen/Qwen2-VL-2B-Instruct] - vllm.worker.model_runner_base.InputProcessingError: Failed to prepare inputs for sequence group with request id: 0, Error: list index out of range | [2025-05-21T05:05:21Z] FAILED models/multimodal/generation/test_qwen2_vl.py::test_qwen2_vl_image_embeddings_input[10-128-half-size_factors2-Qwen/Qwen2-VL-2B-Instruct] - vllm.worker.model_runner_base.InputProcessingError: Failed to prepare inputs for sequence group with request id: 0, Error: list index out of range | [2025-05-21T05:05:21Z] FAILED models/multimodal/generatio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: # Your current environment - There appears to be an issue with QwenVL - Link: https://buildkite.com/vllm/ci/builds/20415#0196f100-f857-45bf-ae5a-a9e5b90e7f62/199-9633 - Logs: ```bash [2025-05-21T05:05:21Z] FAILED models...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug][Failing Test]: Multimodal Test (Standard) - QwenVL bug ### Your current environment - There appears to be an issue with QwenVL - Link: https://buildkite.com/vllm/ci/builds/20415#0196f100-f857-45bf-ae5a-a9e5b90e7f6...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ove ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e.InputProcessingError: Failed to prepare inputs for sequence group with request id: 0, Error: list index out of range -- | [2025-05-21T05:05:21Z] FAILED models/multimodal/generation/test_qwen2_vl.py::test_qwen2_vl_imag...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug][Failing Test]: Multimodal Test (Standard) - QwenVL bug ### Your current environment - There appears to be an issue with QwenVL - Link: https://buildkite.com/vllm/ci/builds/20415#0196f100-f857-45bf-ae5a-a9e5b90e7f6...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
