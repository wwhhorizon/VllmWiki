# vllm-project/vllm#16058: [Bug]: [V1][Speculative Decoding] Broadcasting error (`ValueError`) and socket error (`ZMQError`) using `[ngram]` decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#16058](https://github.com/vllm-project/vllm/issues/16058) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [V1][Speculative Decoding] Broadcasting error (`ValueError`) and socket error (`ZMQError`) using `[ngram]` decoding

### Issue 正文摘录

### Your current environment I'm using the latest `vllm/vllm-openai:v0.8.2` docker image. ### 🐛 Describe the bug I'm running `[ngram]` speculative decoding on `vllm` `v1` using the following parameters on a fine-tuned [Llama-3.2-3B](https://huggingface.co/meta-llama/Llama-3.2-3B): ``` args: ["--model", "/models", "--disable-log-requests", "--disable-uvicorn-access-log","--max-model-len", "350", "--tensor-parallel-size", "1", "--port", "8080", "--speculative-model", "[ngram]", "--num-speculative-tokens", "3", "--ngram-prompt-lookup-max", "4", "--ngram-prompt-lookup-min", "3"] ``` The deployment runs stable at ~350 RPS, but it occasionally crashes with the following two errors, * `error 1`: `ValueError: could not broadcast input array from shape (3,) into shape (2,)`, followed by * `error 2`: `Exception in ASGI application` and `zmq.error.ZMQError: Socket operation on non-socket`. #### Stack trace `error 1`: ``` ERROR 04-04 03:08:52 [core.py:343] EngineCore hit an exception: Traceback (most recent call last): ERROR 04-04 03:08:52 [core.py:343] File \"/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py\", line 336, in run_engine_core ERROR 04-04 03:08:52 [core.py:343] engi...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: [V1][Speculative Decoding] Broadcasting error (`ValueError`) and socket error (`ZMQError`) using `[ngram]` decoding bug ### Your current environment I'm using the latest `vllm/vllm-openai:v0.8.2` docker image. ##...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: decoding on `vllm` `v1` using the following parameters on a fine-tuned [Llama-3.2-3B](https://huggingface.co/meta-llama/Llama-3.2-3B): ``` args: ["--model", "/models", "--disable-log-requests", "--disable-uvicorn-access...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ceive, sender) File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 714, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/routing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Your current environment I'm using the latest `vllm/vllm-openai:v0.8.2` docker image. ### 🐛 Describe the bug I'm running `[ngram]` speculative decoding on `vllm` `v1` using the following parameters on a fine-tuned [Llam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: p! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
