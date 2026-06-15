# vllm-project/vllm#6124: [Bug]: Number of available GPU blocks drop significantly for Phi3-vision

| 字段 | 值 |
| --- | --- |
| Issue | [#6124](https://github.com/vllm-project/vllm/issues/6124) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support |
| 子分类 | install |
| Operator 关键词 | cache;cuda |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Number of available GPU blocks drop significantly for Phi3-vision

### Issue 正文摘录

### Your current environment Two docker containers based on images built from vllm source **3de6e6a3** and **3f3b6b21** ### 🐛 Describe the bug I passed the same model Phi-3-vision-128k-instruct to each docker container: ``` --tensor-parallel-size=1 \ --model=/models/Phi-3-vision-128k-instruct \ ``` For the version needs VLMConfig, here are the parameters ``` --image-input-type="pixel_values" \ --image-feature-size=1921 \ --image-token-id=32044 \ --image-input-shape="1, 3, 1008, 1344" ``` And with the container based on 3de6e6a3 **more latest**, it raises error: ``` INFO 07-04 01:04:14 gpu_executor.py:84] # GPU blocks: 5970, # CPU blocks: 682 [rank0]: ValueError: The model's max seq len (131072) is larger than the maximum number of tokens that can be stored in KV cache (95520). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. ``` But the container based on **3f3b6b21**: ``` INFO 07-04 01:40:03 gpu_executor.py:83] # GPU blocks: 8825, # CPU blocks: 682 INFO 07-04 01:40:05 model_runner.py:906] Capturing the model for CUDA graphs. This may lead to unexpected consequences if the model is not static. To run the model in eager mode, set '...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: drop significantly for Phi3-vision bug ### Your current environment Two docker containers based on images built from vllm source **3de6e6a3** and **3f3b6b21** ### 🐛 Describe the bug I passed the same model Phi-3-vision-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: **3de6e6a3** and **3f3b6b21** ### 🐛 Describe the bug I passed the same model Phi-3-vision-128k-instruct to each docker container: ``` --tensor-parallel-size=1 \ --model=/models/Phi-3-vision-128k-instruct \ ``` For the v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks: 682 INFO 07-04 01:40:05 model_runner.py:906] Capturing the model for CUDA graphs. This may lead to unexpected consequences if the model is not static. To run the model in eager mode, set 'enforce_eager=True' or use...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 31072) is larger than the maximum number of tokens that can be stored in KV cache (95520). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. ``` But the container based...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: Number of available GPU blocks drop significantly for Phi3-vision bug ### Your current environment Two docker containers based on images built from vllm source **3de6e6a3** and **3f3b6b21** ### 🐛 Describe the bug...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
