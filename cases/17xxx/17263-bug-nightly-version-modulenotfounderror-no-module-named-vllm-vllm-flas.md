# vllm-project/vllm#17263: [Bug]: nightly version: ModuleNotFoundError: No module named 'vllm.vllm_flash_attn.layers'

| 字段 | 值 |
| --- | --- |
| Issue | [#17263](https://github.com/vllm-project/vllm/issues/17263) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: nightly version: ModuleNotFoundError: No module named 'vllm.vllm_flash_attn.layers'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` INFO 04-27 14:39:59 [config.py:3574] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 1 68, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448 , 456, 464, 472, 480, 488, 496, 504, 512] is overridden by config [512, 384, 256, 128, 4, 2, 1, 392, 264, 136, 8, 400, 272, 144, 16, 408, 280, 152, 24, 416, 288, 160, 32, 424, 2 96, 168, 40, 432, 304, 176, 48, 440, 312, 184, 56, 448, 320, 192, 64, 456, 328, 200, 72, 464, 336, 208, 80, 472, 344, 216, 88, 120, 480, 352, 248, 224, 96, 488, 504, 360, 232, 1 04, 496, 368, 240, 112, 376] INFO 04-27 14:39:59 [weight_utils.py:265] Using model weights format ['*.safetensors'] Loading safetensors checkpoint shards: 0% Completed | 0/2 [00:00<?, ?it/s] Loading safetensors checkpoint shards: 50% Completed | 1/2 [00:01<00:01, 1.55s/it] Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:03<00:00, 1.69s/it] Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:03<00:00,...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: current environment ### 🐛 Describe the bug ``` INFO 04-27 14:39:59 [config.py:3574] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: nightly version: ModuleNotFoundError: No module named 'vllm.vllm_flash_attn.layers' bug ### Your current environment ### 🐛 Describe the bug ``` INFO 04-27 14:39:59 [config.py:3574] cudagraph sizes specified by mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ent ### 🐛 Describe the bug ``` INFO 04-27 14:39:59 [config.py:3574] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 1 68, 176, 1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 12] Encoder cache will be initialized with a budget of 98304 tokens, and profiled with 1 video items of the maximum feature size. ERROR 04-27 14:43:54 [core.py:396] EngineCore failed to start.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
