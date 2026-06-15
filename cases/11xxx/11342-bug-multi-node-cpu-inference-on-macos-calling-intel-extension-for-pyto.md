# vllm-project/vllm#11342: [Bug]: Multi-Node CPU Inference on MacOS calling `intel_extension_for_pytorch` 

| 字段 | 值 |
| --- | --- |
| Issue | [#11342](https://github.com/vllm-project/vllm/issues/11342) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Multi-Node CPU Inference on MacOS calling `intel_extension_for_pytorch` 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug While attempting to execute `NCCL_DEBUG=TRACE docker run -it --rm -p 8000:8000 --shm-size=4g --env "HUGGING_FACE_HUB_TOKEN= " --env "VLLM_CPU_KVCACHE_SPACE=40" --privileged -e NCCL_IB_HCA=mlx5 vllm-cpu-env-latest --device="cpu" --disable_async_output_proc --enforce-eager --model=meta-llama/Llama-Guard-3-1B --dtype=float16 --tensor-parallel-size 16 --pipeline-parallel-size 2 --distributed-executor-backend="ray" --swap-space=1` for Multi-Node inference; It raise an error in `/usr/local/lib/python3.10/dist-packages/vllm/distributed/parallel_state.py` in `line 338` as it needs `intel_extension_for_pytorch` Module. The error disappeared after commenting lines 338 and 339, would be great for a quick fixing. Moreover, just want to confirm that Ray is supported for CPU Inference on Multi-Node as described in [documentation](https://docs.vllm.ai/en/latest/serving/distributed_serving.html#details-for-distributed-inference-and-serving) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: _async_output_proc --enforce-eager --model=meta-llama/Llama-Guard-3-1B --dtype=float16 --tensor-parallel-size 16 --pipeline-parallel-size 2 --distributed-executor-backend="ray" --swap-space=1` for Multi-Node inference;...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tel_extension_for_pytorch` bug;ray ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug While attempting to execute `NCCL_DEBUG=TRACE docker run -it --rm -p 8000:8000 --shm-size=4g --e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ensor-parallel-size 16 --pipeline-parallel-size 2 --distributed-executor-backend="ray" --swap-space=1` for Multi-Node inference; It raise an error in `/usr/local/lib/python3.10/dist-packages/vllm/distributed/parallel_st...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _ ### 🐛 Describe the bug While attempting to execute `NCCL_DEBUG=TRACE docker run -it --rm -p 8000:8000 --shm-size=4g --env "HUGGING_FACE_HUB_TOKEN= " --env "VLLM_CPU_KVCACHE_SPACE=40" --privileged -e NCCL_IB_HCA=mlx5 v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
