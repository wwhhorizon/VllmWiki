# vllm-project/vllm#11072: [Bug]: vllm serve kv cache does not seem to persist properly across requests

| 字段 | 值 |
| --- | --- |
| Issue | [#11072](https://github.com/vllm-project/vllm/issues/11072) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve kv cache does not seem to persist properly across requests

### Issue 正文摘录

### Your current environment ### Model Input Dumps N/A ### 🐛 Describe the bug I am troubleshooting some log TTFT issues in my environment and it appears to me that the problem is that the KV cache is not being persisted across multiple requests in a conversation. I am using LibreChat as a front end to multiple LLMs, one of which is a local LLM (Llama3.3 Q4_K_M GGUF) running on an A6000 GPU using 'vllm serve'. I am running server with the following command line. ```text vllm serve ./Llama-3.3-70B-Instruct-Q4_K_M.gguf --served-model-name Llama-3.3-70B-Instruct-Q4_K_M --max-num-seqs 8 --max-model-len 4096 --enable-prefix-caching ``` The model is from bartowski/Llama-3.3-70B-Instruct-GGUF on hugging face. Initially I was seeing 45 seconds of latency before first token on every request in every chat. After enabling prefix caching I found that the fist 'new chat' after the model starts up would take 45 seconds to return the first token however the subsequent 'new chats' would return the first token in a few seconds (yay, system prompt caching is working) this is backed up by the vllm output showing the prefix cache hit ratio being positive. The problem that I have now is that every requ...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: vllm serve kv cache does not seem to persist properly across requests bug;stale ### Your current environment ### Model Input Dumps N/A ### 🐛 Describe the bug I am troubleshooting some log TTFT issues in my enviro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: te me a haiku about a cat? Assistant:Whiskers softly fall Moonlight dancing on her back Furry midnight queen ``` So it seems like once the conversation is added to, we loose the advantage of the prefix-caching, or the c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: vllm serve kv cache does not seem to persist properly across requests bug;stale ### Your current environment ### Model Input Dumps N/A ### 🐛 Describe the bug I am troubleshooting some log TTFT issues in my enviro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: properly across requests bug;stale ### Your current environment ### Model Input Dumps N/A ### 🐛 Describe the bug I am troubleshooting some log TTFT issues in my environment and it appears to me that the problem is that...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
