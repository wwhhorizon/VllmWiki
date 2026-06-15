# vllm-project/vllm#23233: [RFC]: Restructure the core loop to allow more asynchrony

| 字段 | 值 |
| --- | --- |
| Issue | [#23233](https://github.com/vllm-project/vllm/issues/23233) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Restructure the core loop to allow more asynchrony

### Issue 正文摘录

### Motivation. Today, the core loop looks like: ```python while True: scheduler_output = self.scheduler.schedule() model_runner_output = self.model_executor.execute_model(scheduler_output) engine_core_outputs = self.scheduler.update_from_output(scheduler_output, model_runner_output) yield engine_core_outputs ``` While simple, this structure doesn't allow us to utilize CPU cycles while the GPU is running the model in `execute_model`. ### Proposed Change. The proposal is to carve out the sampling stage from the `execute_model` method. This way, `execute_model` will be a non-blocking call that returns without no GPU->CPU synchronization at the end. That is: ```python while True: scheduler_output = self.scheduler.schedule() # Prepare inputs and execute the model until the last hidden states. This is non-blocking. self.model_executor.execute_model(scheduler_output) # If structured outputs is used, produce the bitmask here. Otherwise, bitmask is None. bitmask = self.scheduler.get_grammar_bitmask(scheduler_output) # Prepare sampling metadata and sample the next token ids. This is blocking. model_runner_output = self.model_executor.sample(bitmask) engine_core_outputs = self.scheduler.upd...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: from the `execute_model` method. This way, `execute_model` will be a non-blocking call that returns without no GPU->CPU synchronization at the end. That is: ```python while True: scheduler_output = self.scheduler.schedu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Restructure the core loop to allow more asynchrony RFC;stale ### Motivation. Today, the core loop looks like: ```python while True: scheduler_output = self.scheduler.schedule() model_runner_output = self.model_ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: `python while True: scheduler_output = self.scheduler.schedule() model_runner_output = self.model_executor.execute_model(scheduler_output) engine_core_outputs = self.scheduler.update_from_output(scheduler_output, model_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
