# vllm-project/vllm#15125: [Usage]: Qwen2.5-VL-7B-Instruct <|vision_start|><|image_pad|><|vision_end|> always appears before the user text, even i set image after user text

| 字段 | 值 |
| --- | --- |
| Issue | [#15125](https://github.com/vllm-project/vllm/issues/15125) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Qwen2.5-VL-7B-Instruct <\|vision_start\|><\|image_pad\|><\|vision_end\|> always appears before the user text, even i set image after user text

### Issue 正文摘录

### Your current environment ```text I use docker image vllm openai 0.7.3 ``` The phenomenon is consistent with this issue #10286, as image_pad always appears before the user text. using hf transformers ```python from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor from qwen_vl_utils import process_vision_info # default: Load the model on the available device(s) model = Qwen2_5_VLForConditionalGeneration.from_pretrained( "/qwen2.5-vl//Qwen2.5-VL-7B-Instruct", torch_dtype="auto", device_map="auto" ) # default processor processor = AutoProcessor.from_pretrained("/qwen2.5-vl/Qwen2.5-VL-7B-Instruct") messages = [ { "role": "user", "content": [ {"type": "text", "text": "Describe this image."}, { "type": "image", "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg", }, ], } ] # Preparation for inference text = processor.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) print('--------input text after apply_chat_template') print(text) image_inputs, video_inputs = process_vision_info(messages) inputs = processor( text=[text], images=image_inputs, videos=video_inputs, padding=True, return_tensors="pt", ) inputs...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: image after user text usage ### Your current environment ```text I use docker image vllm openai 0.7.3 ``` The phenomenon is consistent with this issue #10286, as image_pad always appears before the user text. using hf t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: id shirt and dark pants, with her legs crossed. She has long hair and is smiling warmly at a large, light-colored dog that is sitting beside her. The dog is wearing a harness and leash, and it is extending its paw towar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Qwen2.5-VL-7B-Instruct <|vision_start|><|image_pad|><|vision_end|> always appears before the user text, even i set image after user text usage ### Your current environment ```text I use docker image vllm openai...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: in zip(inputs.input_ids, generated_ids) ] output_text = processor.batch_decode( generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False ) print(output_text) ``` output ```text --------input t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ration.from_pretrained( "/qwen2.5-vl//Qwen2.5-VL-7B-Instruct", torch_dtype="auto", device_map="auto" ) # default processor processor = AutoProcessor.from_pretrained("/qwen2.5-vl/Qwen2.5-VL-7B-Instruct") messages = [ { "...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
