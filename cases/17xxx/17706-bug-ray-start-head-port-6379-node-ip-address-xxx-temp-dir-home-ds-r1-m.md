# vllm-project/vllm#17706: [Bug]: ray start --head --port=6379 --node-ip-address=xxx --temp-dir=/home/ds-r1/models/deploy/ray-temp-log Changing the default log path (/tmp/ray) causes No current placement group found. Creating a new placement group

| 字段 | 值 |
| --- | --- |
| Issue | [#17706](https://github.com/vllm-project/vllm/issues/17706) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ray start --head --port=6379 --node-ip-address=xxx --temp-dir=/home/ds-r1/models/deploy/ray-temp-log Changing the default log path (/tmp/ray) causes No current placement group found. Creating a new placement group

### Issue 正文摘录

### Your current environment Use ray command # Master Node ray start --head --port=6379 --node-ip-address=xxx --temp-dir=/home/ds-r1/models/deploy/ray-temp-log --resources='{"node:xxx": 1}' --dashboard-host=0.0.0.0 --dashboard-port=19127 --min-worker-port=20000 --max-worker-port=30000 # Worker Node ray start --address=xxx.3:6379 --resources='{"node: ": 1}' The above command mainly changes the default /tmp/ray log path ### 🐛 Describe the bug Use ray command # Master Node ray start --head --port=6379 --node-ip-address=xxx --temp-dir=/home/ds-r1/models/deploy/ray-temp-log --resources='{"node:xxx": 1}' --dashboard-host=0.0.0.0 --dashboard-port=19127 --min-worker-port=20000 --max-worker-port=30000 # Worker Node ray start --address=xxx.3:6379 --resources='{"node: ": 1}' The above command mainly changes the default /tmp/ray log path ##execute command vllm serve $model_path \ --port 19125 \ --host 0.0.0.0 \ --tensor-parallel-size 8 \ --max-model-len 128000 \ --max-num-seqs 1024 \ --max-seq-len 16000 \ --enable_expert_parallel \ --pipeline-parallel-size 2 \ --enable-prefix-caching \ --enable-reasoning \ --reasoning-parser deepseek_r1 \ --enable-chunked-prefill \ --max-num-batched-tokens 10...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ay start --head --port=6379 --node-ip-address=xxx --temp-dir=/home/ds-r1/models/deploy/ray-temp-log Changing the default log path (/tmp/ray) causes No current placement group found. Creating a new placement group bug;ra...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: No current placement group found. Creating a new placement group bug;ray;stale ### Your current environment Use ray command # Master Node ray start --head --port=6379 --node-ip-address=xxx --temp-dir=/home/ds-r1/models/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: a3) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: 28000 \ --max-num-seqs 1024 \ --max-seq-len 16000 \ --enable_expert_parallel \ --pipeline-parallel-size 2 \ --enable-prefix-caching \ --enable-reasoning \ --reasoning-parser deepseek_r1 \ --enable-chunked-prefill \ --ma...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
