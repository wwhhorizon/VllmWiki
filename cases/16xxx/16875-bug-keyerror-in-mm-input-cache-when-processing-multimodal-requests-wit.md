# vllm-project/vllm#16875: [Bug]: KeyError in mm_input_cache when processing multimodal requests with Qwen2.5-VL-72B

| 字段 | 值 |
| --- | --- |
| Issue | [#16875](https://github.com/vllm-project/vllm/issues/16875) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError in mm_input_cache when processing multimodal requests with Qwen2.5-VL-72B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - Environment: vLLM Version: 0.8.5.dev0+gdc1b4a6f1.d20250414 - Model: Qwen/Qwen2.5-VL-72B-Instruct - Platform: CUDA (GPU-based inference) - Problem Description: When submitting multimodal requests (containing images and text questions) to the vLLM API server, a KeyError occurs in the multimodal input cache (mm_input_cache). The error traceback indicates a missing key in the cache, leading to a failure in processing the request. This issue reproduces consistently with multimodal prompts, such as those evaluating image-question relevance. ``` ERROR 04-19 17:04:00 [core.py:387] EngineCore hit an exception: Traceback (most recent call last): ERROR 04-19 17:04:00 [core.py:387] File "/root/anaconda3/envs/vllm_latest/lib/python3.12/site-packages/cachetools/__init__.py", line 68, in __getitem__ ERROR 04-19 17:04:00 [core.py:387] return self.__data[key] ERROR 04-19 17:04:00 [core.py:387] ~~~~~~~~~~~^^^^^ ERROR 04-19 17:04:00 [core.py:387] KeyError: 'baeea367ef018cb2850dd6bc6b4e4cf2a8f2ed5866cf651a8a987e18f54868ba' ERROR 04-19 17:04:00 [core.py:387] ERROR 04-19 17:04:00 [core.py:387] During handling of the above exception, another exceptio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment ### 🐛 Describe the bug - Environment: vLLM Version: 0.8.5.dev0+gdc1b4a6f1.d20250414 - Model: Qwen/Qwen2.5-VL-72B-Instruct - Platform: CUDA (GPU-based inference) - Problem Description: When submi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: KeyError in mm_input_cache when processing multimodal requests with Qwen2.5-VL-72B bug ### Your current environment ### 🐛 Describe the bug - Environment: vLLM Version: 0.8.5.dev0+gdc1b4a6f1.d20250414 - Model: Qwe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: "/root/anaconda3/envs/vllm_latest/lib/python3.12/site-packages/starlette/routing.py", line 714, in __call__ await self.middleware_stack(scope, receive, send) File "/root/anaconda3/envs/vllm_latest/lib/python3.12/site-pa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0+gdc1b4a6f1.d20250414 - Model: Qwen/Qwen2.5-VL-72B-Instruct - Platform: CUDA (GPU-based inference) - Problem Description: When submitting multimodal requests (containing images and text questions) to the vLLM API serve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: KeyError in mm_input_cache when processing multimodal requests with Qwen2.5-VL-72B bug ### Your current environment ### 🐛 Describe the bug - Environment: vLLM Version: 0.8.5.dev0+gdc1b4a6f1.d20250414 - Model: Qwe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
