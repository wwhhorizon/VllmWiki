# vllm-project/vllm#13927: [Usage]:  Qwen2-VL-2B-Instruct Issue when passing a video URL to /chat/completions

| 字段 | 值 |
| --- | --- |
| Issue | [#13927](https://github.com/vllm-project/vllm/issues/13927) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  Qwen2-VL-2B-Instruct Issue when passing a video URL to /chat/completions

### Issue 正文摘录

### Your current environment Image: [v0.7.3](https://hub.docker.com/layers/vllm/vllm-openai/v0.7.3/images/sha256-4f4037303e8c7b69439db1077bb849a0823517c0f785b894dc8e96d58ef3a0c2) Run Command: `--model Qwen/Qwen2.5-VL-7B-Instruct --port 8080` GPU: NVIDIA H100 PCIe I am referencing [this](https://github.com/vllm-project/vllm/issues/9842#:~:text=chat_response%20%3D%20client.chat.completions.create(%0A%20%20%20%20model%3D%22llava%22%2C%0A%20%20%20%20messages%3D%5B%7B%0A%20%20%20%20%20%20%20%20%22role%22%3A%20%22user%22%2C%0A%20%20%20%20%20%20%20%20%22content%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7B%22type%22%3A%20%22text%22%2C%20%22text%22%3A%20%22What%E2%80%99s%20in%20this%20video%3F%22%7D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%7B%22type%22%3A%20%22video_url%22%2C%20%22video_url%22%3A%20%7B%22url%22%3A%20video_url%7D%7D%2C%0A%20%20%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%7D%5D%2C%0A)) and previosuly also [this](https://docs.vllm.ai/en/latest/getting_started/examples/openai_chat_completion_client_for_multimodal.html) (althought it appears this is dated). This is the error I get from the server. [error.txt](https://github.com/user-attachments/files/18996254/error.txt) He...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ns usage;stale ### Your current environment Image: [v0.7.3](https://hub.docker.com/layers/vllm/vllm-openai/v0.7.3/images/sha256-4f4037303e8c7b69439db1077bb849a0823517c0f785b894dc8e96d58ef3a0c2) Run Command: `--model Qwe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Qwen2-VL-2B-Instruct Issue when passing a video URL to /chat/completions usage;stale ### Your current environment Image: [v0.7.3](https://hub.docker.com/layers/vllm/vllm-openai/v0.7.3/images/sha256-4f4037303e8c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n Command: `--model Qwen/Qwen2.5-VL-7B-Instruct --port 8080` GPU: NVIDIA H100 PCIe I am referencing [this](https://github.com/vllm-project/vllm/issues/9842#:~:text=chat_response%20%3D%20client.chat.completions.create(%0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: VL-2B-Instruct Issue when passing a video URL to /chat/completions usage;stale ### Your current environment Image: [v0.7.3](https://hub.docker.com/layers/vllm/vllm-openai/v0.7.3/images/sha256-4f4037303e8c7b69439db1077bb...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 20%20%7D%5D%2C%0A)) and previosuly also [this](https://docs.vllm.ai/en/latest/getting_started/examples/openai_chat_completion_client_for_multimodal.html) (althought it appears this is dated). This is the error I get fro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
