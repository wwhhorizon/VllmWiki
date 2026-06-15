# vllm-project/vllm#41743: [Feature]: Enabling speculative decoding with parallel drafting (P-EAGLE) for multimodal models.

| 字段 | 值 |
| --- | --- |
| Issue | [#41743](https://github.com/vllm-project/vllm/issues/41743) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enabling speculative decoding with parallel drafting (P-EAGLE) for multimodal models.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, speculative decoding with parallel drafting (P-EAGLE) for multimodal models is not supported. When I try to deploy the P-EAGLE head for the Gemma-4-31B-IT model, it throws the error below: EngineCore failed to start. (EngineCore pid=1368036) ERROR 05-05 15:23:43 [core.py:1136] Traceback (most recent call last): (EngineCore pid=1368036) ERROR 05-05 15:23:43 [core.py:1136] File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 1110, in run_engine_core (EngineCore pid=1368036) ERROR 05-05 15:23:43 [core.py:1136] engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore pid=1368036) ERROR 05-05 15:23:43 [core.py:1136] File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore pid=1368036) ERROR 05-05 15:23:43 [core.py:1136] return func(*args, **kwargs) (EngineCore pid=1368036) ERROR 05-05 15:23:43 [core.py:1136] File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 876, in __init__ (EngineCore pid=1368036) ERROR 05-05 15:23:43 [core.py:1136] super().__init__( (EngineCore pid=1368036) ERROR 05-05 1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ure]: Enabling speculative decoding with parallel drafting (P-EAGLE) for multimodal models. feature request ### 🚀 The feature, motivation and pitch Currently, speculative decoding with parallel drafting (P-EAGLE) for mu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Enabling speculative decoding with parallel drafting (P-EAGLE) for multimodal models. feature request ### 🚀 The feature, motivation and pitch Currently, speculative decoding with parallel drafting (P-EAGLE) f...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: y:1136] File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore pid=1368036) ERROR 05-05 15:23:43 [core.py:1136] return func(*args, **kwargs) (EngineCore pid=1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: }'` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: l models is not supported. When I try to deploy the P-EAGLE head for the Gemma-4-31B-IT model, it throws the error below: EngineCore failed to start. (EngineCore pid=1368036) ERROR 05-05 15:23:43 [core.py:1136] Tracebac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
