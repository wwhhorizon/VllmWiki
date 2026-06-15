# vllm-project/vllm#4943: [Feature]: Support for MiniCPM-Llama3-V-2_5 the Multi-modal LLM

| 字段 | 值 |
| --- | --- |
| Issue | [#4943](https://github.com/vllm-project/vllm/issues/4943) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for MiniCPM-Llama3-V-2_5 the Multi-modal LLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Tested with the latest commit but got error: `[rank0]: ValueError: Model architectures ['MiniCPMV'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausalLM', 'JAISLMHeadModel', 'LlamaForCausalLM', 'LlavaForConditionalGeneration', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'OlmoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PhiForCausalLM', 'Phi3ForCausalLM', 'QWenLMHeadModel', 'Qwen2ForCausalLM', 'Qwen2MoeForCausalLM', 'RWForCausalLM', 'StableLMEpochForCausalLM', 'StableLmForCausalLM', 'Starcoder2ForCausalLM', 'ArcticForCausalLM', 'XverseForCausalLM', 'MistralModel']` ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: Support for MiniCPM-Llama3-V-2_5 the Multi-modal LLM feature request ### 🚀 The feature, motivation and pitch Tested with the latest commit but got error: `[rank0]: ValueError: Model architectures ['MiniCPMV']...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: alLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausal...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: GLMForConditionalGeneration', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', '...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ation', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'OlmoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PhiF...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ested with the latest commit but got error: `[rank0]: ValueError: Model architectures ['MiniCPMV'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'Baichua...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
