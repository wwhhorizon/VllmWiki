# vllm-project/vllm#42358: [Installation]: ERROR: No matching distribution found for vllm==0.20.2+rocm721

| 字段 | 值 |
| --- | --- |
| Issue | [#42358](https://github.com/vllm-project/vllm/issues/42358) |
| 状态 | open |
| 标签 | installation;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: ERROR: No matching distribution found for vllm==0.20.2+rocm721

### Issue 正文摘录

### Your current environment collect_env.py din't work, so i'm on Fedora 44 ### How you are installing vllm ```sh pip install vllm==0.20.2+rocm721 --extra-index-url https://wheels.vllm.ai/rocm/0.20.2/rocm721 ``` as shown on the [official landing page](https://vllm.ai/) ### Comman output ``` Looking in indexes: https://pypi.org/simple, https://wheels.vllm.ai/rocm/0.20.2/rocm721 ERROR: Ignored the following yanked versions: 0.2.1 ERROR: Could not find a version that satisfies the requirement vllm==0.20.2+rocm721 (from versions: 0.0.1, 0.1.0, 0.1.1, 0.1.2, 0.1.3, 0.1.4, 0.1.5, 0.1.6, 0.1.7, 0.2.0, 0.2.1.post1, 0.2.2, 0.2.3, 0.2.4, 0.2.5, 0.2.6, 0.2.7, 0.3.0, 0.3.1, 0.3.2, 0.3.3, 0.4.0, 0.4.0.post1, 0.4.1, 0.4.2, 0.4.3, 0.5.0, 0.5.0.post1, 0.5.1, 0.5.2, 0.5.3, 0.5.3.post1, 0.5.4, 0.5.5, 0.6.0, 0.6.1, 0.6.1.post1, 0.6.1.post2, 0.6.2, 0.6.3, 0.6.3.post1, 0.6.4, 0.6.4.post1, 0.6.5, 0.6.6, 0.6.6.post1, 0.7.0, 0.7.1, 0.7.2, 0.7.3, 0.8.0, 0.8.1, 0.8.2, 0.8.3, 0.8.4, 0.8.5, 0.8.5.post1, 0.9.0, 0.9.0.1, 0.9.1, 0.9.2, 0.10.0, 0.10.1, 0.10.1.1, 0.10.2, 0.11.0, 0.11.1, 0.11.2, 0.12.0, 0.13.0, 0.14.0, 0.14.1, 0.15.0, 0.15.1, 0.16.0, 0.17.0, 0.17.1, 0.18.0, 0.18.1, 0.19.0, 0.19.1, 0.20.0, 0.20.1,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: ERROR: No matching distribution found for vllm==0.20.2+rocm721 installation;rocm ### Your current environment collect_env.py din't work, so i'm on Fedora 44 ### How you are installing vllm ```sh pip ins
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: ERROR: No matching distribution found for vllm==0.20.2+rocm721 installation;rocm ### Your current environment collect_env.py din't work, so i'm on Fedora 44 ### How you are installing vllm ```sh pip inst...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
