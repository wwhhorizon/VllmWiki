# vllm-project/vllm#19191: [Bug]: Internvl model performance degradation on v0.8.3 when switching engine from V1 to V0

| 字段 | 值 |
| --- | --- |
| Issue | [#19191](https://github.com/vllm-project/vllm/issues/19191) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;oom;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Internvl model performance degradation on v0.8.3 when switching engine from V1 to V0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I installed vllm v0.8.3 using pip, then I compared speed of one sample image offline inference on Internvl-v2 1B model using V1 and V0 backend separately. The result is: V1 is slower than V0 engine. ```python import time from vllm import LLM, SamplingParams from PIL import Image from transformers import AutoModel, AutoTokenizer # InternVL def run_internvl(question: str): model_name = "path to internvl-v2-1B model" llm = LLM( model=model_name, trust_remote_code=True, ) tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True) messages = [{'role': 'user', 'content': f" \n{question}"}] prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) # Stop tokens for InternVL # models variants may have different stop tokens # please refer to the model card for the correct "stop words": # https://huggingface.co/OpenGVLab/InternVL2-2B/blob/main/conversation.py stop_tokens = [" ", " ", " "] #, " "] # stop_tokens = [] stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens] return llm, prompt, stop_token_ids question = "Convert this table to LaTeX." llm, prompt, stop_toke...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Internvl model performance degradation on v0.8.3 when switching engine from V1 to V0 bug;stale ### Your current environment ### 🐛 Describe the bug I installed vllm v0.8.3 using pip, then I compared speed of one s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: V0 bug;stale ### Your current environment ### 🐛 Describe the bug I installed vllm v0.8.3 using pip, then I compared speed of one sample image offline inference on Internvl-v2 1B model using V1 and V0 backend separately....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: erformance degradation on v0.8.3 when switching engine from V1 to V0 bug;stale ### Your current environment ### 🐛 Describe the bug I installed vllm v0.8.3 using pip, then I compared speed of one sample image offline inf...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: e sample image offline inference on Internvl-v2 1B model using V1 and V0 backend separately. The result is: V1 is slower than V0 engine. ```python import time from vllm import LLM, SamplingParams from PIL import Image f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ide_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
