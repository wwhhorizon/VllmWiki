# vllm-project/vllm#1589: Support both CUDA 11.8 and CUDA 12.1

| 字段 | 值 |
| --- | --- |
| Issue | [#1589](https://github.com/vllm-project/vllm/issues/1589) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Support both CUDA 11.8 and CUDA 12.1

### Issue 正文摘录

Hi vLLM maintainers. I suggest maintaining compatibility with torch 2.0.1 and CUDA 11.8.0 for a few more versions. The way this would work is that you create two versions of the wheel: - PyPi: torch 2.1.0 and CUDA 12.1.1 wheel - GitHub release: additional torch 2.0.1 and CUDA 11.8.0 wheel The idea is that people can still install vLLM from the GitHub release if they do not have the latest CUDA version yet. This can be achieved by the following: ```python VLLM_VERSION = "0.2.2" PYPI_BUILD = os.getenv("PYPI_BUILD", "0") == "1" if not PYPI_BUILD: try: CUDA_VERSION = "".join(os.environ.get("CUDA_VERSION", torch.version.cuda).split("."))[:3] VLLM_VERSION += f"+cu{CUDA_VERSION}" except Exception as ex: raise RuntimeError("Your system must have an Nvidia GPU for installing vLLM") ``` In the GitHub workflow, add a conditional on which and check if the current CUDA version being used to build is the same as the one you want to release on PyPi. ``` if ( $env:CUDA_VERSION -eq $env:PYPI_CUDA_VERSION ){ $env:PYPI_BUILD = 1 } ``` For reference, you can look at `setup.py` and `build.yaml` in AutoAWQ. https://github.com/casper-hansen/AutoAWQ/blob/main/.github/workflows/build.yaml _Originally post...

## 现有链接修复摘要

#1596 Build CUDA11.8 wheels for release

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: aintaining compatibility with torch 2.0.1 and CUDA 11.8.0 for a few more versions. The way this would work is that you create two versions of the wheel: - PyPi: torch 2.1.0 and CUDA 12.1.1 wheel - GitHub release: additi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Support both CUDA 11.8 and CUDA 12.1 Hi vLLM maintainers. I suggest maintaining compatibility with torch 2.0.1 and CUDA 11.8.0 for a few more versions. The way this would work is that you create two versions of the whee...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: can still install vLLM from the GitHub release if they do not have the latest CUDA version yet. This can be achieved by the following: ```python VLLM_VERSION = "0.2.2" PYPI_BUILD = os.getenv("PYPI_BUILD", "0") == "1" if...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#1596](https://github.com/vllm-project/vllm/pull/1596) | closes_keyword | 0.95 | Build CUDA11.8 wheels for release | Closes #1589 This PR is to build and attach CUDA 11.8 version of vLLM wheels when creating a new release. The CUDA 11.8 wheels will be named like `vllm-0.2.2+cu118-cp310-cp310- |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
