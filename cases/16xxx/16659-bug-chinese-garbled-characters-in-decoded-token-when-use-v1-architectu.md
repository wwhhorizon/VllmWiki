# vllm-project/vllm#16659: [Bug]: Chinese garbled characters in decoded_token when use V1 architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#16659](https://github.com/vllm-project/vllm/issues/16659) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Chinese garbled characters in decoded_token when use V1 architecture

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use V1 architecture and set logprobs=0, decoded_token in Logprobs would be chinese garbled characters. However, this issue doesn't occur with the V0 architecture. The opensource model Qwen2.5-VL-7B-Instruct was used for testing. ```python from transformers import AutoProcessor from vllm import LLM, SamplingParams from PIL import Image from qwen_vl_utils import process_vision_info MODEL_PATH = "/home/llm_infer/99-vllm-debug/00-src-files/00-checkpoints/huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct" llm = LLM( model=MODEL_PATH, limit_mm_per_prompt={"image": 1, "video": 0}, max_model_len=8192, max_num_seqs=1 ) sampling_params = SamplingParams( temperature=0.1, top_p=0.001, repetition_penalty=1.05, max_tokens=256, stop_token_ids=[], logprobs=0 ) image_messages = [ {"role": "system", "content": "You are a helpful assistant."}, { "role": "user", "content": [ { "type": "image", "image": Image.open("/home/llm_infer/99-vllm-debug/10-vllm-debug/demo.jpeg").convert('RGB'), "min_pixels": 224 * 224, "max_pixels": 1280 * 28 * 28, }, {"type": "text", "text": "用中文描述一下这张图片"}, ], }, ] # For video input, you can pass following values instead: #...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Chinese garbled characters in decoded_token when use V1 architecture bug;stale ### Your current environment ### 🐛 Describe the bug When I use V1 architecture and set logprobs=0, decoded_token in Logprobs would be...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Qwen2.5-VL-7B-Instruct was used for testing. ```python from transformers import AutoProcessor from vllm import LLM, SamplingParams from PIL import Image from qwen_vl_utils import process_vision_info MODEL_PATH = "/home/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: wever, this issue doesn't occur with the V0 architecture. The opensource model Qwen2.5-VL-7B-Instruct was used for testing. ```python from transformers import AutoProcessor from vllm import LLM, SamplingParams from PIL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Chinese garbled characters in decoded_token when use V1 architecture bug;stale ### Your current environment ### 🐛 Describe the bug When I use V1 architecture and set logprobs=0, decoded_token in Logprobs would be...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
