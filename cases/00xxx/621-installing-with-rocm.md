# vllm-project/vllm#621: Installing with ROCM

| 字段 | 值 |
| --- | --- |
| Issue | [#621](https://github.com/vllm-project/vllm/issues/621) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 44; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Installing with ROCM

### Issue 正文摘录

Hello, I'm trying to install VLLM on AMD server. However unable to build the package because CUDA is not installed. Is their anyway we can configure it to work with ROCM instead? !pip install vllm Error: RuntimeError: Cannot find CUDA_HOME. CUDA must be available in order to build the package. ROCM is installed and verified PyTorch 2-0-ROCm

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Installing with ROCM feature request Hello, I'm trying to install VLLM on AMD server. However unable to build the package because CUDA is not installed. Is their anyway we can configure it to work with ROCM instead?
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Installing with ROCM feature request Hello, I'm trying to install VLLM on AMD server. However unable to build the package because CUDA is not installed. Is their anyway we can configure it to work with ROCM instead? !pi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: build the package because CUDA is not installed. Is their anyway we can configure it to work with ROCM instead? !pip install vllm Error: RuntimeError: Cannot find CUDA_HOME. CUDA must be available in order to build the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Installing with ROCM feature request Hello, I'm trying to install VLLM on AMD server. However unable to build the package because CUDA is not installed. Is their anyway we can configure it to work with ROCM instead? !pi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
