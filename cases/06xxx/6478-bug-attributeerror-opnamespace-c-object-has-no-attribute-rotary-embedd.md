# vllm-project/vllm#6478: [Bug]: AttributeError: '_OpNamespace' '_C' object has no attribute 'rotary_embedding' / gemma-2-9b with vllm=0.5.2 

| 字段 | 值 |
| --- | --- |
| Issue | [#6478](https://github.com/vllm-project/vllm/issues/6478) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: '_OpNamespace' '_C' object has no attribute 'rotary_embedding' / gemma-2-9b with vllm=0.5.2 

### Issue 正文摘录

### Your current environment ```text Versions of relevant libraries: [pip3] flashinfer==0.0.9+cu121torch2.3 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] sentence-transformers==3.0.1 [pip3] torch==2.3.1 [pip3] torchvision==0.18.1 [pip3] transformers==4.42.4 [pip3] triton==2.3.1 [conda] flashinfer 0.0.9+cu121torch2.3 pypi_0 pypi [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] sentence-transformers 3.0.1 pypi_0 pypi [conda] torch 2.3.1 pypi_0 pypi [conda] torchvision 0.18.1 pypi_0 pypi [conda] transformers 4.42.4 pypi_0 pypi [conda] triton 2.3.1 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.2 ``` ### 🐛 Describe the bug I encountered the following error when running Gemma-2-9b. Even after deleting and reinstalling the virtual environment, the same error repeats. ```text INFO 07-17 00:14:06 selector.py:79] Using Flashinfer backend. INFO 07-17 00:14:07 selector.py:79] Using Flashinfer backend. INFO 07-17 00:14:10 model_runner.py:266] Loading model weights took 17.3781 GB ERROR 07-17 00:14:10 _custom_ops.py:42] Error in calling custom op rotary_embedding: '_OpNamespace' '_C' object has no attribut...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ma-2-9b with vllm=0.5.2 bug;stale ### Your current environment ```text Versions of relevant libraries: [pip3] flashinfer==0.0.9+cu121torch2.3 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] sentence-transfor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: Your current environment ```text Versions of relevant libraries: [pip3] flashinfer==0.0.9+cu121torch2.3 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] sentence-transformers==3.0.1 [pip3] torch==2.3.1 [pip3]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: conda] triton 2.3.1 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.2 ``` ### 🐛 Describe the bug I encountered the following error when running Gemma-2-9b. Even after deleting and r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: eError: '_OpNamespace' '_C' object has no attribute 'rotary_embedding' / gemma-2-9b with vllm=0.5.2 bug;stale ### Your current environment ```text Versions of relevant libraries: [pip3] flashinfer==0.0.9+cu121torch2.3 [...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: alize_kv_caches [rank0]: self.model_executor.determine_num_available_blocks()) [rank0]: File "/home/choco_9966/miniconda3/envs/gemma/lib/python3.10/site-packages/vllm/executor/gpu_executor.py", line 78, in determine_num...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
