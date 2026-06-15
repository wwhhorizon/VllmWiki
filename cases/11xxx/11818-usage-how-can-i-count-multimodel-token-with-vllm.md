# vllm-project/vllm#11818: [Usage]: how can i count multimodel token with vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#11818](https://github.com/vllm-project/vllm/issues/11818) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how can i count multimodel token with vllm?

### Issue 正文摘录

### Your current environment ```python from vllm import LLM from vllm.sampling_params import SamplingParams import torch from PIL import Image import io import requests import os # Define the model and sampling parameters MODEL_NAME = "OpenGVLab/InternVL2_5-4B" sampling_params = SamplingParams(max_tokens=300, temperature=0.01, top_p=0.001) # Define context length and number of devices context_length = 3000 num_device = 2 # Initialize the LLM with the allowed local media path llm = LLM( model=MODEL_NAME, tokenizer=MODEL_NAME, speculative_max_model_len=context_length, max_seq_len_to_capture=context_length, max_model_len=context_length, tensor_parallel_size=num_device, trust_remote_code=True, worker_use_ray=num_device, dtype=torch.float16, enable_chunked_prefill=True, gpu_memory_utilization=0.60, enforce_eager=True, max_num_batched_tokens=context_length, allowed_local_media_path="/kaggle/working/" # Add this line , # quantization="fp8" # enable_prefix_caching=True, ) # Define the prompt and image path prompt = "Describe this image in one sentence." image_path = "/kaggle/working/dubu.png" # Function to get image token count def get_image_token_count(image_path, llm): # Get image size...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: m_device, trust_remote_code=True, worker_use_ray=num_device, dtype=torch.float16, enable_chunked_prefill=True, gpu_memory_utilization=0.60, enforce_eager=True, max_num_batched_tokens=context_length, allowed_local_media_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: how can i count multimodel token with vllm? usage ### Your current environment ```python from vllm import LLM from vllm.sampling_params import SamplingParams import torch from PIL import Image import io import...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: oken with vllm? usage ### Your current environment ```python from vllm import LLM from vllm.sampling_params import SamplingParams import torch from PIL import Image import io import requests import os # Define the model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: mport SamplingParams import torch from PIL import Image import io import requests import os # Define the model and sampling parameters MODEL_NAME = "OpenGVLab/InternVL2_5-4B" sampling_params = SamplingParams(max_tokens=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
