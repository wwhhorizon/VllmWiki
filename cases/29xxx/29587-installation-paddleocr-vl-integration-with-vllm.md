# vllm-project/vllm#29587: [Installation]: PaddleOCR-VL integration with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#29587](https://github.com/vllm-project/vllm/issues/29587) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: PaddleOCR-VL integration with vLLM

### Issue 正文摘录

Hello, I encountered the following error when trying to integrate PaddleOCR‑VL with vLLM in the same environment. How would you recommend resolving this issue? Thank you in advance for your help. ## Environment - docker, Linux - python 3.12 - cuda 12.8 - torch 2.9.0 ## Environment Setup ``` bash pip install paddlepaddle==3.2.0 \ paddlepaddle-gpu==3.2.0 \ paddleocr[doc-parser]==3.3.2 \ safetensors-0.6.2-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl \ --no-build-isolation pip install vllm==0.11.1 # installs torch 2.9.0 ``` ## Error The conflict is caused by: - paddlepaddle-gpu 3.2.0 depends on nvidia-cuda-nvrtc-cu12==12.9.41; platform_system == "Linux" and platform_machine == "x86_64" - torch 2.9.0 depends on nvidia-cuda-nvrtc-cu12==12.8.93; platform_system == "Linux" and platform_machine == "x86_64"

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: PaddleOCR-VL integration with vLLM installation Hello, I encountered the following error when trying to integrate PaddleOCR‑VL with vLLM in the same environment. How would you recommend resolving this iss
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nce for your help. ## Environment - docker, Linux - python 3.12 - cuda 12.8 - torch 2.9.0 ## Environment Setup ``` bash pip install paddlepaddle==3.2.0 \ paddlepaddle-gpu==3.2.0 \ paddleocr[doc-parser]==3.3.2 \ safetens...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _system == "Linux" and platform_machine == "x86_64" development ci_build;model_support cuda build_error env_dependency Hello,

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
