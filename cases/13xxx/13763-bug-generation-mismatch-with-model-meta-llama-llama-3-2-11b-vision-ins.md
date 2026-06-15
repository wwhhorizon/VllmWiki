# vllm-project/vllm#13763: [Bug]: Generation mismatch with Model: meta-llama/Llama-3.2-11B-Vision-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#13763](https://github.com/vllm-project/vllm/issues/13763) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Generation mismatch with Model: meta-llama/Llama-3.2-11B-Vision-Instruct

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The output tokens generated from the Model: meta-llama/Llama-3.2-11B-Vision-Instruct with vLLM is different from the one from the transformer library. This seems to happen only when an image is provided in the prompt. The vLLM is run using Open AI API server. Code to generate Transformer result ``` import requests import torch from PIL import Image from transformers import AutoProcessor, AutoTokenizer, MllamaForConditionalGeneration model_id = "meta-llama/Llama-3.2-11B-Vision-Instruct" model = MllamaForConditionalGeneration.from_pretrained( model_id, torch_dtype=torch.bfloat16, device_map="auto", ) processor = AutoProcessor.from_pretrained(model_id) tokenizer = AutoTokenizer.from_pretrained(model_id) url = "https://www.jpcbank.com/assets/img/JPCB_Sample_Cheque_for_PPS.png" image = Image.open(url) messages = [ {"role": "user", "content": [ {"type": "image"}, {"type": "text", "text": "Extract text from the image. Do not generate other explanation, only generate text written on the image, with fields IFC Code, Amount, Account Name, Amount etc."} ]} ] input_text = processor.apply_chat_template(messages, add_generation_prompt=True) in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s run using Open AI API server. Code to generate Transformer result ``` import requests import torch from PIL import Image from transformers import AutoProcessor, AutoTokenizer, MllamaForConditionalGeneration model_id =...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ration mismatch with Model: meta-llama/Llama-3.2-11B-Vision-Instruct bug;stale ### Your current environment ### 🐛 Describe the bug The output tokens generated from the Model: meta-llama/Llama-3.2-11B-Vision-Instruct wit...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: MllamaForConditionalGeneration.from_pretrained( model_id, torch_dtype=torch.bfloat16, device_map="auto", ) processor = AutoProcessor.from_pretrained(model_id) tokenizer = AutoTokenizer.from_pretrained(model_id) url = "h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Generation mismatch with Model: meta-llama/Llama-3.2-11B-Vision-Instruct bug;stale ### Your current environment ### 🐛 Describe the bug The output tokens generated from the Model: meta-llama/Llama-3.2-11B-Vision-I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Generation mismatch with Model: meta-llama/Llama-3.2-11B-Vision-Instruct bug;stale ### Your current environment ### 🐛 Describe the bug The output tokens generated from the Model: meta-llama/Llama-3.2-11B-Vision-I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
