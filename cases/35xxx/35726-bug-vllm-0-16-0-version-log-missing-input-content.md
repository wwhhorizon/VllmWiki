# vllm-project/vllm#35726: [Bug]: Vllm 0.16.0 version log missing input content

| 字段 | 值 |
| --- | --- |
| Issue | [#35726](https://github.com/vllm-project/vllm/issues/35726) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Vllm 0.16.0 version log missing input content

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After upgrading vLLM to version 0.16.0, even with the parameters VLLM_LOG_LEVEL=DEBUG --enable-log-requests --enable-log-outputs, the input text is not visible in the logs; only the input parameters (samplingParams) and the output text are displayed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Vllm 0.16.0 version log missing input content bug ### Your current environment ### 🐛 Describe the bug After upgrading vLLM to version 0.16.0, even with the parameters VLLM_LOG_LEVEL=DEBUG --enable-log-requests --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rsion 0.16.0, even with the parameters VLLM_LOG_LEVEL=DEBUG --enable-log-requests --enable-log-outputs, the input text is not visible in the logs; only the input parameters (samplingParams) and the output text are displ...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
