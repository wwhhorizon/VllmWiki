# vllm-project/vllm#34591: [Bug]: Ministral-3 LoRA adapter fails silently

| 字段 | 值 |
| --- | --- |
| Issue | [#34591](https://github.com/vllm-project/vllm/issues/34591) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ministral-3 LoRA adapter fails silently

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When loading a LoRA adapter on top of `mistralai/Ministral-3-8B-Instruct-2512`, the adapter appears to load but is **not actually applied**: generations match the **base model** output. There is **no warning/error**, which makes it hard to diagnose (basically the same “silent LoRA failure” problem discussed in #34186 when layer prefixes do not match) ## Minimal example Loading the LoRa adapter goes ahead without any warning/failure but response is coming from the base model ```python from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest BASE_MODEL = "mistralai/Ministral-3-8B-Instruct-2512" LORA_DIR = "/path/to/lora_adapter" llm = LLM(model=BASE_MODEL, enable_lora=True) params = SamplingParams(temperature=0.0, max_tokens=128) prompt = " " out = llm.generate( [prompt], params, lora_request=LoRARequest("test_adapter", 1, LORA_DIR), )[0].outputs[0].text print(out) # Expected: LoRA-modified output # Actual (current): matches base model output ``` When debugging this, I observed the same pattern as in #34186 where [get_lora](https://github.com/vllm-project/vllm/blob/v0.15.1/vllm/lora/lora_model.py#L58) returns...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: g/failure but response is coming from the base model ```python from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest BASE_MODEL = "mistralai/Ministral-3-8B-Instruct-2512" LORA_DIR = "/path/to/lo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: rs to load but is **not actually applied**: generations match the **base model** output. There is **no warning/error**, which makes it hard to diagnose (basically the same “silent LoRA failure” problem discussed in #341...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ConditionalGeneration from vllm.model_executor.models.utils import WeightsMapper # Patch HF -> vLLM prefix mapping PixtralForConditionalGeneration.hf_to_vllm_mapper = WeightsMapper( orig_to_new_prefix={ "model.language_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: d_api;hardware_porting;model_support;multimodal_vlm;sampling_logits cuda;triton build_error env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: el_executor.models.utils import WeightsMapper # Patch HF -> vLLM prefix mapping PixtralForConditionalGeneration.hf_to_vllm_mapper = WeightsMapper( orig_to_new_prefix={ "model.language_model.": "language_model.model.", "...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
