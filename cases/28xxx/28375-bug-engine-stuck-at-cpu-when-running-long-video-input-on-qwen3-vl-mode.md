# vllm-project/vllm#28375: [Bug]: Engine stuck at CPU when running long video input on Qwen3-vl model

| 字段 | 值 |
| --- | --- |
| Issue | [#28375](https://github.com/vllm-project/vllm/issues/28375) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;sampling |
| 症状 | oom |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine stuck at CPU when running long video input on Qwen3-vl model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running video input above ~200k video tokens, the engine will be stuck at the `Processed prompts` and GPU utilization is 0. And in multiproc executor, it is infinitely sending empty inputs to workers and receiving null responses. - Sample Code, A case from LVBench ``` # -*- coding: utf-8 -*- import torch from qwen_vl_utils import process_vision_info from transformers import AutoProcessor from vllm import LLM, SamplingParams import time import os def prepare_inputs_for_vllm(messages, processor): text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) # qwen_vl_utils 0.0.14+ reqired image_inputs, video_inputs, video_kwargs = process_vision_info( messages, image_patch_size=processor.image_processor.patch_size, return_video_kwargs=True, return_video_metadata=True ) print(f"video_kwargs: {video_kwargs}") mm_data = {} if image_inputs is not None: mm_data['image'] = image_inputs if video_inputs is not None: mm_data['video'] = video_inputs video_kwargs['do_resize'] = False return { 'prompt': text, 'multi_modal_data': mm_data, 'mm_processor_kwargs': video_kwargs } if __name__ == '__main__': messages...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Engine stuck at CPU when running long video input on Qwen3-vl model bug;stale ### Your current environment ### 🐛 Describe the bug When running video input above ~200k video tokens, the engine will be stuck at the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ] } ] checkpoint_path = "Qwen/Qwen3-VL-30B-A3B-Instruct-FP8" processor = AutoProcessor.from_pretrained(checkpoint_path) torch.cuda.synchronize() startt = time.time() inputs = [prepare_inputs_for_vllm(message, processor)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: rocessor): text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) # qwen_vl_utils 0.0.14+ reqired image_inputs, video_inputs, video_kwargs = process_vision_info( messages, image_patch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Engine stuck at CPU when running long video input on Qwen3-vl model bug;stale ### Your current environment ### 🐛 Describe the bug When running video input above ~200k video tokens, the engine will be stuck at the `Proce...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ponses. - Sample Code, A case from LVBench ``` # -*- coding: utf-8 -*- import torch from qwen_vl_utils import process_vision_info from transformers import AutoProcessor from vllm import LLM, SamplingParams import time i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
