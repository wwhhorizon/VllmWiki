# vllm-project/vllm#28197: [Bug]: MoE models quantized with LLM compressor require `Linear` targets (which llmcompressor doesn't add by default)

| 字段 | 值 |
| --- | --- |
| Issue | [#28197](https://github.com/vllm-project/vllm/issues/28197) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MoE models quantized with LLM compressor require `Linear` targets (which llmcompressor doesn't add by default)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have quantized GLM-4.5-Air through llmcompressor but the default model cannot load. A `Linear` key is missing: ``` (EngineCore_DP0 pid=109) INFO 11-06 06:17:47 [compressed_tensors_moe.py:160] Using CompressedTensorsWNA16MarlinMoEMethod (EngineCore_DP0 pid=109) ERROR 11-06 06:17:47 [core.py:784] EngineCore failed to start. (EngineCore_DP0 pid=109) ERROR 11-06 06:17:47 [core.py:784] Traceback (most recent call last): (EngineCore_DP0 pid=109) ERROR 11-06 06:17:47 [core.py:784] File "/workspace/vllm/vllm/v1/engine/core.py", line 775, in run_engine_core (EngineCore_DP0 pid=109) ERROR 11-06 06:17:47 [core.py:784] engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=109) ERROR 11-06 06:17:47 [core.py:784] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=109) ERROR 11-06 06:17:47 [core.py:784] File "/workspace/vllm/vllm/v1/engine/core.py", line 543, in __init__ (EngineCore_DP0 pid=109) ERROR 11-06 06:17:47 [core.py:784] super().__init__( (EngineCore_DP0 pid=109) ERROR 11-06 06:17:47 [core.py:784] File "/workspace/vllm/vllm/v1/engine/core.py", line 106, in __init__ (EngineCore_DP0 pid=109) ERROR 11-06 06:17:47 [core.py:7...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: : true, "type": "int" } } }, // ... ``` Recipe ```yaml default_stage: default_modifiers: AWQModifier: config_groups: group_0: targets: ['re:.*gate_proj.*', 're:.*up_proj.*', 're:.*down_proj.*'] weights: num_bit
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 0 pid=109) ERROR 11-06 06:17:47 [core.py:784] return CompressedTensorsMoEMethod.get_moe_method(self, layer) (EngineCore_DP0 pid=109) ERROR 11-06 06:17:47 [core.py:784] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: _init__ (EngineCore_DP0 pid=109) ERROR 11-06 06:17:47 [core.py:784] else quant_config.get_quant_method(self, prefix) (EngineCore_DP0 pid=109) ERROR 11-06 06:17:47 [core.py:784] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: MoE models quantized with LLM compressor require `Linear` targets (which llmcompressor doesn't add by default) bug ### Your current environment ### 🐛 Describe the bug I have quantized GLM-4.5-Air through llmcompr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: MoE models quantized with LLM compressor require `Linear` targets (which llmcompressor doesn't add by default) bug ### Your current environment ### 🐛 Describe the bug I have quantized GLM-4.5-Air through llmcompr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
