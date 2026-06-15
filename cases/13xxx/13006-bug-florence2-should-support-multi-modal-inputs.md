# vllm-project/vllm#13006: [Bug]: florence2 should support multi-modal inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#13006](https://github.com/vllm-project/vllm/issues/13006) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: florence2 should support multi-modal inputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to use florenc2 via vllm as your guidance https://docs.vllm.ai/en/latest/getting_started/examples/florence2_inference.html shows, but it seems to use the model as a llm model, other than a vlm model. If i tried to use a multi-modal input, it returns: ValueError: Your model does not support multi-modal inputs should it support multi-modal input since it's a vlm model? Detailed script like below, just changed the input from example to multi-modal input. from PIL import Image from vllm import LLM, SamplingParams import time import torch dtype = torch.float16 llm = LLM( model="Florence-2-base", tokenizer="bart-base", dtype=dtype, trust_remote_code=True, ) prompts = ["\ "] sampling_params = SamplingParams( temperature=0.2, top_p=1.0, min_tokens=0, max_tokens=200, ) image = Image.open("car.jpg").convert("RGB") inputs = { "prompt": prompts, "multi_modal_data": { "image": image }, } outputs = llm.generate(inputs, sampling_params) for output in outputs: prompt = output.prompt encoder_prompt = output.encoder_prompt generated_text = output.outputs[0].text print(f"Encoder prompt: {encoder_prompt!r}, " f"Decoder prompt: {prompt!r},...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: low, just changed the input from example to multi-modal input. from PIL import Image from vllm import LLM, SamplingParams import time import torch dtype = torch.float16 llm = LLM( model="Florence-2-base", tokenizer="bar...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ort Image from vllm import LLM, SamplingParams import time import torch dtype = torch.float16 llm = LLM( model="Florence-2-base", tokenizer="bart-base", dtype=dtype, trust_remote_code=True, ) prompts = ["\ "] sampling_p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: started/examples/florence2_inference.html shows, but it seems to use the model as a llm model, other than a vlm model. If i tried to use a multi-modal input, it returns: ValueError: Your model does not support multi-mod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: florence2 should support multi-modal inputs bug;stale ### Your current environment ### 🐛 Describe the bug I'm trying to use florenc2 via vllm as your guidance https://docs.vllm.ai/en/latest/getting_started/exampl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: }") ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
