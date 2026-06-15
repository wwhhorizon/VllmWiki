# vllm-project/vllm#8276: [Usage]: multi image inference for "OpenGVLab/InternVL2-8B" not working

| 字段 | 值 |
| --- | --- |
| Issue | [#8276](https://github.com/vllm-project/vllm/issues/8276) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: multi image inference for "OpenGVLab/InternVL2-8B" not working

### Issue 正文摘录

multi image inference for "OpenGVLab/InternVL2-8B" not working I got this inference code from here https://github.com/vllm-project/vllm/blob/main/examples/offline_inference_vision_language_multi_image.py ````python from typing import List from vllm import LLM, SamplingParams from vllm.multimodal.utils import fetch_image from transformers import AutoTokenizer import torch num_device = 2 QUESTION = "What is the content of each image?" IMAGE_URLS = [ "https://upload.wikimedia.org/wikipedia/commons/d/da/2015_Kaczka_krzy%C5%BCowka_w_wodzie_%28samiec%29.jpg", "https://upload.wikimedia.org/wikipedia/commons/7/77/002_The_lion_king_Snyggve_in_the_Serengeti_National_Park_Photo_by_Giles_Laurent.jpg", ] def load_internvl(question: str, image_urls: List[str]): model_name = "OpenGVLab/InternVL2-8B" llm = LLM( model=model_name, trust_remote_code=True, max_num_seqs=5, max_model_len=3096, limit_mm_per_prompt={"image": len(image_urls)} , tensor_parallel_size=num_device,worker_use_ray=num_device,dtype=torch.float16 , enable_chunked_prefill=True ,gpu_memory_utilization = 0.99 , enforce_eager=True ) tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True) placeholders = "\n".join(...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: multi image inference for "OpenGVLab/InternVL2-8B" not working usage multi image inference for "OpenGVLab/InternVL2-8B" not working I got this inference code from here https://github.com/vllm-project/vllm/blob/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: worker_use_ray=num_device,dtype=torch.float16 , enable_chunked_prefill=True ,gpu_memory_utilization = 0.99 , enforce_eager=True ) tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True) placeholder...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: offline_inference_vision_language_multi_image.py ````python from typing import List from vllm import LLM, SamplingParams from vllm.multimodal.utils import fetch_image from transformers import AutoTokenizer import torch...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: "}] prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) # Stop tokens for InternVL stop_tokens = [" ", " ", " ", " "] stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: image_urls)} , tensor_parallel_size=num_device,worker_use_ray=num_device,dtype=torch.float16 , enable_chunked_prefill=True ,gpu_memory_utilization = 0.99 , enforce_eager=True ) tokenizer = AutoTokenizer.from_pretrained(...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
