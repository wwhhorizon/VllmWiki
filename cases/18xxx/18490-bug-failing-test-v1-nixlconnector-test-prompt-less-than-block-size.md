# vllm-project/vllm#18490: [Bug][Failing Test]: V1 - NixlConnector `test_prompt_less_than_block_size`

| 字段 | 值 |
| --- | --- |
| Issue | [#18490](https://github.com/vllm-project/vllm/issues/18490) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][Failing Test]: V1 - NixlConnector `test_prompt_less_than_block_size`

### Issue 正文摘录

### Your current environment pytest -v -x `v1/kv_connector/unit/test_nixl_connector.py::test_prompt_less_than_block_size` ### 🐛 Describe the bug Likely due to changes with hybrid memory allocator ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tor ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug][Failing Test]: V1 - NixlConnector `test_prompt_less_than_block_size` bug ### Your current environment pytest -v -x `v1/kv_connector/unit/test_nixl_connector.py::test_prompt_less_than_block_size` ### 🐛 Describe the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug][Failing Test]: V1 - NixlConnector `test_prompt_less_than_block_size` bug ### Your current environment pytest -v -x `v1/kv_connector/unit/test_nixl_connector.py::test_prompt_less_than_block_size` ### 🐛 Describe the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
