# vllm-project/vllm#10153: [Usage]: How to use vllm to run Qwen2-VL-72B?

| 字段 | 值 |
| --- | --- |
| Issue | [#10153](https://github.com/vllm-project/vllm/issues/10153) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | sampling |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to use vllm to run Qwen2-VL-72B?

### Issue 正文摘录

### Your current environment ``` from transformers import AutoProcessor from vllm import LLM, SamplingParams from qwen_vl_utils import process_vision_info MODEL_PATH = "/path/Qwen2-VL-72B-Instruct" llm = LLM( model=MODEL_PATH, limit_mm_per_prompt={"image": 10, "video": 10}, ) sampling_params = SamplingParams( temperature=0.1, top_p=0.001, repetition_penalty=1.05, max_tokens=256, stop_token_ids=[], ) messages = [ {"role": "system", "content": "You are a helpful assistant."}, { "role": "user", "content": [ { "type": "image", "image": "porsche.jpg", "min_pixels": 224 * 224, "max_pixels": 1280 * 28 * 28, }, {"type": "text", "text": "What is the text in the illustrate?"}, ], }, ] # For video input, you can pass following values instead: # "type": "video", # "video": " ", processor = AutoProcessor.from_pretrained(MODEL_PATH) prompt = processor.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, ) image_inputs, video_inputs = process_vision_info(messages) mm_data = {} if image_inputs is not None: mm_data["image"] = image_inputs if video_inputs is not None: mm_data["video"] = video_inputs llm_inputs = { "prompt": prompt, "multi_modal_data": mm_data, } outputs = llm....

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: you like to use vllm I want to run inference of a Qwen2-VL-72B. I use 4 H100-80G. However, it always has out of memory problem. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to use vllm to run Qwen2-VL-72B? usage ### Your current environment ``` from transformers import AutoProcessor from vllm import LLM, SamplingParams from qwen_vl_utils import process_vision_info MODEL_PATH =...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Qwen2-VL-72B? usage ### Your current environment ``` from transformers import AutoProcessor from vllm import LLM, SamplingParams from qwen_vl_utils import process_vision_info MODEL_PATH = "/path/Qwen2-VL-72B-Instruct" l...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ntly asked questions. performance model_support;sampling_logits sampling oom Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: TH) prompt = processor.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, ) image_inputs, video_inputs = process_vision_info(messages) mm_data = {} if image_inputs is not None: mm_data["image"] =...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
