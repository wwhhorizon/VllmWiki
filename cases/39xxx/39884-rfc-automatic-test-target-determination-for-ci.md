# vllm-project/vllm#39884: [RFC]: Automatic test target determination for CI

| 字段 | 值 |
| --- | --- |
| Issue | [#39884](https://github.com/vllm-project/vllm/issues/39884) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Automatic test target determination for CI

### Issue 正文摘录

### Motivation. Our current conditional testing strategy in CI, which relies on `source_file_dependencies` being manually updated, gets old and inaccurate very quickly. We need to start finding an approach to automatically determine which test to run based on code diff that can adjust and scale with changes, at the same time reduce CI cost by not launching more tests unnecessarily. ### Proposed Change. I propose that we start with a simple LLM-based approach: an agent instructions markdown file that is integrated with CI pipeline generator If this approach doesn't work, we can explore more advanced technique: static analysis on dependency graph, train ML model, code coverage report mapping of tests and source files, etc...) ### Feedback Period. _No response_ ### CC List. @dougbtv @avinashsingh77 @AndreasKaratzas ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC]: Automatic test target determination for CI RFC ### Motivation. Our current conditional testing strategy in CI, which relies on `source_file_dependencies` being manually updated, gets old and inaccurate very quick...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: cally determine which test to run based on code diff that can adjust and scale with changes, at the same time reduce CI cost by not launching more tests unnecessarily. ### Proposed Change. I propose that we start with a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tatic analysis on dependency graph, train ML model, code coverage report mapping of tests and source files, etc...) ### Feedback Period. _No response_ ### CC List. @dougbtv @avinashsingh77 @AndreasKaratzas ### Any Other...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e more advanced technique: static analysis on dependency graph, train ML model, code coverage report mapping of tests and source files, etc...) ### Feedback Period. _No response_ ### CC List. @dougbtv @avinashsingh77 @A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
