# vllm-project/vllm#11449: [Bug]: How to run microsoft/llava-med-v1.5-mistral-7b by vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#11449](https://github.com/vllm-project/vllm/issues/11449) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: How to run microsoft/llava-med-v1.5-mistral-7b by vllm

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoConfig, AutoModelForCausalLM, \ MistralConfig, MistralModel, MistralForCausalLM from utils import LlavaMistralConfig,LlavaMistralConfig, LlavaMistralForCausalLM AutoConfig.register("llava_mistral", LlavaMistralConfig) AutoModelForCausalLM.register(LlavaMistralConfig, LlavaMistralForCausalLM) self.llm = LLM( model= "microsoft/llava-med-v1.5-mistral-7b", ) ``` **Error**： ValueError: Model architectures ['LlavaMistralForCausalLM'] are not supported for now. Supported architectures: dict_keys(['AquilaModel', 'AquilaForCausalLM', 'ArcticForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'CohereForCausalLM', 'DbrxForCausalLM', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'GraniteForCausalLM', 'GraniteMoeForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausalLM', 'InternLM2VEForCausalLM', 'JAISLMHeadModel', '...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: ava-med-v1.5-mistral-7b by vllm bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoConfig, AutoModelFo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoConfig, AutoModelForCausalLM, \ MistralConfig, MistralModel, MistralForCausalLM from utils imp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: llava-med-v1.5-mistral-7b", ) ``` **Error**： ValueError: Model architectures ['LlavaMistralForCausalLM'] are not supported for now. Supported architectures: dict_keys(['AquilaModel', 'AquilaForCausalLM', 'ArcticForCausa...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: LM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'GraniteForCausalLM',...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: frontend_api;hardware_porting;model_support;multimodal_vlm cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
