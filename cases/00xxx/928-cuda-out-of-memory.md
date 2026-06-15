# vllm-project/vllm#928: CUDA out of Memory

| 字段 | 值 |
| --- | --- |
| Issue | [#928](https://github.com/vllm-project/vllm/issues/928) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA out of Memory

### Issue 正文摘录

你好，在24G显存 A10上使用“python -m vllm.entrypoints.openai.api_server --model ./baichuan13b_new --host 0.0.0.0 --port 6000 --trust-remote-code --dtype half”部署，报错： ``` torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 134.00 MiB (GPU 0; 22.06 GiB total capacity; 21.64 GiB already allocated; 14.38 MiB free; 21.65 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF ``` 这个使用多卡部署的话怎么配置呢

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: out of memory. Tried to allocate 134.00 MiB (GPU 0; 22.06 GiB total capacity; 21.64 GiB already allocated; 14.38 MiB free; 21.65 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting ma...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: model ./baichuan13b_new --host 0.0.0.0 --port 6000 --trust-remote-code --dtype half”部署，报错： ``` torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 134.00 MiB (GPU 0; 22.06 GiB total capacity; 21.64 GiB al...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: CUDA out of Memory 你好，在24G显存 A10上使用“python -m vllm.entrypoints.openai.api_server --model ./baichuan13b_new --host 0.0.0.0 --port 6000 --trust-remote-code --dtype half”部署，报错： ``` torch.cuda.OutOfMemoryError: CUDA out of m
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: CONF ``` 这个使用多卡部署的话怎么配置呢 performance model_support;scheduler_memory cuda oom dtype;env_dependency 你好，在24G显存 A10上使用“python -m vllm.entrypoints.openai.api_server --model ./baichuan13b_new --host 0.0.0.0 --port 6000 --trus...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: f Memory 你好，在24G显存 A10上使用“python -m vllm.entrypoints.openai.api_server --model ./baichuan13b_new --host 0.0.0.0 --port 6000 --trust-remote-code --dtype half”部署，报错： ``` torch.cuda.OutOfMemoryError: CUDA out of memory. Tr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
