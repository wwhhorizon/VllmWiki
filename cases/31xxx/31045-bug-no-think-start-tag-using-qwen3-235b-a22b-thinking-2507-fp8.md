# vllm-project/vllm#31045: [Bug]: No <think> start tag using Qwen3-235B-A22B-Thinking-2507-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#31045](https://github.com/vllm-project/vllm/issues/31045) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: No <think> start tag using Qwen3-235B-A22B-Thinking-2507-FP8

### Issue 正文摘录

### Your current environment I am using vllm docker latest (2025-12-19) Ubuntu 24, 8 H100 94GB each one Model: https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507-FP8 ### 🐛 Describe the bug Hi ! After uses: ```sh docker run -d --name vllm-qwen-235b \ --gpus '"device=1,2,3,4"' \ --ipc=host \ -p 8001:8001 \ -v /srv/models:/models \ vllm/vllm-openai:latest \ --model /models/qwen3-235b-fp8 \ --port 8001 \ --tensor-parallel-size 4 \ --max-model-len 65536 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --enable-chunked-prefill ``` I tried: ```sh root@srv-ia-020:/home/fontesc# curl -s http://10.120.191.20:8001/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer dummy" -d '{ "model": "/models/qwen3-235b-fp8", "messages": [{"role":"user","content":"how many is 1+1?"}] }' ``` but the answer is: {"id":"chatcmpl-a552f115b7aa5d68","object":"chat.completion","created":1766171761,"model":"/models/qwen3-235b-fp8","choices":[{"index":0,"message":{"role":"assistant","content":"Okay, the user asked \"how many is 1+1?\" Hmm, this seems like a very basic math question. Maybe they're a young child just learning addition, or perhaps someone testing if I'm pa...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ent environment I am using vllm docker latest (2025-12-19) Ubuntu 24, 8 H100 94GB each one Model: https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507-FP8 ### 🐛 Describe the bug Hi ! After uses: ```sh docker run -d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: No <think> start tag using Qwen3-235B-A22B-Thinking-2507-FP8 bug ### Your current environment I am using vllm docker latest (2025-12-19) Ubuntu 24, 8 H100 94GB each one Model: https://huggingface.co/Qwen/Qwen3-23...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: A22B-Thinking-2507-FP8 bug ### Your current environment I am using vllm docker latest (2025-12-19) Ubuntu 24, 8 H100 94GB each one Model: https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507-FP8 ### 🐛 Describe the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: No <think> start tag using Qwen3-235B-A22B-Thinking-2507-FP8 bug ### Your current environment I am using vllm docker latest (2025-12-19) Ubuntu 24, 8 H100 94GB each one Model: https://huggingface.co/Qwen/Qwen3-23...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: able-auto-tool-choice \ --tool-call-parser hermes \ --enable-chunked-prefill ``` I tried: ```sh root@srv-ia-020:/home/fontesc# curl -s http://10.120.191.20:8001/v1/chat/completions -H "Content-Type: application/json" -H...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
