# vllm-project/vllm#35163: [Bug]: AMD docker image still using torch 2.9 despite 2.10.0 in `requirements/rocm-build.txt`

| 字段 | 值 |
| --- | --- |
| Issue | [#35163](https://github.com/vllm-project/vllm/issues/35163) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: AMD docker image still using torch 2.9 despite 2.10.0 in `requirements/rocm-build.txt`

### Issue 正文摘录

### Your current environment: CI ### 🐛 Describe the bug In the AMD: build_image job I see that torch 2.9.1+git8907517 is being used ``` #16 7.261 Requirement already satisfied: torch>=1.10.0 in /usr/local/lib/python3.12/dist-packages (from xgrammar==0.1.29->-r /app/vllm/requirements/common.txt (line 27)) (2.9.1+git8907517)#16 7.261 Requirement already satisfied: torch>=1.10.0 in /usr/local/lib/python3.12/dist-packages (from xgrammar==0.1.29->-r /app/vllm/requirements/common.txt (line 27)) (2.9.1+git8907517) ``` https://buildkite.com/vllm/amd-ci/builds/5275/steps/canvas?sid=019c8d3c-27b4-4999-957e-14abb27a046f&tab=output#019c8d43-6266-4e6f-9f6f-8846a0e66b0c/L813 If I understand correctly, the AMD: build image job is building pytorch from https://github.com/vllm-project/vllm/blob/22a97e66134a26c74b9dae73d9446c4e32718269/docker/Dockerfile.rocm_base#L4-L5 which is still using a commit from 2.9, even though the rest of CI has been bumped to 2.10 in https://github.com/vllm-project/vllm/pull/30525. This seems like a bug to me as requirements/rocm-build.txt has been updated to 2.10.0 https://github.com/vllm-project/vllm/blob/main/requirements/rocm-build.txt This is blocking for me as I am...

## 现有链接修复摘要

#16 Add custom kernel for RMS normalization

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: AMD docker image still using torch 2.9 despite 2.10.0 in `requirements/rocm-build.txt` bug;rocm ### Your current environment: CI ### 🐛 Describe the bug In the AMD: build_image job I see that torch 2.9.1+git890751...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: : AMD docker image still using torch 2.9 despite 2.10.0 in `requirements/rocm-build.txt` bug;rocm ### Your current environment: CI ### 🐛 Describe the bug In the AMD: build_image job I see that torch 2.9.1+git8907517 is...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: hub.com/vllm-project/vllm/blob/main/requirements/rocm-build.txt This is blocking for me as I am migrating the CUDA kernels in this repo to the libtorch stable ABI and the PRs require >=torch 2.10. Some of these kernels...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;hardware_porting cuda;kernel build_error env_dependency #16 Add...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | 29->-r /app/vllm/requirements/common.txt (line 27)) (2.9.1+git8907517)#16 7.261 requirement already satisfied: torch>=1.10.0 in /usr/local/lib/python3.12/dist-packages (from xgram… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
