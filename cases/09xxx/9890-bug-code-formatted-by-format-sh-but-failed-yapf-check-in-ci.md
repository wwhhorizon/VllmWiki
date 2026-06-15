# vllm-project/vllm#9890: [Bug]: Code formatted by format.sh but failed yapf check in CI

| 字段 | 值 |
| --- | --- |
| Issue | [#9890](https://github.com/vllm-project/vllm/issues/9890) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Code formatted by format.sh but failed yapf check in CI

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The code snippet was formatted using format.sh but failed the YAPF check in CI https://github.com/cooleel/vllm/blob/5c2ed3305bc8d3c0caa831eb7e4c217d9c754639/tests/models/decoder_only/vision_language/vlm_utils/model_utils.py#L283-L284 The yapf error message is ``` Run yapf --diff --recursive . --- ./tests/models/decoder_only/vision_language/vlm_utils/model_utils.py (original) +++ ./tests/models/decoder_only/vision_language/vlm_utils/model_utils.py (reformatted) @@ -280,8 +280,10 @@ def __call__(self, text: str, images: Union[Image, List[Image]], **kwargs): - from vllm.model_executor.models.h2ovl import ( - IMG_CONTEXT, IMG_END, IMG_START, image_to_pixel_values) + from vllm.model_executor.models.h2ovl import (IMG_CONTEXT, IMG_END, + IMG_START, + image_to_pixel_values + ) images = [images] if isinstance(images, Image) else images pixel_values = [ image_to_pixel_values(image, Error: Process completed with exit code 1. ``` If I modify the code to align with YAPF’s reformatting suggestions, format.sh then reverts the changes. If I just agreed with yapf and push code ruff failed at ``` Run isort . --c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Code formatted by format.sh but failed yapf check in CI bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The code snippet was formatted using format.sh but failed the YA...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Code formatted by format.sh but failed yapf check in CI bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The code snippet was formatted using format.sh but failed the YA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: at. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: /cooleel/vllm/blob/5c2ed3305bc8d3c0caa831eb7e4c217d9c754639/tests/models/decoder_only/vision_language/vlm_utils/model_utils.py#L283-L284 The yapf error message is ``` Run yapf --diff --recursive . --- ./tests/models/dec...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
