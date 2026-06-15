# vllm-project/vllm#3312: how to run gemma-7b model with vllm 0.3.3 under cuda 118??

| 字段 | 值 |
| --- | --- |
| Issue | [#3312](https://github.com/vllm-project/vllm/issues/3312) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> how to run gemma-7b model with vllm 0.3.3 under cuda 118??

### Issue 正文摘录

hello friends, I meet a problem when I want to run gemma model with vllm 0.3.3 under cuda 118, the error is ![image](https://github.com/vllm-project/vllm/assets/145645189/7e06749f-a32d-4df4-83b0-18ed73a5d004) I have tried # Install vLLM with CUDA 11.8. export VLLM_VERSION=0.2.4 export PYTHON_VERSION=38 pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu118-cp${PYTHON_VERSION}-cp${PYTHON_VERSION}-manylinux1_x86_64.whl # Re-install PyTorch with CUDA 11.8. pip uninstall torch -y pip install torch --upgrade --index-url https://download.pytorch.org/whl/cu118 # Re-install xFormers with CUDA 11.8. pip uninstall xformers -y pip install --upgrade xformers --index-url https://download.pytorch.org/whl/cu118 but it doesn't work , anyone has runed successfully in the same environment with me ? hope your help~~~ if you can provide me with a docker image I would be grateful

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: /assets/145645189/7e06749f-a32d-4df4-83b0-18ed73a5d004) I have tried # Install vLLM with CUDA 11.8. export VLLM_VERSION=0.2.4 export PYTHON_VERSION=38 pip install https://github.com/vllm-project/vllm/releases/download/v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: how to run gemma-7b model with vllm 0.3.3 under cuda 118?? stale hello friends, I meet a problem when I want to run gemma model with vllm 0.3.3 under cuda 118, the error is ![image](https://github.com/vllm-project/vllm/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: how to run gemma-7b model with vllm 0.3.3 under cuda 118?? stale hello friends, I meet a problem when I want to run gemma model with vllm 0.3.3 under cuda 118, the error is ![image](https://github.com/vllm-project/vllm/...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: how to run gemma-7b model with vllm 0.3.3 under cuda 118?? stale hello friends, I meet a problem when I want to run gemma model with vllm 0.3.3 under cuda 118, the error is ![image](https://github.com/vllm-project/vllm/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: how to run gemma-7b model with vllm 0.3.3 under cuda 118?? stale hello friends, I meet a problem when I want to run gemma model with vllm 0.3.3 under cuda 118, the error is ![image](https://github.com/vllm-project/vllm/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
