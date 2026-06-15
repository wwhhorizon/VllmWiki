# vllm-project/vllm#28996: [Usage]: How to run a single data parallel deployment across multiple nodes without ray

| 字段 | 值 |
| --- | --- |
| Issue | [#28996](https://github.com/vllm-project/vllm/issues/28996) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to run a single data parallel deployment across multiple nodes without ray

### Issue 正文摘录

### Your current environment 2 Nodes, each node has 8 H20 GPUs. ### How would you like to use vllm According to https://docs.vllm.ai/en/latest/serving/data_parallel_deployment/#internal-load-balancing ```shell # node0 vllm serve Qwen3-Coder-480B-A35B-Instruct --trust-remote-code --max-num-seqs 64 --max-model-len 131072 --port $PORT0 --host :: --data-parallel-size 2 --data-parallel-size-local 1 --data-parallel-address $NODE0_IPV6 --data-parallel-rpc-port $PORT1 # node1 vllm serve Qwen3-Coder-480B-A35B-Instruct --trust-remote-code --max-num-seqs 64 --max-model-len 131072 --headless --data-parallel-size 2 --data-parallel-size-local 1 --data-parallel-start-rank 1 --data-parallel-address $NODE0_IPV6 --data-parallel-rpc-port $NODE0_PORT1 ``` but all of them are hanging on waiting for init message from front-end. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: arallel_deployment/#internal-load-balancing ```shell # node0 vllm serve Qwen3-Coder-480B-A35B-Instruct --trust-remote-code --max-num-seqs 64 --max-model-len 131072 --port $PORT0 --host :: --data-parallel-size 2 --data-p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s.vllm.ai/en/latest/serving/data_parallel_deployment/#internal-load-balancing ```shell # node0 vllm serve Qwen3-Coder-480B-A35B-Instruct --trust-remote-code --max-num-seqs 64 --max-model-len 131072 --port $PORT0 --host...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nd. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: --data-parallel-rpc-port $NODE0_PORT1 ``` but all of them are hanging on waiting for init message from front-end. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: # How would you like to use vllm According to https://docs.vllm.ai/en/latest/serving/data_parallel_deployment/#internal-load-balancing ```shell # node0 vllm serve Qwen3-Coder-480B-A35B-Instruct --trust-remote-code --max...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
