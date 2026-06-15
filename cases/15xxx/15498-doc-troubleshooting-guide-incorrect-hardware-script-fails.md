# vllm-project/vllm#15498: [Doc]: Troubleshooting guide incorrect hardware script fails

| 字段 | 值 |
| --- | --- |
| Issue | [#15498](https://github.com/vllm-project/vllm/issues/15498) |
| 状态 | closed |
| 标签 | documentation;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Troubleshooting guide incorrect hardware script fails

### Issue 正文摘录

### 📚 The doc issue The troubleshooting guide to detect incorrect hardware / driver has a [script](https://docs.vllm.ai/en/latest/getting_started/troubleshooting.html#incorrect-hardware-driver) that one can run. The multi-node script fails because of the `c10d` `rdzv_backend`. This issue has been filed in upstream: https://github.com/pytorch/pytorch/issues/85300. The non-leader invocations of the aforementioned script fails with error as follows: ```bash worker # torchrun --nnodes 2 --nproc-per-node=gpu --rdzv_backend=c10d --rdzv_endpoint=leader test.py W0323 01:38:17.786000 275 torch/distributed/run.py:792] W0323 01:38:17.786000 275 torch/distributed/run.py:792] ***************************************** W0323 01:38:17.786000 275 torch/distributed/run.py:792] Setting OMP_NUM_THREADS environment variable for each process to be 1 in default, to avoid your system being overloaded, please further tune the variable for optimal performance in your application as needed. W0323 01:38:17.786000 275 torch/distributed/run.py:792] ***************************************** [W323 01:38:19.204441686 socket.cpp:759] [c10d] The IPv6 network addresses of (leader-6b8cr, 35421) cannot be retrieved (g...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: hat one can run. The multi-node script fails because of the `c10d` `rdzv_backend`. This issue has been filed in upstream: https://github.com/pytorch/pytorch/issues/85300. The non-leader invocations of the aforementioned...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: Troubleshooting guide incorrect hardware script fails documentation;unstale ### 📚 The doc issue The troubleshooting guide to detect incorrect hardware / driver has a [script](https://docs.vllm.ai/en/latest/getting_st...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ect incorrect hardware / driver has a [script](https://docs.vllm.ai/en/latest/getting_started/troubleshooting.html#incorrect-hardware-driver) that one can run. The multi-node script fails because of the `c10d` `rdzv_bac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
