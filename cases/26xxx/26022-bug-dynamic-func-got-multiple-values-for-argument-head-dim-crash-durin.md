# vllm-project/vllm#26022: [Bug]: `dynamic_func() got multiple values for argument 'HEAD_DIM'` crash during startup when using `-dcp`

| 字段 | 值 |
| --- | --- |
| Issue | [#26022](https://github.com/vllm-project/vllm/issues/26022) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `dynamic_func() got multiple values for argument 'HEAD_DIM'` crash during startup when using `-dcp`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM crashes with `dynamic_func() got multiple values for argument 'HEAD_DIM'` during startup when using `-dcp 4`: ```sh # ~latest commit as of writing export VLLM_COMMIT=1405f0c7bab17b10682d2de337bd544b3e9f2f92 && uv pip install vllm[flashinfer] --torch-backend=auto --extra-index-url https://wheels.vllm.ai/${VLLM_COMMIT} CUDA_VISIBLE_DEVICES='0,1,2,3' vllm serve RedHatAI/DeepSeek-R1-0528-quantized.w4a16 --port 3000 --tensor-parallel-size 4 -dcp 4 --served-model-name default --host 0.0.0.0 ``` The issue does not exist in the latest stable version, `0.10.2`. ### Startup / crash logs: https://gist.github.com/josephrocca/af3ae259dd63c5392245131fa58e7d7f Note: For the log lines like `Worker_TP0 ....` and `Worker_TP1 ....`, etc. I've removed all but the TP0 lines, since they were of course duplicated 4 times.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ng export VLLM_COMMIT=1405f0c7bab17b10682d2de337bd544b3e9f2f92 && uv pip install vllm[flashinfer] --torch-backend=auto --extra-index-url https://wheels.vllm.ai/${VLLM_COMMIT} CUDA_VISIBLE_DEVICES='0,1,2,3' vllm serve Re...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: M_COMMIT=1405f0c7bab17b10682d2de337bd544b3e9f2f92 && uv pip install vllm[flashinfer] --torch-backend=auto --extra-index-url https://wheels.vllm.ai/${VLLM_COMMIT} CUDA_VISIBLE_DEVICES='0,1,2,3' vllm serve RedHatAI/DeepSe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: MIT} CUDA_VISIBLE_DEVICES='0,1,2,3' vllm serve RedHatAI/DeepSeek-R1-0528-quantized.w4a16 --port 3000 --tensor-parallel-size 4 -dcp 4 --served-model-name default --host 0.0.0.0 ``` The issue does not exist in the latest...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rch-backend=auto --extra-index-url https://wheels.vllm.ai/${VLLM_COMMIT} CUDA_VISIBLE_DEVICES='0,1,2,3' vllm serve RedHatAI/DeepSeek-R1-0528-quantized.w4a16 --port 3000 --tensor-parallel-size 4 -dcp 4 --served-model-nam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 528-quantized.w4a16 --port 3000 --tensor-parallel-size 4 -dcp 4 --served-model-name default --host 0.0.0.0 ``` The issue does not exist in the latest stable version, `0.10.2`. ### Startup / crash logs: https://gist.gith...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
