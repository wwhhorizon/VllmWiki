# vllm-project/vllm#3668: [Installation]: Subprocess error with setuptools regarding PyTorch version when using Python 3.12

| 字段 | 值 |
| --- | --- |
| Issue | [#3668](https://github.com/vllm-project/vllm/issues/3668) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Subprocess error with setuptools regarding PyTorch version when using Python 3.12

### Issue 正文摘录

### Your current environment ```text Collecting vllm Downloading vllm-0.3.3.tar.gz (315 kB) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 315.2/315.2 kB 11.0 MB/s eta 0:00:00 Installing build dependencies ... error error: subprocess-exited-with-error × pip subprocess to install build dependencies did not run successfully. │ exit code: 1 ╰─> [8 lines of output] Collecting ninja Using cached ninja-1.11.1.1-py2.py3-none-manylinux1_x86_64.manylinux_2_5_x86_64.whl.metadata (5.3 kB) Collecting packaging Using cached packaging-24.0-py3-none-any.whl.metadata (3.2 kB) Collecting setuptools>=49.4.0 Downloading setuptools-69.2.0-py3-none-any.whl.metadata (6.3 kB) ERROR: Could not find a version that satisfies the requirement torch==2.1.2 (from versions: 2.2.0, 2.2.1, 2.2.2) ERROR: No matching distribution found for torch==2.1.2 [end of output] note: This error originates from a subprocess, and is likely not a problem with pip. error: subprocess-exited-with-error × pip subprocess to install build dependencies did not run successfully. │ exit code: 1 ╰─> See above for output. ``` ### How you are installing vllm ```sh pip install vllm ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Subprocess error with setuptools regarding PyTorch version when using Python 3.12 installation ### Your current environment ```text Collecting vllm Downloading vllm-0.3.3.tar.gz (315 kB) ━━━━━━━━━━
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: d ninja-1.11.1.1-py2.py3-none-manylinux1_x86_64.manylinux_2_5_x86_64.whl.metadata (5.3 kB) Collecting packaging Using cached packaging-24.0-py3-none-any.whl.metadata (3.2 kB) Collecting setuptools>=49.4.0 Downloading se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
