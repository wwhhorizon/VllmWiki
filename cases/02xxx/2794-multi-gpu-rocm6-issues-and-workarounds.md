# vllm-project/vllm#2794: Multi GPU ROCm6 issues, and workarounds

| 字段 | 值 |
| --- | --- |
| Issue | [#2794](https://github.com/vllm-project/vllm/issues/2794) |
| 状态 | closed |
| 标签 | rocm |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Multi GPU ROCm6 issues, and workarounds

### Issue 正文摘录

I ran into a series of issues trying to get VLLM stood up on a system with multiple MI210s. I figured I'd document my issues and workarounds so that someone could pick up the baton later, or at least save someone some debugging time later. 1. Ray will deadlock with multiple AMD GPUs. Ray doesn't officially support AMD GPUs in v2.9; I updated Ray to nightlies (v3.0). ``` pip uninstall ray pip install -U "ray[default] @ https://s3-us-west-2.amazonaws.com/ray-wheels/latest/ray-3.0.0.dev0-cp310-cp310-manylinux2014_x86_64.whl" ``` 2. Something might have changed with how Ray exposes GPUs to workers. Only 1 GPU was exposed to each worker, so `torch.cuda.set_device()` with anything other than 0 would fail. I tweaked worker.py to always use 0, but I don't think this is a viable long-term fix. ``` diff --git a/vllm/worker/worker.py b/vllm/worker/worker.py index c97e82a..a63fbd9 100644 --- a/vllm/worker/worker.py +++ b/vllm/worker/worker.py @@ -68,6 +68,7 @@ class Worker: self.gpu_cache = None def init_model(self) -> None: + print(f"***** local_rank {self.local_rank} hit init_model, is_driver: {self.is_driver_worker} *****") if self.device_config.device.type == "cuda": # torch.distributed.a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: me later. 1. Ray will deadlock with multiple AMD GPUs. Ray doesn't officially support AMD GPUs in v2.9; I updated Ray to nightlies (v3.0). ``` pip uninstall ray pip install -U "ray[default] @ https://s3-us-west-2.amazon...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Multi GPU ROCm6 issues, and workarounds rocm I ran into a series of issues trying to get VLLM stood up on a system with multiple MI210s. I figured I'd document my issues and workarounds so that someone could pick up the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 8,6 +68,7 @@ class Worker: self.gpu_cache = None def init_model(self) -> None: + print(f"***** local_rank {self.local_rank} hit init_model, is_driver: {self.is_driver_worker} *****") if self.device_config.device.type ==...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: torch.cuda.set_device(0) _check_if_gpu_supports_dtype(self.model_config.dtype) else: ``` performance ci_build;distributed_parallel;hardware_porting cuda dtype;env_dependency I ran into a series of issues trying to get V...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: _check_if_gpu_supports_dtype(self.model_config.dtype) else: ``` performance ci_build;distributed_parallel;hardware_porting cuda dtype;env_dependency I ran into a series of issues trying to get VLLM stood up on a system...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
