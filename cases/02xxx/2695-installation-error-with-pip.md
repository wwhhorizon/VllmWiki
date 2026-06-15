# vllm-project/vllm#2695: Installation Error with Pip

| 字段 | 值 |
| --- | --- |
| Issue | [#2695](https://github.com/vllm-project/vllm/issues/2695) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Installation Error with Pip

### Issue 正文摘录

I get the following error while running - `pip install vllm` ``` Collecting vllm Using cached vllm-0.3.0.tar.gz (264 kB) Installing build dependencies ... error error: subprocess-exited-with-error × pip subprocess to install build dependencies did not run successfully. │ exit code: 1 ╰─> [8 lines of output] Collecting ninja Using cached ninja-1.11.1.1-py2.py3-none-macosx_10_9_universal2.macosx_10_9_x86_64.macosx_11_0_arm64.macosx_11_0_universal2.whl.metadata (5.3 kB) Collecting packaging Using cached packaging-23.2-py3-none-any.whl.metadata (3.2 kB) Collecting setuptools>=49.4.0 Using cached setuptools-69.0.3-py3-none-any.whl.metadata (6.3 kB) ERROR: Could not find a version that satisfies the requirement torch==2.1.2 (from versions: 2.2.0) ERROR: No matching distribution found for torch==2.1.2 [end of output] ``` Update: I was using Python 3.12. I downgraded my Python to 3.10 and the issue was resolved (as per the documentation I found on installation [here](https://docs.vllm.ai/en/latest/getting_started/installation.html))

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Installation Error with Pip I get the following error while running - `pip install vllm` ``` Collecting vllm Using cached vllm-0.3.0.tar.gz (264 kB) Installing build dependencies ... error error: subprocess-exited-
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: iversal2.macosx_10_9_x86_64.macosx_11_0_arm64.macosx_11_0_universal2.whl.metadata (5.3 kB) Collecting packaging Using cached packaging-23.2-py3-none-any.whl.metadata (3.2 kB) Collecting setuptools>=49.4.0 Using cached s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: e documentation I found on installation [here](https://docs.vllm.ai/en/latest/getting_started/installation.html))

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
