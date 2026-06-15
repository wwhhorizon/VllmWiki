# vllm-project/vllm#20607: [Bug]: Use VLLM to deploy the NYUAD-ComNets/FaceScanPaliGemma_Race model and google/paligemma2-3b-pt-224 as a tokenizer.

| 字段 | 值 |
| --- | --- |
| Issue | [#20607](https://github.com/vllm-project/vllm/issues/20607) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Use VLLM to deploy the NYUAD-ComNets/FaceScanPaliGemma_Race model and google/paligemma2-3b-pt-224 as a tokenizer.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Use VLLM to deploy the NYUAD-ComNets/FaceScanPaliGemma_Race model and google/paligemma2-3b-pt-224 as a tokenizer for race recognition.I placed the NYUAD-ComNets/FaceScanPaliGemma_Race model and google/paligemma2-3b-pt-224 in a folder and used the command: CUDA_VISIBLE_DEVICES=3 python -m vllm.entrypoints.openai.api_server --model /home/data/LLM/FaceScanPaliGemma_Fused --tokenizer /home/data/LLM/FaceScanPaliGemma_Fused --served-model-name FaceScanPaliGemma --dtype bfloat16 --port 8106 --host 0.0.0.0 However, this result is unstable and often wrong. However, using the reasoning example given by NYUAD-ComNets/FaceScanPaliGemma_Race, the result is very accurate. The reasoning method is as follows: from PIL import Image import torch from transformers import PaliGemmaProcessor, PaliGemmaForConditionalGeneration, BitsAndBytesConfig, TrainingArguments, Trainer model = PaliGemmaForConditionalGeneration.from_pretrained('NYUAD-ComNets/FaceScanPaliGemma_Race',torch_dtype=torch.bfloat16) input_text = "what is the race of the person in the image?" processor = PaliGemmaProcessor.from_pretrained("google/paligemma-3b-pt-224") device = torch.devic...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Use VLLM to deploy the NYUAD-ComNets/FaceScanPaliGemma_Race model and google/paligemma2-3b-pt-224 as a tokenizer. bug ### Your current environment ### 🐛 Describe the bug Use VLLM to deploy the NYUAD-ComNets/FaceS...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e result is very accurate. The reasoning method is as follows: from PIL import Image import torch from transformers import PaliGemmaProcessor, PaliGemmaForConditionalGeneration, BitsAndBytesConfig, TrainingArguments, Tr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: data/LLM/FaceScanPaliGemma_Fused --served-model-name FaceScanPaliGemma --dtype bfloat16 --port 8106 --host 0.0.0.0 However, this result is unstable and often wrong. However, using the reasoning example given by NYUAD-Co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model and google/paligemma2-3b-pt-224 in a folder and used the command: CUDA_VISIBLE_DEVICES=3 python -m vllm.entrypoints.openai.api_server --model /home/data/LLM/FaceScanPaliGemma_Fused --tokenizer /home/data/LLM/FaceS...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: output = model.generate(**inputs, max_length=500) result=processor.decode(output[0], skip_special_tokens=True)[len(input_text):].strip() Why does this problem happen? Thank you very much for taking the time out of your...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
