# vllm-project/vllm#30776: [Usage]: Qwen3-omni's offline usage

| 字段 | 值 |
| --- | --- |
| Issue | [#30776](https://github.com/vllm-project/vllm/issues/30776) |
| 状态 | closed |
| 标签 | bug;usage;stale |
| 评论 | 52; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Qwen3-omni's offline usage

### Issue 正文摘录

### Your current environment I used the code below in vllm==0.12.0, but failed. ``` import os import torch from vllm import LLM, SamplingParams from transformers import Qwen3OmniMoeProcessor from qwen_omni_utils import process_mm_info def build_input(processor, messages, use_audio_in_video): text = processor.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, ) # print(text[0]) # print(len(text[0])) audios, images, videos = process_mm_info(messages, use_audio_in_video=use_audio_in_video) inputs = { 'prompt': text, 'multi_modal_data': {}, "mm_processor_kwargs": { "use_audio_in_video": use_audio_in_video, }, } if images is not None: inputs['multi_modal_data']['image'] = images if videos is not None: inputs['multi_modal_data']['video'] = videos if audios is not None: inputs['multi_modal_data']['audio'] = audios return inputs if __name__ == '__main__': # vLLM engine v1 not supported yet os.environ['VLLM_USE_V1'] = '1' os.environ['CUDA_DEVICES'] = '0,1,2,3,4,5,6,7' MODEL_PATH = "Qwen3-Omni-30B-A3B-Instruct" llm = LLM( model=MODEL_PATH, trust_remote_code=True, gpu_memory_utilization=0.95, tensor_parallel_size=1, limit_mm_per_prompt={'image': 3, 'video': 3, 'audio'...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rent environment I used the code below in vllm==0.12.0, but failed. ``` import os import torch from vllm import LLM, SamplingParams from transformers import Qwen3OmniMoeProcessor from qwen_omni_utils import process_mm_i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Usage]: Qwen3-omni's offline usage bug;usage;stale ### Your current environment I used the code below in vllm==0.12.0, but failed. ``` import os import torch from vllm import LLM, SamplingParams from transformers impor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Qwen3-omni's offline usage bug;usage;stale ### Your current environment I used the code below in vllm==0.12.0, but failed. ``` import os import torch from vllm import LLM, SamplingParams from transformers impor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
