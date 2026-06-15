# vllm-project/vllm#22959: [Bug]: Fail to load auto_round quantization format with quantized lm_head

| 字段 | 值 |
| --- | --- |
| Issue | [#22959](https://github.com/vllm-project/vllm/issues/22959) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fail to load auto_round quantization format with quantized lm_head

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when loading the auto_round format quantized model with quantized lm_head. It shows error: ValueError: There is no module or parameter named 'lm_head.qweight' is Glm4MoeForCaulsalLM. Then main problem is that the argument "prefix" in vllm/model_executor/layers/quantization/auto_round.py got empty for some layers. I add a logger to print the prefix and got the follow logs: [1;36m(VllmWorker TP2 pid=2079254)[0;0m DEBUG 08-14 23:24:25 [auto_round.py:381] prefix=model.layers.91.self_attn.o_proj [1;36m(VllmWorker TP2 pid=2079254)[0;0m DEBUG 08-14 23:24:25 [auto_round.py:280] [model.layers.91.self_attn.o_proj] Type: RowParallelLinear, Bits: 8, Group Size: 128, Sym: True [1;36m(VllmWorker TP2 pid=2079254)[0;0m DEBUG 08-14 23:24:25 [auto_round.py:381] prefix=model.layers.91.self_attn.attn [1;36m(VllmWorker TP2 pid=2079254)[0;0m DEBUG 08-14 23:24:25 [auto_round.py:280] [model.layers.91.self_attn.attn] Type: Attention, Bits: 4, Group Size: 128, Sym: True [1;36m(VllmWorker TP2 pid=2079254)[0;0m DEBUG 08-14 23:24:25 [auto_round.py:381] prefix=model.layers.91.mlp.experts [1;36m(VllmWorker TP2 pid=2079254)[0;0m DEBUG 08-14 23:24:25...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Fail to load auto_round quantization format with quantized lm_head bug;stale ### Your current environment ### 🐛 Describe the bug when loading the auto_round format quantized model with quantized lm_head. It shows...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. development activation_norm;attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding attention;cuda;m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: prefix= [1;36m(VllmWorker TP2 pid=2079254)[0;0m DEBUG 08-14 23:24:25 [backends.py:39] Using InductorAdaptor [1;36m(VllmWorker TP0 pid=2079252)[0;0m DEBUG 08-14 23:24:25 [__init__.py:3816] enabled custom ops: Counter...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 79252)[0;0m DEBUG 08-14 23:24:25 [base_loader.py:47] Loading weights on cuda ... [1;36m(VllmWorker TP2 pid=2079254)[0;0m DEBUG 08-14 23:24:25 [auto_round.py:381] prefix= ### Before submitting a new issue... - [x] Mak...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: lueError: There is no module or parameter named 'lm_head.qweight' is Glm4MoeForCaulsalLM. Then main problem is that the argument "prefix" in vllm/model_executor/layers/quantization/auto_round.py got empty for some layer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
