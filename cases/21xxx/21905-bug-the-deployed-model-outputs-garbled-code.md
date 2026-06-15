# vllm-project/vllm#21905: [Bug]: The deployed model outputs garbled code

| 字段 | 值 |
| --- | --- |
| Issue | [#21905](https://github.com/vllm-project/vllm/issues/21905) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The deployed model outputs garbled code

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The output error content is as follows: JMllo 在 oook * oooo 窗口下的性能略优于 RXsso（+o. oo%）。 The correct output should be: JM1100在300 * 300窗口下的性能略优于RX550 This is my startup method: ```bash sudo docker run -d --gpus all \ -p 6611:6611 \ --mount type=bind,source=/home,target=/home \ --mount type=bind,source=/data,target=/data \ --security-opt seccomp=unconfined \ --security-opt apparmor=unconfined -it \ --shm-size '100gb' \ --ulimit memlock=-1 \ --restart unless-stopped \ --name vllm-server \ 769b4c5df41a \ /bin/bash -c "CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server --port 6611 --trust-remote-code --host 0.0.0.0 --model /data/ftp/compute/model-data/models/Qwen/Qwen3-8B --served-model-name local-Qwen3-8B --disable-custom-all-reduce --tensor-parallel-size 1 --max-model-len 8192 --gpu-memory-utilization 0.9 " ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tart unless-stopped \ --name vllm-server \ 769b4c5df41a \ /bin/bash -c "CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server --port 6611 --trust-remote-code --host 0.0.0.0 --model /data/ftp/compute/model-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The deployed model outputs garbled code bug;stale ### Your current environment ### 🐛 Describe the bug The output error content is as follows: JMllo 在 oook * oooo 窗口下的性能略优于 RXsso（+o. oo%）。 The correct output shoul...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: JM1100在300 * 300窗口下的性能略优于RX550 This is my startup method: ```bash sudo docker run -d --gpus all \ -p 6611:6611 \ --mount type=bind,source=/home,target=/home \ --mount type=bind,source=/data,target=/data \ --security-opt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: The deployed model outputs garbled code bug;stale ### Your current environment ### 🐛 Describe the bug The output error content is as follows: JMllo 在 oook * oooo 窗口下的性能略优于 RXsso（+o. oo%）。 The correct output shoul...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
