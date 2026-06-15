# vllm-project/vllm#9615: [Bug]: Broken outputs for large contexts if `max_model_len` is fixed.

| 字段 | 值 |
| --- | --- |
| Issue | [#9615](https://github.com/vllm-project/vllm/issues/9615) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Broken outputs for large contexts if `max_model_len` is fixed.

### Issue 正文摘录

[model_input.txt](https://github.com/user-attachments/files/17492230/model_input.txt) ### Your current environment ### Model Input Dumps Model input is attached in model_input.txt Model output: ` // TODO("` Ground_truth: ` navigationTarget (` ### 🐛 Describe the bug I generted code using `deepseek-ai/deepseek-coder-1.3b-base` model with long context. I fix rather large `max_model_len = 16600` and input sequence length is `16000`, `max_tokens = 100`. In this case the generation is broken, does not correspond to ground truth at all (mainly generates "TODO"). The problem can be fixed by adding and setting other parameter `max_seq_len_to_capture` equal to `max_model_len`. There is no this issue if the context length is smaller - less than 8000 tokens. I use the following arguments: ``` from vllm import LLM generation_engine = LLM( hf_model_path=deepseek-ai/deepseek-coder-1.3b-base, max_model_len=16600, ) sampling_params = SamplingParams( temperature: 0.0 max_tokens: 100 min_tokens: 5 stop: ["\n"]) ``` I use version 0.6.3. GPU - single RTX 4090 (24Gb) Is it a bug or I am using it wrong? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and as...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: - less than 8000 tokens. I use the following arguments: ``` from vllm import LLM generation_engine = LLM( hf_model_path=deepseek-ai/deepseek-coder-1.3b-base, max_model_len=16600, ) sampling_params = SamplingParams( temp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: qual to `max_model_len`. There is no this issue if the context length is smaller - less than 8000 tokens. I use the following arguments: ``` from vllm import LLM generation_engine = LLM( hf_model_path=deepseek-ai/deepse...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Broken outputs for large contexts if `max_model_len` is fixed. bug;stale [model_input.txt](https://github.com/user-attachments/files/17492230/model_input.txt) ### Your current environment ### Model Input Dumps Mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Bug]: Broken outputs for large contexts if `max_model_len` is fixed. bug;stale [model_input.txt](https://github.com/user-attachments/files/17492230/model_input.txt) ### Your current environment ### Model Input Dumps Mod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error env_dependency [model_input.txt](https://github.com/user-attachments/files/17492230/model_input.txt)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
