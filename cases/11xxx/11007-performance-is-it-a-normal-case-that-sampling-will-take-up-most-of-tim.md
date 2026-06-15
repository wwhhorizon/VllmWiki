# vllm-project/vllm#11007: [Performance]: Is it a normal case that sampling will take up most of time during the execution of one iteration?

| 字段 | 值 |
| --- | --- |
| Issue | [#11007](https://github.com/vllm-project/vllm/issues/11007) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Is it a normal case that sampling will take up most of time during the execution of one iteration?

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression When trying to benchmarking vLLM, we found that during the execution of each iteration, Samling (`self.model.sample()` in the source code of _model_runner.py_) will take most of the time, far more longer than the computation time of attention and linear layers. For instance, when batch_size is 1, sampling will took about 25ms while the end-to-end time of one iteration is only about 30ms. And when batch_size is 100, sampling will took about 80ms while the end-to-end time of one iteration is only about 90ms. Is it a normal case? We were testing on 2080Ti GPU with vLLM v0.6.3post1 and Llama2-7b-chathf. ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: LM, we found that during the execution of each iteration, Samling (`self.model.sample()` in the source code of _model_runner.py_) will take most of the time, far more longer than the computation time of attention and li...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression When trying to benchmarking vLLM, we found that during the execution of each iteration, Samling (`self.model.sample()` in the source code...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: take up most of time during the execution of one iteration? performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression When trying to benchmarking vLLM, we found that during...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
