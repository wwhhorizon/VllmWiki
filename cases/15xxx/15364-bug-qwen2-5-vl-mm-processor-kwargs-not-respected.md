# vllm-project/vllm#15364: [Bug]: Qwen2.5-VL mm_processor_kwargs not respected

| 字段 | 值 |
| --- | --- |
| Issue | [#15364](https://github.com/vllm-project/vllm/issues/15364) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL mm_processor_kwargs not respected

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoProcessor from qwen_vl_utils import process_vision_info sampling_params = SamplingParams( n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1, top_k=-1, max_tokens=256, logprobs=1, ) vlm = LLM( model="Qwen/Qwen2.5-VL-7B-Instruct", tensor_parallel_size=1, max_model_len=8192, seed=42, enforce_eager=False, trust_remote_code=True, dtype="auto", quantization=None, max_num_seqs=32, gpu_memory_utilization=0.95, task="generate", limit_mm_per_prompt={"image": 2, "video": 0}, mm_processor_kwargs={ "max_pixels": 256 * 28 * 28, "min_pixels": 4 * 28 * 28, }, ) processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct/") # Not working as expected messages = [ {"role": "system", "content": "You are a helpful assistant."}, { "role": "user", "content": [ { "type": "image", "image": "https://rukminim2.flixcart.com/image/xif0q/t-shirt/c/b/u/l-men-temu-polo-001-rizim-original-imah5yz96xfqphkc.jpeg", }, { "type": "image", "image": "https://rukminim2.flixcart.com/image/xif0q/t-shirt/c/b/u/l-men-temu-polo-001-rizim-ori...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoProcessor from qwen_vl_utils import process_vision_info sampling_params = SamplingParams( n=1,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen2.5-VL mm_processor_kwargs not respected bug ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoProcessor from qwen_vl_utils import...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 2, seed=42, enforce_eager=False, trust_remote_code=True, dtype="auto", quantization=None, max_num_seqs=32, gpu_memory_utilization=0.95, task="generate", limit_mm_per_prompt={"image": 2, "video": 0}, mm_processor_kwargs=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tion;sampling_logits attention;cache;cuda;operator;quantization;sampling;triton build_error;slowdown dtype;env_dependency;shape Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: odel_support;multimodal_vlm;quantization;sampling_logits attention;cache;cuda;operator;quantization;sampling;triton build_error;slowdown dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
