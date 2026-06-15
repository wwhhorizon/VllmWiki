# vllm-project/vllm#16140: [Bug]: vllm serve hangs indefinitely when --tokenizer-pool-size is greater than one

| 字段 | 值 |
| --- | --- |
| Issue | [#16140](https://github.com/vllm-project/vllm/issues/16140) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;mismatch;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve hangs indefinitely when --tokenizer-pool-size is greater than one

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM serve hangs indefinitely at the log line: when `--tokenizer-pool-size` option is set to a value greater than 0 (the default). Here's the full output of running the following command: ```bash vllm serve Qwen/Qwen2.5-0.5B-Instruct --dtype half --tokenizer-pool-size 1 ``` The trace log file was too big to attach (350 megabytes), but here's the last 100 lines: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding atten...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: the following command: ```bash vllm serve Qwen/Qwen2.5-0.5B-Instruct --dtype half --tokenizer-pool-size 1 ``` The trace log file was too big to attach (350 megabytes), but here's the last 100 lines: ### Before submittin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 's the full output of running the following command: ```bash vllm serve Qwen/Qwen2.5-0.5B-Instruct --dtype half --tokenizer-pool-size 1 ``` The trace log file was too big to attach (350 megabytes), but here's the last 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;crash;import_error;mismatch;nan_inf;o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
