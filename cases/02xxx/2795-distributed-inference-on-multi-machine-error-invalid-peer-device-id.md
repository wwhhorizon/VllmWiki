# vllm-project/vllm#2795: Distributed inference on multi machine (error Invalid peer device id) 

| 字段 | 值 |
| --- | --- |
| Issue | [#2795](https://github.com/vllm-project/vllm/issues/2795) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Distributed inference on multi machine (error Invalid peer device id) 

### Issue 正文摘录

I'm a newbie, and I'm running an example at https://docs.vllm.ai/en/latest/serving/distributed_serving.html locally with 2 machines, each with an RTX 3090 GPU. I changed tensor_parallel_size to 2 and model to "vinai/PhoGPT-4B". On the head node, I run: NCCL_SOCKET_IFNAME=eth0 NCCL_DEBUG=INFO CUDA_VISIBLE_DEVICES=0 ray start --head. On the other nodes, I run: NCCL_SOCKET_IFNAME=eth0 NCCL_DEBUG=INFO CUDA_VISIBLE_DEVICES=0 ray start --address='10.0.0.1'. Then, on the head node, when I run the example code: python main.py, I get the following error: ``` Traceback (most recent call last): File "/data2/bientd/vllm/test.py", line 25, in llm = LLM(model="facebook/opt-13b", tensor_parallel_size=2,download_dir='/data2/bientd/')#,pipeline_parallel_size=3 don't support File "/data2/bientd/anaconda3/envs/vllm/lib/python3.9/site-packages/vllm/entrypoints/llm.py", line 109, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/data2/bientd/anaconda3/envs/vllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 356, in from_engine_args engine = cls(*engine_configs, File "/data2/bientd/anaconda3/envs/vllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line...

## 现有链接修复摘要

#2760 Some fixes for custom allreduce kernels

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t/serving/distributed_serving.html locally with 2 machines, each with an RTX 3090 GPU. I changed tensor_parallel_size to 2 and model to "vinai/PhoGPT-4B". On the head node, I run: NCCL_SOCKET_IFNAME=eth0 NCCL_DEBUG=INFO...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ines, each with an RTX 3090 GPU. I changed tensor_parallel_size to 2 and model to "vinai/PhoGPT-4B". On the head node, I run: NCCL_SOCKET_IFNAME=eth0 NCCL_DEBUG=INFO CUDA_VISIBLE_DEVICES=0 ray start --head. On the other...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ice id ``` development distributed_parallel;model_support cuda crash env_dependency #2760 Some fixes for custom allreduce kernels I'm a newbie, and I'm running an example at https://docs.vllm.ai/en/latest/serving/distri...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ug I'm a newbie, and I'm running an example at https://docs.vllm.ai/en/latest/serving/distributed_serving.html locally with 2 machines, each with an RTX 3090 GPU. I changed tensor_parallel_size to 2 and model to "vinai/...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#2760](https://github.com/vllm-project/vllm/pull/2760) | closes_keyword | 0.95 | Some fixes for custom allreduce kernels | fix #2795 7. <s>disable custom allreduce by default by setting the argument to True. User can explicitly opt-in by setting it to False.</s> |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
