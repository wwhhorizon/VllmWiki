# vllm-project/vllm#16555: [Bug]: Custom Hugging Face model with `tie_word_embeddings=False` causes `lm_head` loading issue

| 字段 | 值 |
| --- | --- |
| Issue | [#16555](https://github.com/vllm-project/vllm/issues/16555) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Custom Hugging Face model with `tie_word_embeddings=False` causes `lm_head` loading issue

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Description I have a custom Hugging Face model that extends `Gemma3ForCausalLM` and changes the way input embeddings are processed. Think of a vision-language model (VLM), where image embeddings and text embeddings are merged and passed into the language model. Here’s a minimal example to illustrate the structure: ```python import torch from transformers import Gemma3ForCausalLM, Gemma3TextConfig class CustomGemma3ForCausalLM(Gemma3ForCausalLM): def __init__(self, config: Gemma3TextConfig): config.tie_word_embeddings = False super().__init__(config) self.my_custom_embedding = MyEmbeddingLayer(...) # custom input embedding logic def forward(self, input_ids, **kwargs): embeds = self.my_custom_embedding(input_ids) return super().forward(input_embeds=embeds, **kwargs) ``` Because `tie_word_embeddings` is set to `False`, vLLM currently tries to **create and load** a new `lm_head`, which causes conflicts. --- ## What goes wrong In `vllm.model_executor.models.transformers_model.TransformersForCausalLM`, we have: ```python class TransformersForCausalLM(nn.Module, SupportsQuant, SupportsLoRA, SupportsPP): def __init__(self, *, vllm_con...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Custom Hugging Face model with `tie_word_embeddings=False` causes `lm_head` loading issue bug;stale ### Your current environment ### 🐛 Describe the bug ## Description I have a custom Hugging Face model that exten...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: model. Here’s a minimal example to illustrate the structure: ```python import torch from transformers import Gemma3ForCausalLM, Gemma3TextConfig class CustomGemma3ForCausalLM(Gemma3ForCausalLM): def __init__(self, confi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: lmConfig, prefix: str = ""): ... self.model = TransformersModel(vllm_config=vllm_config, prefix=prefix) if get_pp_group().is_last_rank: self.unpadded_vocab_size = config.vocab_size self.lm_head = ParallelLMHead( config....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: odel with `tie_word_embeddings=False` causes `lm_head` loading issue bug;stale ### Your current environment ### 🐛 Describe the bug ## Description I have a custom Hugging Face model that extends `Gemma3ForCausalLM` and c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
