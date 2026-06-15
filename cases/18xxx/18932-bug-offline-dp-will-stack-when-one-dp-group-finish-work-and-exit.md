# vllm-project/vllm#18932: [Bug]: offline dp will stack when one dp group finish work and exit

| 字段 | 值 |
| --- | --- |
| Issue | [#18932](https://github.com/vllm-project/vllm/issues/18932) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: offline dp will stack when one dp group finish work and exit

### Issue 正文摘录

### Your current environment last main ### 🐛 Describe the bug - How to produce: https://github.com/vllm-project/vllm/blob/3de3eadf5b1c271ccd7140526ffb3f850d6b0189/examples/offline_inference/data_parallel.py#L115 condister we have two dp group, first generate 10 tokens, second generate as long as max_model_len(for example, 10000) You will see the first dp group finish and send a sigterm signal to its child proc, causing the scond dp group stack in global comm(for example, global ep comm, global dp comm in set_forward_context). - The reason I investigated: in v1 llm_engine: https://github.com/vllm-project/vllm/blob/3de3eadf5b1c271ccd7140526ffb3f850d6b0189/vllm/v1/engine/llm_engine.py#L78, we do not have a dp_group member for multiprocess mode. and `has_unfinished_requests` https://github.com/vllm-project/vllm/blob/3de3eadf5b1c271ccd7140526ffb3f850d6b0189/vllm/v1/engine/llm_engine.py#L159-L163 will not consider all dp group status. So when the first dp group finish its work in our example, it will exit directly, causing the scond dp group stack. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom ri...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ck. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e two dp group, first generate 10 tokens, second generate as long as max_model_len(for example, 10000) You will see the first dp group finish and send a sigterm signal to its child proc, causing the scond dp group stack...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: o not have a dp_group member for multiprocess mode. and `has_unfinished_requests` https://github.com/vllm-project/vllm/blob/3de3eadf5b1c271ccd7140526ffb3f850d6b0189/vllm/v1/engine/llm_engine.py#L159-L163 will not consid...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
