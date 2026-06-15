# vllm-project/vllm#32651: [Bug]: v0.13 CPU fails with more than 16 OMP threads

| 字段 | 值 |
| --- | --- |
| Issue | [#32651](https://github.com/vllm-project/vllm/issues/32651) |
| 状态 | closed |
| 标签 | bug;stale;cpu |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.13 CPU fails with more than 16 OMP threads

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash vllm bench throughput --model TinyLlama/TinyLlama-1.1B-Chat-v0.6 --input-len 256 --output-len 256 --num-prompts=1000 ``` Allocates 32 threads (32 cores on one die, which is OK) and then sits there doing nothing. There are periodic messages that 256 tokens are being processed and 744 are enqueued. ```bash taskset -c 0-31:2 vllm bench throughput --model TinyLlama/TinyLlama-1.1B-Chat-v0.6 --input-len 256 --output-len 256 --num-prompts=1000 ``` Allocates 16 threads and then proceeds as normal. Similar experiments with any other thread number limiting method yield the same result - up to 16 OMP threads - works, 17 or more - soft hang. The API server is responding, there are messages on the console, but no processing whatsoever. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: v0.13 CPU fails with more than 16 OMP threads bug;stale;cpu ### Your current environment ### 🐛 Describe the bug ```bash vllm bench throughput --model TinyLlama/TinyLlama-1.1B-Chat-v0.6 --input-len 256 --output-le...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: environment ### 🐛 Describe the bug ```bash vllm bench throughput --model TinyLlama/TinyLlama-1.1B-Chat-v0.6 --input-len 256 --output-len 256 --num-prompts=1000 ``` Allocates 32 threads (32 cores on one die, which is OK)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Your current environment ### 🐛 Describe the bug ```bash vllm bench throughput --model TinyLlama/TinyLlama-1.1B-Chat-v0.6 --input-len 256 --output-len 256 --num-prompts=1000 ``` Allocates 32 threads (32 cores on one die,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
