# vllm-project/vllm#24006: [Bug]: Gemma3n audio path crashes when input_features is a list not a Tensor.

| 字段 | 值 |
| --- | --- |
| Issue | [#24006](https://github.com/vllm-project/vllm/issues/24006) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma3n audio path crashes when input_features is a list not a Tensor.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug * In `gemma3n_mm.py::_process_audio_input` we call: `audio_input["input_features"].squeeze(1)` * For batched audio requests, `input_features` arrives as a Python list → `AttributeError: 'list' object has no attribute 'squeeze'` → EngineCore dies. * Result: repeated HTTP 500s on `/v1/chat/completions` and NCCL shutdown warning. *Logs attached below.* ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cache...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e call: `audio_input["input_features"].squeeze(1)` * For batched audio requests, `input_features` arrives as a Python list → `AttributeError: 'list' object has no attribute 'squeeze'` → EngineCore dies. * Result: repeat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cache;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf;slow...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Gemma3n audio path crashes when input_features is a list not a Tensor. bug ### Your current environment ### 🐛 Describe the bug * In `gemma3n_mm.py::_process_audio_input` we call: `audio_input["input_features"].squ

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
