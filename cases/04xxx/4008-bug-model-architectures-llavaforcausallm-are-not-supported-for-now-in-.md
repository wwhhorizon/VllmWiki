# vllm-project/vllm#4008: [Bug]: Model architectures ['LlavaForCausalLM'] are not supported for now in vllm 0.4.0.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#4008](https://github.com/vllm-project/vllm/issues/4008) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Model architectures ['LlavaForCausalLM'] are not supported for now in vllm 0.4.0.post1

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I am using: ``` from vllm import LLM model = LLM( model="llava-hf/llava-1.5-13b-hf", image_input_type="pixel_values", download_dir="/tmp/models", image_token_id=32000, image_input_shape="1,3,336,336", image_feature_size=576, ) ``` which throws error: ValueError: Model architectures ['LlavaForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausalLM', 'JAISLMHeadModel', 'LlamaForCausalLM', 'LlavaForConditionalGeneration', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'OLMoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PhiForCausalLM', 'QWenLMHeadModel', 'Qwen2ForCausalLM', 'Qwen2MoeForCausa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Model architectures ['LlavaForCausalLM'] are not supported for now in vllm 0.4.0.post1 bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I am using: ``` fro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: collect_env.py` ``` ### 🐛 Describe the bug I am using: ``` from vllm import LLM model = LLM( model="llava-hf/llava-1.5-13b-hf", image_input_type="pixel_values", download_dir="/tmp/models", image_token_id=32000, image_in...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: alLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausal...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ation', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'OLMoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PhiForCausalLM', 'QWenLMHe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: Model architectures ['LlavaForCausalLM'] are not supported for now in vllm 0.4.0.post1 bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I am using: ``` fro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
