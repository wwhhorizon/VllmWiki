# vllm-project/vllm#803:  Issue Building vllm Wheel: Unsupported GPU Architecture 'compute_89'

| 字段 | 值 |
| --- | --- |
| Issue | [#803](https://github.com/vllm-project/vllm/issues/803) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

>  Issue Building vllm Wheel: Unsupported GPU Architecture 'compute_89'

### Issue 正文摘录

I'm trying to build the vllm package from source (pip install vllm), but I'm encountering an error related to CUDA and GPU architecture. I am using RTX 4090. Here are the crucial parts of the log: ``` Building wheels for collected packages: vllm Building wheel for vllm (pyproject.toml) ... error error: subprocess-exited-with-error ... building 'vllm.cache_ops' extension Emitting ninja build file ... ... /usr/local/cuda/bin/nvcc -I/tmp/pip-build-env-... (other flags and paths) nvcc fatal : Unsupported gpu architecture 'compute_89' ``` Here is my compute cluster: --- 6790722 Age:15 min.[Remaining](https://vast.ai/faq#Instances):1d 19h71.69.80.64:44536-44750North Carolina, US1x RTX 409081.8 TFLOPS m:9663host:39244verified0.3/24.6 GB 3506.9 GB/s ROME2D16 PCIE 4.0, 8x12.5 GB/s AMD EPYC 7662 64-Core Processor 25.6/256 cpu 4/52 GB nvme 4972 MB/s6.9/21.0 GB 516.4 Mbps514.0 MbpsMax CUDA: 12.2 GPU: 0% 35C , CPU: 4% Status: success, running pytorch/pytorch_2.0.1-cuda11.7-cudnn8-devel/jupyter $0.263/hr Current State : running Next State : running Docker Image: pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel Image Runtype : jupyter_direc ssh_direc ssh_proxy Environment : { "JUPYTER_DIR": "/" } Doc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Issue Building vllm Wheel: Unsupported GPU Architecture 'compute_89' installation I'm trying to build the vllm package from source (pip install vllm), but I'm encountering an error related to CUDA and GPU architecture....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Issue Building vllm Wheel: Unsupported GPU Architecture 'compute_89' installation I'm trying to build the vllm package from source (pip install vllm), but I'm encountering an error related to CUDA and GPU architecture....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: issue before? Any suggestions on how to resolve it? development ci_build;model_support cuda build_error env_dependency I'm trying to build the vllm package from source (pip install vllm), but I'm encountering an error r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
