# vllm-project/vllm#19130: [Bug]: Qwen2.5 VL offline inference example bug

| 字段 | 值 |
| --- | --- |
| Issue | [#19130](https://github.com/vllm-project/vllm/issues/19130) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5 VL offline inference example bug

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug run the following command: `python examples/offline_inference/vision_language_multi_image.py -m qwen2_5_vl` got the following error: ``` INFO 06-04 05:50:53 [__init__.py:244] Automatically detected platform cuda. Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`. You have video processor config saved in `preprocessor.json` file which is deprecated. Video processor configs should be saved in their own `video_preprocessor.json` file. You can rename the file or load and save the processor back which renames it automatically. Loading from `preprocessor.json` will be removed in v5.0. Traceback (most recent call last): File "/workspace/vllm/examples/offline_inference/vision_language_multi_image.py", line 867, in main(args) File "/workspace/vllm/examples/offline_inference/vision_language_multi_image.py", line 858, in main run_generate(model, QUESTION, image_urls, seed)...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen2.5 VL offline inference example bug bug ### Your current environment ### 🐛 Describe the bug run the following command: `python examples/offline_inference/vision_language_multi_image.py -m qwen2_5_vl` got the
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampli...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `` INFO 06-04 05:50:53 [__init__.py:244] Automatically detected platform cuda. Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default beha...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ponse.raise_for_status() File "/usr/local/lib/python3.10/dist-packages/requests/models.py", line 1021, in raise_for_status raise HTTPError(http_error_msg, response=self) requests.exceptions.HTTPError: 403 Client Error:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
