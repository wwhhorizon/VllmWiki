# vllm-project/vllm#17557: [Bug]: Function calling does not work with Mistral Small

| 字段 | 值 |
| --- | --- |
| Issue | [#17557](https://github.com/vllm-project/vllm/issues/17557) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Function calling does not work with Mistral Small

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using a tool (in my case is calling a tool on librechat with a mcp server) I always get this error. Tried to add vllm chat template found on vllm repos but it's the same behaviour. Running vllm with this command line ``` python3 -m vllm.entrypoints.openai.api_server --model mistralai/Mistral-Small-3.1-24B-Instruct-2503 --download-dir /models --gpu-memory-utilization 0.95 --tensor-parallel-size 2 --enable-auto-tool-choice --tool-call-parser mistral --tokenizer_mode mistral --config_format mistral --load_format mistral ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Function calling does not work with Mistral Small bug ### Your current environment ### 🐛 Describe the bug When using a tool (in my case is calling a tool on librechat with a mcp server) I always get this error. T...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: th this command line ``` python3 -m vllm.entrypoints.openai.api_server --model mistralai/Mistral-Small-3.1-24B-Instruct-2503 --download-dir /models --gpu-memory-utilization 0.95 --tensor-parallel-size 2 --enable-auto-to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
