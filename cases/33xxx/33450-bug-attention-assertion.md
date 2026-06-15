# vllm-project/vllm#33450: [Bug]: Attention Assertion

| 字段 | 值 |
| --- | --- |
| Issue | [#33450](https://github.com/vllm-project/vllm/issues/33450) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Attention Assertion

### Issue 正文摘录

### Your current environment B200 ### 🐛 Describe the bug ``` (Worker_DP0_TP0_EP0 pid=1742344) ERROR 01-30 17:41:21 [multiproc_executor.py:852] assert num_decode_tokens % num_decodes == 0, ( (Worker_DP0_TP0_EP0 pid=1742344) ERROR 01-30 17:41:21 [multiproc_executor.py:852] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_DP0_TP0_EP0 pid=1742344) ERROR 01-30 17:41:21 [multiproc_executor.py:852] AssertionError: TRTLLM decode requires uniform query lengths per request. ``` ``` chg run --gpus 4 -- vllm serve microsoft/Phi-mini-MoE-instruct -dp 2 -tp 2 --enable-expert-parallel --port 8005 --attention-backend FLASHINFER eval: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model={{MODEL}},base_url=http://localhost:{{PORT}}/v1/completions,num_concurrent=1000,tokenized_requests=False" --limit 1000 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Attention Assertion bug ### Your current environment B200 ### 🐛 Describe the bug ``` (Worker_DP0_TP0_EP0 pid=1742344) ERROR 01-30 17:41:21 [multiproc_executor.py:852] assert num_decode_tokens % num_decodes == 0,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: oE-instruct -dp 2 -tp 2 --enable-expert-parallel --port 8005 --attention-backend FLASHINFER eval: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model={{MODEL}},base_url=http://localhost:{{PORT}}/v1...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: per request. ``` ``` chg run --gpus 4 -- vllm serve microsoft/Phi-mini-MoE-instruct -dp 2 -tp 2 --enable-expert-parallel --port 8005 --attention-backend FLASHINFER eval: lm_eval \ --model local-completions \ --tasks gsm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 1742344) ERROR 01-30 17:41:21 [multiproc_executor.py:852] assert num_decode_tokens % num_decodes == 0, ( (Worker_DP0_TP0_EP0 pid=1742344) ERROR 01-30 17:41:21 [multiproc_executor.py:852] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: p 2 --enable-expert-parallel --port 8005 --attention-backend FLASHINFER eval: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model={{MODEL}},base_url=http://localhost:{{PORT}}/v1/completions,num_con...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
