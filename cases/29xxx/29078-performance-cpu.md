# vllm-project/vllm#29078: [Performance]: 多实例导致的cpu占用过高

| 字段 | 值 |
| --- | --- |
| Issue | [#29078](https://github.com/vllm-project/vllm/issues/29078) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;triton |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: 多实例导致的cpu占用过高

### Issue 正文摘录

### Your current environment GPU: RTX4090 cuda version: cuda12.8 vllm version: 0.11.0 中文：我使用triton server的 vllm backend 启动了4个 minerU2.5 模型的实例，我的服务器上有2张卡，我每张卡启动了1个实例，我发现cpu负载有时候极高，几乎占满了我的服务器，我的服务器有96核，vllm backend使用的是AsyncLLMEngine，我观察到在单卡上启动一个实例时，我发送200张小尺寸的文字图做OCR时，fps可以达到最高，也就是每秒可以处理200张的图片，cpu负载在40-50%左右，为了进一步增加性能，我在两张卡上各启动了一个实例，但是我观察到此时cpu负载几乎达到99%，占用了极高的cpu，每个实例的fps只有120左右，性能几乎没有提升。 我做了大量的测试，我开始以为是triton server的问题，但经过排查，我认为问题可能出现在vllm推理时占用了很高的cpu，因为我不使用triton server，使用 `vllm serve`来模拟同样的情况，每个vllm实例推理时也占用掉了20-30%的cpu，如果这样，我的服务器即使有再多的GPU，也不能够提升模型的性能，我该如何调试？ english： I launched 4 instances of the minerU2.5 model using the vllm backend of Triton Server. My server is equipped with 2 GPUs, with 1 instance running on each GPU. However, I noticed that the CPU load sometimes spikes to extremely high levels, nearly maxing out the server—which has 192 CPU cores. The vllm backend uses AsyncLLMEngine. When running a single instance on one GPU and sending 200 small-sized text images for OCR, I achieved the highest FPS—processing up to 200 images per second—with the CPU load hovering around 40-50%. To further improve performance, I launched one instance on each of the two GPUs. But in this...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Performance]: 多实例导致的cpu占用过高 usage ### Your current environment GPU: RTX4090 cuda version: cuda12.8 vllm version: 0.11.0 中文：我使用triton server的 vllm backend 启动了4个 minerU2.5 模型的实例，我的服务器上有2张卡，我每张卡启动了1个实例，我发现cpu负载有时候极高，几乎占满了...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ironment GPU: RTX4090 cuda version: cuda12.8 vllm version: 0.11.0 中文：我使用triton server的 vllm backend 启动了4个 minerU2.5 模型的实例，我的服务器上有2张卡，我每张卡启动了1个实例，我发现cpu负载有时候极高，几乎占满了我的服务器，我的服务器有96核，vllm backend使用的是AsyncLLMEngine，我观察到在单卡上...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nce]: 多实例导致的cpu占用过高 usage ### Your current environment GPU: RTX4090 cuda version: cuda12.8 vllm version: 0.11.0 中文：我使用triton server的 vllm backend 启动了4个 minerU2.5 模型的实例，我的服务器上有2张卡，我每张卡启动了1个实例，我发现cpu负载有时候极高，几乎占满了我的服务器，我的服...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: GPU，也不能够提升模型的性能，我该如何调试？ english： I launched 4 instances of the minerU2.5 model using the vllm backend of Triton Server. My server is equipped with 2 GPUs, with 1 instance running on each GPU. However, I noticed that the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: d around 120 FPS, with almost no performance gain. I conducted numerous tests. Initially, I suspected the issue was with Triton Server, but after troubleshooting, I believe the problem lies in the high CPU usage during...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
