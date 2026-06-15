# vllm-project/vllm#16540: [Bug]: vllm gives 400 bad request with high logprob count on Mistral-small because pydantic flags logits of byte tokens as invalid

| 字段 | 值 |
| --- | --- |
| Issue | [#16540](https://github.com/vllm-project/vllm/issues/16540) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: vllm gives 400 bad request with high logprob count on Mistral-small because pydantic flags logits of byte tokens as invalid

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Unfortunately just starting up the vllm server and sending a request that causes the bug doesn't seem to reproduce it, yet if I run my ReAct LLM agent for a while I will eventually reach a state where pydantic flags one of the logits returned by the mock OpenAI API as invalid for the schema. I assume what's going on here is someone set pydantic to flag anything that's not a string as an invalid token and it turns out that some models like Mistral-small can return partial UTF-8 as bytes, breaking it. I am running VLLM with these settings: ``` python -m vllm.entrypoints.openai.api_server --model "mistralai/Mistral-Small-3.1-24B-Instruct-2503" --served-model-name "mistralai/Mistral-Small-3.1-24B-Instruct-2503" --max-logprobs 100 --gpu-memory-utilization=0.9 --disable-log-requests --disable-log-stats --port 5001 --tensor-parallel-size 8 --max-num-seqs 512 --enable-prefix-caching --max-model-len 131072 --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral ``` And my error looks like this: ``` With logprobs = 100 {'object': 'error', 'message': "1 validation error for CompletionLogProbs\ntop_l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 400} ``` When I reach the bugged state of the server this code is sufficient to reproduce the issue (external file for the .json because it's 70k characters and I'm not sure how sensitive the formatting is to reproduce...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: thing that's not a string as an invalid token and it turns out that some models like Mistral-small can return partial UTF-8 as bytes, breaking it. I am running VLLM with these settings: ``` python -m vllm.entrypoints.op...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: vllm gives 400 bad request with high logprob count on Mistral-small because pydantic flags logits of byte tokens as invalid bug;stale ### Your current environment ### 🐛 Describe the bug Unfortunately just startin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vllm gives 400 bad request with high logprob count on Mistral-small because pydantic flags logits of byte tokens as invalid bug;stale ### Your current environment ### 🐛 Describe the bug Unfortunately just startin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
