# vllm-project/vllm#12153: [Performance]: Very low generation throughput on CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#12153](https://github.com/vllm-project/vllm/issues/12153) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Very low generation throughput on CPU

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am deploying vLLM API server with `ibm-granite/granite-3.1-8b-instruct` model on an Ubuntu server with only CPUs available. I noticed that the average generation throughput is as low as 0.1 token/s as shown below in the logs, plus it took 10 mins from "Added request" to actually generation (which was spent for prompt processing I believe?) ``` INFO 01-17 07:46:18 engine.py:270] Added request chatcmpl-522a81bb1b6d4e6196db0786acf51046. WARNING 01-17 07:57:05 _logger.py:72] Pin memory is not supported on CPU. INFO 01-17 07:57:05 metrics.py:467] Avg prompt throughput: 0.1 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. INFO 01-17 07:57:22 metrics.py:467] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. INFO 01-17 07:57:37 metrics.py:467] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.1 tokens/s, R...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: the image to deploy using https://github.com/vllm-project/vllm/blob/main/Dockerfile.cpu, just updated the model. `docker build -f Dockerfile.cpu -t vllm-cpu-env-granite --shm-size=60g .` And run the image with below con...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: Very low generation throughput on CPU performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am deployi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: am deploying vLLM API server with `ibm-granite/granite-3.1-8b-instruct` model on an Ubuntu server with only CPUs available. I noticed that the average generation throughput is as low as 0.1 token/s as shown below in the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Very low generation throughput on CPU performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am deployi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ory ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
