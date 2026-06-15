# vllm-project/vllm#9113: [Performance] In v0.6.2, when tp=1, TPOT becomes very slow for batch sizes of 10 or so. (not happened in v0.5.5)

| 字段 | 值 |
| --- | --- |
| Issue | [#9113](https://github.com/vllm-project/vllm/issues/9113) |
| 状态 | closed |
| 标签 | performance;unstale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance] In v0.6.2, when tp=1, TPOT becomes very slow for batch sizes of 10 or so. (not happened in v0.5.5)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug In vLLM v0.6.2, when tp=1, TPOT becomes very slow for batch sizes of 10 or so. The vLLM arguments are as follows. ``` --model - /data/models/llama-3-8b-instruct/base --tensor-parallel-size - “1” --load-format - “auto” --max-model-len - “8192” --disable-log-requests --uvicorn-log-level - “warning” image: aspcr01-queffmyz.scr.skr-west.scp-in.com/serving/vllm:v0.6.2 ``` I tested with the same load in v0.5.5, and it handled fine. When I looked at why it was slowing down, I realized that I was using very little GPU resources and only using 100% of the CPU cores. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;slowdown env_dependency;shape Y...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ened in v0.5.5) performance;unstale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug In vLLM v0.6.2, when tp=1, TPOT becomes very slow for batch sizes of 10 or so. The vLLM argumen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: slow for batch sizes of 10 or so. (not happened in v0.5.5) performance;unstale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug In vLLM v0.6.2, when tp=1, TPOT becomes very slow fo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Performance] In v0.6.2, when tp=1, TPOT becomes very slow for batch sizes of 10 or so. (not happened in v0.5.5) performance;unstale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
