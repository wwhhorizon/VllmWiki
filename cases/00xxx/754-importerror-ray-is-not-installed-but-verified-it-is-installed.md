# vllm-project/vllm#754: ImportError: Ray is not installed. but verified it is installed!

| 字段 | 值 |
| --- | --- |
| Issue | [#754](https://github.com/vllm-project/vllm/issues/754) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ImportError: Ray is not installed. but verified it is installed!

### Issue 正文摘录

llm = LLM(model="meta-llama/Llama-2-70b-chat-hf", tensor_parallel_size=4) I having the following error File ~/miniconda3/envs/vllm/lib/python3.8/site-packages/vllm/engine/ray_utils.py:64, in initialize_cluster(parallel_config, engine_use_ray, ray_address) 62 if parallel_config.worker_use_ray or engine_use_ray: 63 if ray is None: ---> 64 raise ImportError( 65 "Ray is not installed. Please install Ray to use distributed " 66 "serving.") 67 # Connect to a ray cluster. 68 ray.init(address=ray_address, ignore_reinit_error=True) **ImportError: Ray is not installed. Please install Ray to use distributed serving.** But verified it is installed with vllm with: import ray ray.init() running version 2.6.2 , Also tried to uninstall and install older versions!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: portError: Ray is not installed. but verified it is installed! llm = LLM(model="meta-llama/Llama-2-70b-chat-hf", tensor_parallel_size=4) I having the following error File ~/miniconda3/envs/vllm/lib/python3.8/site-packag...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ImportError: Ray is not installed. but verified it is installed! llm = LLM(model="meta-llama/Llama-2-70b-chat-hf", tensor_parallel_size=4) I having the following error File ~/miniconda3/envs/vllm/lib/python3.8/site-pac

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
