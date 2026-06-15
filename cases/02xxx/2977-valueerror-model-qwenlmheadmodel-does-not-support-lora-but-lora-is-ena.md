# vllm-project/vllm#2977: ValueError: Model QWenLMHeadModel does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github.

| 字段 | 值 |
| --- | --- |
| Issue | [#2977](https://github.com/vllm-project/vllm/issues/2977) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ValueError: Model QWenLMHeadModel does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github.

### Issue 正文摘录

from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest llm = LLM(model="/home/data/llm/LLaMA-Factory-qwen1.5/models/Qwen-1_8B-Chat", enable_lora=True, trust_remote_code=True) text_format_lora_path = '/home/data/llm/LLaMA-Factory-qwen1.5/qwen1_lora' sampling_params = SamplingParams( temperature=0, max_tokens=256 ) prompts = [ "test", ] outputs = llm.generate( prompts, sampling_params, lora_request=LoRARequest("text_format_adapter", 1, text_format_lora_path) ) print(outputs) INFO 02-22 09:23:19 llm_engine.py:79] Initializing an LLM engine with config: model='/home/data/llm/LLaMA-Factory-qwen1.5/models/Qwen-1_8B-Chat', tokenizer='/home/data/llm/LLaMA-Factory-qwen1.5/models/Qwen-1_8B-Chat', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, seed=0) WARNING 02-22 09:23:20 tokenizer.py:64] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. Traceback (most recent cal...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ValueError: Model QWenLMHeadModel does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github. feature request from vllm imp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github. feature request from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: antization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, seed=0) WARNING 02-22 09:23:20 tokenizer.py:64] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast token...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, seed=0) WARNING 02-22 09:23:20 tokenizer.py:64] Using a slow...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
