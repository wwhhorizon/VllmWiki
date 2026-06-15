# vllm-project/vllm#25108: [Bug]: vLLM chat breaks during multi-turn chat

| 字段 | 值 |
| --- | --- |
| Issue | [#25108](https://github.com/vllm-project/vllm/issues/25108) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM chat breaks during multi-turn chat

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM chat breaks on trivial multi-turn chats. I was testing out vLLM chat using `meta-llama/Llama-3.1-8B-Instruct` and serving it via `vllm serve meta-llama/Llama-3.1-8B-Instruct`. After giving it the following simple input, it crashed immediately on only the second turn: ``` vllm chat INFO 09-17 22:27:30 [__init__.py:216] Automatically detected platform cuda. Using model: meta-llama/Llama-3.1-8B-Instruct Please enter a message for the chat model: > Ground control to major tom, your circuit's dead, there's something wrong. Can you hear me Major Tom? Can you hear me Major Tom? Can you hear- I think I can finish the lyrics for you. "Can you hear me Major Tom? Can you hear me Major Tom? Can you hear me Major Tom? (Can you hear me, Major Tom?) Ground Control to Major Tom, your circuit's dead, there's something wrong Can you hear me, Major Tom? Can you hear me, Major Tom? Ground Control to Major Tom, there's something wrong Can you hear me, Major Tom? Can you hear me, Major Tom? There's something wrong Can you hear me, Major Tom? Ground Control to Major Tom" That's a famous song by David Bowie, from his 1969 album "Space Oddity". > I...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: vLLM chat breaks during multi-turn chat bug;stale ### Your current environment ### 🐛 Describe the bug vLLM chat breaks on trivial multi-turn chats. I was testing out vLLM chat using `meta-llama/Llama-3.1-8B-Instr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: enter a message for the chat model: > Ground control to major tom, your circuit's dead, there's something wrong. Can you hear me Major Tom? Can you hear me Major Tom? Can you hear- I think I can finish the lyrics for yo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s on trivial multi-turn chats. I was testing out vLLM chat using `meta-llama/Llama-3.1-8B-Instruct` and serving it via `vllm serve meta-llama/Llama-3.1-8B-Instruct`. After giving it the following simple input, it crashe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 2/site-packages/vllm/entrypoints/cli/main.py", line 54, in main args.dispatch_function(args) File "/mnt/7TB-a/osilkin/non-critical-changes/training_hub/.venv/lib/python3.12/site-packages/vllm/entrypoints/cli/openai.py",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: at INFO 09-17 22:27:30 [__init__.py:216] Automatically detected platform cuda. Using model: meta-llama/Llama-3.1-8B-Instruct Please enter a message for the chat model: > Ground control to major tom, your circuit's dead,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
