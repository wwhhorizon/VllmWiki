# vllm-project/vllm#24784: [Bug]: multi_modal_uuids ignored during pre-processing

| 字段 | 值 |
| --- | --- |
| Issue | [#24784](https://github.com/vllm-project/vllm/issues/24784) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: multi_modal_uuids ignored during pre-processing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It appears multi_modal_uuids are ignored during request pre-processing (input_processor#preprocess) resulting in unnecessary hash calculations for all specified multimodal objects. Below is some minimal code to recreate this (requires you to have two test images locally). If you comment out the specification of multi_modal_uuids you'll notice that there is no change in speed. Prefix caching works correctly (as it relies on the redundant hashes calculated during #preprocess) but adding requests ends up being quite slow. ``` import random from vllm import LLM, SamplingParams from PIL import Image from transformers import AutoProcessor if __name__ == "__main__": model = LLM( model="Qwen/Qwen2.5-VL-7B-Instruct", trust_remote_code=True, enable_prefix_caching=True, allowed_local_media_path="/home/amith/metrics/annotations/corpus/full/images", max_model_len=10000, limit_mm_per_prompt={"image": 1, "video": 0}, ) processor = AutoProcessor.from_pretrained( "Qwen/Qwen2.5-VL-7B-Instruct" ) images = [Image.open(image_path).copy() for image_path in image_paths] batch_inputs = [] for image, image_path in zip(images, image_paths): for i in range...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: cessor#preprocess) resulting in unnecessary hash calculations for all specified multimodal objects. Below is some minimal code to recreate this (requires you to have two test images locally). If you comment out the spec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: preprocess) resulting in unnecessary hash calculations for all specified multimodal objects. Below is some minimal code to recreate this (requires you to have two test images locally). If you comment out the specificati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ix. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ### 🐛 Describe the bug It appears multi_modal_uuids are ignored during request pre-processing (input_processor#preprocess) resulting in unnecessary hash calculations for all specified multimodal objects. Below is some m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
