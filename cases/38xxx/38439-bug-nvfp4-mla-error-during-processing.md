# vllm-project/vllm#38439: [Bug]: NVFP4 + MLA error during processing

| 字段 | 值 |
| --- | --- |
| Issue | [#38439](https://github.com/vllm-project/vllm/issues/38439) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: NVFP4 + MLA error during processing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I believe that #33972 has broken models with MLA, as MLA attention processing assumes that the fp4 marlin linear can be run with `weight_global_scale.dtype=torch.float32` and eye `bfloat16`. Replication: ```python3 from vllm import LLM llm = LLM("inference-optimization/DeepSeek-V3-debug-empty-NVFP4A16") ``` ``` (EngineCore pid=3426083) File "/home/kylesayrs/vllm/vllm/model_executor/layers/attention/mla_attention.py", line 714, in process_weights_after_loading (EngineCore pid=3426083) kv_b_proj_weight = get_and_maybe_dequant_weights( (EngineCore pid=3426083) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=3426083) File "/home/kylesayrs/vllm/vllm/model_executor/layers/quantization/utils/quant_utils.py", line 390, in get_and_maybe_dequant_weights (EngineCore pid=3426083) dequant_weights = layer.quant_method.apply(layer, eye, bias=None).to(out_dtype) (EngineCore pid=3426083) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=3426083) File "/home/kylesayrs/vllm/vllm/model_executor/layers/quantization/compressed_tensors/compresse d_tensors.py", line 921, in apply (EngineCore pid=3426083) return scheme.apply_weights(layer, x...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 9: [Bug]: NVFP4 + MLA error during processing bug ### Your current environment ### 🐛 Describe the bug I believe that #33972 has broken models with MLA, as MLA attention processing assumes that the fp4 marlin linear can be...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pe=torch.float32` and eye `bfloat16`. Replication: ```python3 from vllm import LLM llm = LLM("inference-optimization/DeepSeek-V3-debug-empty-NVFP4A16") ``` ``` (EngineCore pid=3426083) File "/home/kylesayrs/vllm/vllm/mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: environment ### 🐛 Describe the bug I believe that #33972 has broken models with MLA, as MLA attention processing assumes that the fp4 marlin linear can be run with `weight_global_scale.dtype=torch.float32` and eye `bflo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: apply_fp4_marlin_linear (EngineCore pid=3426083) output = ops.marlin_gemm( (EngineCore pid=3426083) ^^^^^^^^^^^^^^^^ (EngineCore pid=3426083) File "/home/kylesayrs/vllm/vllm/_custom_ops.py", line 1301, in marlin_gemm (E...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
