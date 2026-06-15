# vllm-project/vllm#38967: [Bug] vLLM >= 0.18.0 NCCL segfault (cuMemCreate) with TP>1 on RTX 4090 (SM 89)

| 字段 | 值 |
| --- | --- |
| Issue | [#38967](https://github.com/vllm-project/vllm/issues/38967) |
| 状态 | open |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] vLLM >= 0.18.0 NCCL segfault (cuMemCreate) with TP>1 on RTX 4090 (SM 89)

### Issue 正文摘录

### Your current environment - vLLM version: 0.18.0 - GPU: 2× RTX 4090 48GB (SM 89) - NCCL: 2.27.5 (bundled in vllm/vllm-openai:v0.18.0) - CUDA: 12.x - OS: openEuler 22.03 SP4 ### Problem Starting from v0.18.0, any TP>1 deployment on RTX 4090 results in NCCL segfault during `cuMemCreate`. This was working fine on v0.10.0 (V0 engine). ### Reproduction ```bash docker run --gpus all --shm-size 32g --network host \ vllm/vllm-openai:v0.18.0 \ --model Qwen/Qwen3.5-35B-A3B \ --tensor-parallel-size 2 \ --trust-remote-code --max-model-len 4096 ``` ### Error ``` !!!!!!! Segfault encountered !!!!!!! File " ", line 0, in cuMemCreate File "misc/cudawrap.cc", line 92, in ncclCuMemHostEnable() File "misc/cudawrap.cc", line 202, in ncclCuMemHostEnable() File "misc/cudawrap.cc", line 280, in initOnceFunc File "misc/cudawrap.cc", line 298, in ncclCudaLibraryInit() ``` ### Workarounds tried (all failed) - `NCCL_CUMEM=0` + `NCCL_P2P_DISABLE=1` → same segfault - `VLLM_USE_V1=0` → "Unknown vLLM environment variable" (V0 engine removed in 0.18.0) - `--distributed-executor-backend mp` → same segfault - `--shm-size 32g` + `--network host` → same segfault ### Workaround Roll back to v0.10.0 (V0 engine) for...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: eate) with TP>1 on RTX 4090 (SM 89) ### Your current environment - vLLM version: 0.18.0 - GPU: 2× RTX 4090 48GB (SM 89) - NCCL: 2.27.5 (bundled in vllm/vllm-openai:v0.18.0) - CUDA: 12.x - OS: openEuler 22.03 SP4 ### Pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug] vLLM >= 0.18.0 NCCL segfault (cuMemCreate) with TP>1 on RTX 4090 (SM 89) ### Your current environment - vLLM version: 0.18.0 - GPU: 2× RTX 4090 48GB (SM 89) - NCCL: 2.27.5 (bundled in vllm/vllm-openai:v0.18.0) - C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: all --shm-size 32g --network host \ vllm/vllm-openai:v0.18.0 \ --model Qwen/Qwen3.5-35B-A3B \ --tensor-parallel-size 2 \ --trust-remote-code --max-model-len 4096 ``` ### Error ``` !!!!!!! Segfault encountered !!!!!!! Fi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: onment variable" (V0 engine removed in 0.18.0) - `--distributed-executor-backend mp` → same segfault - `--shm-size 32g` + `--network host` → same segfault ### Workaround Roll back to v0.10.0 (V0 engine) for TP>1 on RTX...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: er GPUs (SM 89). development ci_build;distributed_parallel;model_support;quantization cuda;quantization crash Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
