# vllm-project/vllm#10918: [Bug]: Illegal Memory access was encounterd when running UT: pytest -s -v vllm/tests/spec_decode/test_multi_step_worker.py::test_use_draft_model_runner_advance_step

| 字段 | 值 |
| --- | --- |
| Issue | [#10918](https://github.com/vllm-project/vllm/issues/10918) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Illegal Memory access was encounterd when running UT: pytest -s -v vllm/tests/spec_decode/test_multi_step_worker.py::test_use_draft_model_runner_advance_step

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Run NVIDIA Memory Check Command: `compute-sanitizer --tool memcheck --demangle simple pytest -s -v vllm/tests/spec_decode/test_multi_step_worker.py::test_use_draft_model_runner_advance_step` A illegal Memory access was encountered. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: mory access was encounterd when running UT: pytest -s -v vllm/tests/spec_decode/test_multi_step_worker.py::test_use_draft_model_runner_advance_step bug;stale ### Your current environment ### Model Input Dumps _No respon...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t -s -v vllm/tests/spec_decode/test_multi_step_worker.py::test_use_draft_model_runner_advance_step bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Run NVIDIA Memory Chec...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Illegal Memory access was encounterd when running UT: pytest -s -v vllm/tests/spec_decode/test_multi_step_worker.py::test_use_draft_model_runner_advance_step bug;stale ### Your current environment ### Model Input...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
