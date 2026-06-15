# vllm-project/vllm#15078: [Bug]: new bug after loosening type check on `llava_onevision.py`

| 字段 | 值 |
| --- | --- |
| Issue | [#15078](https://github.com/vllm-project/vllm/issues/15078) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: new bug after loosening type check on `llava_onevision.py`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, @DarkLight1337 This is a bug report when I'm trying #15021 to fix #15017. After I tried the specific change to `llava_onevision.py` following #15021, I came across a new bug like this: ```text ERROR 03-18 13:40:00 engine.py:140] File ".../anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/model_executor/models/llava_onevision.py", line 952, in forward ERROR 03-18 13:40:00 engine.py:140] inputs_embeds = self.get_input_embeddings_v0( ERROR 03-18 13:40:00 engine.py:140] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-18 13:40:00 engine.py:140] File ".../anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/model_executor/models/llava_onevision.py", line 913, in get_input_embeddings_v0 ERROR 03-18 13:40:00 engine.py:140] video_embeds = self._process_video_pixels(video_input) ERROR 03-18 13:40:00 engine.py:140] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-18 13:40:00 engine.py:140] File ".../anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/model_executor/models/llava_onevision.py", line 828, in _process_video_pixels ERROR 03-18 13:40:00 engine.py:140] num_videos, frames, c, h, w = video_pixel.shape ERROR 03-18 13:40:00 engine.p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: a bug report when I'm trying #15021 to fix #15017. After I tried the specific change to `llava_onevision.py` following #15021, I came across a new bug like this: ```text ERROR 03-18 13:40:00 engine.py:140] File ".../ana...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nk? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency;shape Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: y:140] File ".../anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/model_executor/models/llava_onevision.py", line 952, in forward ERROR 03-18 13:40:00 engine.py:140] inputs_embeds = self.get_input_embeddings_v0(
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: development ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
