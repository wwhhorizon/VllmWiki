# vllm-project/vllm#26223: [Bug]: Silent hang when video frames exceed profiled encoder budget (Qwen2-VL, num_frames > _MAX_FRAMES_PER_VIDEO)

| 字段 | 值 |
| --- | --- |
| Issue | [#26223](https://github.com/vllm-project/vllm/issues/26223) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Silent hang when video frames exceed profiled encoder budget (Qwen2-VL, num_frames > _MAX_FRAMES_PER_VIDEO)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving **Qwen/Qwen2-VL-7B-Instruct** with **V1 engine**, requests that include a video with **more frames than the profiled limit** (e.g., `media-io-kwargs.video.num_frames=32`) **hang indefinitely** with 0 tokens scheduled per step and no user-visible error. GPU stays idle; CPU spins. **Minimal repro (no external data):** 1. Start server (key flags shown) ```bash vllm serve Qwen/Qwen2-VL-7B-Instruct \ --media-io-kwargs '{"video": {"num_frames": 32}}' \ --mm-processor-kwargs.max_pixels 460800 ``` 2. Send a request with one video + a short text prompt (OpenAI-compatible) ```shell curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "Qwen/Qwen2-VL-7B-Instruct", "messages": [{ "role": "user", "content": [ { "type": "video_url", "video_url": { "url": "file:///ABSOLUTE/PATH/TO/your_video.mp4" } }, { "type": "text", "text": "Describe this video." } ] }] }' ``` **Observed results:** * The request is accepted (“Added request …”) but **never completes**. * Engine logs keep reporting **0 scheduled tokens / 0 reqs running**, GPU utilization ~0%. Similar symptoms are documented in other...

## 现有链接修复摘要

#33110 [Bugfix] Early-reject requests with MM data longer than encode cache capacity

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ofiled encoder budget (Qwen2-VL, num_frames > _MAX_FRAMES_PER_VIDEO) bug;stale ### Your current environment ### 🐛 Describe the bug When serving **Qwen/Qwen2-VL-7B-Instruct** with **V1 engine**, requests that include a v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Silent hang when video frames exceed profiled encoder budget (Qwen2-VL, num_frames > _MAX_FRAMES_PER_VIDEO) bug;stale ### Your current environment ### 🐛 Describe the bug When serving **Qwen/Qwen2-VL-7B-Instruct**...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: runtime**, `media-io-kwargs.video.num_frames` allows **32 frames**, producing ~2× tokens. * The scheduler’s encoder allocation check fails (required tokens > compute budget). After the first step schedules only text tok...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: or (b) an **actionable error** explaining that the encoder budget is too small (e.g., “multimodal encoder tokens required X > budget Y; increase `--max-num-batched-tokens` or reduce frames/resolution”). --- **Root cause...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Silent hang when video frames exceed profiled encoder budget (Qwen2-VL, num_frames > _MAX_FRAMES_PER_VIDEO) bug;stale ### Your current environment ### 🐛 Describe the bug When serving **Qwen/Qwen2-VL-7B-Instruct**...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33110](https://github.com/vllm-project/vllm/pull/33110) | closes_keyword | 0.95 | [Bugfix] Early-reject requests with MM data longer than encode cache capacity | Fixes [#26223](https://github.com/vllm-project/vllm/issues/26223) This PR prevents a hang in the V1 engine when a multimodal request contains an input (e.g., a video with many fram |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
