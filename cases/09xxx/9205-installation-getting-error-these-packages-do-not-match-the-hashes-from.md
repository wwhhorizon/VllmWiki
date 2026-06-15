# vllm-project/vllm#9205: [Installation]: Getting "ERROR: THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE..." error

| 字段 | 值 |
| --- | --- |
| Issue | [#9205](https://github.com/vllm-project/vllm/issues/9205) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Getting "ERROR: THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE..." error

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm I used both `pip install vllm` and `pip install https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl` I always get `ERROR: THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE. If you have updated the package versions, please update the hashes. Otherwise, examine the package contents carefully; someone may have tampered with them. unknown package:` I checked some solutions online. I separately tried - Adding `--no-cache-dir` flag during pip install - Upgrading `pip` - Removing `~/.cache/pip` directory - Running `pip cache purge` However, II get the same error. Does anyone face this issue? Could you help me? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Getting "ERROR: THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE..." error installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es. Otherwise, examine the package contents carefully; someone may have tampered with them. unknown package:` I checked some solutions online. I separately tried - Adding `--no-cache-dir` flag during pip install - Upgra...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: O NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE..." error installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm I used both `pip install vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
