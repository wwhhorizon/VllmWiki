# vllm-project/vllm#15496: [Bug]: Llama-3.2-11B-Vision-Instruct has an issue in vision language embedding

| 字段 | 值 |
| --- | --- |
| Issue | [#15496](https://github.com/vllm-project/vllm/issues/15496) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama-3.2-11B-Vision-Instruct has an issue in vision language embedding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Tried to Run `meta-llama/Llama-3.2-11B-Vision-Instruct` to generate embedding but got an error. ``` import torch from vllm import LLM from vllm.multimodal.utils import fetch_image # Model Selection MODEL_NAME = "meta-llama/Llama-3.2-11B-Vision-Instruct" # Image and Prompt IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/American_Eskimo_Dog.jpg/360px-American_Eskimo_Dog.jpg" PROMPT = " Describe the scene in detail." # Fetch Image image_data = fetch_image(IMAGE_URL) # Initialize Model llm = LLM( model=MODEL_NAME, task="embed", trust_remote_code=True, allowed_local_media_path=True, max_model_len=1000, max_num_seqs=1, tensor_parallel_size=4, limit_mm_per_prompt={"image": 1, "video": 1} ) # Run Inference output = llm.embed({"prompt": PROMPT, "multi_modal_data": {"image": image_data}}) # Print Result print("Output Embedding:", output[0].outputs.embedding) ``` INFO 03-25 17:34:33 [__init__.py:256] Automatically detected platform cuda. WARNING 03-25 17:37:12 [config.py:676] CUDA graph is not supported for mllama yet, fallback to the eager mode. WARNING 03-25 17:37:46 [arg_utils.py:1765] --task embed is not supported...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: ma-3.2-11B-Vision-Instruct has an issue in vision language embedding bug;stale ### Your current environment ### 🐛 Describe the bug Tried to Run `meta-llama/Llama-3.2-11B-Vision-Instruct` to generate embedding but got an...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Llama-3.2-11B-Vision-Instruct has an issue in vision language embedding bug;stale ### Your current environment ### 🐛 Describe the bug Tried to Run `meta-llama/Llama-3.2-11B-Vision-Instruct` to generate embedding...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ma-3.2-11B-Vision-Instruct` to generate embedding but got an error. ``` import torch from vllm import LLM from vllm.multimodal.utils import fetch_image # Model Selection MODEL_NAME = "meta-llama/Llama-3.2-11B-Vision-Ins...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: -25 17:37:12 [config.py:676] CUDA graph is not supported for mllama yet, fallback to the eager mode. WARNING 03-25 17:37:46 [arg_utils.py:1765] --task embed is not supported by the V1 Engine. Falling back to V0. INFO 03...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ide_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=1000, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
