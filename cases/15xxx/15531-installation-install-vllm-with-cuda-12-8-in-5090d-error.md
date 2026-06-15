# vllm-project/vllm#15531: [Installation]: install vllm with CUDA 12.8 in 5090D error

| 字段 | 值 |
| --- | --- |
| Issue | [#15531](https://github.com/vllm-project/vllm/issues/15531) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: install vllm with CUDA 12.8 in 5090D error

### Issue 正文摘录

### Your current environment Hi there! I’ve successfully deployed the vLLM service using an RTX 4090 GPU with the Qwen2.5-14B-Instruct model. Now, I’ve got a new RTX 5090 GPU, but I’m running into some issues. The CUDA version on this machine is 12.8, and I installed the corresponding PyTorch version using:pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128 However, when I try to run the service in the vLLM Conda environment, I get dependency conflict errors like this: ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behavior is the source of the following dependency conflicts. xformers 0.0.29.post2 requires torch==2.6.0, but you have torch 2.8.0.dev20250325+cu128 which is incompatible. vllm 0.8.1 requires torch==2.6.0, but you have torch 2.8.0.dev20250325+cu128 which is incompatible. vllm 0.8.1 requires torchaudio==2.6.0, but you have torchaudio 2.6.0.dev20250325+cu128 which is incompatible. vllm 0.8.1 requires torchvision==0.21.0, but you have torchvision 0.22.0.dev20250325+cu128 which is incompatible. When I try to start the service using the command: VLLM_USE_M...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: install vllm with CUDA 12.8 in 5090D error installation ### Your current environment Hi there! I’ve successfully deployed the vLLM service using an RTX 4090 GPU with the Qwen2.5-14B-Instruct model. Now, I
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Installation]: install vllm with CUDA 12.8 in 5090D error installation ### Your current environment Hi there! I’ve successfully deployed the vLLM service using an RTX 4090 GPU with the Qwen2.5-14B-Instruct model. Now,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ve successfully deployed the vLLM service using an RTX 4090 GPU with the Qwen2.5-14B-Instruct model. Now, I’ve got a new RTX 5090 GPU, but I’m running into some issues. The CUDA version on this machine is 12.8, and I in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;model_support cuda import_error env_dependency Your current envi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
