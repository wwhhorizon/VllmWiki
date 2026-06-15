# vllm-project/vllm#27992: [Bug]: Encoder cache should not be greater than max model len

| 字段 | 值 |
| --- | --- |
| Issue | [#27992](https://github.com/vllm-project/vllm/issues/27992) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Encoder cache should not be greater than max model len

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running Qwen3-8B-VL with the command `vllm serve Qwen/Qwen3-VL-8B-Instruct-FP8 --max-model-len 32768 --gpu-memory-utilization 0.86 --host 0.0.0.0 --port 8100` we see in the startup logs INFO 11-03 12:02:17 [gpu_model_runner.py:3344] Encoder cache will be initialized with a budget of 153600 tokens, and profiled with 1 video items of the maximum feature size. which causes ~10GB of memory to be allocated, even though our max request length can only be 32k. This seems to be a bug, unless the encoder cache length is not tied to the max model length in any way. If it is separate, then can a max-encoder-cache-len flag be made so we can set it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;samp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ning Qwen3-8B-VL with the command `vllm serve Qwen/Qwen3-VL-8B-Instruct-FP8 --max-model-len 32768 --gpu-memory-utilization 0.86 --host 0.0.0.0 --port 8100` we see in the startup logs INFO 11-03 12:02:17 [gpu_model_runne...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Encoder cache should not be greater than max model len bug ### Your current environment ### 🐛 Describe the bug When running Qwen3-8B-VL with the command `vllm serve Qwen/Qwen3-VL-8B-Instruct-FP8 --max-model-len 3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: size. which causes ~10GB of memory to be allocated, even though our max request length can only be 32k. This seems to be a bug, unless the encoder cache length is not tied to the max model length in any way. If it is se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
