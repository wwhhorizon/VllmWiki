# vllm-project/vllm#22231: [Usage]:  Model architectures ['Qwen3ForCausalLM'] are not supported for now.

| 字段 | 值 |
| --- | --- |
| Issue | [#22231](https://github.com/vllm-project/vllm/issues/22231) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  Model architectures ['Qwen3ForCausalLM'] are not supported for now.

### Issue 正文摘录

### Your current environment ValueError: Model architectures ['Qwen3ForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'ArcticForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'GraniteForCausalLM', 'GraniteMoeForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausalLM', 'JAISLMHeadModel', 'JambaForCausalLM', 'LlamaForCausalLM', 'LLaMAForCausalLM', 'MambaForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'MiniCPM3ForCausalLM', 'NemotronForCausalLM', 'OlmoForCausalLM', 'OlmoeForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PersimmonForCausalLM', 'PhiForCausalLM', 'Phi3ForCausalLM', 'Phi3SmallForCausalLM', 'PhiMoEForCausalLM', 'Qwen2ForCausalLM', 'Qwen2MoeForCausalLM', 'RWForCausalLM', 'StableLMEpochForCausalLM', 'StableLmForCausalLM', 'S...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Usage]: Model architectures ['Qwen3ForCausalLM'] are not supported for now. usage ### Your current environment ValueError: Model architectures ['Qwen3ForCausalLM'] are not supported for now. Supported architectures: ['...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: Model architectures ['Qwen3ForCausalLM'] are not supported for now. usage ### Your current environment ValueError: Model architectures ['Qwen3ForCausalLM'] are not supported for now. Supported architectures: ['...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: LM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'GraniteForCausalLM',...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ausalLM', 'BloomForCausalLM', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: salLM', 'MambaForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'MiniCPM3ForCausalLM', 'NemotronForCausalLM', 'OlmoForCausalLM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
