# vllm-project/vllm#1807: request a vllm.whl for cuda11.8_torch2.0.1_py39

| 字段 | 值 |
| --- | --- |
| Issue | [#1807](https://github.com/vllm-project/vllm/issues/1807) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> request a vllm.whl for cuda11.8_torch2.0.1_py39

### Issue 正文摘录

hi the authors. Since the latest vllm (0.2.2) for cuda11.8 is built with torch 2.1.0 (which is incompatible with cuda 11.8)， could you please release a vllm.whl that is built with torch 2.0.1 and py39 ? best wishes~

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: request a vllm.whl for cuda11.8_torch2.0.1_py39 hi the authors. Since the latest vllm (0.2.2) for cuda11.8 is built with torch 2.1.0 (which is incompatible with cuda 11.8)， could you please release a vllm.whl that is bu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: request a vllm.whl for cuda11.8_torch2.0.1_py39 hi the authors. Since the latest vllm (0.2.2) for cuda11.8 is built with torch 2.1.0 (which is incompatible with cuda 11.8)， could you please release a vllm.whl that is bu
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: est a vllm.whl for cuda11.8_torch2.0.1_py39 hi the authors. Since the latest vllm (0.2.2) for cuda11.8 is built with torch 2.1.0 (which is incompatible with cuda 11.8)， could you please release a vllm.whl that is built...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
