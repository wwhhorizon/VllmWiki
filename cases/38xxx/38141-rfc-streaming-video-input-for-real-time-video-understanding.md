# vllm-project/vllm#38141: [RFC] Streaming Video Input for Real-Time Video Understanding

| 字段 | 值 |
| --- | --- |
| Issue | [#38141](https://github.com/vllm-project/vllm/issues/38141) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;fp8 |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC] Streaming Video Input for Real-Time Video Understanding

### Issue 正文摘录

## Motivation Real-time video understanding — where a model continuously processes a live camera or video stream and responds to user queries about what it sees — is rapidly becoming a core capability of frontier AI platforms: - **Google Gemini Live**: camera streaming on Android/iOS - **ByteDance Doubao**: real-time video call with visual reasoning - **Apple Visual Intelligence**: on-device camera understanding - **NVIDIA Live VLM WebUI**: WebRTC webcam → VLM backend The market demand is massive: AI video analytics ($5-21B in 2025, 22-33% CAGR), manufacturing visual inspection ($30B → $90B by 2033), video surveillance ($6B → $49B by 2035), and robotics/embodied AI (NVIDIA Jetson Thor shipping with onboard VLM inference). **vLLM already has 90% of the infrastructure needed.** The v1 engine ships `StreamingInput`, resumable requests, a WebSocket `/v1/realtime` endpoint, EVS frame pruning, encoder caching, chunked prefill, prefix caching, and disaggregated encoder support. However, all of this is currently wired only for audio. Extending it to video frames is a natural next step with high impact and relatively low implementation cost. ### Use Cases | Use Case | FPS Needed | Latency...

## 现有链接修复摘要

#39642 [Realtime][Video] Add streaming video input for real-time video understanding

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: deo Understanding ## Motivation Real-time video understanding — where a model continuously processes a live camera or video stream and responds to user queries about what it sees — is rapidly becoming a core capability...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: responds to user queries about what it sees — is rapidly becoming a core capability of frontier AI platforms: - **Google Gemini Live**: camera streaming on Android/iOS - **ByteDance Doubao**: real-time video call with v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: infrastructure needed.** The v1 engine ships `StreamingInput`, resumable requests, a WebSocket `/v1/realtime` endpoint, EVS frame pruning, encoder caching, chunked prefill, prefix caching, and disaggregated encoder supp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: tok/frame: ~4-5 hours before KV cache fills - 2 FPS: ~1-1.5 hours - With FP8 KV on H100: doubles capacity correctness attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;schedu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ively low implementation cost. ### Use Cases | Use Case | FPS Needed | Latency Target | |----------|-----------|----------------| | Robotics / embodied AI | 2-8 | ` template. ### Implementation Phases | Phase | Descript...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39642](https://github.com/vllm-project/vllm/pull/39642) | mentioned | 0.6 | [Realtime][Video] Add streaming video input for real-time video understanding | se 1 of [RFC: Streaming Video Input for Real-Time Video Understanding #38141](https://github.com/vllm-project/vllm/issues/38141). Fix the issue where AsyncScheduler crashes due to… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
