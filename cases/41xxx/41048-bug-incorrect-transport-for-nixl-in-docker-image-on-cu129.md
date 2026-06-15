# vllm-project/vllm#41048: [Bug]: Incorrect Transport for NIXL in Docker image on cu129

| 字段 | 值 |
| --- | --- |
| Issue | [#41048](https://github.com/vllm-project/vllm/issues/41048) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect Transport for NIXL in Docker image on cu129

### Issue 正文摘录

### Your current environment H200, CU129, Infiniband, CKS `docker.io/vllm/vllm-openai:v0.20.0-cu129-ubuntu2404` ### 🐛 Describe the bug ``` (EngineCore pid=60) INFO 04-27 19:07:51 [worker.py:679] Registering KV_Caches. use_mla: False, kv_buffer_device: cuda, use_host_buffer: False W0427 19:07:51.968335 60 ucx_utils.cpp:581] memory is detected as host, check that UCX is configured with CUDA support W0427 19:07:52.036051 60 ucx_utils.cpp:581] memory is detected as host, check that UCX is configured with CUDA support W0427 19:07:52.102112 60 ucx_utils.cpp:581] memory is detected as host, check that UCX is configured with CUDA support W0427 19:07:52.167722 60 ucx_utils.cpp:581] memory is detected as host, check that UCX is configured with CUDA support W0427 19:07:52.239140 60 ucx_utils.cpp:581] memory is detected as host, check that UCX is configured with CUDA support W0427 19:07:52.306804 60 ucx_utils.cpp:581] memory is detected as host, check that UCX is configured with CUDA support W0427 19:07:52.363077 60 ucx_utils.cpp:581] memory is detected as host, check that UCX is configured with CUDA support W0427 19:07:52.419334 60 ucx_utils.cpp:581] memory is detected as host, check that UC...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Incorrect Transport for NIXL in Docker image on cu129 bug ### Your current environment H200, CU129, Infiniband, CKS `docker.io/vllm/vllm-openai:v0.20.0-cu129-ubuntu2404` ### 🐛 Describe the bug ``` (EngineCore pid...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [worker.py:679] Registering KV_Caches. use_mla: False, kv_buffer_device: cuda, use_host_buffer: False W0427 19:07:51.968335 60 ucx_utils.cpp:581] memory is detected as host, check that UCX is configured with CUDA suppor...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: can answer lots of frequently asked questions. correctness ci_build cuda mismatch Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0) INFO 04-27 19:07:51 [worker.py:679] Registering KV_Caches. use_mla: False, kv_buffer_device: cuda, use_host_buffer: False W0427 19:07:51.968335 60 ucx_utils.cpp:581] memory is detected as host, check that UCX is conf...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 60 ucx_utils.cpp:581] memory is detected as host, check that UCX is configured with CUDA support W0427 19:07:52.036051 60 ucx_utils.cpp:581] memory is detected as host, check that UCX is configured with CUDA support W04...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
