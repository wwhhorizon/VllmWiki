# vllm-project/vllm#23252: [Bug]: VLLM TPU docker image includes ~3GB of pip cache.

| 字段 | 值 |
| --- | --- |
| Issue | [#23252](https://github.com/vllm-project/vllm/issues/23252) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: VLLM TPU docker image includes ~3GB of pip cache.

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug The vllm/vllm-tpu image includes ~3.6 G of extra bloat of pip cache. Dockerfile: https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.tpu Evidence ``` docker run --rm -it --entrypoint=/bin/bash vllm/vllm-tpu:4823ff7989603be3183536268fff79ebdca07a2c root@119d09c98723:/workspace/vllm# du -ah / | sort -rh | head -n 10 ... 3.6G /root/.cache/pip ... ``` ~500GB seems to come from the base image. ``` docker run --rm -it --entrypoint=/bin/bash us-central1-docker.pkg.dev/tpu-pytorch-releases/docker/xla:nightly_3.12_tpuvm root@e50aede2a830:/# du -hs /root/.cache/pip 532M /root/.cache/pip ``` 3 GB was accidentally added due with https://github.com/vllm-project/vllm/pull/17374 since: `pip install` command will install package dependencies, while `python setup.py develop` didn't. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: VLLM TPU docker image includes ~3GB of pip cache. bug;stale ### Your current environment N/A ### 🐛 Describe the bug The vllm/vllm-tpu image includes ~3.6 G of extra bloat of pip cache. Dockerfile: https://github....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 't. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: VLLM TPU docker image includes ~3GB of pip cache. bug;stale ### Your current environment N/A ### 🐛 Describe the bug The vllm/vllm-tpu image includes ~3.6 G of extra bloat of pip cache. Dockerfile: https://github....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
