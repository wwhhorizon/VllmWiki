# vllm-project/vllm#14416: [Bug]: terminate called after throwing an instance of 'std::system_error'   what():  Operation not permitted

| 字段 | 值 |
| --- | --- |
| Issue | [#14416](https://github.com/vllm-project/vllm/issues/14416) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: terminate called after throwing an instance of 'std::system_error'   what():  Operation not permitted

### Issue 正文摘录

### Your current environment ![Image](https://github.com/user-attachments/assets/7c909f89-89c2-46f7-8855-60010e3236d5) ### 🐛 Describe the bug bash run_cluster.sh m.daocloud.io/docker.io/vllm/vllm-openai xxxx --head /data02/guanli/ds_1.5b/deepseek-ai terminate called after throwing an instance of 'std::system_error' what(): Operation not permitted node node ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 0010e3236d5) ### 🐛 Describe the bug bash run_cluster.sh m.daocloud.io/docker.io/vllm/vllm-openai xxxx --head /data02/guanli/ds_1.5b/deepseek-ai terminate called after throwing an instance of 'std::system_error' what():...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ode ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n instance of 'std::system_error' what(): Operation not permitted bug;stale ### Your current environment ![Image](https://github.com/user-attachments/assets/7c909f89-89c2-46f7-8855-60010e3236d5) ### 🐛 Describe the bug b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
