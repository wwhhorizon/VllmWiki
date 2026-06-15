# vllm-project/vllm#327: torch.cuda.DeferredCudaCallError when installing vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#327](https://github.com/vllm-project/vllm/issues/327) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> torch.cuda.DeferredCudaCallError when installing vllm

### Issue 正文摘录

Hi, I'm trying to run vllm on a 4-GPU Linux machine. When I followed the Installation guide to `pip install vllm`, I got this error: ``` torch.cuda.DeferredCudaCallError: CUDA call failed lazily at initialization with error: device >= 0 && device < num_gpus INTERNAL ASSERT FAILED at "../aten/src/ATen/cuda/CUDAContext.cpp":50, please report a bug to PyTorch. ``` If I explicitly set the visible device to just device:0, via: ``` export CUDA_VISIBLE_DEVICES=0 ``` then the installation worked fine. However, when I switched back to the default (`export CUDA_VISIBLE_DEVICES=0,1,2,3`), the `DeferredCudaCallError` occurred. Similar pattern was observed when I tried to do `llm = LLM(model="facebook/opt-125m")`; it'd only worked when visible device is pinned to just 1 GPU. Has anyone run into similar issues?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: torch.cuda.DeferredCudaCallError when installing vllm installation Hi, I'm trying to run vllm on a 4-GPU Linux machine. When I followed the Installation guide to `pip install vllm`, I got this error: ``` torch.cuda.Defe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: torch.cuda.DeferredCudaCallError when installing vllm installation Hi, I'm trying to run vllm on a 4-GPU Linux machine. When I followed the Installation guide to `pip install vllm`, I got this error: ``` torch.cuda.Defe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: r` occurred. Similar pattern was observed when I tried to do `llm = LLM(model="facebook/opt-125m")`; it'd only worked when visible device is pinned to just 1 GPU. Has anyone run into similar issues? development ci_build...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
