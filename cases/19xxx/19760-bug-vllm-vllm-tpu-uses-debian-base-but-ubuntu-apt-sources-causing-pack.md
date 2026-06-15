# vllm-project/vllm#19760: [Bug]: vllm/vllm-tpu uses Debian base but Ubuntu APT sources, causing package installation errors

| 字段 | 值 |
| --- | --- |
| Issue | [#19760](https://github.com/vllm-project/vllm/issues/19760) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm/vllm-tpu uses Debian base but Ubuntu APT sources, causing package installation errors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Description: The vllm/vllm-tpu Docker image appears to be based on Debian (e.g., /etc/debian_version shows bookworm/sid), but the APT package sources point to Ubuntu (e.g., jammy). This inconsistency causes package management failures. Reproduction Steps 1. Pull and run the image: docker run -it vllm/vllm-tpu /bin/bash 2. Inside the container: cat /etc/debian_version # Shows 'bookworm/sid' cat /etc/apt/sources.list # Points to Ubuntu 'jammy' repos apt update && apt install awk 3. This leads to: dpkg-deb: error: ... uses unknown compression for member 'control.tar.zst' E: Sub-process /usr/bin/dpkg returned an error code (1) Impact • Package upgrades and reinstallations fail due to incompatible compression formats. • Standard tooling such as pip, venv, or apt install are affected. • Blocks installing development tools (e.g., gawk, zstd, python3.11-dev). Expected Behavior The base OS and APT sources should match. If the image is based on Debian, the package sources should point to Debian repositories (e.g., deb.debian.org) to ensure compatibility. Suggested Fix Update the image to: • correct /etc/apt/sources.list to point to Debian...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: : vllm/vllm-tpu uses Debian base but Ubuntu APT sources, causing package installation errors bug;stale ### Your current environment ### 🐛 Describe the bug Description: The vllm/vllm-tpu Docker image appears to be based...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: an. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ackage upgrades and reinstallations fail due to incompatible compression formats. • Standard tooling such as pip, venv, or apt install are affected. • Blocks installing development tools (e.g., gawk, zstd, python3.11-de...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ian base but Ubuntu APT sources, causing package installation errors bug;stale ### Your current environment ### 🐛 Describe the bug Description: The vllm/vllm-tpu Docker image appears to be based on Debian (e.g., /etc/de...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
