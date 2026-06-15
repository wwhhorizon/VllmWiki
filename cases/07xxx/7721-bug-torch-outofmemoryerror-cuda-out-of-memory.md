# vllm-project/vllm#7721: [Bug]: torch.OutOfMemoryError: CUDA out of memory

| 字段 | 值 |
| --- | --- |
| Issue | [#7721](https://github.com/vllm-project/vllm/issues/7721) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.OutOfMemoryError: CUDA out of memory

### Issue 正文摘录

### Your current environment ![img_v3_02du_9ada6e58-9987-48f4-951c-267a26b083dg](https://github.com/user-attachments/assets/44efcaec-d7ca-473e-8a73-25f0771ba787) ### 🐛 Describe the bug my py script is as follows: ```py from vllm import LLM, SamplingParams from transformers import AutoModel, AutoTokenizer import os import torch from PIL import Image torch.cuda.empty_cache() model_name = "./MiniCPM-V-2_6/" tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True) llm = LLM( model=model_name, trust_remote_code=True, tensor_parallel_size=1, gpu_memory_utilization=0.9, max_seq_len_to_capture=2048, enforce_eager=False ) ``` after Runing the code, i get an OOM error ```text 2024-08-21 07:23:29,967 - root - INFO - I'm a message 2024-08-21 07:23:33,518 - datasets - INFO - PyTorch version 2.4.0 available. 2024-08-21 07:23:33,712 - root - INFO - app 2024-08-21 07:23:34,290 - transformers_modules.v1.configuration_minicpm - INFO - vision_config is None, using default vision config INFO 08-21 07:23:34 llm_engine.py:174] Initializing an LLM engine (v0.5.4) with config: model='/opt/apps/models/miniCPM-v2.6/v1', speculative_config=None, tokenizer='/opt/apps/models/miniCPM-v2.6/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 7) ### 🐛 Describe the bug my py script is as follows: ```py from vllm import LLM, SamplingParams from transformers import AutoModel, AutoTokenizer import os import torch from PIL import Image torch.cuda.empty_cache() mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ```py from vllm import LLM, SamplingParams from transformers import AutoModel, AutoTokenizer import os import torch from PIL import Image torch.cuda.empty_cache() model_name = "./MiniCPM-V-2_6/" tokenizer = AutoTokenize...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None), seed=0, served_model_name=/opt/apps/models/miniCPM-v2.6/...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: enforce_eager=False ) ``` after Runing the code, i get an OOM error ```text 2024-08-21 07:23:29,967 - root - INFO - I'm a message 2024-08-21 07:23:33,518 - datasets - INFO - PyTorch version 2.4.0 available. 2024-08-21 0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
