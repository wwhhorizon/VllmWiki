# vllm-project/vllm#39279: [Bug]: vllm.entrypoints.chat_utils.ChatTemplateResolutionError: As of transformers v4.44, default chat template is no longer allowed, so you must provide a chat template if the tokenizer does not define one.

| 字段 | 值 |
| --- | --- |
| Issue | [#39279](https://github.com/vllm-project/vllm/issues/39279) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm.entrypoints.chat_utils.ChatTemplateResolutionError: As of transformers v4.44, default chat template is no longer allowed, so you must provide a chat template if the tokenizer does not define one.

### Issue 正文摘录

### Your current environment vllm:v0.19.0 ### 🐛 Describe the bug using vllm 0.19.0，upgrade transformers to 5.5.0 - - command: - /bin/sh - -c - | pip install transformers>=5.5.0 \ exec python3 -m vllm.entrypoints.openai.api_server \ --host "0.0.0.0" \ --port "8000" \ --model /models/gemma-4-31B/ \ --served-model-name local-gemma4-31b \ --enable-chunked-prefill \ --gpu-memory-utilization "0.87" \ --tensor-parallel-size "4" \ --trust-remote-code \ --max-model-len "131072" \ --uvicorn-log-level warning \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --reasoning-parser gemma4 \ --limit-mm-per-prompt '{"image": 15, "audio": 1}' \ --async-scheduling \ --default-chat-template-kwargs '{"enable_thinking": true}' request error: vllm.entrypoints.chat_utils.ChatTemplateResolutionError: As of transformers v4.44, default chat template is no longer allowed, so you must provide a chat template if the tokenizer does not define one. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: --host "0.0.0.0" \ --port "8000" \ --model /models/gemma-4-31B/ \ --served-model-name local-gemma4-31b \ --enable-chunked-prefill \ --gpu-memory-utilization "0.87" \ --tensor-parallel-size "4"
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: --served-model-name local-gemma4-31b \ --enable-chunked-prefill \ --gpu-memory-utilization "0.87" \ --tensor-parallel-size "4" \ --trust-remote-code \ --max-model-len "131072" \ --uvicorn-log-leve
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: - /bin/sh - -c - | pip install transformers>=5.5.0 \ exec python3 -m vllm.entrypoints.openai.api_server \ --host "0.0.0.0" \ --port "8000" \ --model /models/gemma-4-31B/ \
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: 0.0.0" \ --port "8000" \ --model /models/gemma-4-31B/ \ --served-model-name local-gemma4-31b \ --enable-chunked-prefill \ --gpu-memory-utilization "0.87" \ --tensor-parallel-size "4" \

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
