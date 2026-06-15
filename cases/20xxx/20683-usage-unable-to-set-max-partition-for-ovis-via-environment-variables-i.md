# vllm-project/vllm#20683: [Usage]: Unable to set MAX_PARTITION for OVIS via environment variables in vllm serve

| 字段 | 值 |
| --- | --- |
| Issue | [#20683](https://github.com/vllm-project/vllm/issues/20683) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Unable to set MAX_PARTITION for OVIS via environment variables in vllm serve

### Issue 正文摘录

### Your current environment ‘’‘ export NPROC_PER_NODE=1 export CUDA_VISIBLE_DEVICES=1 export MAX_PARTITION=4 vllm serve ${MODEL_PATH} --host 0.0.0.0 --tensor-parallel-size 1 --trust-remote-code --port 8056 --max-model-len 32768 --gpu-memory-utilization 0.9 --max-num-batched-tokens 8192 ‘’‘’ I’m trying to configure the OVIS model with a specific `MAX_PARTITION` value. I attempted to pass this parameter via an environment variable when starting the server with `vllm serve`, but it does not seem to take effect. Could you please advise on the correct way to set `MAX_PARTITION` for an OVIS model when using `vllm serve`? Or is there an alternative recommended approach? Thanks for your help! ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tched-tokens 8192 ‘’‘’ I’m trying to configure the OVIS model with a specific `MAX_PARTITION` value. I attempted to pass this parameter via an environment variable when starting the server with `vllm serve`, but it does...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e;stale ### Your current environment ‘’‘ export NPROC_PER_NODE=1 export CUDA_VISIBLE_DEVICES=1 export MAX_PARTITION=4 vllm serve ${MODEL_PATH} --host 0.0.0.0 --tensor-parallel-size 1 --trust-remote-code --port 8056 --ma...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ODE=1 export CUDA_VISIBLE_DEVICES=1 export MAX_PARTITION=4 vllm serve ${MODEL_PATH} --host 0.0.0.0 --tensor-parallel-size 1 --trust-remote-code --port 8056 --max-model-len 32768 --gpu-memory-utilization 0.9 --max-num-ba...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: set MAX_PARTITION for OVIS via environment variables in vllm serve usage;stale ### Your current environment ‘’‘ export NPROC_PER_NODE=1 export CUDA_VISIBLE_DEVICES=1 export MAX_PARTITION=4 vllm serve ${MODEL_PATH} --hos...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
