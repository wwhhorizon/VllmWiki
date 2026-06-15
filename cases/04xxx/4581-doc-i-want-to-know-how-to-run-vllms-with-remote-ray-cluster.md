# vllm-project/vllm#4581: [Doc]:  i want to know. How to run vllms with remote ray cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#4581](https://github.com/vllm-project/vllm/issues/4581) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]:  i want to know. How to run vllms with remote ray cluster

### Issue 正文摘录

### 📚 The doc issue i want to know. How to run vllms with remote ray cluster my code is from llama_index.llms.vllm import Vllm import ray ray.init(address="ray://10.0.233.89:10001") llm = Vllm(model="./Mistral-7B-Instruct-v0.1",dtype="float16",tensor_parallel_size=2, temperature=0,max_new_tokens=100,vllm_kwargs={"swap_space": 1,"gpu_memory_utilization": 0.5,"max_model_len": 4096,}) ### Suggest a potential alternative/fix _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: "ray://10.0.233.89:10001") llm = Vllm(model="./Mistral-7B-Instruct-v0.1",dtype="float16",tensor_parallel_size=2, temperature=0,max_new_tokens=100,vllm_kwargs={"swap_space": 1,"gpu_memory_utilization": 0.5,"max_model_len...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: want to know. How to run vllms with remote ray cluster my code is from llama_index.llms.vllm import Vllm import ray ray.init(address="ray://10.0.233.89:10001") llm = Vllm(model="./Mistral-7B-Instruct-v0.1",dtype="float1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: un vllms with remote ray cluster my code is from llama_index.llms.vllm import Vllm import ray ray.init(address="ray://10.0.233.89:10001") llm = Vllm(model="./Mistral-7B-Instruct-v0.1",dtype="float16",tensor_parallel_siz...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: i want to know. How to run vllms with remote ray cluster documentation;stale ### 📚 The doc issue i want to know. How to run vllms with remote ray cluster my code is from llama_index.llms.vllm import Vllm import ray ray....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
