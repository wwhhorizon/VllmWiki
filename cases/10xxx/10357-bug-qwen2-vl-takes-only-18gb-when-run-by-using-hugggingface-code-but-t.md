# vllm-project/vllm#10357: [Bug]: Qwen2 VL takes only 18Gb when run by using hugggingface code, but the same model takes 38 GB GPU memory with VLM

| 字段 | 值 |
| --- | --- |
| Issue | [#10357](https://github.com/vllm-project/vllm/issues/10357) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2 VL takes only 18Gb when run by using hugggingface code, but the same model takes 38 GB GPU memory with VLM

### Issue 正文摘录

### Your current environment ### Model Input Dumps Thanks for the great work. I used to run multimodels by using huggingface, recently i heard about vLLM and checked the same model in huggingface and by using the code in vLLM. Noted the GPU usage is 1x than in vLLM. Please check the below results for more information. Model : Qwen2-VL-7B-Instruct Machine: NVIDIA A100 Image & prompt: Used same image and prompt for both experiments. ### 🐛 Describe the bug **Huggingface code** ```python from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor from qwen_vl_utils import process_vision_info model = Qwen2VLForConditionalGeneration.from_pretrained( "Qwen/Qwen2-VL-7B-Instruct", torch_dtype="auto", device_map="auto" ) processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct") messages = [ { "role": "user", "content": [ { "type": "image", "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg", }, {"type": "text", "text": "Describe this image."}, ], } ] text = processor.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) image_inputs, video_inputs = process_vision_info(messages) inputs = processor(...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen2 VL takes only 18Gb when run by using hugggingface code, but the same model takes 38 GB GPU memory with VLM bug ### Your current environment ### Model Input Dumps Thanks for the great work. I used to run mul...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ## 🐛 Describe the bug **Huggingface code** ```python from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor from qwen_vl_utils import process_vision_info model = Qwen2VLForConditionalGene...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: in zip(inputs.input_ids, generated_ids) ] output_text = processor.batch_decode( generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False ) print(output_text) ``` **GPU Usage :** ![image](https...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: tionalGeneration.from_pretrained( "Qwen/Qwen2-VL-7B-Instruct", torch_dtype="auto", device_map="auto" ) processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct") messages = [ { "role": "user", "content": [ {...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ults for more information. Model : Qwen2-VL-7B-Instruct Machine: NVIDIA A100 Image & prompt: Used same image and prompt for both experiments. ### 🐛 Describe the bug **Huggingface code** ```python from transformers impor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
