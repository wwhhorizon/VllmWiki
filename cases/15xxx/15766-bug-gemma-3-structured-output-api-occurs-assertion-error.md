# vllm-project/vllm#15766: [Bug]: gemma 3 structured output api occurs assertion error

| 字段 | 值 |
| --- | --- |
| Issue | [#15766](https://github.com/vllm-project/vllm/issues/15766) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gemma 3 structured output api occurs assertion error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use vllm v0.8.2 with docker compose, to test structured output api on gemma-3-27b-it, and get this errror. ``` vllm-llm-1 | ERROR 03-30 02:15:01 [engine.py:160] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/guided_decoding/xgrammar_decoding.py", line 355, in __call__ vllm-llm-1 | ERROR 03-30 02:15:01 [engine.py:160] assert self.matchers[i].accept_token(sampled_token) vllm-llm-1 | ERROR 03-30 02:15:01 [engine.py:160] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ vllm-llm-1 | ERROR 03-30 02:15:01 [engine.py:160] AssertionError vllm-llm-1 | CRITICAL 03-30 02:15:01 [launcher.py:116] MQLLMEngine is already dead, terminating server process ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r current environment ### 🐛 Describe the bug I use vllm v0.8.2 with docker compose, to test structured output api on gemma-3-27b-it, and get this errror. ``` vllm-llm-1 | ERROR 03-30 02:15:01 [engine.py:160] File "/usr/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: gemma 3 structured output api occurs assertion error bug;structured-output;stale ### Your current environment ### 🐛 Describe the bug I use vllm v0.8.2 with docker compose, to test structured output api on gemma-3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory attention;cache;cuda;operator;quantization;sampling crash;slowdown dtype;env_dependency Your current...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: mma 3 structured output api occurs assertion error bug;structured-output;stale ### Your current environment ### 🐛 Describe the bug I use vllm v0.8.2 with docker compose, to test structured output api on gemma-3-27b-it,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
