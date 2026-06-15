# vllm-project/vllm#18419: [Bug][Failing Test] v1-test - v1/kv_connector/unit/test_nixl_connector.py::test_prompt_less_than_block_size

| 字段 | 值 |
| --- | --- |
| Issue | [#18419](https://github.com/vllm-project/vllm/issues/18419) |
| 状态 | closed |
| 标签 | bug;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][Failing Test] v1-test - v1/kv_connector/unit/test_nixl_connector.py::test_prompt_less_than_block_size

### Issue 正文摘录

### Your current environment Still failing on main as of commit bca55b556f ### 🐛 Describe the bug Failing tests: ``` v1/kv_connector/unit/test_nixl_connector.py::test_prompt_less_than_block_size - AssertionError: assert 1 == 0 ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nector/unit/test_nixl_connector.py::test_prompt_less_than_block_size bug;ci-failure ### Your current environment Still failing on main as of commit bca55b556f ### 🐛 Describe the bug Failing tests: ``` v1/kv_connector/un...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: est - v1/kv_connector/unit/test_nixl_connector.py::test_prompt_less_than_block_size bug;ci-failure ### Your current environment Still failing on main as of commit bca55b556f ### 🐛 Describe the bug Failing tests: ``` v1/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug][Failing Test] v1-test - v1/kv_connector/unit/test_nixl_connector.py::test_prompt_less_than_block_size bug;ci-failure ### Your current environment Still failing on main as of commit bca55b556f ### 🐛 Describe the bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
