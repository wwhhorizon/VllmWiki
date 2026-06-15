# vllm-project/vllm#3196: Unable to run distributed inference on ray with llama-65B, tensor_parallel_size > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#3196](https://github.com/vllm-project/vllm/issues/3196) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support |
| 子分类 | memory |
| Operator 关键词 | attention;cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Unable to run distributed inference on ray with llama-65B, tensor_parallel_size > 1

### Issue 正文摘录

**Issue Description:** When I tried to deploy the llama-hf-65B model on an 8-GPU machine, I followed the example in Distributed Inference and Serving ([link](https://docs.vllm.ai/en/latest/serving/distributed_serving.html)) and wrote the following code: ```python from vllm import LLM llm = LLM("/mnt/llm_dataset/evaluation_pretrain/models/sota/llama-hf-65b/", trust_remote_code=True, tensor_parallel_size=4) ``` However, Ray raised an OOM exception, as shown in the attached image. Note that setting `tensor_parallel_size=8` results in the same exception. ![vllm_ray](https://github.com/vllm-project/vllm/assets/21336062/bd2f6de3-10ea-40bd-a044-328a5c66294b) Even when I replaced the model_dir with the llama-13B model, setting tensor_parallel_size=8 still triggers a Ray OOM exception. When I set the model directory to llama-13B and `tensor_parallel_size=4`, the model *sometimes* can loads and infers successfully. However, it takes a considerable amount of time for initializing the Ray environment and paged attention memory, and it's uncertain whether the program is stuck. Here is information about my local environment: - ubuntu 22.04 - Driver Version: 470.182.03 CUDA Version: 12.3 - 8xA80...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: U machine, I followed the example in Distributed Inference and Serving ([link](https://docs.vllm.ai/en/latest/serving/distributed_serving.html)) and wrote the following code: ```python from vllm import LLM llm = LLM("/m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Unable to run distributed inference on ray with llama-65B, tensor_parallel_size > 1 **Issue Description:** When I tried to deploy the llama-hf-65B model on an 8-GPU machine, I followed the example in Distributed Inferen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e in Distributed Inference and Serving ([link](https://docs.vllm.ai/en/latest/serving/distributed_serving.html)) and wrote the following code: ```python from vllm import LLM llm = LLM("/mnt/llm_dataset/evaluation_pretra...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: out my local environment: - ubuntu 22.04 - Driver Version: 470.182.03 CUDA Version: 12.3 - 8xA800 with 80GB on local machine - Python 3.8.18 - transformers: 4.38.2 - vllm: 0.3.3 performance attention_kv_cache;distribute...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: st_remote_code=True, tensor_parallel_size=4) ``` However, Ray raised an OOM exception, as shown in the attached image. Note that setting `tensor_parallel_size=8` results in the same exception. ![vllm_ray](https://github...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
