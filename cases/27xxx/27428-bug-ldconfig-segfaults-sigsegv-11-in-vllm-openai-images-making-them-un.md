# vllm-project/vllm#27428: [Bug]: ldconfig segfaults (SIGSEGV 11) in vllm-openai images, making them unusable for non-root Singularity users

| 字段 | 值 |
| --- | --- |
| Issue | [#27428](https://github.com/vllm-project/vllm/issues/27428) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ldconfig segfaults (SIGSEGV 11) in vllm-openai images, making them unusable for non-root Singularity users

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using Singularity on a HPC. The `vllm/vllm-openai:v0.11.0` and `vllm/vllm-openai:latest` Docker images are unusable in standard non-root environments (like HPC clusters) due to a segfault in `ldconfig`. When the container starts, torch.inductor (a dependency) tries to check for system libraries by running `/sbin/ldconfig -p`. This command immediately crashes with a `Segmentation Fault (SIGSEGV 11)`. This strongly indicates the container image was built with a corrupt `/etc/ld.so.cache` file. This bug creates a catch-22 for non-root users: The container won't run because `ldconfig` crashes. The user cannot fix the corrupt cache file because they don't have `sudo` or `--fakeroot` permissions to run `rm /etc/ld.so.cache && ldconfig` inside the container. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: on a HPC. The `vllm/vllm-openai:v0.11.0` and `vllm/vllm-openai:latest` Docker images are unusable in standard non-root environments (like HPC clusters) due to a segfault in `ldconfig`. When the container starts, torch.i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: ldconfig segfaults (SIGSEGV 11) in vllm-openai images, making them unusable for non-root Singularity users bug;stale ### Your current environment ### 🐛 Describe the bug I am using Singularity on a HPC. The `vllm/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: m-openai images, making them unusable for non-root Singularity users bug;stale ### Your current environment ### 🐛 Describe the bug I am using Singularity on a HPC. The `vllm/vllm-openai:v0.11.0` and `vllm/vllm-openai:la...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
