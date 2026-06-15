# vllm-project/vllm#40690: [Bug] MultiConnector bypasses the deprecated-signature shim and breaks old-style child connectors

| 字段 | 值 |
| --- | --- |
| Issue | [#40690](https://github.com/vllm-project/vllm/issues/40690) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] MultiConnector bypasses the deprecated-signature shim and breaks old-style child connectors

### Issue 正文摘录

### Summary `MultiConnector.__init__` instantiates its child connectors by calling `connector_cls(...)` directly, bypassing the backward-compat shim that `KVConnectorFactory.create_connector` / `_get_connector_class_with_compat` added in #27887. As a result, any legacy connector whose `__init__` still has the pre-#27887 signature `(self, vllm_config, role)` fails with `TypeError` the moment it is placed inside a `MultiConnector`, even though the same connector works fine when used as a top-level connector (where it only produces the expected `deprecated signature` warning). ### Environment - vLLM: 0.18.0 (also reproduced against current main, commit `bf45e6d0a`) - Reproducing connector: `LMCacheAscendConnectorV1Dynamic` from [LMCache-Ascend](https://github.com/LMCache/LMCache-Ascend) (tracks vLLM ≤ 0.11.0, still uses the 2-arg signature) ### Repro `--kv-transfer-config` with a `MultiConnector` that wraps a legacy 2-arg connector: \`\`\`json { \"kv_connector\": \"MultiConnector\", \"kv_role\": \"kv_producer\", \"engine_id\": \"0\", \"kv_connector_extra_config\": { \"connectors\": [ {\"kv_connector\": \"LMCacheAscendConnectorV1Dynamic\", \"kv_role\": \"kv_both\", \"kv_connector_modu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 18.0 (also reproduced against current main, commit `bf45e6d0a`) - Reproducing connector: `LMCacheAscendConnectorV1Dynamic` from [LMCache-Ascend](https://github.com/LMCache/LMCache-Ascend) (tracks vLLM ≤ 0.11.0, still us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nnector whose `__init__` still has the pre-#27887 signature `(self, vllm_config, role)` fails with `TypeError` the moment it is placed inside a `MultiConnector`, even though the same connector works fine when used as a...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: `deprecated signature` warning). ### Environment - vLLM: 0.18.0 (also reproduced against current main, commit `bf45e6d0a`) - Reproducing connector: `LMCacheAscendConnectorV1Dynamic` from [LMCache-Ascend](https://github....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: but when `--kv-transfer-config` is set vLLM already disables the hybrid KV cache manager, so the check does not fire. Happy to send a PR if the direction is acceptable. ### Workaround Patch the legacy connector's signat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
