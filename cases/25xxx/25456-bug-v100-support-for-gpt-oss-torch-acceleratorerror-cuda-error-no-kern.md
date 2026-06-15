# vllm-project/vllm#25456: [Bug]: v100 support for gpt-oss: torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device

| 字段 | 值 |
| --- | --- |
| Issue | [#25456](https://github.com/vllm-project/vllm/issues/25456) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v100 support for gpt-oss: torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Minimal steps to reproduce the vllm error: Step 1: Installing vllm nightly (`vLLM API server version 0.10.2rc3.dev372+gc98be0a23`) with pytorch cu118 build (for v100 support) ``` pip install uv uv venv --python 3.12 --seed source .venv/bin/activate uv pip install -U vllm --extra-index-url https://wheels.vllm.ai/nightly --extra-index-url https://download.pytorch.org/whl/nightly/cu118 UV_TORCH_BACKEND=cu118 ``` Step 2: modify `vllm/model_executor/layers/quantization/mxfp4.py` for mxfp4 support ```python @classmethod def get_min_capability(cls) -> int: #return 80 return 70 ... @classmethod def get_supported_act_dtypes(cls) -> list[torch.dtype]: #return [torch.bfloat16] return [torch.bfloat16, torch.float16] ``` Step 2: Call vllm server ``` vllm serve openai/gpt-oss-20b --tensor-parallel-size 8 --async-scheduling ``` Error message: ``` (Worker_TP3 pid=2541127) ERROR 09-22 23:19:03 [multiproc_executor.py:597] Traceback (most recent call last): (Worker_TP3 pid=2541127) ERROR 09-22 23:19:03 [multiproc_executor.py:597] File "/gpfs/fs1/projects/llmservice_nemo_mlops/users/yuanhangs/codes/.venv/lib/python3.12/site-packages/vllm/v1/executor...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: 8 UV_TORCH_BACKEND=cu118 ``` Step 2: modify `vllm/model_executor/layers/quantization/mxfp4.py` for mxfp4 support ```python @classmethod def get_min_capability(cls) -> int: #return 80 return 70 ... @classmethod def get_s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 🐛 Describe the bug Minimal steps to reproduce the vllm error: Step 1: Installing vllm nightly (`vLLM API server version 0.10.2rc3.dev372+gc98be0a23`) with pytorch cu118 build (for v100 support) ``` pip install uv uv ven...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: v100 support for gpt-oss: torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device bug;stale ### Your current environment ### 🐛 Describe the bug Minimal steps to reproduce the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [multiproc_executor.py:597] qweight = weight[i].view(torch.int32).T.contiguous() (Worker_TP3 pid=2541127) ERROR 09-22 23:19:03 [multiproc_executor.py:597] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP3 pid=25411...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: v100 support for gpt-oss: torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device bug;stale ### Your current environment ### 🐛 Describe the bug Minimal steps to reproduce the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
