# vllm-project/vllm#28283: [Bug]: nccl stuck issue

| 字段 | 值 |
| --- | --- |
| Issue | [#28283](https://github.com/vllm-project/vllm/issues/28283) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: nccl stuck issue

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using a docker container for vLLM. I noticed that when I use `nvidia/cuda:13.0.X-cudnn-devel-ubuntu24.04` with `tp > 1`, it gets stuck here: `INFO 11-07 09:24:25 [pynccl.py:111] vLLM is using nccl==2.27.5`. But it works fine with `nvidia/cuda:12.9.X-cudnn-devel-ubuntu24.04` because I assume `12.9` is the current default now. My question is: why does the CUDA image version really matter with vLLM? Just asking since I'm not experiencing this with SGLang, where `tp > 1` still works well even if I use either `12.8`, `12.9`, or even `13.0` `nvidia/cuda` image. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: le ### Your current environment ### 🐛 Describe the bug I am using a docker container for vLLM. I noticed that when I use `nvidia/cuda:13.0.X-cudnn-devel-ubuntu24.04` with `tp > 1`, it gets stuck here: `INFO 11-07 09:24:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: am using a docker container for vLLM. I noticed that when I use `nvidia/cuda:13.0.X-cudnn-devel-ubuntu24.04` with `tp > 1`, it gets stuck here: `INFO 11-07 09:24:25 [pynccl.py:111] vLLM is using nccl==2.27.5`. But it wo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: nccl stuck issue bug;stale ### Your current environment ### 🐛 Describe the bug I am using a docker container for vLLM. I noticed that when I use `nvidia/cuda:13.0.X-cudnn-devel-ubuntu24.04` with `tp > 1`, it gets...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
