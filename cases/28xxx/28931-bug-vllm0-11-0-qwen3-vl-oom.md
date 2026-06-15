# vllm-project/vllm#28931: [Bug]: vllm0.11.0 启动 qwen3-vl 服务，显存不释放，导致 OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#28931](https://github.com/vllm-project/vllm/issues/28931) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 30; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | gemm;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm0.11.0 启动 qwen3-vl 服务，显存不释放，导致 OOM

### Issue 正文摘录

### Your current environment vllm 0.11.0 ununtu python3.12 nvidia 4090*2 24G ### 🐛 Describe the bug vllm serve /models/Qwen3-VL-32B-Instruct-AWQ-4bit \ --max-model-len 8192 \ -tp 2 --port 8000 --host 0.0.0.0 \ --gpu-memory-utilization 0.8 --dtype bfloat16 \ --allowed-local-media-path /models/Qwen3-VL-32B-Instruct-AWQ-4bit/data \ --limit-mm-per-prompt '{"image": 2, "video": 1}' \ --enable-prefix-caching 刚开始启动的时候显存占用 17G，然后不同的请求打进来， 显存慢慢增长，达到一个高峰 22333MiB / 24564MiB，这时候显存增长就慢了 之后不知道什么时候，就因为 OOM 的原因导致服务崩溃 English: At the beginning of startup, the video memory occupied 17G, and then different requests came in. The video memory gradually increases, reaching a peak of 22333MiB / 24564MiB. At this point, the growth of video memory slows down. After that, I don't know when, but the service crashed due to OOM. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: tp 2 --port 8000 --host 0.0.0.0 \ --gpu-memory-utilization 0.8 --dtype bfloat16 \ --allowed-local-media-path /models/Qwen3-VL-32B-Instruct-AWQ-4bit/data \ --limit-mm-per-prompt '{"image": 2, "video": 1}' \ --enable-pref...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm0.11.0 启动 qwen3-vl 服务，显存不释放，导致 OOM bug ### Your current environment vllm 0.11.0 ununtu python3.12 nvidia 4090*2 24G ### 🐛 Describe the bug vllm serve /models/Qwen3-VL-32B-Instruct-AWQ-4bit \ --max-model-len 8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: OM. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: vllm0.11.0 启动 qwen3-vl 服务，显存不释放，导致 OOM bug ### Your current environment vllm 0.11.0 ununtu python3.12 nvidia 4090*2 24G ### 🐛 Describe the bug vllm serve /models/Qwen3-VL-32B-Instruct-AWQ-4bit \ --max-model-len 8...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: d questions. performance distributed_parallel;model_support;quantization gemm;quantization crash;oom dtype Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
