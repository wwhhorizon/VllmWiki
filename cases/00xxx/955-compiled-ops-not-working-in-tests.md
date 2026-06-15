# vllm-project/vllm#955: Compiled ops not working in tests.

| 字段 | 值 |
| --- | --- |
| Issue | [#955](https://github.com/vllm-project/vllm/issues/955) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Compiled ops not working in tests.

### Issue 正文摘录

Hi there, So i'm building vllm using the `nvcr.io/nvidia/cuda:11.8.0-devel-ubuntu22.04` docker image (with python 3.10 and conda installed also) I'm creating a conda environment using: ``` conda create --name vllm python==3.10 ``` Then installing into this conda environment using: ``` pip install -e . pip install -r requirements-dev.txt ``` However when I try to run the tests `pytest .`, all of the compiled kernels throw exceptions: ``` ImportError while importing test module '/mnt/fast/home/bam4d/vllm/tests/kernels/test_activation.py'. Hint: make sure your test modules/packages have valid Python names. Traceback: ../.conda/envs/vllm/lib/python3.10/importlib/__init__.py:126: in import_module return _bootstrap._gcd_import(name[level:], package, level) tests/kernels/test_activation.py:4: in from vllm import activation_ops E ImportError: /mnt/fast/home/bam4d/vllm/vllm/activation_ops.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv ``` Any ideas?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Compiled ops not working in tests. Hi there, So i'm building vllm using the `nvcr.io/nvidia/cuda:11.8.0-devel-ubuntu22.04` docker image (with python 3.10 and conda installed also) I'm creating a conda environment using
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: king in tests. Hi there, So i'm building vllm using the `nvcr.io/nvidia/cuda:11.8.0-devel-ubuntu22.04` docker image (with python 3.10 and conda installed also) I'm creating a conda environment using: ``` conda create --...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Compiled ops not working in tests. Hi there, So i'm building vllm using the `nvcr.io/nvidia/cuda:11.8.0-devel-ubuntu22.04` docker image (with python 3.10 and conda installed also) I'm creating a conda environment using:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
