# vllm-project/vllm#2634: pip install vllm not working

| 字段 | 值 |
| --- | --- |
| Issue | [#2634](https://github.com/vllm-project/vllm/issues/2634) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> pip install vllm not working

### Issue 正文摘录

The `pip install vllm` runs successfully. But `vllm` is still not available from within python. ``` harsht ~/temp $ pip install vllm Defaulting to user installation because normal site-packages is not writeable Requirement already satisfied: vllm in /home/harsht/.local/lib/python3.8/site-packages (0.2.7) Requirement already satisfied: ninja in /home/harsht/.local/lib/python3.8/site-packages (from vllm) (1.11.1.1) Requirement already satisfied: psutil in /home/harsht/.local/lib/python3.8/site-packages (from vllm) (5.9.4) Requirement already satisfied: ray>=2.5.1 in /home/harsht/.local/lib/python3.8/site-packages (from vllm) (2.9.1) Requirement already satisfied: sentencepiece in /home/harsht/.local/lib/python3.8/site-packages (from vllm) (0.1.99) Requirement already satisfied: numpy in /home/harsht/.local/lib/python3.8/site-packages (from vllm) (1.24.4) Requirement already satisfied: torch==2.1.2 in /home/harsht/.local/lib/python3.8/site-packages (from vllm) (2.1.2) Requirement already satisfied: transformers>=4.36.0 in /home/harsht/.local/lib/python3.8/site-packages (from vllm) (4.37.1) Requirement already satisfied: xformers==0.0.23.post1 in /home/harsht/.local/lib/python3.8/site...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: pip install vllm not working The `pip install vllm` runs successfully. But `vllm` is still not available from within python. ``` harsht ~/temp $ pip install vllm Defaulting to user installation because normal site-packa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: packages (from ray>=2.5.1->vllm) (2.31.0) Requirement already satisfied: huggingface-hub =0.19.3 in /home/harsht/.local/lib/python3.8/site-packages (from transformers>=4.36.0->vllm) (0.20.3) Requirement already satisfie...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ages (from torch==2.1.2->vllm) (12.1.105) Requirement already satisfied: triton==2.1.0 in /home/harsht/.local/lib/python3.8/site-packages (from torch==2.1.2->vllm) (2.1.0) Requirement already satisfied: nvidia-nvjitlink...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: aioprometheus[starlette]->vllm) (3.9.12) Requirement already satisfied: quantile-python>=1.1 in /home/harsht/.local/lib/python3.8/site-packages (from aioprometheus[starlette]->vllm) (1.1) Requirement already satisfied:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: om torch==2.1.2->vllm) (2023.12.2) Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.1.105 in /home/harsht/.local/lib/python3.8/site-packages (from torch==2.1.2->vllm) (12.1.105) Requirement already satisfied: n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
