# vllm-project/vllm#4395: [Installation]: sdist is not available for v0.4.1

| 字段 | 值 |
| --- | --- |
| Issue | [#4395](https://github.com/vllm-project/vllm/issues/4395) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: sdist is not available for v0.4.1

### Issue 正文摘录

https://pypi.org/project/vllm/#files are missing source tarball for the latest release, related to https://github.com/vllm-project/vllm/issues/4181 To check, try installing from the source. ```sh VLLM_TARGET_DEVICE=cpu pip install vllm --no-cache-dir --no-binary :all: ``` ``` Collecting vllm Downloading vllm-0.3.3.tar.gz (315 kB) ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Installation]: sdist is not available for v0.4.1 installation https://pypi.org/project/vllm/#files are missing source tarball for the latest release, related to https://github.com/vllm-project/vllm/issues/4181 To check,
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ttps://pypi.org/project/vllm/#files are missing source tarball for the latest release, related to https://github.com/vllm-project/vllm/issues/4181 To check, try installing from the source. ```sh VLLM_TARGET_DEVICE=cpu p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
