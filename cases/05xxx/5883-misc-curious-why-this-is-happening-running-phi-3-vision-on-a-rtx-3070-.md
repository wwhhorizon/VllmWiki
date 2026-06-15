# vllm-project/vllm#5883: [Misc]: Curious why this is happening: Running phi-3-vision on a RTX 3070 (8GB VRAM) works with transformer but not with vllm (goes out of memory)

| 字段 | 值 |
| --- | --- |
| Issue | [#5883](https://github.com/vllm-project/vllm/issues/5883) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Curious why this is happening: Running phi-3-vision on a RTX 3070 (8GB VRAM) works with transformer but not with vllm (goes out of memory)

### Issue 正文摘录

### Anything you want to discuss about vllm. I was wondering why does this happen? I am new to this space and was playing around with different machines, models and frameworks. I am able to inference single image (on RTX3070) in around 70s using huggingface transformer. Tried similar thing using vllm (current main branch), it got out of memory which got me curious. ```python from transformers import AutoModelForCausalLM, AutoProcessor from PIL import Image import torch model_id = "microsoft/Phi-3-vision-128k-instruct" device = "cuda:0" model = AutoModelForCausalLM.from_pretrained(model_id, cache_dir="/content/my_models/phi_3_vision", device_map="cuda", trust_remote_code=True, torch_dtype="auto", _attn_implementation="eager") processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True) def process_image(image_path): """Processes a single image and returns the model's response.""" messages = [ { "role": "user", "content": " \nWhat is the destination address?", } ] prompt = processor.tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) image = Image.open(image_path) inputs = processor(prompt, [image], return_tensors="pt").to("cuda:0") g...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ? I am new to this space and was playing around with different machines, models and frameworks. I am able to inference single image (on RTX3070) in around 70s using huggingface transformer. Tried similar thing using vll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: it got out of memory which got me curious. ```python from transformers import AutoModelForCausalLM, AutoProcessor from PIL import Image import torch model_id = "microsoft/Phi-3-vision-128k-instruct" device = "cuda:0" mo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ust_remote_code=True, torch_dtype="auto", _attn_implementation="eager") processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True) def process_image(image_path): """Processes a sin
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Misc]: Curious why this is happening: Running phi-3-vision on a RTX 3070 (8GB VRAM) works with transformer but not with vllm (goes out of memory) ### Anything you want to discuss about vllm. I was wondering why does th...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: el_support;multimodal_vlm;quantization;sampling_logits cuda;quantization oom env_dependency;shape Anything you want to discuss about vllm.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
