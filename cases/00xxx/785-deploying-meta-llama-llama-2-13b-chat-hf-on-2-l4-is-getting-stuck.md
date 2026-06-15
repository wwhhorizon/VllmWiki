# vllm-project/vllm#785: Deploying meta-llama/Llama-2-13b-chat-hf on 2 L4 is getting stuck

| 字段 | 值 |
| --- | --- |
| Issue | [#785](https://github.com/vllm-project/vllm/issues/785) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | crash;mismatch;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Deploying meta-llama/Llama-2-13b-chat-hf on 2 L4 is getting stuck

### Issue 正文摘录

I am having trouble deploying llama2 13b chat model using vllm. I would appreciate any pointers here. Here's my Dockerfile that I am using to create image ``` FROM nvcr.io/nvidia/pytorch:22.12-py3 RUN pip uninstall torch -y RUN pip install vllm CMD ["python", "-m", "vllm.entrypoints.api_server", "--port", "8080", "--model", "meta-llama/Llama-2-13b-chat-hf", "--tensor-parallel-size", "2"] ``` #### Console ``` This container image and its contents are governed by the NVIDIA Deep Learning Container License. By pulling and using the container, you accept the terms and conditions of this license: https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license Downloading (…)lve/main/config.json: 100%|██████████| 587/587 [00:00 from ray.util.state.api import ( File "/usr/local/lib/python3.8/dist-packages/ray/util/state/api.py", line 17, in from ray.util.state.common import ( File "/usr/local/lib/python3.8/dist-packages/ray/util/state/common.py", line 420, in class ActorState(StateSchema): File "pydantic/dataclasses.py", line 224, in pydantic.dataclasses.dataclass.wrap File "pydantic/dataclasses.py", line 336, in pydantic.dataclasses._add_pydantic_validation_attributes File "pyda...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: having trouble deploying llama2 13b chat model using vllm. I would appreciate any pointers here. Here's my Dockerfile that I am using to create image ``` FROM nvcr.io/nvidia/pytorch:22.12-py3 RUN pip uninstall torch -y...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Deploying meta-llama/Llama-2-13b-chat-hf on 2 L4 is getting stuck I am having trouble deploying llama2 13b chat model using vllm. I would appreciate any pointers here. Here's my Dockerfile that I am using to create imag...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: lama/Llama-2-13b-chat-hf', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=2, seed=0) INFO 08-17 20:19:20 tokeniz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` correctness ci_build;distributed_parallel;frontend_api;model_support cuda crash;mismatch;oom dtype;env_dependency I am having trouble deploying llama2 13b chat model using vllm. I would appreciate any pointers here.
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ness ci_build;distributed_parallel;frontend_api;model_support cuda crash;mismatch;oom dtype;env_dependency I am having trouble deploying llama2 13b chat model using vllm. I would appreciate any pointers here.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
