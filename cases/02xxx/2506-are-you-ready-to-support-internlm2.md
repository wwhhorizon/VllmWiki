# vllm-project/vllm#2506: Are you ready to support InternLM2?

| 字段 | 值 |
| --- | --- |
| Issue | [#2506](https://github.com/vllm-project/vllm/issues/2506) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Are you ready to support InternLM2?

### Issue 正文摘录

ValueError: Model architectures ['InternLM2ForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'DeciLMForCausalLM', 'FalconForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'LlamaForCausalLM', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'OPTForCausalLM', 'PhiForCausalLM', 'QWenLMHeadModel', 'RWForCausalLM', 'YiForCausalLM']

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Are you ready to support InternLM2? ValueError: Model architectures ['InternLM2ForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'DeciLMForCausalLM', 'FalconForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM',...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Are you ready to support InternLM2? ValueError: Model architectures ['InternLM2ForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCa...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'DeciLMForCausalLM', 'FalconForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCau...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
