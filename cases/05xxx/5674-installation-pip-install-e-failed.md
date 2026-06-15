# vllm-project/vllm#5674: [Installation]: pip install -e failed

| 字段 | 值 |
| --- | --- |
| Issue | [#5674](https://github.com/vllm-project/vllm/issues/5674) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: pip install -e failed

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Versions of relevant libraries: [pip3] numpy==1.26.3 [pip3] pytorch-triton-rocm==2.3.0 [pip3] sentence-transformers==3.0.1 [pip3] torch==2.3.0+rocm6.0 [pip3] torchaudio==2.3.0+rocm6.0 [pip3] torchvision==0.18.0+rocm6.0 [pip3] transformers==4.40.0 [conda] numpy 1.26.3 pypi_0 pypi [conda] pytorch-triton-rocm 2.3.0 pypi_0 pypi [conda] sentence-transformers 3.0.1 pypi_0 pypi [conda] torch 2.3.0+rocm6.0 pypi_0 pypi [conda] torchaudio 2.3.0+rocm6.0 pypi_0 pypi [conda] torchvision 0.18.0+rocm6.0 pypi_0 pypi [conda] transformers 4.40.0 pypi_0 pypi ROCM Version: 6.0.32830-d62f6a171 Neuron SDK Version: N/A vLLM Version: 0.5.0.post1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Enabled; Neuron: Disabled GPU Topology: Could not collect ### How you are installing vllm hi, i follow ur instruction build a docker : docker build -f Dockerfile.rocm -t vllm-rocm . , successfully, but i got errors when i use vllm backend, then i tried to modify some vllm codes. soi have to reinstall in a eidtable mode, but failed. when i tried to install form source: git clone https://github.com/vllm-project/vllm.git cd vllm # export VLLM_I...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: pip install -e failed installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` Versions of relevant libraries: [pip3] numpy==1.26.3 [pip3] pytorch-triton-rocm==2.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: rsions of relevant libraries: [pip3] numpy==1.26.3 [pip3] pytorch-triton-rocm==2.3.0 [pip3] sentence-transformers==3.0.1 [pip3] torch==2.3.0+rocm6.0 [pip3] torchaudio==2.3.0+rocm6.0 [pip3] torchvision==0.18.0+rocm6.0 [p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ``` Versions of relevant libraries: [pip3] numpy==1.26.3 [pip3] pytorch-triton-rocm==2.3.0 [pip3] sentence-transformers==3.0.1 [pip3] torch==2.3.0+rocm6.0 [pip3] torchaudio==2.3.0+rocm6.0 [pip3] torchvision==0.18.0+rocm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: pip install -e failed installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` Versions of relevant libraries: [pip3] numpy==1.26.3 [pip3] pytorch-triton-rocm==2....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
