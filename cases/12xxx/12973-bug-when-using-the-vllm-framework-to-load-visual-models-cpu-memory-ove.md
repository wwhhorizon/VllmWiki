# vllm-project/vllm#12973: [Bug]: When using the VLLM framework to load visual models, CPU memory overflow occurs while continuously processing data with images.

| 字段 | 值 |
| --- | --- |
| Issue | [#12973](https://github.com/vllm-project/vllm/issues/12973) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 34; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When using the VLLM framework to load visual models, CPU memory overflow occurs while continuously processing data with images.

### Issue 正文摘录

# The problem I encountered After deploying Qwen2-VL-7B-Instruct-GPTQ-Int4 using VLLM, continuous requests from clients will cause CPU memory to continue to rise. Is it because some memory has not been reclaimed? ﻿ My specific usage scenario is: I have two GPUs. When I use the ray framework for distributed deployment, as the number of VL models processed increases, my CPU memory becomes larger, leading to actor crashes in ray. ﻿ I have tested the native loading method of Qwen2-VL-7B-Instruct-GPTQ-Int4 and it does not cause CPU memory overflow. Once the VLLM framework is used for loading, there will be continuous CPU overflow ﻿ [Special note]: When you test, be sure to change the image each time, so that you can clearly see the CPU memory overflow. If only the same image is used, it will only leak once, causing the memory overflow to appear inconspicuous. # My code and environment ### Here is my code ``` def getMessage(pic_file): messages = [{'role': 'system', 'content': 'You are a very useful assistant, please strictly follow the requirements to complete the task!'}, {'role': 'user', 'content': [{'type': 'image_url', 'image_url': pic_file, 'min_pixels': 50176, 'max_pixels': 141120...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: When using the VLLM framework to load visual models, CPU memory overflow occurs while continuously processing data with images. bug # The problem I encountered After deploying Qwen2-VL-7B-Instruct-GPTQ-Int4 using...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tinue to rise. Is it because some memory has not been reclaimed? ﻿ My specific usage scenario is: I have two GPUs. When I use the ray framework for distributed deployment, as the number of VL models processed increases,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: g # The problem I encountered After deploying Qwen2-VL-7B-Instruct-GPTQ-Int4 using VLLM, continuous requests from clients will cause CPU memory to continue to rise. Is it because some memory has not been reclaimed? ﻿ My...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: path,temperature,top_p,max_token,min_pixels,max_pixels): os.environ["CUDA_VISIBLE_DEVICES"] ="0" model_path = "/mnt/data/programdata/vl_model/Qwen2-VL-7B-Instruct-GPTQ-Int4" llm = LLM(model=model_path, limit_mm_per_prom...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: c']) text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) image_inputs, _ = process_vision_info(messages) mm_data = {} if image_inputs is not None: mm_data["image"] = image_inputs l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
