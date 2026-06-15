# vllm-project/vllm#33954: [Bug]: `Qwen/Qwen3-VL-Embedding-8B` embedding quality declines significantly sometime after vLLM version `0.14.0rc2.dev199+gc80f92c14`

| 字段 | 值 |
| --- | --- |
| Issue | [#33954](https://github.com/vllm-project/vllm/issues/33954) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `Qwen/Qwen3-VL-Embedding-8B` embedding quality declines significantly sometime after vLLM version `0.14.0rc2.dev199+gc80f92c14`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The quality of embeddings generated with `Qwen/Qwen3-VL-Embedding-8B` declines significantly sometime after vLLM version `0.14.0rc2.dev199+gc80f92c14`. That means later versions of vLLM generate embeddings that result in a significantly lower cosine similarity for identical inputs than embeddings generated with vLLM version `0.14.0rc2.dev199+gc80f92c14`. I have not yet determined at what point in the vLLM version history the degraded embedding quality is implemented into the code, but I have tested vLLM version `0.14.0rc2.dev199+gc80f92c14` (which produces high quality embeddings) and vLLM version `0.15.2.dev0+g1892993bc` (which produces low quality embeddings). The below code implements a minimum reproducible example that demonstrates the degraded embedding quality: - Using vLLM version `0.14.0rc2.dev199+gc80f92c14`, the script outputs `Similarity score:0.7420985784733204`. - Using vLLM version `0.15.2.dev0+g1892993bc`, the script outputs `Similarity score:0.5265245045245712`. The lower similarity score makes the embeddings practically unusable! Minimum reproducible example: ```python from typing import Any import requests impor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: bedding-8B` embedding quality declines significantly sometime after vLLM version `0.14.0rc2.dev199+gc80f92c14` bug ### Your current environment ### 🐛 Describe the bug The quality of embeddings generated with `Qwen/Qwen3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: `Qwen/Qwen3-VL-Embedding-8B` embedding quality declines significantly sometime after vLLM version `0.14.0rc2.dev199+gc80f92c14` bug ### Your current environment ### 🐛 Describe the bug The quality of embeddings ge...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: sunset, as the dog offers its paw in a heartwarming display of companionship and trust." image_instruction = "Represent the user's input." user_prompt_image_url = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Minimum reproducible example: ```python from typing import Any import requests import base64 import numpy as np # vllm config model = "Qwen/Qwen3-VL-Embedding-8B" base_url = "http://localhost:8000/" # text and image pro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
