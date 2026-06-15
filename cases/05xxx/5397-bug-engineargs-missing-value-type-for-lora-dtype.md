# vllm-project/vllm#5397: [Bug]: EngineArgs missing value type for `lora_dtype`

| 字段 | 值 |
| --- | --- |
| Issue | [#5397](https://github.com/vllm-project/vllm/issues/5397) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | triton |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EngineArgs missing value type for `lora_dtype`

### Issue 正文摘录

### Your current environment ```text Versions of relevant libraries: [pip3] numpy==1.22.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.41.1 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu12==2.18.1.0.4.0 [conda] numpy 1.22.4 py39hc58783e_0 conda-forge [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0 pypi_0 pypi [conda] transformers 4.41.1 pypi_0 pypi [conda] triton 2.3.0 pypi_0 pypi [conda] vllm-nccl-cu12 2.18.1.0.4.0 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.2 ``` ### 🐛 Describe the bug ```python import vllm vllm.EngineArgs(model='a', lora_dtype='float16') ``` raises ```python --------------------------------------------------------------------------- TypeError Traceback (most recent call last) Cell In[40], line 1 ----> 1 ea = vllm.EngineArgs(model='a', lora_dtype='float16') TypeError: __init__() got an unexpected keyword argument 'lora_dtype' ``` # Fix Modify `lora_dtype = 'auto'` to `lora_dtype: str = 'auto'` in [arg_utils.py](https://github.com/vllm-project/vllm/blob/v0.4.3/vllm/engine/arg_utils.py#L70).

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ng value type for `lora_dtype` bug ### Your current environment ```text Versions of relevant libraries: [pip3] numpy==1.22.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.41.1 [pip3] triton=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: EngineArgs missing value type for `lora_dtype` bug ### Your current environment ```text Versions of relevant libraries: [pip3] numpy==1.22.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.41.1 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu12==2.18.1.0.4.0 [conda] numpy 1.22.4 py39hc58783e_0 conda-forge [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: conda] vllm-nccl-cu12 2.18.1.0.4.0 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.2 ``` ### 🐛 Describe the bug ```python import vllm vllm.EngineArgs(model='a', lora_dtype='float16'...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 0.4.2 ``` ### 🐛 Describe the bug ```python import vllm vllm.EngineArgs(model='a', lora_dtype='float16') ``` raises ```python --------------------------------------------------------------------------- TypeError Tracebac...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
