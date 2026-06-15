# vllm-project/vllm#9389: [Installation]:  Failed building wheel for aiohttp Failed to build aiohttp ERROR: Could not build wheels for aiohttp, which is required to install pyprojec                                                                                                                                                             t.toml-based projects

| 字段 | 值 |
| --- | --- |
| Issue | [#9389](https://github.com/vllm-project/vllm/issues/9389) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]:  Failed building wheel for aiohttp Failed to build aiohttp ERROR: Could not build wheels for aiohttp, which is required to install pyprojec                                                                                                                                                             t.toml-based projects

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Failed building wheel for aiohttp Failed to build aiohttp ERROR: Could not build wheels for aiohttp, which is required to install pyprojec t.toml-based projects ![root@v2631866_ ~_bot 15 10 2024 14_21_44](https://github.com/user-attachments/assets/4cfc4488-001d-4364-af42-20161608f9c3) ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Failed building wheel for aiohttp Failed to build aiohttp ERROR: Could not build wheels for aiohttp, which is required to install pyprojec
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t.toml-based projects installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` Failed building wheel for aiohttp Failed to build aiohttp ERROR: Could not build wheels for aiohttp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
