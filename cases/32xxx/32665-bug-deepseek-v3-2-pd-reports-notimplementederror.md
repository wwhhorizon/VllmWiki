# vllm-project/vllm#32665: [Bug]: [DeepSeek-V3.2] PD reports `NotImplementedError`

| 字段 | 值 |
| --- | --- |
| Issue | [#32665](https://github.com/vllm-project/vllm/issues/32665) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [DeepSeek-V3.2] PD reports `NotImplementedError`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When starting vllm with the following command: ```shell vllm serve --port=8312 --gpu-memory-utilization=0.85 --tokenizer-mode=deepseek_v32 --enable-expert-parallel --model /home/ubuntu/DeepSeek-V3.2 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' -tp 2 -dp 4 -dpl 2 -dpa xx.xx.xxx.xx-dpr 0 ``` It reports `NotImplementedError` error: ``` (Worker_DP1_TP1_EP3 pid=486380) ERROR 01-20 12:14:56 [multiproc_executor.py:839] Traceback (most recent call last): (Worker_DP1_TP1_EP3 pid=486380) ERROR 01-20 12:14:56 [multiproc_executor.py:839] File "/root/workspaces/kebe/vllm/vllm/v1/executor/multiproc_executor.py", line 834, in worker_busy_loop (Worker_DP1_TP1_EP3 pid=486380) ERROR 01-20 12:14:56 [multiproc_executor.py:839] output = func(*args, **kwargs) (Worker_DP1_TP1_EP3 pid=486380) ERROR 01-20 12:14:56 [multiproc_executor.py:839] ^^^^^^^^^^^^^^^^^^^^^ (Worker_DP1_TP1_EP3 pid=486380) ERROR 01-20 12:14:56 [multiproc_executor.py:839] File "/root/workspaces/kebe/vllm/vllm/v1/worker/worker_base.py", line 320, in initialize_from_config (Worker_DP1_TP1_EP3 pid=486380) ERROR 01-20 12:14:56 [multiproc_executor.py:839] se...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tilization=0.85 --tokenizer-mode=deepseek_v32 --enable-expert-parallel --model /home/ubuntu/DeepSeek-V3.2 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' -tp 2 -dp 4 -dpl 2 -dpa xx.xx.xxx.xx-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: P3 pid=486380) ERROR 01-20 12:14:56 [multiproc_executor.py:839] self.backend_name = backend.get_name() (Worker_DP1_TP1_EP3 pid=486380) ERROR 01-20 12:14:56 [multiproc_executor.py:839] ^^^^^^^^^^^^^^^^^^ (Worker_DP1_TP1_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: od. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: 312 --gpu-memory-utilization=0.85 --tokenizer-mode=deepseek_v32 --enable-expert-parallel --model /home/ubuntu/DeepSeek-V3.2 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' -tp 2 -dp 4 -dpl 2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
