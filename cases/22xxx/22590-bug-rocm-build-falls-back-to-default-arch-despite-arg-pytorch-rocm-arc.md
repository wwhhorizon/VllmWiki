# vllm-project/vllm#22590: [Bug]: ROCm build falls back to default arch despite ARG_PYTORCH_ROCM_ARCH set in Dockerfile.rocm

| 字段 | 值 |
| --- | --- |
| Issue | [#22590](https://github.com/vllm-project/vllm/issues/22590) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ROCm build falls back to default arch despite ARG_PYTORCH_ROCM_ARCH set in Dockerfile.rocm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Description of the issue As the title suggests, the ROCm build falls back to default arch despite `ARG_PYTORCH_ROCM_ARCH` set in `Dockerfile.rocm`. The `GPU_TARGETS` is not set when setup.py is ran. I did not want to just reply to this related [Issue #20984](https://github.com/vllm-project/vllm/issues/20984), because mine affects dockerfiles. # Steps to recreate the issue ```shell rm -rf vllm git clone https://github.com/vllm-project/vllm.git cd vllm podman build \ --no-cache \ --format docker \ --build-arg ARG_PYTORCH_ROCM_ARCH="gfx1030" \ --tag localhost/vllm:latest \ --file docker/Dockerfile.rocm \ . ``` # Quick and dirty fix for my specific GPU arch Obviously, this is not the final solution. ```shell rm -rf vllm git clone https://github.com/vllm-project/vllm.git cd vllm # force CMake to use specified GPU_TARGETS sed -i '/verbose = envs.VERBOSE/i \ \ \ \ \ \ \ \ cmake_args += ['\''-DGPU_TARGETS=gfx1030'\'']' setup.py podman build \ --no-cache \ --format docker \ --build-arg ARG_PYTORCH_ROCM_ARCH="gfx1030" \ --tag localhost/vllm:latest \ --file docker/Dockerfile.rocm \ . ``` ### Before submitting a new issue... - [x] Make sur...

## 现有链接修复摘要

#20988 [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | #31079 Fix ROCm build to respect PYTORCH_ROCM_ARCH for GPU_TARGETS (issue #22590)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: ROCm build falls back to default arch despite ARG_PYTORCH_ROCM_ARCH set in Dockerfile.rocm bug;rocm;stale ### Your current environment ### 🐛 Describe the bug # Description of the issue As the title suggests, the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: ROCm build falls back to default arch despite ARG_PYTORCH_ROCM_ARCH set in Dockerfile.rocm bug;rocm;stale ### Your current environment ### 🐛 Describe the bug # Description of the issue As the title suggests, the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: hub.com/vllm-project/vllm.git cd vllm podman build \ --no-cache \ --format docker \ --build-arg ARG_PYTORCH_ROCM_ARCH="gfx1030" \ --tag localhost/vllm:latest \ --file docker/Dockerfile.rocm \ . ``` # Quick and dirty fix...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: fault arch despite ARG_PYTORCH_ROCM_ARCH set in Dockerfile.rocm bug;rocm;stale ### Your current environment ### 🐛 Describe the bug # Description of the issue As the title suggests, the ROCm build falls back to default a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: --build-arg ARG_PYTORCH_ROCM_ARCH="gfx1030" \ --tag localhost/vllm:latest \ --file docker/Dockerfile.rocm \ . ``` # Quick and dirty fix for my specific GPU arch Obviously, this is not the final solution. ```shell rm -rf...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20988](https://github.com/vllm-project/vllm/pull/20988) | mentioned | 0.6 | [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | st 7 days to test True Positives ``` Found 4 issues to process: 1. #22590: [Bug]: ROCm build falls back to default arch despite ARG_PYT... [bug, rocm] 2. #22458: [Feature]: Please… |
| [#31079](https://github.com/vllm-project/vllm/pull/31079) | closes_keyword | 0.95 | Fix ROCm build to respect PYTORCH_ROCM_ARCH for GPU_TARGETS (issue #22590) | Fixes #22590 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
