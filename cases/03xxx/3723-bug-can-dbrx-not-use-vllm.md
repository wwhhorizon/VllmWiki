# vllm-project/vllm#3723: [Bug]: Can dbrx not use Vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#3723](https://github.com/vllm-project/vllm/issues/3723) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Can dbrx not use Vllm?

### Issue 正文摘录

### Your current environment python -m vllm.entrypoints.openai.api_server --model /data1/LLM/model/AI-ModelScope/dbrx-instruct --trust-remote-code ### 🐛 Describe the bug ValueError: Model architectures ['DbrxForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausalLM', 'LlamaForCausalLM', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'OLMoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PhiForCausalLM', 'QWenLMHeadModel', 'Qwen2ForCausalLM', 'RWForCausalLM', 'StableLMEpochForCausalLM', 'StableLmForCausalLM', 'Starcoder2ForCausalLM']

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: our current environment python -m vllm.entrypoints.openai.api_server --model /data1/LLM/model/AI-ModelScope/dbrx-instruct --trust-remote-code ### 🐛 Describe the bug ValueError: Model architectures ['DbrxForCausalLM'] ar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', '...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: salLM', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'OLMoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PhiForCausalLM', 'QWenLMHe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: instruct --trust-remote-code ### 🐛 Describe the bug ValueError: Model architectures ['DbrxForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'Ba...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCaus...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
