# vllm-project/vllm#10891: [Bug, V1]: LlaVa outputs wrong results in batch inference with V1 code（V0 code is correct)

| 字段 | 值 |
| --- | --- |
| Issue | [#10891](https://github.com/vllm-project/vllm/issues/10891) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug, V1]: LlaVa outputs wrong results in batch inference with V1 code（V0 code is correct)

### Issue 正文摘录

### Your current environment ### Model Input Dumps Version： 0.6.4.post2.dev221+g3bc94cab Test Image： [test_img.zip](https://github.com/user-attachments/files/18004889/test_img.zip) ### 🐛 Describe the bug @WoosukKwon Here is an fatal bug on V1 offline batch inference ``` import os from vllm import LLM, SamplingParams, envs from PIL import Image import time prompt = "USER: \nWhat is the content of this image?\nASSISTANT:" fname = 'animal.jpg' # get form the .zip file image = Image.open(fname).convert('RGB') envs.VLLM_USE_V1 = True llm = LLM(model='llava-1.5-7b-hf', trust_remote_code=True, dtype="bfloat16", tokenizer_mode="auto", gpu_memory_utilization=0.9, max_model_len=1000, max_num_batched_tokens=1200) sampling_params = SamplingParams(temperature=0, max_tokens=128) inputs = { "prompt": prompt, "multi_modal_data": { "image": image } } outputs = llm.generate([inputs, inputs], sampling_params) for output in outputs: text = output.outputs[0].text print(text) print() print("done") ``` The output is > The image features a black and white panda bear sitting in a grassy area. The panda is eating grass, and it appears to be enjoying the meal. The scene is set in a lush green environment, w...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: is correct) bug ### Your current environment ### Model Input Dumps Version： 0.6.4.post2.dev221+g3bc94cab Test Image： [test_img.zip](https://github.com/user-attachments/files/18004889/test_img.zip) ### 🐛 Describe the bug...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: USE_V1 = True llm = LLM(model='llava-1.5-7b-hf', trust_remote_code=True, dtype="bfloat16", tokenizer_mode="auto", gpu_memory_utilization=0.9, max_model_len=1000, max_num_batched_tokens=1200) sampling_params = SamplingPa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ith V1 code（V0 code is correct) bug ### Your current environment ### Model Input Dumps Version： 0.6.4.post2.dev221+g3bc94cab Test Image： [test_img.zip](https://github.com/user-attachments/files/18004889/test_img.zip) ##...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ult ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tization;sampling_logits;speculative_decoding cuda;operator;quantization;triton build_error dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
