# vllm-project/vllm#20851: [Bug]:  Killing process and hung when running DP>=4

| 字段 | 值 |
| --- | --- |
| Issue | [#20851](https://github.com/vllm-project/vllm/issues/20851) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Killing process and hung when running DP>=4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running 100b multimodal with Moe on 1X8 H100, and enable_expert_parallel=True. I tried tp8 and tp4,dp2, the model works good, when I tried tp2 dp4 or tp1 dp8, it will possibly print Killing process near allocate kv cache: (EngineCore_6 pid=689874) INFO 07-12 01:23:06 [kv_cache_utils.py:715] GPU KV cache size: 136,416 tokens (EngineCore_6 pid=689874) INFO 07-12 01:23:06 [kv_cache_utils.py:719] Maximum concurrency for 4,096 tokens per request: 33.30x (EngineCore_6 pid=689874) zjldbg selected_backend None attention_cls vllm.v1.attention.backends.flash_attn.FlashAttentionBackend backend_by_global_setting None (EngineCore_6 pid=689874) zjldbg kv_cache .layers.0.self_attn.attn torch.Size([2, 8526, 16, 8, 128]) **_Killing process 688587 that didn't stop within 5 minutes._** (EngineCore_4 pid=689912) INFO 07-12 01:24:11 [gpu_model_runner.py:2014] Graph capturing finished in 64 secs, took 9.25 GiB (EngineCore_1 pid=689917) INFO 07-12 01:24:11 [gpu_model_runner.py:2014] Graph capturing finished in 64 secs, took 9.25 GiB (EngineCore_7 pid=689902) INFO 07-12 01:24:11 [gpu_model_runner.py:2014] Graph capturing finished in 64 secs, took 9...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 096 tokens per request: 33.30x (EngineCore_6 pid=689874) zjldbg selected_backend None attention_cls vllm.v1.attention.backends.flash_attn.FlashAttentionBackend backend_by_global_setting None (EngineCore_6 pid=689874) zj...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;sampling_logits;speculative_decoding attention;cache;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### 🐛 Describe the bug I am running 100b multimodal with Moe on 1X8 H100, and enable_expert_parallel=True. I tried tp8 and tp4,dp2, the model works good, when I tried tp2 dp4 or tp1 dp8, it will possibly print Killing p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: # Your current environment ### 🐛 Describe the bug I am running 100b multimodal with Moe on 1X8 H100, and enable_expert_parallel=True. I tried tp8 and tp4,dp2, the model works good, when I tried tp2 dp4 or tp1 dp8, it wi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: nvironment ### 🐛 Describe the bug I am running 100b multimodal with Moe on 1X8 H100, and enable_expert_parallel=True. I tried tp8 and tp4,dp2, the model works good, when I tried tp2 dp4 or tp1 dp8, it will possibly prin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
