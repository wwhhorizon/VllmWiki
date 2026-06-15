# vllm-project/vllm#12891: [Bug]: Can't deploy DeepSeek R1 with lora failure on vLLM Engine V1

| 字段 | 值 |
| --- | --- |
| Issue | [#12891](https://github.com/vllm-project/vllm/issues/12891) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda |
| 症状 | build_error;crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't deploy DeepSeek R1 with lora failure on vLLM Engine V1

### Issue 正文摘录

### Your current environment and the `DEEPSEEK_VLLM_ENGINE_ARGS` is set to: ```text DEEPSEEK_VLLM_ENGINE_ARGS=--model ${CHAT_COMPLETIONS_DEEPSEEK_MODEL} --tensor-parallel-size 8 --max-model-len 21774 --max-num-batched-token 32368 --max-num-seqs 32 --gpu-memory-utilization 0.7 --enable-chunked-prefill false --enable-prefix-caching --trust-remote-code ``` ### 🐛 Describe the bug ```text ds-chat-completions | CRITICAL 02-07 03:13:57 multiproc_executor.py:48] MulitprocExecutor got fatal signal from worker processes, shutting down. See stack trace above for root cause issue. ds-chat-completions | (VllmWorker rank=6 pid=430) Traceback (most recent call last): ds-chat-completions | (VllmWorker rank=6 pid=430) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap ds-chat-completions | (VllmWorker rank=6 pid=430) self.run() ds-chat-completions | (VllmWorker rank=6 pid=430) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run ds-chat-completions | (VllmWorker rank=6 pid=430) self._target(*self._args, **self._kwargs) ds-chat-completions | (VllmWorker rank=6 pid=430) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;model_support attention;cuda build_error;crash Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: EPSEEK_VLLM_ENGINE_ARGS` is set to: ```text DEEPSEEK_VLLM_ENGINE_ARGS=--model ${CHAT_COMPLETIONS_DEEPSEEK_MODEL} --tensor-parallel-size 8 --max-model-len 21774 --max-num-batched-token 32368 --max-num-seqs 32 --gpu-memor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: en 32368 --max-num-seqs 32 --gpu-memory-utilization 0.7 --enable-chunked-prefill false --enable-prefix-caching --trust-remote-code ``` ### 🐛 Describe the bug ```text ds-chat-completions | CRITICAL 02-07 03:13:57 multipr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ^^^^^^^^^^ ds-chat-completions | (VllmWorker rank=6 pid=430) TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'q_lora_rank' ``` ### Before submitting a new issue... - [x] Make sure you already...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
