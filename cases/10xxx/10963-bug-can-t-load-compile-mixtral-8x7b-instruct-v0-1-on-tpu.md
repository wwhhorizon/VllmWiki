# vllm-project/vllm#10963: [Bug]: Can't load/compile Mixtral-8x7B-Instruct-v0.1 on TPU

| 字段 | 值 |
| --- | --- |
| Issue | [#10963](https://github.com/vllm-project/vllm/issues/10963) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't load/compile Mixtral-8x7B-Instruct-v0.1 on TPU

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ## Can't load/compile `Mixtral-8x7B-Instruct-v0.1` on TPU I'm trying to run `Mixtral-8x7B-Instruct-v0.1` on a TPU `v6e-8` but it fails at the compilation phase - here is the launcher command: ``` vllm serve "mistralai/Mixtral-8x7B-Instruct-v0.1" --download_dir /dev/shm --num-scheduler-steps 4 --swap-space 16 --disable-log-requests --tensor_parallel_size=8 --max-model-len=2048 ``` Here are the error logs - (I uploaded them as the trace is long): [Error-log-short.txt](https://github.com/user-attachments/files/18043616/Error-log-short.txt) Verbose error: [mixtral-error-log-verbose.txt](https://github.com/user-attachments/files/18043639/mixtral-error-log-verbose.txt) My setup: ``` pip list | grep torch torch 2.6.0.dev20241126+cpu torch-xla 2.6.0+git39e67b5 torchvision 0.20.0.dev20241126+cpu pip list | grep libtpu libtpu_nightly 0.1.dev20241122+nightly pip list | grep jax jax 0.4.36.dev20241122 jaxlib 0.4.36.dev20241122 ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page]...

## 现有链接修复摘要

#11764 [Hardware][TPU] workaround fix for MoE on TPU

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Can't load/compile Mixtral-8x7B-Instruct-v0.1 on TPU bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ## Can't load/compile `Mixtral-8x7B-Instruct-v0.1` on TPU I'm tryin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rve "mistralai/Mixtral-8x7B-Instruct-v0.1" --download_dir /dev/shm --num-scheduler-steps 4 --swap-space 16 --disable-log-requests --tensor_parallel_size=8 --max-model-len=2048 ``` Here are the error logs - (I uploaded t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: xtral-8x7B-Instruct-v0.1 on TPU bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ## Can't load/compile `Mixtral-8x7B-Instruct-v0.1` on TPU I'm trying to run `Mixtral-8x7B-Instr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: d_error;nan_inf env_dependency #11764 [Hardware][TPU] workaround fix for MoE on TPU Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#11764](https://github.com/vllm-project/vllm/pull/11764) | closes_keyword | 0.95 | [Hardware][TPU] workaround fix for MoE on TPU | FIX [#10963](https://github.com/vllm-project/vllm/issues/10963) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
