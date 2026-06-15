# vllm-project/vllm#15266: [Feature]: Can support CPU inference with Ray cluster?

| 字段 | 值 |
| --- | --- |
| Issue | [#15266](https://github.com/vllm-project/vllm/issues/15266) |
| 状态 | closed |
| 标签 | feature request;ray;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Can support CPU inference with Ray cluster?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Can vllm support CPU inference with Ray cluster now? How to use it? I have Ray cluster with two nodes, as follow: ``` ======== Autoscaler status: 2025-03-21 02:55:20.232713 ======== Node status --------------------------------------------------------------- Active: 1 node_211c6676b30ed72f47827575ebf7360457841df4a44d8a09228163be 1 node_d5b1b2aabbbed13ed9f8cd9111b6818c97e269d1c01c1378fab26e74 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/256.0 CPU 0B/323.77GiB memory 0B/142.75GiB object_store_memory Demands: (no resource demands) ``` And I run vllm at only one node of the ray cluster, by: ``` VLLM_CPU_KVCACHE_SPACE=64 python3 -m vllm.entrypoints.openai.api_server --port 8080 --trust-remote-code --served-model-name QwQ32B --dtype float16 --model /root/LLM/QwQmodelscop/ --tensor-parallel-size 2 ``` When I submit a inference task, there is no resource consume as shown by *ray status*, and only cpus of the one node is busy(100%), the cpu of other nodes is idle(0%). Can vllm support CPU inference with Ray cluster now? How to use it? ### Alternatives _N...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: use it? I have Ray cluster with two nodes, as follow: ``` ======== Autoscaler status: 2025-03-21 02:55:20.232713 ======== Node status --------------------------------------------------------------- Active: 1 node_211c66...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Can support CPU inference with Ray cluster? feature request;ray;stale ### 🚀 The feature, motivation and pitch Can vllm support CPU inference with Ray cluster now? How to use it? I have Ray cluster with two no...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: m.entrypoints.openai.api_server --port 8080 --trust-remote-code --served-model-name QwQ32B --dtype float16 --model /root/LLM/QwQmodelscop/ --tensor-parallel-size 2 ``` When I submit a inference task, there is no resourc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
