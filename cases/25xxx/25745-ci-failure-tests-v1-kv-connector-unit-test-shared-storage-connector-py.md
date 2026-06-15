# vllm-project/vllm#25745: [CI Failure]: tests/v1/kv_connector/unit/test_shared_storage_connector.py::test_shared_storage_connector_hashes

| 字段 | 值 |
| --- | --- |
| Issue | [#25745](https://github.com/vllm-project/vllm/issues/25745) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: tests/v1/kv_connector/unit/test_shared_storage_connector.py::test_shared_storage_connector_hashes

### Issue 正文摘录

### Your current environment https://buildkite.com/vllm/ci/builds/32569#01998466-b8b5-4be4-a42f-4c89db46cafc ### 🐛 Describe the bug ``` [2025-09-26T05:37:19Z] _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ -- | [2025-09-26T05:37:19Z] | [2025-09-26T05:37:19Z] self = | [2025-09-26T05:37:19Z] kv_tranfer_config = KVTransferConfig(kv_connector='SharedStorageConnector', engine_id='4fa58fae-f2cd-420e-a38e-74855f04597b', kv_buffer_de...{'shared_storage_path': '/tmp/pytest-of-root/pytest-1/test_shared_storage_connector_0'}, kv_connector_module_path=None) | [2025-09-26T05:37:19Z] | [2025-09-26T05:37:19Z] def __init__(self, kv_tranfer_config: KVTransferConfig): | [2025-09-26T05:37:19Z] # This should be called on frontend process. | [2025-09-26T05:37:19Z] > assert not has_kv_transfer_group() | [2025-09-26T05:37:19Z] E AssertionError | [2025-09-26T05:37:19Z] | [2025-09-26T05:37:19Z] /usr/local/lib/python3.12/dist-packages/vllm/distributed/kv_transfer/kv_connector/v1/metrics.py:54: AssertionError ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [docum...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: tests/v1/kv_connector/unit/test_shared_storage_connector.py::test_shared_storage_connector_hashes bug ### Your current environment https://buildkite.com/vllm/ci/builds/32569#01998466-b8b5-4be4-a42f-4c89db46
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: | [2025-09-26T05:37:19Z] self = | [2025-09-26T05:37:19Z] kv_tranfer_config = KVTransferConfig(kv_connector='SharedStorageConnector', engine_id='4fa58fae-f2cd-420e-a38e-74855f04597b', kv_buffer_de...{'shared_storage_path...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: tests/v1/kv_connector/unit/test_shared_storage_connector.py::test_shared_storage_connector_hashes bug ### Your current environment https://buildkite.com/vllm/ci/builds/32569#01998466-b8b5-4be4-a42f-4c89db4...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
