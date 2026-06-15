# vllm-project/vllm#20476: [RFC]: A developer friendly tool for multi-instance deployment with Ray

| 字段 | 值 |
| --- | --- |
| Issue | [#20476](https://github.com/vllm-project/vllm/issues/20476) |
| 状态 | closed |
| 标签 | RFC;ray;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: A developer friendly tool for multi-instance deployment with Ray

### Issue 正文摘录

### Motivation. Developing, deploying and debugging vLLM in a multi-instance, multi-node environment (disaggregated prefill, DP+EP, load balancing, etc.) is not friendly. You have to start vLLM instances on multiple nodes with scripts, then manually collect the server addresses, and implement a router to schedule the requests. And it takes time to locate the failed instances and relevant logs when errors occur. K8s can be a solution, but it is too heavy for testing or debugging before ready for production. We need a **light-weight**, **developer-oriented** tool to facilitate **developing & testing** in a cluster-wide setting. ### Proposed Change. Add a Ray native deployment tool under vllm/examples, named dllm (deploying vLLM, call for a better name...) maybe. Can be installed locally with pip. **The tool supports:** - Deploy instances on a multi-node Ray cluster with a single command. - Deploy a disaggregated prefill cluster with X prefill instances and Y decode instances. - APIs follow the online serving entrypoints (vllm/entripoints/openai.api_server.py) implementation. - Manage and monitor instances status and logs with Ray Dashboard. - Automatically allocate and reclaim GPU r...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: A developer friendly tool for multi-instance deployment with Ray RFC;ray;stale ### Motivation. Developing, deploying and debugging vLLM in a multi-instance, multi-node environment (disaggregated prefill, DP+EP, load bal...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ces=1 \ --num-decode-instances=1 \ --prefill-command="vllm serve Qwen/Qwen2.5_7B_Instruct -tp=2 --gpu-memory-utilization=0.8 --kv-transfer-config {...} \" --decode-command="vllm serve Qwen/Qwen2.5_7B_Instruct -tp=2 --gp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nstance, multi-node environment (disaggregated prefill, DP+EP, load balancing, etc.) is not friendly. You have to start vLLM instances on multiple nodes with scripts, then manually collect the server addresses, and impl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ith scripts, then manually collect the server addresses, and implement a router to schedule the requests. And it takes time to locate the failed instances and relevant logs when errors occur. K8s can be a solution, but...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
