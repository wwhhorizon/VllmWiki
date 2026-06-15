# vllm-project/vllm#41814: NixlConnector hardcodes backends=["UCX"] default; no env-var override path; LIBFABRIC/EFA operators must discover kv_connector_extra_config.backends from source

| 字段 | 值 |
| --- | --- |
| Issue | [#41814](https://github.com/vllm-project/vllm/issues/41814) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel |
| 子分类 |  |
| Operator 关键词 | operator |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> NixlConnector hardcodes backends=["UCX"] default; no env-var override path; LIBFABRIC/EFA operators must discover kv_connector_extra_config.backends from source

### Issue 正文摘录

### Your current environment - vLLM 0.17.1 (bundled in `nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.1.0`) - Dynamo 1.1.0 runtime (for disaggregated prefill/decode serving) - NIXL `nixl_cu12` 1.0.1 with LIBFABRIC + UCX plugins both present on disk - AWS EFA hardware (SRD transport, libfabric provider `efa`) - 2× P5.48xlarge H100 HyperPod nodes - `libplugin_LIBFABRIC.so` and `libplugin_UCX.so` both available at `/opt/dynamo/venv/lib/python3.12/site-packages/.nixl_cu12.mesonpy.libs/plugins/` ### 🐛 Describe the bug `NixlConnector` hardcodes `backends=["UCX"]` as the default in `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py:1023`. There is no environment-variable fallback for backend selection, and this default is not documented. Operators running vLLM + NIXL on EFA (where UCX can't establish cross-node handshakes, but libfabric works) have no way to switch backends short of reading the source. The NIXL library itself supports multiple backends — the limitation is entirely in vLLM's default. ```python # nixl_connector.py:1022-1024 self.nixl_backends = vllm_config.kv_transfer_config.get_from_extra_config( "backends", ["UCX"] ) ``` Setting `NIXL_BACKEND=LIBFABRIC` or `VLLM_N...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: NixlConnector hardcodes backends=["UCX"] default; no env-var override path; LIBFABRIC/EFA operators must discover kv_connector_extra_config.backends from source ### Your current environment - vLLM 0.17.1 (bundled in `nv...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: tantiated ... NIXL transfer failure: handshake_failed ``` ### 🛠️ How to reproduce 1. Deploy disaggregated vLLM with `NixlConnector` on AWS EFA (or any non-RDMA-over-Ethernet fabric where UCX can't handshake). 2. Set `--...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ypassing it — catches the common operator mistake. ### Evidence Reproducible from commit ` ` on our PR branch. Verified against `nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.1.0`. Cross-references: - Downstream blocker: [aws...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: override path; LIBFABRIC/EFA operators must discover kv_connector_extra_config.backends from source ### Your current environment - vLLM 0.17.1 (bundled in `nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.1.0`) - Dynamo 1.1.0 ru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ai-dynamo/vllm-runtime:1.1.0`) - Dynamo 1.1.0 runtime (for disaggregated prefill/decode serving) - NIXL `nixl_cu12` 1.0.1 with LIBFABRIC + UCX plugins both present on disk - AWS EFA hardware (SRD transport, libfabric pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
