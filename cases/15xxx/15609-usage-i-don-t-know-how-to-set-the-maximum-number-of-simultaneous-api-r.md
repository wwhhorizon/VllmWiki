# vllm-project/vllm#15609: [Usage]: I don't know how to set the maximum number of simultaneous API requests to be processed when calling an API

| 字段 | 值 |
| --- | --- |
| Issue | [#15609](https://github.com/vllm-project/vllm/issues/15609) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: I don't know how to set the maximum number of simultaneous API requests to be processed when calling an API

### Issue 正文摘录

### Your current environment When I execute the following script docker run --runtime nvidia --gpus all \ -v /home/model-tran/models/DeepSeek-R1-Distill-Qwen-32B/:/deepseek-r1-32b \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HF_HUB_OFFLINE=1" \ -p 8000:8000 \ --ipc=host \ -d \ vllm/vllm-openai:latest \ --gpu-memory-utilization 0.9 \ --tensor-parallel-size 4 \ --max-concurrency 20 \ --model /deepseek-r1-32b appear api_server.py: error: unrecognized arguments: --max-concurrency 20 ### How would you like to use vllm I want to set the maximum concurrent number of requests for external API calls to VLLM models when there are too many requests ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: following script docker run --runtime nvidia --gpus all \ -v /home/model-tran/models/DeepSeek-R1-Distill-Qwen-32B/:/deepseek-r1-32b \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HF_HUB_OFFLINE=1" \ -p 8000...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: usage ### Your current environment When I execute the following script docker run --runtime nvidia --gpus all \ -v /home/model-tran/models/DeepSeek-R1-Distill-Qwen-32B/:/deepseek-r1-32b \ -v ~/.cache/huggingface:/root/....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: sts ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: I don't know how to set the maximum number of simultaneous API requests to be processed when calling an API usage ### Your current environment When I execute the following script docker run --runtime nvidia --g...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 1" \ -p 8000:8000 \ --ipc=host \ -d \ vllm/vllm-openai:latest \ --gpu-memory-utilization 0.9 \ --tensor-parallel-size 4 \ --max-concurrency 20 \ --model /deepseek-r1-32b appear api_server.py: error: unrecognized argumen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
