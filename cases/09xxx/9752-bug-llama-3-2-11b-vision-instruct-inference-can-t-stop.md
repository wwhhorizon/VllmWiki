# vllm-project/vllm#9752: [Bug]: Llama-3.2-11B-Vision-Instruct Inference Can't Stop

| 字段 | 值 |
| --- | --- |
| Issue | [#9752](https://github.com/vllm-project/vllm/issues/9752) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama-3.2-11B-Vision-Instruct Inference Can't Stop

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Derectly runing: https://github.com/vllm-project/vllm/blob/main/examples/offline_inference_vision_language.py, and set `max_tokens` in the code as 1024 ``` python offline_inference_vision_language.py --model-type mllama ``` The model output will continue to the maximum tokens and will not stop early: ``` Loading safetensors checkpoint shards: 100% Completed | 5/5 [01:31 for decoder start token id because decoder start token id is not available. Processed prompts: 100%|████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:20<00:00, 20.23s/it, est. speed input: 0.54 toks/s, output: 50.61 toks/s] Output : The image shows a cherry blossom tree in front of a tall tower. The tree is in full bloom, with pink flowers covering the branches. The tower is white and has a distinctive shape, with a large dome at the top and a narrow base. The sky is blue and clear, suggesting a sunny day. The overall atmosphere of the image is one of beauty and tranquility, with the vibrant colors of the flowers and the towering structure creating a sense of awe and wonder. The image...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ty, or to showcase the natural beauty of the cherry blossom tree and the architectural grandeur of the tower. It could also be used to promote tourism or cultural events related to the tower or the cherry blossom season...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Llama-3.2-11B-Vision-Instruct Inference Can't Stop bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Derectly runing: https://github.com/vllm-project/vllm/blob/main/
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Llama-3.2-11B-Vision-Instruct Inference Can't Stop bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Derectly runing: https://github.com/vllm-project/vllm/blob/main...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the intersection of nature and architecture, inviting the viewer to appreciate the beauty of both. The image is likely intended to evoke a sense of wonder and appreciation for the natural world and human ingenuity. It m...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ws a cherry blossom tree in front of a tall tower. The tree is in full bloom, with pink flowers covering the branches. The tower is white and has a distinctive shape, with a large dome at the top and a narrow base. The...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
