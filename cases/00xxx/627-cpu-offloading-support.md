# vllm-project/vllm#627: CPU offloading support

| 字段 | 值 |
| --- | --- |
| Issue | [#627](https://github.com/vllm-project/vllm/issues/627) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> CPU offloading support

### Issue 正文摘录

Hi vLLM genius @zhuohan123 @WoosukKwon My requirement is to run the inference of [Llama2 70b chat](https://huggingface.co/meta-llama/Llama-2-70b-hf) on a server with **2** A100 80G. Currently, using the [fastchat.serve.model_worker](https://github.com/lm-sys/FastChat/blob/main/fastchat/serve/model_worker.py#L441) in [FastChat](https://github.com/lm-sys/FastChat) and specifying **num-gpus 2** can work, and we found that a portion of the weights are offloaded to the CPU. After reading HuggingFace's [documentation](https://huggingface.co/docs/accelerate/usage_guides/big_modeling), we found that when the [device_map defaults to auto](https://github.com/lm-sys/FastChat/blob/main/fastchat/model/model_adapter.py#L170) >By passing device_map="auto", we tell 🤗 Accelerate to determine automatically where to put each layer of the model depending on the available resources: > - first, we use the maximum space available on the GPU(s) > - if we still need space, we store the remaining weights on the CPU > - if there is not enough RAM, we store the remaining weights on the hard drive as memory-mapped tensors On vLLM, when the GPU util is not specified in the [API Server](https://github.com/vllm-...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ius @zhuohan123 @WoosukKwon My requirement is to run the inference of [Llama2 70b chat](https://huggingface.co/meta-llama/Llama-2-70b-hf) on a server with **2** A100 80G. Currently, using the [fastchat.serve.model_worke...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: worker.py#L441) in [FastChat](https://github.com/lm-sys/FastChat) and specifying **num-gpus 2** can work, and we found that a portion of the weights are offloaded to the CPU. After reading HuggingFace's [documentation](...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: https://huggingface.co/meta-llama/Llama-2-70b-hf) on a server with **2** A100 80G. Currently, using the [fastchat.serve.model_worker](https://github.com/lm-sys/FastChat/blob/main/fastchat/serve/model_worker.py#L441) in...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: CPU offloading support feature request Hi vLLM genius @zhuohan123 @WoosukKwon My requirement is to run the inference of [Llama2 70b chat](https://huggingface.co/meta-llama/Llama-2-70b-hf) on a server with **2** A100 80G.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: CPU offloading support feature request Hi vLLM genius @zhuohan123 @WoosukKwon My requirement is to run the inference of [Llama2 70b chat](https://huggingface.co/meta-llama/Llama-2-70b-hf) on a server with **2** A100 80G...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
