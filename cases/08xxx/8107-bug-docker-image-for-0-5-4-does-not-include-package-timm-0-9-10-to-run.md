# vllm-project/vllm#8107: [Bug]: Docker image for 0.5.4 does not include package timm==0.9.10 to run MiniCPMV

| 字段 | 值 |
| --- | --- |
| Issue | [#8107](https://github.com/vllm-project/vllm/issues/8107) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Docker image for 0.5.4 does not include package timm==0.9.10 to run MiniCPMV

### Issue 正文摘录

### Your current environment nil ### 🐛 Describe the bug Running [docker image 0.5.4](https://hub.docker.com/layers/vllm/vllm-openai/v0.5.4/images/sha256-7ab0cf7b287876cec65752a1b7ac99790ecd2a609da80c4d1dd1fbeaf987abf6?context=explore) with the following entrypoint: ``` python3 -m vllm.entrypoints.openai.api_server --port 8088 --load-format auto --gpu-memory-utilization 0.90 --enforce-eager --disable-log-requests --model HwwwH/MiniCPM-V-2 --served-model-name HwwwH/MiniCPM-V-2 --trust-remote-code --max-model-len 4096 --tensor-parallel-size 1 ``` Server errors out with error, [code ref](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/minicpmv.py#L759): ``` install timm==0.9.10 ``` Willing to create MR for fix ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Docker image for 0.5.4 does not include package timm==0.9.10 to run MiniCPMV bug ### Your current environment nil ### 🐛 Describe the bug Running [docker image 0.5.4](https://hub.docker.com/layers/vllm/vllm-openai...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nt: ``` python3 -m vllm.entrypoints.openai.api_server --port 8088 --load-format auto --gpu-memory-utilization 0.90 --enforce-eager --disable-log-requests --model HwwwH/MiniCPM-V-2 --served-model-name HwwwH/MiniCPM-V-2 -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: fix ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -format auto --gpu-memory-utilization 0.90 --enforce-eager --disable-log-requests --model HwwwH/MiniCPM-V-2 --served-model-name HwwwH/MiniCPM-V-2 --trust-remote-code --max-model-len 4096 --tensor-parallel-size 1 ``` Ser...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
