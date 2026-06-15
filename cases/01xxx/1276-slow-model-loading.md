# vllm-project/vllm#1276: Slow model loading

| 字段 | 值 |
| --- | --- |
| Issue | [#1276](https://github.com/vllm-project/vllm/issues/1276) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;quantization |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Slow model loading

### Issue 正文摘录

Hi! My setup is: - NVIDIA A100 (CUDA 12.2) - AMD EPYC 7702 - Ubuntu 20.04 I'm running an API server like this: `python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model TheBloke/WizardCoder-Python-34B-V1.0-AWQ --quantization awq --trust-remote-code --max-num-batched-tokens 4096 --max-model-len 4096` What's an adequate time for executing API server with AWQ model that size? I have to wait around 50 minutes and I can't estimate if it's okay or not. Also if I interrupt the server after it has already loaded and then run it again, the execution takes around 5 min. I had Tesla V100 previously, and I tried it with non quantized models, and it seemed much faster. So I'm trying to figure it out if there's somthing wrong with my new setup, or AWQ format loading is slow. I also did some quick test: running simple "torch.cuda.is_available()" takes around 3 minutes to execute on the first run, and done almost immediately after

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Slow model loading Hi! My setup is: - NVIDIA A100 (CUDA 12.2) - AMD EPYC 7702 - Ubuntu 20.04 I'm running an API server like this: `python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model TheBloke...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Slow model loading Hi! My setup is: - NVIDIA A100 (CUDA 12.2) - AMD EPYC 7702 - Ubuntu 20.04 I'm running an API server like this: `python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model TheBloke...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e frontend_api;model_support;quantization cuda;quantization slowdown env_dependency Hi!
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: t 0.0.0.0 --port 8000 --model TheBloke/WizardCoder-Python-34B-V1.0-AWQ --quantization awq --trust-remote-code --max-num-batched-tokens 4096 --max-model-len 4096` What's an adequate time for executing API server with AWQ...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: with my new setup, or AWQ format loading is slow. I also did some quick test: running simple "torch.cuda.is_available()" takes around 3 minutes to execute on the first run, and done almost immediately after performance...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
