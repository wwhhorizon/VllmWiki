# vllm-project/vllm#3772: [Bug]: n_inner divisible to number of GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#3772](https://github.com/vllm-project/vllm/issues/3772) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: n_inner divisible to number of GPUs

### Issue 正文摘录

### Your current environment I was using the latest docker image(0.4.0) with 4-8L4 GPUs for the mentioned problem. I also tested this with installing from source as well with a custom docker image. ### 🐛 Describe the bug Hello, first of all, thank you for the grand work! I was trying to utilize the recently supported JAIS models. When I try [jais-30b-chat-v3](https://huggingface.co/core42/jais-30b-chat-v3) with 8xL4 GPUs, I was getting the error ```bash ... AssertionError: 19114 is not divisible by 8 [repeated 2x across cluster] ``` I wanted to test the [jais-13b-chat](https://huggingface.co/core42/jais-13b-chat) model for the same purpose to see if I can deploy it to 4xL4 GPUs and I got ```bash ... AssertionError: 13653 is not divisible by 4 [repeated 2x across cluster] ``` Commands that I was utilizing can be generalized along the lines of: ```bash MODEL=core42/jais-30b-chat-v3 NUM_GPUS=8 docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model $MODEL \ --tensor-parallel-size $NUM_GPUS \ --trust-remote-code \ --gpu-memory-utilization 0.95 \ --load-format safetensors \ --served-model-...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: for the grand work! I was trying to utilize the recently supported JAIS models. When I try [jais-30b-chat-v3](https://huggingface.co/core42/jais-30b-chat-v3) with 8xL4 GPUs, I was getting the error ```bash ... Assertion...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: r of GPUs bug;stale ### Your current environment I was using the latest docker image(0.4.0) with 4-8L4 GPUs for the mentioned problem. I also tested this with installing from source as well with a custom docker image. #...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: n_inner divisible to number of GPUs bug;stale ### Your current environment I was using the latest docker image(0.4.0) with 4-8L4 GPUs for the mentioned problem. I also tested this with installing from source as w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: number of GPUs bug;stale ### Your current environment I was using the latest docker image(0.4.0) with 4-8L4 GPUs for the mentioned problem. I also tested this with installing from source as well with a custom docker ima...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
