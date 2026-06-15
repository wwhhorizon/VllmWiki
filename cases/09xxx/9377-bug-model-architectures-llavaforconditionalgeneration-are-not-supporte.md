# vllm-project/vllm#9377: [Bug]: Model architectures ['LlavaForConditionalGeneration'] are not supported for now.

| 字段 | 值 |
| --- | --- |
| Issue | [#9377](https://github.com/vllm-project/vllm/issues/9377) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model architectures ['LlavaForConditionalGeneration'] are not supported for now.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm serve llava-hf/llava-1.5-13b-hf --dtype auto --api-key token-abc123 ValueError: Model architectures ['LlavaForConditionalGeneration'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'ArcticForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'GraniteForCausalLM', 'GraniteMoeForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausalLM', 'JAISLMHeadModel', 'JambaForCausalLM', 'LlamaForCausalLM', 'LLaMAForCausalLM', 'MambaForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'MiniCPM3ForCausalLM', 'NemotronForCausalLM', 'OlmoForCausalLM', 'OlmoeForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PersimmonForCausalLM', 'PhiForCausalLM', 'Phi3ForCausalLM', 'Phi3SmallFor...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: Model architectures ['LlavaForConditionalGeneration'] are not supported for now. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm serve llava-hf/llava-1.5-13b-hf --
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ausalLM', 'BloomForCausalLM', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Model architectures ['LlavaForConditionalGeneration'] are not supported for now. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm serve llava-hf/llava-1.5-13b-hf --...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: sponse_ ### 🐛 Describe the bug vllm serve llava-hf/llava-1.5-13b-hf --dtype auto --api-key token-abc123 ValueError: Model architectures ['LlavaForConditionalGeneration'] are not supported for now. Supported architecture...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: LM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'GraniteForCausalLM',...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
