# vllm-project/vllm#15087: [Usage]: Request to Include vllm["audio,video"] Package in v0.8.0 Docker Image

| 字段 | 值 |
| --- | --- |
| Issue | [#15087](https://github.com/vllm-project/vllm/issues/15087) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Request to Include vllm["audio,video"] Package in v0.8.0 Docker Image

### Issue 正文摘录

### Your current environment When serving Whisper with the v0.8.0 image, calling the /v1/audio/transcriptions endpoint results in an ImportError due to the missing vllm[audio] package: ImportError: Please install vllm[audio] for audio support The container itself sets up without issues, but the error occurs upon sending requests to the audio transcription endpoint. Although adding pip install vllm[audio] as shown below in the deployment configuration resolves the issue: containers: - command: - sh - '-c' - > pip install vllm[audio] && python3 -m vllm.entrypoints.openai.api_server --port=8080 --model=/mnt/models --tensor-parallel-size=1 --gpu_memory_utilization=0.9 I request that the official v0.8.0 Docker image be updated to include the vllm["audio,video"] package, ensuring proper support for audio (and video) functionalities without additional deployment modifications. ### How would you like to use vllm In a k8s environment, the whisper-large-v3-turbo model is served using the vllm v0.8.0 image. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Usage]: Request to Include vllm["audio,video"] Package in v0.8.0 Docker Image usage;stale ### Your current environment When serving Whisper with the v0.8.0 image, calling the /v1/audio/transcriptions endpoint results i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Although adding pip install vllm[audio] as shown below in the deployment configuration resolves the issue: containers: - command: - sh - '-c' - > pip install vllm[audio] && python3 -m vllm.entrypoints.openai.api_server...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Request to Include vllm["audio,video"] Package in v0.8.0 Docker Image usage;stale ### Your current environment When serving Whisper with the v0.8.0 image, calling the /v1/audio/transcriptions endpoint results i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ge. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
