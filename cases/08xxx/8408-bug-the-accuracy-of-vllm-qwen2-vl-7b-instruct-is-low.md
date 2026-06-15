# vllm-project/vllm#8408: [Bug]: The accuracy of vllm-Qwen2-VL-7B-Instruct is low.

| 字段 | 值 |
| --- | --- |
| Issue | [#8408](https://github.com/vllm-project/vllm/issues/8408) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The accuracy of vllm-Qwen2-VL-7B-Instruct is low.

### Issue 正文摘录

### Your current environment from PIL import Image from transformers import AutoProcessor from vllm import LLM, SamplingParams from qwen_vl_utils import process_vision_info MODEL_PATH = '/workspace/mnt/storage/trt-llama/Qwen2-VL-7B-Instruct' IMAGE_PATH = '/workspace/mnt/storage/llm_storge/vllm/examples/demo.jpeg' llm = LLM( model=MODEL_PATH, dtype = 'float32', limit_mm_per_prompt={'image': 10, 'video': 10}, ) sampling_params = SamplingParams( temperature=0.1, top_p=0.001, repetition_penalty=1.05, max_tokens=256, stop_token_ids=[], ) messages = [ {'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': [ { 'type': 'image', 'image': IMAGE_PATH, 'max_pixels': 12845056, }, { 'type': 'text', 'text': '输出击掌的检测框', }, ]}, ] processor = AutoProcessor.from_pretrained(MODEL_PATH) prompt = processor.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, ) image_inputs, video_inputs = process_vision_info(messages) mm_data = {} if image_inputs is not None: mm_data['image'] = image_inputs if video_inputs is not None: mm_data['video'] = video_inputs llm_inputs = { 'prompt': prompt, 'multi_modal_data': mm_data, } #击掌(529,516),(583,594) outputs =...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: The accuracy of vllm-Qwen2-VL-7B-Instruct is low. bug;stale ### Your current environment from PIL import Image from transformers import AutoProcessor from vllm import LLM, SamplingParams from qwen_vl_utils import...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: lm_storge/vllm/examples/demo.jpeg' llm = LLM( model=MODEL_PATH, dtype = 'float32', limit_mm_per_prompt={'image': 10, 'video': 10}, ) sampling_params = SamplingParams( temperature=0.1, top_p=0.001, repetition_penalty=1.0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: The accuracy of vllm-Qwen2-VL-7B-Instruct is low. bug;stale ### Your current environment from PIL import Image from transformers import AutoProcessor from vllm import LLM, SamplingParams from qwen_vl_utils import...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: The accuracy of vllm-Qwen2-VL-7B-Instruct is low. bug;stale ### Your current environment from PIL import Image from transformers import AutoProcessor from vllm import LLM, SamplingParams from qwen_vl_utils import...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -VL-7B-Instruct is low. bug;stale ### Your current environment from PIL import Image from transformers import AutoProcessor from vllm import LLM, SamplingParams from qwen_vl_utils import process_vision_info MODEL_PATH =...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
