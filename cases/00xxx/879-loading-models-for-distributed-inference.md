# vllm-project/vllm#879: loading models for distributed inference

| 字段 | 值 |
| --- | --- |
| Issue | [#879](https://github.com/vllm-project/vllm/issues/879) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> loading models for distributed inference

### Issue 正文摘录

Hello. I am trying to use vLLM for distributed inference and am running into consistent runtime errors. **Infrastructure:** 8xA100 GPUs **Relevant versions:** Python 3.9.14, vllm 0.1.4, ray 2.6.3, NVIDIA-SMI Driver Version: 530.30.02, CUDA Version: 12.1 **Sample code** I'm using, as referenced in quickstart [guide](https://vllm.readthedocs.io/en/latest/serving/distributed_serving.html) `from vllm import LLM llm = LLM("facebook/opt-13b", tensor_parallel_size=4)` **Resulting error:** `File "/home/amartino/.pyenv/versions/3.9.14/lib/python3.9/site-packages/torch/distributed/distributed_c10d.py", line 1702, in all_reduce work = group.allreduce([tensor], opts) RuntimeError: Inplace update to inference tensor outside InferenceMode is not allowed.You can make a clone to get a normal tensor before doing inplace update.See https://github.com/pytorch/rfcs/pull/17 for more details.` I also tried loading a different model (from a local file) and saw the same error. Is this an issue with CUDA 12 compatibility?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: o consistent runtime errors. **Infrastructure:** 8xA100 GPUs **Relevant versions:** Python 3.9.14, vllm 0.1.4, ray 2.6.3, NVIDIA-SMI Driver Version: 530.30.02, CUDA Version: 12.1 **Sample code** I'm using, as referenced...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ce and am running into consistent runtime errors. **Infrastructure:** 8xA100 GPUs **Relevant versions:** Python 3.9.14, vllm 0.1.4, ray 2.6.3, NVIDIA-SMI Driver Version: 530.30.02, CUDA Version: 12.1 **Sample code** I'm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: loading models for distributed inference Hello. I am trying to use vLLM for distributed inference and am running into consistent runtime errors. **Infrastructure:** 8xA100 GPUs **Relevant versions:** Python 3.9.14, vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ng, as referenced in quickstart [guide](https://vllm.readthedocs.io/en/latest/serving/distributed_serving.html) `from vllm import LLM llm = LLM("facebook/opt-13b", tensor_parallel_size=4)` **Resulting error:** `File "/h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
