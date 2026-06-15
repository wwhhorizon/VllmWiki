# vllm-project/vllm#12967: [Bug]: Triton error when initializing `LLM(...)` when `enable_lora=True` and `cuda` device != `cuda:0`

| 字段 | 值 |
| --- | --- |
| Issue | [#12967](https://github.com/vllm-project/vllm/issues/12967) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton error when initializing `LLM(...)` when `enable_lora=True` and `cuda` device != `cuda:0`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the `LLM` class for offline inference with LoRA in a multi-GPU setting, Triton produces an error about being unable to access some pointers. I'm using `vllm` for generation in `trl`'s `GRPOTrainer` class, and I get this error during the their `__init__` method. I've managed to isolate the issue to the following blocks in the Python interpreter. It seems like there are some device issues. Here are two examples, one of which works, and one of which produces the error I described: **Works OK:** ``` from peft import get_peft_model, LoraConfig from transformers import AutoModelForCausalLM from vllm import LLM model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Llama-8B") peft_config = LoraConfig(r=16, lora_alpha=64, lora_dropout=0.05, target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]) model = get_peft_model(model, peft_config) llm = LLM( model.name_or_path, device="cuda:0", gpu_memory_utilization=0.5, dtype="auto", enable_prefix_caching=True, max_model_len=4096, enable_lora=True, max_lora_rank=16 ) ``` **Does not work:** ``` from peft import get_peft_model...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e of which produces the error I described: **Works OK:** ``` from peft import get_peft_model, LoraConfig from transformers import AutoModelForCausalLM from vllm import LLM model = AutoModelForCausalLM.from_pretrained("d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ces the error I described: **Works OK:** ``` from peft import get_peft_model, LoraConfig from transformers import AutoModelForCausalLM from vllm import LLM model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepS...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: .name_or_path, device="cuda:0", gpu_memory_utilization=0.5, dtype="auto", enable_prefix_caching=True, max_model_len=4096, enable_lora=True, max_lora_rank=16 ) ``` **Does not work:** ``` from peft import get_peft_model,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : Triton error when initializing `LLM(...)` when `enable_lora=True` and `cuda` device != `cuda:0` bug ### Your current environment ### 🐛 Describe the bug When using the `LLM` class for offline inference with LoRA in a m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Triton error when initializing `LLM(...)` when `enable_lora=True` and `cuda` device != `cuda:0` bug ### Your current environment ### 🐛 Describe the bug When using the `LLM` class for offline inference with LoRA i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
