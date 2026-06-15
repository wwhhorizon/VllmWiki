# vllm-project/vllm#27661: [RFC]: Consolidated tool call parser implementations by type (JSON, Python, XML, Harmony)

| 字段 | 值 |
| --- | --- |
| Issue | [#27661](https://github.com/vllm-project/vllm/issues/27661) |
| 状态 | open |
| 标签 | RFC;unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Consolidated tool call parser implementations by type (JSON, Python, XML, Harmony)

### Issue 正文摘录

### Motivation. When someone wants to add a new tool call parser today, they typically choose an existing tool call parser that looks close to what is needed, copy it into a new file, and adjust things here and there as needed for their specific model. Sometimes tests get added, and sometimes not. Sometimes the changes to the copied parser make meaningful fixes, and sometimes the changes to the copied parser add bugs. Generally, we have a few buckets of tool call parsers based on the format the models are trained to output - JSON, Python, XML, or Hamony style tool calls. But, we have N different implementations of streaming partial JSON parsing, N different python parsing, and so on. Instead of multiple copies of each of those, ideally we'd maintain one high quality implementation for streaming partial JSON parsing that's extensible enough to handle the needs of individual model differences. ### Proposed Change. The overall change I propose is a refactoring of the existing tool call parsers, lowering the burden to add a new tool call parser, reducing the maintenance and bug permutations possible, and providing us higher test coverage of all tool call parsers so we can systematical...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: into a new file, and adjust things here and there as needed for their specific model. Sometimes tests get added, and sometimes not. Sometimes the changes to the copied parser make meaningful fixes, and sometimes the cha...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: new file, and adjust things here and there as needed for their specific model. Sometimes tests get added, and sometimes not. Sometimes the changes to the copied parser make meaningful fixes, and sometimes the changes to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: just things here and there as needed for their specific model. Sometimes tests get added, and sometimes not. Sometimes the changes to the copied parser make meaningful fixes, and sometimes the changes to the copied pars...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: l call parser implementations by type (JSON, Python, XML, Harmony) RFC;unstale ### Motivation. When someone wants to add a new tool call parser today, they typically choose an existing tool call parser that looks close...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
