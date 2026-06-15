# vllm-project/vllm#36584: [Bug]: Qwen3.5-35B-A3B FlashInfer JIT compilation fails with C++17 feature errors (e.g., std::is_unsigned_v) when using vLLM 0.17.0

| 字段 | 值 |
| --- | --- |
| Issue | [#36584](https://github.com/vllm-project/vllm/issues/36584) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-35B-A3B FlashInfer JIT compilation fails with C++17 feature errors (e.g., std::is_unsigned_v) when using vLLM 0.17.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug sec-agentic-rag-judge2-blue-t70348fbbb7d-master-0:%!(EXTRA string=(EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] using std::is_standard_layout_v; (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] ^ (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] /home/jovyan/.conda/envs/vllm0170/lib/python3.13/site-packages/flashinfer/data/cutlass/include/cute/util/type_traits.hpp(145): error: namespace "std" has no member "is_unsigned_v" (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] using std::is_unsigned_v; (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] ^ (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] /home/jovyan/.conda/envs/vllm0170/lib/python3.13/site-packages/flashinfer/data/cutlass/include/cute/util/type_traits.hpp(147): error: namespace "std" has no member "is_signed_v" (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] using std::is_signed_v; (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] ^ (EngineCore_DP0 pid=227)...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Qwen3.5-35B-A3B FlashInfer JIT compilation fails with C++17 feature errors (e.g., std::is_unsigned_v) when using vLLM 0.17.0 bug ### Your current environment ### 🐛 Describe the bug sec-agentic-rag-judge2-blue-t70...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: cu". (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] ninja: build stopped: subcommand failed. (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] ', please check the stack trace above for the root...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ation of "/home/jovyan/.cache/flashinfer/0.6.4/90a/generated/gdn_prefill_sm90/gdn_prefill_kernel_half_g0b1a0i0.cu". (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] ninja: build stopped: subcommand failed. (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3.5-35B-A3B FlashInfer JIT compilation fails with C++17 feature errors (e.g., std::is_unsigned_v) when using vLLM 0.17.0 bug ### Your current environment ### 🐛 Describe the bug sec-agentic-rag-judge2-blue-t70...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: P0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] using std::is_standard_layout_v; (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] ^ (EngineCore_DP0 pid=227) ERROR 03-10 11:46:00 [core.py:1102] (EngineCore_DP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
